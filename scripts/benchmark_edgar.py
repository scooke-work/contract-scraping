#!/usr/bin/env python3
"""
benchmark_edgar.py
==================

Mine the scraped SEC EDGAR agreements (``output/raw/sec-edgar-contracts/*.json``) into a
data-backed market-benchmark report (``docs/edgar-benchmark.md``): clause-presence
frequencies, governing-law distribution, payment terms, auto-renewal, and more.

Reproducible — re-run after refreshing/expanding the corpus to regenerate the report:

    python scripts/benchmark_edgar.py
    python scripts/benchmark_edgar.py --input output --out docs/edgar-benchmark.md

Detection reuses the regex/keyword + jurisdiction logic in ``extract_structured.py``, so
it is automated and *directional*: clause **presence** detection is fairly reliable;
specific **value** extraction (cap multiples, exact terms) is approximate.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone

# Reuse the shared extractors from the repo root.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import extract_structured as es  # noqa: E402

# Clause-presence signals: the extractor's set plus a consequential-waiver probe.
CLAUSE_SIGNS = dict(es._CLAUSE_SIGNS)
CLAUSE_SIGNS["consequential-damages waiver"] = [
    r"consequential damages", r"indirect[^.]{0,30}damages", r"lost profits"]


def load(input_dir: str) -> list[dict]:
    recs = []
    for f in sorted(glob.glob(os.path.join(input_dir, "raw", "sec-edgar-contracts", "*.json"))):
        try:
            recs.append(json.load(open(f, encoding="utf-8")))
        except (OSError, json.JSONDecodeError):
            pass
    return recs


def pct(n: int, d: int) -> str:
    return f"{round(100 * n / d)}%" if d else "—"


def is_amendment(rec: dict, text: str) -> bool:
    head = (str(rec.get("title", "")) + " " + str(rec.get("matched_query", "")) + " " + text[:300]).lower()
    return "amendment" in head


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Generate the EDGAR market-benchmark report.")
    ap.add_argument("--input", default="output")
    ap.add_argument("--out", default="docs/edgar-benchmark.md")
    args = ap.parse_args(argv)

    recs = load(args.input)
    N = len(recs)
    if N == 0:
        sys.exit(f"No EDGAR records under {args.input}/raw/sec-edgar-contracts/. Run the scraper first.")

    texts = [re.sub(r"\s+", " ", es._strip_edgar_header(r.get("text", ""))) for r in recs]
    lows = [t.lower() for t in texts]
    amend = [is_amendment(r, t) for r, t in zip(recs, texts)]
    n_amend = sum(amend)
    # "base" = full agreements (amendments don't restate clauses, so they understate presence)
    base_idx = [i for i in range(N) if not amend[i]]
    nb = len(base_idx)

    # --- composition ---
    types = Counter((str(r.get("matched_query", "")) or "—").title() for r in recs)
    forms = Counter((str(r.get("form", "")) or "—") for r in recs)
    years = Counter((str(r.get("file_date", ""))[:4] or "—") for r in recs)
    companies = {(str(r.get("company", "")).split("  (")[0]).strip() for r in recs}
    wcs = sorted(r.get("word_count", 0) for r in recs)
    median_wc = wcs[len(wcs) // 2] if wcs else 0

    # --- clause presence (over base agreements) ---
    clause_counts = {}
    for name, pats in CLAUSE_SIGNS.items():
        clause_counts[name] = sum(1 for i in base_idx if any(re.search(p, lows[i]) for p in pats))
    clause_sorted = sorted(clause_counts.items(), key=lambda kv: kv[1], reverse=True)

    # --- governing law (over base) ---
    gov = Counter()
    gov_found = 0
    for i in base_idx:
        j = es._extract_governing_law(texts[i])
        if j:
            gov[j] += 1
            gov_found += 1

    # --- payment terms (over base) ---
    netN = Counter()
    pay_found = 0
    for i in base_idx:
        m = es._PAYMENT.search(texts[i])
        if m:
            netN[f"Net {m.group(1)}"] += 1
            pay_found += 1

    # --- headline indicators (over base) ---
    def share(pred):
        return sum(1 for i in base_idx if pred(lows[i]))
    cap = share(lambda l: bool(re.search(r"aggregate liability|in no event shall|liability[^.]{0,40}exceed|total liability", l)))
    autoren = share(lambda l: bool(re.search(r"automatically renew|auto-?renew|renewal term|successive", l)))
    arb = clause_counts.get("arbitration", 0)
    cross = share(lambda l: ("international sale of goods" in l) or ("cisg" in l) or ("incoterms" in l))

    gen = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    L = []
    L.append("# SEC EDGAR Market Benchmark\n")
    L.append(f"> Data-backed clause benchmarks mined from **{N} real executed B2B agreements** "
             f"(SEC EDGAR exhibit-10 material contracts) collected by this scraper. "
             f"Generated {gen}. This is a **directional** read of market practice from a small, "
             f"automated sample — not a substitute for a professional benchmarking service.\n")
    L.append("**Read the caveats at the bottom before quoting any figure.**\n")

    # composition
    L.append("\n## Sample composition\n")
    L.append(f"- **{N}** agreements — **{nb}** full agreements + **{n_amend}** amendments "
             f"({pct(n_amend, N)} are amendments, which don't restate clauses).")
    L.append(f"- **{len(companies)}** distinct filers · median length **{median_wc:,} words**.")
    L.append(f"- Filing years: " + ", ".join(f"{y} ({c})" for y, c in sorted(years.items(), reverse=True) if y != "—") + ".")
    L.append("\n**By contract type (search query that surfaced it):**\n")
    L.append("| Agreement type | Count |\n|---|---|")
    for t, c in types.most_common():
        L.append(f"| {t} | {c} |")

    # clause presence
    L.append(f"\n## Clause presence — % of the {nb} full agreements\n")
    L.append("_Keyword detection; counts the clause's presence, not its strength. "
             "Computed over full agreements only (amendments excluded)._\n")
    L.append("| Clause | Present | % |\n|---|---|---|")
    for name, c in clause_sorted:
        L.append(f"| {name} | {c}/{nb} | {pct(c, nb)} |")

    # governing law
    L.append(f"\n## Governing law — where detectable ({gov_found}/{nb} agreements)\n")
    if gov:
        L.append("| Jurisdiction | Count | % of detected |\n|---|---|---|")
        for j, c in gov.most_common(12):
            L.append(f"| {j} | {c} | {pct(c, gov_found)} |")
    else:
        L.append("_No governing-law jurisdiction detected._")

    # payment terms
    L.append(f"\n## Payment terms — where stated ({pay_found}/{nb} agreements)\n")
    if netN:
        L.append("| Net terms | Count |\n|---|---|")
        for term, c in netN.most_common():
            L.append(f"| {term} | {c} |")
    else:
        L.append("_No explicit \"Net N\" payment term detected._")

    # headline indicators
    L.append("\n## Headline indicators (full agreements)\n")
    L.append("| Indicator | Share |\n|---|---|")
    L.append(f"| Contains a limitation-of-liability / cap clause | {pct(cap, nb)} |")
    L.append(f"| Contains auto-renewal / evergreen language | {pct(autoren, nb)} |")
    L.append(f"| Contains an arbitration clause | {pct(arb, nb)} |")
    L.append(f"| References cross-border sale-of-goods (CISG/Incoterms) | {pct(cross, nb)} |")

    # methodology
    L.append("\n## Methodology & limitations\n")
    L.append(f"- **Sample.** {N} documents pulled via SEC EDGAR full-text search, filtered to "
             "**EX-10 (\"Material Contracts\") exhibits** matching this scraper's B2B contract-type "
             "query taxonomy (MSA, supply, reseller, distribution, licensing, SaaS, SOW, etc.). "
             "It is **not** a random or representative sample of all B2B contracts — it skews to "
             "public-company filings and to the queried agreement types.")
    L.append("- **Small N.** Treat every figure as directional. Percentages move materially with "
             "a few documents at this sample size.")
    L.append("- **Amendments excluded** from clause/term stats: many EDGAR hits are short "
             f"amendments ({n_amend} here) that don't restate clauses; including them would "
             "understate clause presence.")
    L.append("- **Temporal skew.** Full-text search surfaced many older filings in this sample, "
             "so modern clauses (data protection/privacy, AI terms) are under-represented "
             "relative to contracts signed today — note the low data-protection share above.")
    L.append("- **Governing law caveat.** The jurisdiction scan can pick up a party's *state of "
             "incorporation* (e.g. Nevada/Delaware) rather than the choice-of-law state; read the "
             "distribution as indicative, not exact.")
    L.append("- **Automated detection.** Clause *presence* uses keyword matching (reliable-ish); "
             "governing law uses a jurisdiction-near-cue scan; payment terms use a `Net N` regex. "
             "Specific **values** (cap multiples, exact renewal terms) are not reliably extractable "
             "by regex and are intentionally not reported as precise figures.")
    L.append("- **Reproducible.** Regenerate with `python scripts/benchmark_edgar.py` after "
             "expanding the corpus (raise `max_pages`/`per_query` for the EDGAR source in "
             "`sources.yaml`); a larger N makes these figures meaningfully stronger.")
    L.append("\n*Source agreements are US-government public-domain SEC filings. This report is a "
             "research aid, not legal advice.*")

    out = args.out
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"Wrote {out} — N={N} ({nb} full, {n_amend} amendments), {len(clause_sorted)} clauses, "
          f"gov-law {gov_found}/{nb}, payment {pay_found}/{nb}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
