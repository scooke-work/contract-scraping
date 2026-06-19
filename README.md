# B2B Contracts Knowledge Scraper

[![tests](https://github.com/scooke-work/contract-scraping/actions/workflows/tests.yml/badge.svg)](https://github.com/scooke-work/contract-scraping/actions/workflows/tests.yml)

A polite, reusable Python tool that scrapes authoritative sources on **business-to-business
(B2B) contracts and contracting** and turns them into clean, structured data an LLM can
ingest directly (RAG / embeddings), plus an optional **structured-extraction** pass that
turns *real executed agreements* into one row of fields per contract.

It is **polite by design**: it obeys every site's `robots.txt`, rate-limits per host,
identifies itself with a descriptive User-Agent, and extracts only the main article
text (navigation, ads, and boilerplate are stripped out).

> **It never stores raw contract files.** PDF/Word exhibits are parsed to *text in memory*
> and discarded — only the extracted text + metadata are kept on disk.

## What it produces

After a run, everything lands in the `output/` folder:

| File | Purpose |
|------|---------|
| `chunks.jsonl` | One overlapping, paragraph-aware text chunk per line, with metadata — **ready for embeddings / RAG / LLM ingestion**. |
| `agreements.jsonl` | *(from `extract_structured.py`)* One **structured row per real agreement**: parties, governing law, term, clause inventory, etc. |
| `knowledge_base.md` | A single human-readable digest of everything collected, grouped by source. |
| `raw/<source>/*.json` | One clean record per page (full text + title, URL, date, word count, fetched-at). |
| `manifest.json` | Summary of the run: pages, chunks, and per-source counts. |

## Install

Requires **Python 3.9+**.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt          # core scraper (incl. PDF/Word parsing)
# For the structured-extraction pass + tests:
pip install -r requirements-dev.txt
```

## Use — scrape

```bash
# Crawl every source in sources.yaml
python scrape_contracts.py

# See what's configured without crawling
python scrape_contracts.py --list

# Crawl just one source (repeatable)
python scrape_contracts.py --source "Cornell LII"

# Cap pages per source (good for a quick test)
python scrape_contracts.py --max-pages 5

# Add to an existing knowledge base instead of rebuilding (dedups by URL)
python scrape_contracts.py --append --source "SEC EDGAR Contracts"

# Skip PDF/Word exhibits entirely instead of parsing their text
python scrape_contracts.py --no-binaries

# Write somewhere else
python scrape_contracts.py --output ./my_kb
```

Re-run any time to refresh. A plain run **rebuilds** the digest/chunks/manifest from
scratch; `--append` loads the existing corpus, fetches only URLs you don't already have,
and rewrites the derived files from the union.

## Use — structured extraction (real agreements)

`extract_structured.py` is a **decoupled post-pass**. It reads the `real-agreements`
records under `output/raw/` and writes one structured row per contract to
`output/agreements.jsonl`:

```bash
# LLM-backed if the Anthropic SDK is installed AND ANTHROPIC_API_KEY is set:
export ANTHROPIC_API_KEY=sk-ant-...
python extract_structured.py

# No API key? Runs automatically in heuristic mode (regex/keyword, no network):
python extract_structured.py --no-llm

# Cheaper/faster model, or only the first N agreements:
python extract_structured.py --model claude-haiku-4-5-20251001 --max 10
```

Each row carries the source metadata (`company`, `form`, `file_date`, `url`, …) plus
extracted fields: `parties`, `agreement_type`, `effective_date`, `governing_law`, `term`,
`auto_renewal`, `termination`, `liability_cap`, `indemnification`, `confidentiality`,
`payment_terms`, `clause_inventory`, `summary`, and `extraction_method` (`llm`|`heuristic`).

The LLM backend forces a schema-validated tool call (no brittle JSON parsing) and is
**resilient per-document**: if a single call fails it falls back to heuristics for that
contract rather than aborting the run. The core scraper has **zero LLM dependencies** —
this pass is entirely optional.

The **heuristic backend** (no key, no network) extracts the clause inventory,
indemnity/confidentiality flags, payment terms, effective date, agreement type, term, and
— with reasonable precision — parties (entity-name parsing that skips "a Delaware
corporation"-style descriptors) and governing law (matched against a list of real
jurisdictions, preferring the choice-of-law clause over a party's state of incorporation).
It first strips EDGAR's SGML/filename header noise. It's best-effort: recall is lower than
the LLM's, and genuinely silent fields stay empty — many EDGAR hits are short *amendments*
that don't restate parties/term/governing law, so empty there is correct, not a miss.

## The sources

`sources.yaml` ships with a curated, scraping-tolerant set:

- **Cornell Legal Information Institute** — primary US law: UCC Article 2 (sale of goods,
  the core of B2B commerce) plus Wex entries on contracts, breach, indemnity, force
  majeure, and warranties. *Followed (crawls related pages).*
- **Wikipedia** — broad conceptual coverage: MSAs, SOWs, SLAs, NDAs, Incoterms,
  liquidated damages, contract management, procurement, RFPs, and more.
- **CISG (Trans-Lex)** — the full inline text of the UN Convention on Contracts for the
  International Sale of Goods, the governing framework for cross-border B2B sale-of-goods
  contracts. *(The former `iicl.law.virginia.edu` host is defunct; Trans-Lex carries the
  complete article text on one page.)*
- **Investopedia** — *disabled*: returns HTTP 403 to automated clients, so it's
  commented out in `sources.yaml` rather than evaded. Concepts are covered by
  Cornell LII + Wikipedia.
- **SEC EDGAR Contracts** — **real executed B2B agreements** from public-company filings
  (exhibit-10 material contracts). Queries EDGAR full-text search across an 18-phrase
  contract taxonomy (MSA, supply, reseller, distribution, licensing, SaaS, SOW, OEM,
  strategic alliance, …) and pulls the actual documents, so the knowledge base contains
  authentic clause language, not just theory.

### About the EDGAR source

A different *kind* of source (`type: edgar`) that searches rather than crawls seeds:

```yaml
- name: "SEC EDGAR Contracts"
  category: "real-agreements"
  type: edgar
  max_pages: 24          # total agreements to collect (bump to sample more)
  per_query: 3           # cap per query (keeps variety across the taxonomy)
  forms: ["8-K", "10-K", "10-Q", "S-1"]
  # start_date: "2018-01-01"   # optional date window (EDGAR FTS covers 2001-present)
  # end_date:   "2025-12-31"
  queries:
    - "master services agreement"
    - "reseller agreement"
    # ...add any contract type you want real examples of
```

EDGAR records carry extra metadata (`company`, `form`, `file_date`, `matched_query`).
Real contracts are long, so they produce many chunks — keep `max_pages` modest at first.
The SEC asks automated clients to send a descriptive User-Agent with a contact email —
set `config.edgar_user_agent` at the top of `sources.yaml`.

### PDF / Word exhibits

Most EDGAR exhibits are HTML. When one is a **PDF or Word** document, it is fetched and
parsed to **text in memory** (`pdfminer.six` / `python-docx`); the binary is **never
written to disk**. Toggle with `config.parse_binaries` (or `--no-binaries` to skip them).
Exhibits larger than `config.max_binary_mb` are skipped.

## Adding your own sources

Edit `sources.yaml`. Each source supports:

```yaml
- name: "Some Source"
  category: "concepts"            # label kept on every record/chunk
  seeds:                          # starting URLs (always fetched)
    - "https://example.com/start"
  allowed_domains:                # crawl never leaves these (optional)
    - "example.com"
  follow_links: true              # follow in-domain links? default false
  max_pages: 40                   # cap for this source
  include_patterns:               # regex a URL must match to be followed
    - "example\\.com/articles/"
  exclude_patterns:               # regex that disqualifies a URL
    - "(login|\\?|#)"
```

Global knobs (rate limit, chunk size, binary parsing, etc.) live under the `config:`
block at the top of `sources.yaml`.

## Tests

Offline unit tests (no network) cover the crawler helpers, the chunker, EDGAR URL
construction, append/dedup, DOCX parsing, and the structured-extraction backends:

```bash
python -m pytest -q
```

## Architecture & roadmap

Lightweight by default: `requests` + `trafilatura` (+ `BeautifulSoup` for link
discovery). The fetch step is the only host-specific part, which keeps a **hybrid**
escalation path open: a headless-browser (Playwright) fetcher can be slotted in behind
the same pipeline for any future JS-rendered source (e.g. vendor/CLM product sites).
That renderer is **not wired yet** — every source currently configured is static HTML,
so nothing needs it.

```
sources.yaml -> crawl/search -> fetch -> extract -> chunk -> write
                                  |                            |-> chunks.jsonl       (RAG)
                       requests (now) / Playwright (future)    |-> knowledge_base.md  (digest)
                                                               |-> raw/*.json + manifest.json
                                          extract_structured.py -> agreements.jsonl   (structured)
```

## Notes & good citizenship

- Pages disallowed by a site's `robots.txt` are skipped automatically and logged.
- The default delay is 1.5s between hits to the same host. Lower it only for sites you
  control or have permission to crawl faster. (SEC asks for ≤10 req/s aggregate.)
- Scraped text is for **research / knowledge** use. Respect each source's terms and
  copyright before redistributing collected content.

## Reference

- [`docs/negotiation-playbook.md`](docs/negotiation-playbook.md) — **B2B Contracts: Where
  Vendors Start vs. Where Deals Land** — a 25-clause negotiation playbook: vendor opening
  positions vs. typical post-negotiation landings, with rationale and key levers (partly
  grounded in the scraped EDGAR agreements).
- [`docs/vendor-defense-playbook.md`](docs/vendor-defense-playbook.md) — **Vendor-Defense
  Playbook** — the vendor-side cheat-sheet for the same 25 clauses: opening ask, fallback
  ladder (give → get), red lines, and escalation triggers, plus an approval/escalation
  matrix and a deal-breaker red-lines quick reference.

## License

MIT — see [LICENSE](LICENSE). This licenses the **scraper code**, not any content you
collect with it: EDGAR filings are US-government public domain, but Wikipedia (CC-BY-SA),
Trans-Lex, and Cornell LII carry their own terms — keep that in mind before redistributing
a scraped corpus.
