#!/usr/bin/env python3
"""
extract_structured.py
======================

A decoupled *post-pass* over a knowledge base produced by ``scrape_contracts.py``.
It reads the per-page records under ``<output>/raw/`` (by default only those in the
``real-agreements`` category — i.e. real executed B2B contracts from SEC EDGAR) and
emits one **structured row per agreement** to ``<output>/agreements.jsonl``:

    {parties, agreement_type, effective_date, governing_law, term, auto_renewal,
     termination, liability_cap, indemnification, confidentiality, payment_terms,
     clause_inventory, summary, extraction_method, ... source metadata ...}

Two extraction backends:

  * **LLM** (default, if the Anthropic SDK is installed and ``ANTHROPIC_API_KEY`` is
    set): sends each contract's text to Claude and forces a structured tool call,
    so the output is schema-validated JSON — no brittle parsing.
  * **Heuristic** (automatic fallback, or ``--no-llm``): regex/keyword extraction.
    Lower recall, but needs no API key and no network.

This is deliberately separate from the crawler so the core scraper keeps zero LLM
dependencies. It never reads or writes the source contract files — only the text
already extracted into the knowledge base.

Usage
-----
    python extract_structured.py                          # output/ -> output/agreements.jsonl
    python extract_structured.py --input ./kb             # other knowledge-base dir
    python extract_structured.py --category real-agreements
    python extract_structured.py --no-llm                 # heuristics only (no API key needed)
    python extract_structured.py --model claude-haiku-4-5-20251001   # cheaper/faster
    python extract_structured.py --max 5                  # only the first N agreements
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Latest balanced model; override with --model. Haiku 4.5
# (claude-haiku-4-5-20251001) is a cheaper/faster choice for bulk extraction.
DEFAULT_MODEL = "claude-sonnet-4-6"

# How much contract text to send to the LLM per document (chars). Contracts are
# long; key terms cluster early but liability/termination can be mid-document.
DEFAULT_MAX_CHARS = 120_000


# ---------------------------------------------------------------------------
# Structured-output schema (also the Anthropic tool input_schema)
# ---------------------------------------------------------------------------
RECORD_SCHEMA = {
    "type": "object",
    "properties": {
        "agreement_type": {"type": "string",
                           "description": "e.g. 'Master Services Agreement', 'Reseller Agreement'"},
        "parties": {"type": "array", "items": {"type": "string"},
                    "description": "Legal names of the contracting parties"},
        "effective_date": {"type": "string",
                           "description": "Effective/execution date, YYYY-MM-DD if possible; '' if absent"},
        "governing_law": {"type": "string",
                          "description": "Governing-law jurisdiction, e.g. 'New York'; '' if absent"},
        "term": {"type": "string", "description": "Initial term / duration; '' if absent"},
        "auto_renewal": {"type": "string",
                         "description": "Renewal mechanics, or 'none' if not auto-renewing"},
        "termination": {"type": "string", "description": "Key termination rights; '' if absent"},
        "liability_cap": {"type": "string",
                          "description": "Limitation-of-liability cap, e.g. 'fees paid in prior 12 months'; '' if absent"},
        "indemnification": {"type": "boolean", "description": "Does the contract contain an indemnity?"},
        "confidentiality": {"type": "boolean", "description": "Does it contain confidentiality obligations?"},
        "payment_terms": {"type": "string", "description": "Payment terms, e.g. 'Net 30'; '' if absent"},
        "clause_inventory": {"type": "array", "items": {"type": "string"},
                             "description": "List of notable clause types present"},
        "summary": {"type": "string", "description": "One-sentence plain-English summary"},
    },
    "required": ["agreement_type", "parties", "governing_law", "clause_inventory", "summary"],
}

# Keys we expect back, with sensible empties (so heuristic + LLM rows share a shape).
EMPTY_FIELDS = {
    "agreement_type": "", "parties": [], "effective_date": "", "governing_law": "",
    "term": "", "auto_renewal": "", "termination": "", "liability_cap": "",
    "indemnification": False, "confidentiality": False, "payment_terms": "",
    "clause_inventory": [], "summary": "",
}


# ---------------------------------------------------------------------------
# Heuristic backend (no API key, no network)
# ---------------------------------------------------------------------------
# Known governing-law jurisdictions. Matching against this set keeps precision
# high — free-form capture after "laws of" pulls in far too much noise.
_US_STATES = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
    "Washington", "West Virginia", "Wisconsin", "Wyoming",
    "District of Columbia",
]
_OTHER_JURISDICTIONS = [
    "England and Wales", "England", "Scotland", "Northern Ireland",
    "United Kingdom", "Ireland", "Switzerland", "Germany", "France",
    "Netherlands", "Luxembourg", "Singapore", "Hong Kong", "Japan", "Canada",
    "Ontario", "Quebec", "British Columbia", "Australia", "New South Wales",
    "Sweden", "Spain", "Italy", "Belgium", "Denmark", "Finland", "Norway",
    "Israel", "India", "China", "Brazil", "Mexico",
]
# Longest names first so e.g. "New York" wins over a stray "York".
_JURIS_RE = re.compile(
    r"\b(" + "|".join(re.escape(j) for j in sorted(
        _US_STATES + _OTHER_JURISDICTIONS, key=len, reverse=True)) + r")\b")
# Governing-law context cues; a jurisdiction counts only if it sits just after one.
# Strong cues (the actual choice-of-law clause) are tried before broad ones, so a
# party's "organized under the laws of X" doesn't outrank the real governing law.
_GOV_STRONG = re.compile(r"governed|governing law|construed in accordance", re.I)
_GOV_CUE = re.compile(r"govern|laws?\s+of|jurisdiction|construed|venue", re.I)

# Corporate-entity suffixes, longest variants first so "Corporation" beats "Corp".
_PARTY_SUFFIX = (
    r"Incorporated|Corporation|Company|Limited|Holdings|"
    r"L\.?L\.?C|L\.?L\.?P|L\.?P|GmbH|N\.?V|S\.?p\.?A|S\.?A\.?S|S\.?A|"
    r"Pte\.?\s*Ltd|Inc|Corp|Co|Ltd|LLC|LP|LLP|plc|AG|BV"
)
# An entity = capitalized tokens ending in a suffix. (?i:...) makes only the
# suffix case-insensitive, so ALL-CAPS names ("VISTEON CORP") match while name
# tokens still must start uppercase. "and" is excluded as a connector so
# "Acme Corp and Beta LLC" splits into two parties, not one. The trailing
# lookahead stops "Co" from matching inside "Communications".
_ENTITY_RE = re.compile(
    r"\b([A-Z][\w&.\-]*(?:[ ,]+(?:of |the )?[A-Z][\w&.\-]*){0,5}[ ,]+"
    r"(?i:" + _PARTY_SUFFIX + r"))(?=\W|$)")
_PARTY_BETWEEN = re.compile(
    r"\b(?:by and between|by and among|between|among)\b(.{5,300}?)"
    r"(?:\bwitnesseth\b|\brecitals?\b|\bwhereas\b|\bagree\b|\. )", re.I)
# Looks like an entity but is not a contracting party.
_PARTY_BLOCKLIST = re.compile(
    r"securities and exchange|commission|exhibit|agreement|amendment|"
    r"regulation|schedule|annex|\brule\b", re.I)
# "Delaware corporation", "a Nevada company" — entity descriptors, not party names.
_DESCRIPTOR_RE = re.compile(
    r"^(?:" + "|".join(re.escape(j) for j in sorted(
        _US_STATES + _OTHER_JURISDICTIONS, key=len, reverse=True)) +
    r")\s+(?:corporation|company|limited|llc|partnership|lp)\b", re.I)

_DATE = re.compile(
    r"(?:effective|dated|made|entered into)(?:\s+as\s+of)?\s+(?:this\s+)?"
    r"([A-Z][a-z]+\s+\d{1,2},?\s+\d{4}"
    r"|\d{1,2}(?:st|nd|rd|th)?\s+(?:day\s+of\s+)?[A-Z][a-z]+,?\s+\d{4}"
    r"|\d{4}-\d{2}-\d{2})", re.I)

# Initial term / duration, e.g. "initial term of three (3) years".
_NUMWORD = r"\d{1,3}|one|two|three|four|five|six|seven|eight|nine|ten|twelve"
_TERM = re.compile(
    r"(?:initial term|term of this agreement|term hereof|"
    r"agreement shall (?:continue|remain in (?:full )?(?:force and )?effect|"
    r"have an? (?:initial )?term)|continue in (?:full )?(?:force and )?effect for|"
    r"for an? initial (?:period|term) of|for a (?:period|term) of)"
    r"[^.]{0,80}?\b(?:" + _NUMWORD + r")(?:\s*\(\d{1,3}\))?\s+(?:year|month)s?\b", re.I)

# A title line, e.g. "MASTER SERVICES AGREEMENT" / "Third Amendment to ...".
# No "." in the token class, so a match can't run across a sentence boundary.
_AGMT_TYPE = re.compile(
    r"\b((?:[A-Z][A-Za-z&'-]+\s+){1,6}"
    r"(?:AGREEMENT|AMENDMENT|CONTRACT|ADDENDUM|MEMORANDUM|GUARANTY|GUARANTEE))\b")
# SEC redaction/boilerplate that can masquerade as a title — never an agreement type.
_TYPE_BLOCKLIST = re.compile(
    r"registrant|commission|portions|omitted|redacted|confidential treatment|"
    r"pursuant|regulation|securities|material contract", re.I)
# Leading connector words to trim from a captured name/title (e.g. "To "/"By ").
# Deliberately excludes a/an/old/new so real names like "New Relic" survive.
_LEAD_RE = re.compile(
    r"^(?:(?:by|and|between|among|whereas|the|this|that|to|of)\s+)+", re.I)

# clause type -> regex fragments that signal its presence
_CLAUSE_SIGNS = {
    "indemnification": [r"indemnif"],
    "limitation of liability": [r"limitation of liability", r"in no event shall", r"aggregate liability"],
    "confidentiality": [r"confidential"],
    "termination": [r"terminat"],
    "governing law": [r"governing law", r"governed by"],
    "force majeure": [r"force majeure"],
    "arbitration": [r"arbitrat"],
    "assignment": [r"assign(?:ment|s|ed)?\b"],
    "warranty": [r"warrant(?:y|ies|s)\b"],
    "intellectual property": [r"intellectual property"],
    "auto-renewal": [r"automatically renew", r"auto-?renew", r"renewal term"],
    "payment terms": [r"payment terms", r"\bnet\s+\d+\b", r"invoice"],
    "non-solicitation": [r"non-?solicit"],
    "data protection": [r"data protection", r"personal data", r"\bGDPR\b"],
    "insurance": [r"\binsurance\b"],
}

_PAYMENT = re.compile(r"\bnet\s+(\d{1,3})\b", re.I)


def _clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip(" .,;:-")


def _strip_edgar_header(text: str) -> str:
    """Drop the SGML/filename noise EDGAR prepends to an exhibit, e.g.
    'EX-10.3 4 k35009exv10w3.htm  ...' -> the actual contract text."""
    return re.sub(r"^\s*EX-\S+\s+\d+\s+\S+?\.(?:htm|html|txt)\s+", "", text, flags=re.I)


def _extract_governing_law(text: str) -> str:
    """Find a known jurisdiction sitting just after a governing-law cue. Strong
    cues (the actual choice-of-law clause) are tried before broad ones."""
    for cues in (_GOV_STRONG, _GOV_CUE):
        for cue in cues.finditer(text):
            jm = _JURIS_RE.search(text, cue.start(), cue.end() + 80)
            if jm:
                return jm.group(1)
    return ""


def _extract_parties(text: str) -> list:
    """Entity names from the 'between X and Y' preamble (or the head as fallback)."""
    head = text[:2500]
    between = _PARTY_BETWEEN.search(head)
    scope = between.group(1) if between else head
    found: list = []
    seen: set = set()
    for em in _ENTITY_RE.finditer(scope):
        name = _LEAD_RE.sub("", _clean(em.group(1)))
        if (len(name) < 3 or _PARTY_BLOCKLIST.search(name)
                or _DESCRIPTOR_RE.match(name)):       # skip "Delaware corporation"
            continue
        if name.lower() in seen:                      # case-insensitive dedup
            continue
        seen.add(name.lower())
        found.append(name)
        if len(found) >= 3:
            break
    return found


def _extract_term(text: str) -> str:
    m = _TERM.search(text)
    return _clean(m.group(0))[:140] if m else ""


def _extract_agreement_type(text: str) -> str:
    head = _strip_edgar_header(text)[:1500]
    for m in _AGMT_TYPE.finditer(head):
        t = _LEAD_RE.sub("", _clean(m.group(1)))
        if not t or _TYPE_BLOCKLIST.search(t):        # skip redaction boilerplate
            continue
        return t.title() if t.isupper() else t        # title-case ALL-CAPS headings
    return ""


def heuristic_extract(text: str) -> dict:
    out = dict(EMPTY_FIELDS)
    # Strip EDGAR header noise, then collapse whitespace so phrases split across
    # line breaks (common in scraped HTML / PDF text) still match.
    text = re.sub(r"\s+", " ", _strip_edgar_header(text))
    low = text.lower()

    inventory = [name for name, signs in _CLAUSE_SIGNS.items()
                 if any(re.search(p, low) for p in signs)]
    out["clause_inventory"] = inventory
    out["indemnification"] = "indemnification" in inventory
    out["confidentiality"] = "confidentiality" in inventory

    out["governing_law"] = _extract_governing_law(text)
    out["parties"] = _extract_parties(text)
    out["term"] = _extract_term(text)
    out["agreement_type"] = _extract_agreement_type(text)

    m = _DATE.search(text)
    if m:
        out["effective_date"] = _clean(m.group(1))

    if "auto-renewal" in inventory:
        out["auto_renewal"] = "present (see renewal clause)"
    if "limitation of liability" in inventory:
        out["liability_cap"] = "present (see limitation-of-liability clause)"

    m = _PAYMENT.search(text)
    if m:
        out["payment_terms"] = f"Net {m.group(1)}"

    return out


# ---------------------------------------------------------------------------
# LLM backend (Anthropic)
# ---------------------------------------------------------------------------
_SYSTEM = (
    "You are a meticulous commercial-contracts analyst. Extract the requested "
    "fields from the B2B agreement text and report them via the record_contract "
    "tool. Use ONLY what the text supports — if a field is absent, return an empty "
    "string, empty array, or false. Never invent parties, dates, or figures."
)

_TOOL = {
    "name": "record_contract",
    "description": "Record the structured fields extracted from a B2B contract.",
    "input_schema": RECORD_SCHEMA,
}


class LLMUnavailable(Exception):
    pass


def make_client():
    """Return an Anthropic client, or raise LLMUnavailable with a clear reason."""
    try:
        from anthropic import Anthropic
    except ImportError as exc:
        raise LLMUnavailable("anthropic SDK not installed (pip install anthropic)") from exc
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise LLMUnavailable("ANTHROPIC_API_KEY not set")
    return Anthropic()


def llm_extract(client, model: str, text: str, max_chars: int) -> dict:
    resp = client.messages.create(
        model=model,
        max_tokens=1024,
        system=_SYSTEM,
        tools=[_TOOL],
        tool_choice={"type": "tool", "name": "record_contract"},
        messages=[{"role": "user",
                   "content": "Extract the fields from this contract:\n\n" + text[:max_chars]}],
    )
    for block in resp.content:
        if getattr(block, "type", None) == "tool_use":
            data = dict(EMPTY_FIELDS)
            data.update(block.input or {})
            return data
    raise RuntimeError("model returned no tool_use block")


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def iter_records(input_dir: Path, category: str | None):
    raw = input_dir / "raw"
    if not raw.exists():
        sys.exit(f"No raw/ dir under {input_dir}. Run scrape_contracts.py first.")
    for jf in sorted(raw.rglob("*.json")):
        try:
            rec = json.loads(jf.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if category and rec.get("category") != category:
            continue
        if rec.get("text"):
            yield rec


def carry_metadata(rec: dict) -> dict:
    """Source metadata to keep alongside the extracted fields."""
    keys = ("id", "source", "category", "url", "company", "form",
            "file_date", "matched_query", "title", "word_count")
    return {k: rec[k] for k in keys if k in rec}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Extract structured fields from scraped B2B agreements into agreements.jsonl")
    ap.add_argument("--input", default="output", help="Knowledge-base dir (with raw/) [default: output]")
    ap.add_argument("--out", help="Output JSONL [default: <input>/agreements.jsonl]")
    ap.add_argument("--category", default="real-agreements",
                    help="Only process records in this category ('' for all) [default: real-agreements]")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"Anthropic model [default: {DEFAULT_MODEL}]")
    ap.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS,
                    help="Max contract chars sent to the LLM per doc")
    ap.add_argument("--max", type=int, help="Only process the first N agreements")
    ap.add_argument("--no-llm", action="store_true", help="Heuristics only (no API key / network)")
    args = ap.parse_args(argv)

    input_dir = Path(args.input)
    out_path = Path(args.out) if args.out else input_dir / "agreements.jsonl"
    category = args.category or None

    # Choose backend.
    client = None
    if not args.no_llm:
        try:
            client = make_client()
            print(f"[llm] using {args.model}")
        except LLMUnavailable as exc:
            print(f"[llm] unavailable ({exc}); falling back to heuristics")
    else:
        print("[heuristics] --no-llm set")

    records = list(iter_records(input_dir, category))
    if args.max:
        records = records[: args.max]
    if not records:
        print(f"No records in category {category!r} under {input_dir}/raw. Nothing to do.")
        return 0

    print(f"Processing {len(records)} agreement(s) -> {out_path}")
    n_llm = n_heur = 0
    with out_path.open("w", encoding="utf-8") as fh:
        for i, rec in enumerate(records, 1):
            fields, method = None, "heuristic"
            if client is not None:
                try:
                    fields = llm_extract(client, args.model, rec["text"], args.max_chars)
                    method = "llm"
                    n_llm += 1
                except Exception as exc:                # per-doc resilience
                    print(f"  [{i}] LLM failed ({type(exc).__name__}: {exc}); using heuristics")
            if fields is None:
                fields = heuristic_extract(rec["text"])
                n_heur += 1
            if not fields.get("agreement_type"):
                fields["agreement_type"] = rec.get("matched_query") or rec.get("title") or ""
            row = {**carry_metadata(rec), **fields, "extraction_method": method}
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            label = (fields.get("agreement_type") or rec.get("title") or rec.get("url"))[:60]
            print(f"  [{i}/{len(records)}] ({method}) {label}")

    print(f"\nDone. {len(records)} row(s) -> {out_path}  (llm={n_llm}, heuristic={n_heur})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
