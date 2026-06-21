# SEC EDGAR Market Benchmark

> Data-backed clause benchmarks mined from **120 real executed B2B agreements** (SEC EDGAR exhibit-10 material contracts) collected by this scraper. Generated 2026-06-21. This is a **directional** read of market practice from a small, automated sample — not a substitute for a professional benchmarking service.

**Read the caveats at the bottom before quoting any figure.**


## Sample composition

- **120** agreements — **78** full agreements + **42** amendments (35% are amendments, which don't restate clauses).
- **83** distinct filers · median length **3,685 words**.
- Filing years: 2026 (2), 2025 (4), 2024 (4), 2023 (4), 2022 (2), 2021 (4), 2020 (4), 2019 (5), 2018 (3), 2017 (3), 2016 (4), 2015 (4), 2014 (1), 2013 (6), 2012 (3), 2011 (7), 2010 (7), 2009 (6), 2008 (7), 2007 (4), 2006 (7), 2005 (6), 2004 (4), 2003 (8), 2002 (4), 2001 (7).

**By contract type (search query that surfaced it):**

| Agreement type | Count |
|---|---|
| Master Services Agreement | 8 |
| Statement Of Work | 8 |
| Consulting Agreement | 8 |
| End User License Agreement | 8 |
| Reseller Agreement | 8 |
| Value Added Reseller Agreement | 8 |
| Manufacturing And Supply Agreement | 8 |
| Master Purchase Agreement | 8 |
| Software License Agreement | 8 |
| Professional Services Agreement | 8 |
| Distribution Agreement | 8 |
| Master Supply Agreement | 8 |
| Software As A Service Agreement | 8 |
| Subscription Agreement | 8 |
| Strategic Alliance Agreement | 8 |

## Clause presence — % of the 78 full agreements

_Keyword detection; counts the clause's presence, not its strength. Computed over full agreements only (amendments excluded)._

| Clause | Present | % |
|---|---|---|
| confidentiality | 70/78 | 90% |
| termination | 69/78 | 88% |
| assignment | 66/78 | 85% |
| governing law | 65/78 | 83% |
| warranty | 60/78 | 77% |
| indemnification | 55/78 | 71% |
| payment terms | 45/78 | 58% |
| intellectual property | 41/78 | 53% |
| insurance | 33/78 | 42% |
| limitation of liability | 31/78 | 40% |
| force majeure | 29/78 | 37% |
| consequential-damages waiver | 27/78 | 35% |
| auto-renewal | 21/78 | 27% |
| arbitration | 16/78 | 21% |
| non-solicitation | 5/78 | 6% |
| data protection | 5/78 | 6% |

## Governing law — where detectable (58/78 agreements)

| Jurisdiction | Count | % of detected |
|---|---|---|
| California | 14 | 24% |
| Delaware | 9 | 16% |
| Nevada | 8 | 14% |
| New York | 7 | 12% |
| Florida | 3 | 5% |
| New Jersey | 2 | 3% |
| North Carolina | 2 | 3% |
| Texas | 2 | 3% |
| Rhode Island | 1 | 2% |
| India | 1 | 2% |
| Germany | 1 | 2% |
| Singapore | 1 | 2% |

## Payment terms — where stated (7/78 agreements)

| Net terms | Count |
|---|---|
| Net 30 | 7 |

## Headline indicators (full agreements)

| Indicator | Share |
|---|---|
| Contains a limitation-of-liability / cap clause | 37% |
| Contains auto-renewal / evergreen language | 29% |
| Contains an arbitration clause | 21% |
| References cross-border sale-of-goods (CISG/Incoterms) | 13% |

## Methodology & limitations

- **Sample.** 120 documents pulled via SEC EDGAR full-text search, filtered to **EX-10 ("Material Contracts") exhibits** matching this scraper's B2B contract-type query taxonomy (MSA, supply, reseller, distribution, licensing, SaaS, SOW, etc.). It is **not** a random or representative sample of all B2B contracts — it skews to public-company filings and to the queried agreement types.
- **Small N.** Treat every figure as directional. Percentages move materially with a few documents at this sample size.
- **Amendments excluded** from clause/term stats: many EDGAR hits are short amendments (42 here) that don't restate clauses; including them would understate clause presence.
- **Temporal skew.** Full-text search surfaced many older filings in this sample, so modern clauses (data protection/privacy, AI terms) are under-represented relative to contracts signed today — note the low data-protection share above.
- **Governing law caveat.** The jurisdiction scan can pick up a party's *state of incorporation* (e.g. Nevada/Delaware) rather than the choice-of-law state; read the distribution as indicative, not exact.
- **Automated detection.** Clause *presence* uses keyword matching (reliable-ish); governing law uses a jurisdiction-near-cue scan; payment terms use a `Net N` regex. Specific **values** (cap multiples, exact renewal terms) are not reliably extractable by regex and are intentionally not reported as precise figures.
- **Reproducible.** Regenerate with `python scripts/benchmark_edgar.py` after expanding the corpus (raise `max_pages`/`per_query` for the EDGAR source in `sources.yaml`); a larger N makes these figures meaningfully stronger.

*Source agreements are US-government public-domain SEC filings. This report is a research aid, not legal advice.*
