# SEC EDGAR Market Benchmark

> Data-backed clause benchmarks mined from **370 real executed B2B agreements** (SEC EDGAR exhibit-10 material contracts) collected by this scraper. Generated 2026-06-21. This is a **directional** read of market practice from a small, automated sample — not a substitute for a professional benchmarking service.

**Read the caveats at the bottom before quoting any figure.**


## Sample composition

- **370** agreements — **270** full agreements + **100** amendments (27% are amendments, which don't restate clauses).
- **245** distinct filers · median length **4,953 words**.
- Filing years: 2026 (6), 2025 (10), 2024 (12), 2023 (8), 2022 (11), 2021 (11), 2020 (7), 2019 (10), 2018 (13), 2017 (13), 2016 (14), 2015 (13), 2014 (15), 2013 (11), 2012 (14), 2011 (24), 2010 (26), 2009 (17), 2008 (14), 2007 (14), 2006 (16), 2005 (18), 2004 (17), 2003 (19), 2002 (15), 2001 (22).

**By contract type (search query that surfaced it):**

| Agreement type | Count |
|---|---|
| Consulting Agreement | 23 |
| Manufacturing And Supply Agreement | 23 |
| Master Supply Agreement | 23 |
| End User License Agreement | 23 |
| Master Services Agreement | 23 |
| Statement Of Work | 23 |
| Software As A Service Agreement | 23 |
| Reseller Agreement | 23 |
| Software License Agreement | 23 |
| Value Added Reseller Agreement | 23 |
| Master Purchase Agreement | 23 |
| Strategic Alliance Agreement | 23 |
| Distribution Agreement | 23 |
| Professional Services Agreement | 23 |
| Subscription Agreement | 23 |
| Joint Development Agreement | 15 |
| Licensing Agreement | 10 |

## Clause presence — % of the 270 full agreements

_Keyword detection; counts the clause's presence, not its strength. Computed over full agreements only (amendments excluded)._

| Clause | Present | % |
|---|---|---|
| termination | 251/270 | 93% |
| assignment | 242/270 | 90% |
| governing law | 236/270 | 87% |
| confidentiality | 235/270 | 87% |
| warranty | 220/270 | 81% |
| indemnification | 204/270 | 76% |
| payment terms | 162/270 | 60% |
| intellectual property | 161/270 | 60% |
| insurance | 132/270 | 49% |
| limitation of liability | 130/270 | 48% |
| force majeure | 117/270 | 43% |
| consequential-damages waiver | 117/270 | 43% |
| arbitration | 91/270 | 34% |
| auto-renewal | 68/270 | 25% |
| non-solicitation | 27/270 | 10% |
| data protection | 23/270 | 9% |

## Governing law — where detectable (223/270 agreements)

| Jurisdiction | Count | % of detected |
|---|---|---|
| New York | 53 | 24% |
| California | 34 | 15% |
| Delaware | 30 | 13% |
| Nevada | 19 | 9% |
| Texas | 13 | 6% |
| Florida | 8 | 4% |
| England and Wales | 5 | 2% |
| New Jersey | 4 | 2% |
| Illinois | 4 | 2% |
| Georgia | 4 | 2% |
| Massachusetts | 3 | 1% |
| Pennsylvania | 3 | 1% |

## Payment terms — where stated (10/270 agreements)

| Net terms | Count |
|---|---|
| Net 30 | 8 |
| Net 15 | 1 |
| Net 11 | 1 |

## Headline indicators (full agreements)

| Indicator | Share |
|---|---|
| Contains a limitation-of-liability / cap clause | 45% |
| Contains auto-renewal / evergreen language | 30% |
| Contains an arbitration clause | 34% |
| References cross-border sale-of-goods (CISG/Incoterms) | 19% |

## Methodology & limitations

- **Sample.** 370 documents pulled via SEC EDGAR full-text search, filtered to **EX-10 ("Material Contracts") exhibits** matching this scraper's B2B contract-type query taxonomy (MSA, supply, reseller, distribution, licensing, SaaS, SOW, etc.). It is **not** a random or representative sample of all B2B contracts — it skews to public-company filings and to the queried agreement types.
- **Small N.** Treat every figure as directional. Percentages move materially with a few documents at this sample size.
- **Amendments excluded** from clause/term stats: many EDGAR hits are short amendments (100 here) that don't restate clauses; including them would understate clause presence.
- **Temporal skew.** Full-text search surfaced many older filings in this sample, so modern clauses (data protection/privacy, AI terms) are under-represented relative to contracts signed today — note the low data-protection share above.
- **Governing law caveat.** The jurisdiction scan can pick up a party's *state of incorporation* (e.g. Nevada/Delaware) rather than the choice-of-law state; read the distribution as indicative, not exact.
- **Automated detection.** Clause *presence* uses keyword matching (reliable-ish); governing law uses a jurisdiction-near-cue scan; payment terms use a `Net N` regex. Specific **values** (cap multiples, exact renewal terms) are not reliably extractable by regex and are intentionally not reported as precise figures.
- **Reproducible.** Regenerate with `python scripts/benchmark_edgar.py` after expanding the corpus (raise `max_pages`/`per_query` for the EDGAR source in `sources.yaml`); a larger N makes these figures meaningfully stronger.

*Source agreements are US-government public-domain SEC filings. This report is a research aid, not legal advice.*
