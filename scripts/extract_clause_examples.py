#!/usr/bin/env python3
"""
extract_clause_examples.py
==========================

Mine the scraped SEC EDGAR agreements (``output/raw/sec-edgar-contracts/*.json``) for
**verbatim, real-world clause excerpts** and write them to ``docs/real-clause-examples.md``,
attributed to the filer. The companion to the (idealized) clause bank — this is the real,
sometimes-messy thing as it appears in executed contracts.

Reproducible:

    python scripts/extract_clause_examples.py
    python scripts/extract_clause_examples.py --per-clause 2 --maxchars 600
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import extract_structured as es  # noqa: E402

# clause -> ordered list of anchor regexes (first match wins as the excerpt start)
CLAUSES = [
    ("Limitation of Liability", [r"in no event (?:shall|will) (?:either party|any party|a party|provider|the company|licensor)", r"\bliabilit[a-z]*[^.]{0,40}(?:exceed|capped)\b", r"limitation of liability"]),
    ("Exclusion of Consequential Damages", [r"in no event[^.]{0,60}(?:indirect|consequential)", r"(?:indirect|consequential)[^.]{0,30}damages"]),
    ("Indemnification", [r"shall (?:indemnify|defend(?:,| and) indemnify)", r"agrees to indemnify", r"\bindemnification\b"]),
    ("Warranty Disclaimer", [r'\bas is\b', r"disclaims all", r"warranties of merchantability", r"no warranties"]),
    ("Confidentiality", [r'"confidential information" (?:means|shall mean)', r"confidential information.{0,40}means", r"\bconfidentiality\b"]),
    ("Governing Law", [r"(?:governed by|construed in accordance)[^.]{0,60}laws of", r"governing law"]),
    ("Term & Auto-Renewal", [r"automatically renew", r"shall (?:continue|remain) in (?:full )?(?:force and )?effect", r"initial term"]),
    ("Termination", [r"may terminate this agreement", r"terminate this agreement (?:upon|for|if)"]),
    ("Force Majeure", [r"force majeure"]),
    ("Assignment", [r"(?:may not|shall not) assign", r"neither party may assign", r"assign this agreement"]),
    ("Payment Terms", [r"net (?:thirty|30|forty-five|45|sixty|60)\b", r"payment terms", r"shall be due (?:and payable )?within"]),
    ("Entire Agreement", [r"entire agreement", r"constitutes the entire"]),
]


def load(input_dir):
    out = []
    for f in sorted(glob.glob(os.path.join(input_dir, "raw", "sec-edgar-contracts", "*.json"))):
        try:
            out.append(json.load(open(f, encoding="utf-8")))
        except (OSError, json.JSONDecodeError):
            pass
    return out


def excerpt_at(text, start, maxchars):
    seg = text[start:start + maxchars].strip()
    # trim to the last sentence end so we don't cut mid-thought
    cut = max(seg.rfind(". "), seg.rfind("; "), seg.rfind(". ") )
    if cut >= 150:
        seg = seg[:cut + 1]
    return seg.strip()


def score(seg):
    s = 0.0
    n = len(seg)
    if 250 <= n <= 600:
        s += 3
    if n < 180:
        s -= 4
    if seg.endswith((".", ";")):
        s += 2
    if re.search(r"by their nature|shall survive|which survive|intended to survive", seg, re.I):
        s -= 3                             # demote survival-clause lists (not the substantive clause)
    s -= (seg.count("[") + seg.count("]") + seg.count("*") + seg.count("•")) * 1.5
    letters = [c for c in seg if c.isalpha()]
    if letters:
        upper = sum(1 for c in letters if c.isupper()) / len(letters)
        if upper > 0.6:                  # penalize ALL-CAPS run-ons
            s -= 3
    if seg[:1].isalpha():
        s += 1
    return s


def company_of(rec):
    return (str(rec.get("company", "")).split("  (")[0]).strip() or "Unknown filer"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Extract real clause excerpts from the EDGAR corpus.")
    ap.add_argument("--input", default="output")
    ap.add_argument("--out", default="docs/real-clause-examples.md")
    ap.add_argument("--per-clause", type=int, default=3)
    ap.add_argument("--maxchars", type=int, default=620)
    args = ap.parse_args(argv)

    recs = load(args.input)
    if not recs:
        sys.exit(f"No EDGAR records under {args.input}/raw/sec-edgar-contracts/. Run the scraper first.")
    texts = [(r, re.sub(r"\s+", " ", es._strip_edgar_header(r.get("text", "")))) for r in recs]

    gen = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    L = []
    L.append("# Real Clause Examples — from SEC EDGAR\n")
    L.append(f"> Verbatim clause excerpts pulled from the real executed agreements in this "
             f"scraper's corpus ({len(recs)} EX-10 material contracts), attributed to the filer. "
             f"Generated {gen}. These are the **real, sometimes-messy** thing — the companion to "
             f"the idealized [clause bank](clause-library.md). Excerpts are lightly trimmed to a "
             f"sentence boundary; source agreements are public-domain SEC filings. Illustrative, "
             f"not endorsed templates, and not legal advice.\n")

    total = 0
    for clause, anchors in CLAUSES:
        cand = []
        seen_co = set()
        for rec, t in texts:
            m = None
            for a in anchors:
                m = re.search(a, t, re.I)
                if m:
                    break
            if not m:
                continue
            seg = excerpt_at(t, m.start(), args.maxchars)
            if len(seg) < 160:
                continue
            cand.append((score(seg), company_of(rec), seg, rec))
        cand.sort(key=lambda c: c[0], reverse=True)
        picks = []
        for sc, co, seg, rec in cand:
            if co in seen_co:
                continue
            seen_co.add(co)
            picks.append((co, seg, rec))
            if len(picks) >= args.per_clause:
                break
        if not picks:
            continue
        L.append(f"\n## {clause}\n")
        for co, seg, rec in picks:
            disp = seg if len(seg) <= args.maxchars else seg[:args.maxchars] + "…"
            atype = (str(rec.get("matched_query", "")) or "Agreement").title()
            form = rec.get("form", "")
            date = rec.get("file_date", "")
            url = rec.get("url", "")
            L.append(f"> {disp}\n>\n> — *{atype} · {co} · {form} · {date}* · [SEC filing]({url})\n")
            total += 1

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    open(args.out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"Wrote {args.out} — {total} excerpts across {sum(1 for c,_ in CLAUSES)} clause types, from {len(recs)} agreements")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
