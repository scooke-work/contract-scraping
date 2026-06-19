# B2B Contracts: Where Vendors Start vs. Where Deals Land

> A negotiation-playbook reference for B2B SaaS / technology + professional-services
> agreements: for each major clause, the **vendor's standard opening position**, where it
> **typically lands** after a sophisticated customer negotiates, and **why**, plus the key
> levers. Several entries are grounded in real executed agreements (SEC EDGAR exhibit-10
> material contracts).
>
> **General market-practice reference, not legal advice.** Positions and enforceability
> vary by jurisdiction, industry, and deal — have counsel adapt anything here to your
> specific agreement.

A vendor's first draft is aggressive by design, not by malice. One standard paper has to scale across the entire customer base, so the vendor anchors at the lowest defensible number on every risk term and concedes upward deal-by-deal — anchoring is cheaper than re-papering and re-pricing. It retains the risk it can control and insure (its own IP, its cyber/E&O tower, its uptime), exports the risk it cannot (the customer's downstream business loss), and folds everything under a single cap and a single consequential-damages waiver to minimize the surface area sales and the CLM must track. The customer, conversely, is shifting catastrophic and uninsurable risk back onto the party that controls it — pulling data breach, IP, and confidentiality out of the general cap; capping price drift; and buying a clean exit. The landings below are the rational meeting points where each side trades what is cheap to it for what it values most.

## I. Risk Allocation

### 1. Limitation of Liability — Aggregate Cap + Supercaps
| | Position |
|---|---|
| **Vendor starts** | Single one-sided cap at **1× trailing-12-month fees** (often "fees *paid*," per-order), broad consequential-damages waiver, no carve-outs, anti-stacking, all exposure under one cap |
| **Typically lands** | Mutual general cap at **1× trailing-12-mo fees, paid-*or-payable*** with a "greater of fees or $X" year-one floor; **data/privacy supercap 2–3×** (3–5× or cyber-limit-pegged in large deals); **uncapped carve-outs**: IP indemnity, confidentiality, gross negligence/willful misconduct, fraud, death/bodily injury, payment |

**Why it lands here:** 1× trailing-12-mo fees is the genuine market default for the *general* cap, so the value isn't the multiple — it's moving high-severity heads off the 1× number. The vendor holds the general cap (insurance math), concedes a bounded supercap on catastrophic-but-insurable events, and accepts uncapped exposure where a cap is indefensible (gross negligence, willful misconduct, fraud, bodily injury) or risks "failing of its essential purpose" (UCC 2-719(2)).
**Key levers:** cap period *and* metric (paid vs. paid-or-payable) • aggregate vs. per-order • "greater of" floor • supercap multiplier/scope • cyber-limit peg • **whether carve-outs escape the consequential-damages *exclusion*, not just the dollar cap (most-missed — a "capped-and-excluded" indemnity is worthless)** • mutuality of the dollar cap • UCC 2-719(2) survival • SLA-credit sole-remedy carve-out.

### 2. Exclusion of Consequential / Indirect Damages
| | Position |
|---|---|
| **Vendor starts** | Broad mutual waiver naming lost profits/revenue/data as **own enumerated heads**, "regardless of characterization as direct or indirect," "even if a remedy fails of its essential purpose," **no carve-outs** |
| **Typically lands** | Mutual abstract waiver **survives**; lost-profits exclusion survives as a named head; customer wins **costs to recover/restore data + breach-response** as recoverable, lost profits recoverable *through* carved-out breaches (security/confidentiality/IP), carve-out list mirroring the LoL |

**Why it lands here:** The category-level mutual waiver is rational for both — neither wants open-ended liability for the other's business losses. The fight migrates to named heads and carve-outs (the *Hadley v. Baxendale* trap). Customers don't win blanket direct-lost-profit recovery; they win that third-party amounts they must *pay out* aren't swept away and post-GDPR/CCPA breach-response/forensics costs come back (usually cyber-insured anyway).
**Key levers:** true mutuality • lost profits as named head vs. indirect-only • routing losses back *via* carve-outs • "costs to recover data" (won) vs. "value of lost data" (excluded) • third-party amounts as direct • FOEP language • ALL-CAPS conspicuousness (UCC 2-316/2-719).

### 3. Indemnification (IP infringement + third-party claims)
| | Position |
|---|---|
| **Vendor starts** | One-way (vendor→customer), narrow ("issued" US patents, no trademark/trade-secret), absolute exclusions, vendor-controlled defense + sole settlement, indemnity **trapped under the 1× cap** |
| **Typically lands** | **Mutual**; patent/copyright/trademark + trade-secret; exclusions trimmed to "to the extent"; **carved out of the consequential-damages exclusion** (near-universal); **dollar treatment = super-cap 2–3×** (5× high end; uncapped is enterprise, not mid-market default); notice-and-prejudice; substance-based settlement consent |

**Why it lands here:** Keep two cap questions distinct. (a) Carving the indemnity out of the *consequential-damages exclusion* is uncontested — without it, defense costs/settlements are barred as "indirect" and the indemnity is illusory. (b) The contested one is the *dollar cap*, and the honest mid-market answer is a **super-cap (2–3×), not uncapped** — unlimited is the line insurers/reserves can't price. Defense control stays with the indemnitor (it pays, protects its installed base).
**Key levers:** mutuality • infringe vs. infringe-or-misappropriate; issued vs. pending patents • "defend" from tender vs. mere "indemnify" • remedy ladder (procure/modify/terminate) • **two distinct cap questions** • super-cap sizing • notice-and-prejudice • separate counsel on conflict • settlement consent • AI-output/open-source indemnity.

### 4. Warranties & Disclaimers
| | Position |
|---|---|
| **Vendor starts** | Thin express warranty ("**substantially** in accordance with Documentation," vendor URL, short window), AS-IS disclaimer of all implied warranties, re-perform/refund **sole remedy**, beta/AI fully AS-IS |
| **Typically lands** | Firms to "**materially** in accordance," pinned to a dated Documentation version, **continuous for the full subscription term** (SaaS); added bilateral warranties (authority, compliance-with-law, anti-malware/no-disabling-code, security exhibit); disclaimer survives but loses **non-infringement**; sole-remedy non-exclusive for security/IP/confidentiality; chronic-failure termination + refund |

**Why it lands here:** The customer concedes the AS-IS disclaimer and "no uninterrupted/error-free" (bulletproof between merchants; uptime → SLA, bugs → conformity warranty) and spends leverage on the "except as expressly stated" subordination so the disclaimer can't gut the SLA/security/compliance promises, plus a chronic-failure exit. SaaS *performance* warranties are coterminous with the term; only IP/title/authority/no-malicious-code reps durably survive.
**Key levers:** "substantially" vs. "materially" • Documentation pinned vs. URL • full-term vs. delivery-window • non-infringement/title struck from disclaimer • "except as expressly stated" subordination • SLA-vs-warranty boundary • sole-remedy escapes • bilateral warranties • beta/AI carve-outs • survival.

## II. IP & Data

### 5. IP Ownership & License Grant
| | Position |
|---|---|
| **Vendor starts** | Expansive "Vendor Technology" sweeping in anything "generic/reusable"; broad **feedback** assignment; **residuals** clause (no trade-secret carve-out); AI reservation to train on Customer Data, vendor owns Output |
| **Typically lands** | Clean split: each retains background IP; custom deliverables **present-tense "hereby assigns" + work-for-hire backup**; customer data/CI **never** vendor IP; feedback **license** survives (CI excluded); **residuals deleted or trade-secret-carved**; AI: **no training on customer data without consent** (opt-out floor; opt-in now the enterprise floor), Output to customer |

**Why it lands here:** The vendor can't give up platform ownership (the whole business + insurability line), so customers stop fighting for it and win what they care about: their data never becoming vendor IP, bespoke work assigned, control over training. The feedback license survives (existential to roadmap, near-costless to customer). "Hereby assigns + WFH backup" because work-for-hire alone fails for software (outside the nine 17 U.S.C. 101 categories).
**Key levers:** scope of "Vendor Technology" • **AI training rights (opt-out vs. opt-in; de-identified only) — often deal-defining** • Output ownership • present-tense assignment + WFH recital • custom-vs-platform split + license-back • feedback license vs. assignment • residuals • resist joint ownership • IP indemnity uncapped + indefinite survival.

### 6. Confidentiality
| | Position |
|---|---|
| **Vendor starts** | Mutual-but-tilted; objective "reasonably understood to be confidential" (no marking); **term + 3 (or 5) yrs** tail **+ indefinite trade-secret carve-out**; sometimes residuals |
| **Typically lands** | Balanced/mutual; objective standard **stays** (market norm); **term + 3 yrs modal** (5 = customer-favorable); trade secrets indefinite; **regulated/personal data protected as long as retained**; residuals deleted/narrowed; return-or-destroy + certification + backup carve-out; breach **super-capped**, uncapped for trade-secret theft/willful breach/security incidents |

**Why it lands here:** One of the least leverage-sensitive clauses — both disclose, so it resolves to market norms. The objective no-marking standard and indefinite trade-secret carve-out are *alignment*, not concessions (a fixed expiry risks forfeiting trade-secret status under DTSA/UTSA). Super-cap-plus-targeted-uncapped because unbounded exposure for an inadvertent slip is uninsurable.
**Key levers:** survival tail (2/3/5 yrs) • indefinite trade-secret carve-out • residuals • customer regulated-data carve-out • "at least as protective" recipients • compelled-disclosure mechanics • return/destroy + certification • **super-cap with uncapped trade-secret/willful/security exceptions** • injunctive relief/no-bond.

### 7. Data Protection, Privacy & Security (DPA)
| | Position |
|---|---|
| **Vendor starts** | Vendor form DPA via URL; breach notice "without undue delay" after vendor **confirms**; **general** subprocessor authorization; "commercially reasonable" security; **no on-site audit**; privacy losses **under the 1× cap** |
| **Typically lands** | Notice "**no later than 72 (often 48) hrs** from becoming **aware**" + content + assist; general authorization stays **+ push notice + 30-day objection** + terminate-affected-service; vendor **directly liable for subprocessors**; **maintains** SOC 2 Type II/ISO 27001 + lapse hook; report-first audit + for-cause backstop; privacy losses to a **2–3× super-cap** (cyber-pegged) **+ carved out of the consequential waiver** |

**Why it lands here:** The customer-as-controller owes its *own* regulator a 72-hr GDPR Art. 33 notice, so a defined processor clock is a necessity — but 24h is over-asked; because the GDPR text says "without undue delay" for the processor leg, vendors hold 48–72h. Subprocessor general-authorization-plus-objection is the Art. 28 equilibrium (delegate the work, not the responsibility). Super-cap because an uncapped breach is uninsurable while 1× fees is derisory against the customer's own fines.
**Key levers:** notice trigger + clock (aware vs. confirm) • assist costs • subprocessor model + objection window • **vendor direct liability for subs** • "maintains" + lapse hook • audit (report-only vs. on-site) • **super-cap + consequential carve-out** • SCCs/IDTA/DPF + TIA + roles • return/deletion + DSR assist • **no-AI-training/no-secondary-use covenant (sharpest 2025–26 lever)**.

## III. Commercial Terms

### 8. Payment Terms & Late Fees
| | Position |
|---|---|
| **Vendor starts** | Net 30, annual-in-advance, non-refundable, **no set-off**; **1.5%/mo (18% p.a.) or max-by-law**, auto-accruing; pay-first-dispute-later; broad suspension on any past-due; one-way attorneys' fees |
| **Typically lands** | Net 30–45 (60 large/regulated); interest **only on undisputed amounts after notice + 10–15 day cure**; **good-faith dispute carve-out**; suspension narrowed to undisputed/post-cure + SLA tolling; no-set-off retained but **customer may apply earned SLA credits**; fees mutual or struck |

**Why it lands here:** The vendor keeps its cash-flow architecture (advance billing, no-set-off for receivables financing, a real deterrent); the customer kills the traps that turn a billing error into a service cutoff. The dispute carve-out is near-universal — no sophisticated buyer lets a contested invoice suspend a business-critical system — and the vendor concedes it cheaply. The usury "whichever is less" qualifier is a non-negotiable backstop (UK/EU: must clear the Late Payment Act/Directive 2011/7).
**Key levers:** net period + invoice-date vs. conforming-invoice clock • **good-faith dispute carve-out (must exist)** • rate + usury qualifier • accrual auto vs. notice+cure • suspension notice/cure/undisputed-only • set-off vs. SLA-credit set-off • prepay/multi-year discount • collection costs • tax gross-up.

### 9. Price / Fee Escalation at Renewal
| | Position |
|---|---|
| **Vendor starts** | "**Greater of 5–7% or CPI**," CPI uncapped/loose, applied to **list/then-current** rates (silent discount clawback), auto-renew + long notice |
| **Typically lands** | **Fixed cap ~3–5%** (5% common enterprise; 3% large; 0% largest); "greater of" flipped to "**lesser of CPI and X%**"/hard ceiling; CPI **pinned to a named BLS index** if it survives; **calculated off the customer's discounted rate** (highest-value, lowest-resistance ask); first renewal often flat; anti-compounding |

**Why it lands here:** 3–5% is the genuine enterprise norm, so the fight is closing the vendor's tail risk (uncapped / whichever-is-greater), not the headline. The off-discounted-rate fix is table stakes — "fees off list" silently claws back the year-1 discount. At CPI ~3% in 2026 the cap/index/base asks don't move the median, only cap catastrophic-year exposure, so the trade clears. *Confirm the cap lives in the governing document, not just the Order Form.* (Real: Oracle support addendum 4% cap; CuraScript/Jazz MSA named BLS sub-index.)
**Key levers:** cap number • "greater of" → "lesser of" • named BLS series • **discounted-rate base vs. list (the prize)** • first-year flat / multi-year lock • anti-compounding • overage at contracted unit price • no unilateral mid-term increase • precedence • benchmarking/MFN for 5yr+ deals.

### 10. Most Favored Customer / Pricing-Parity & Benchmarking
| | Position |
|---|---|
| **Vendor starts** | **Silence, then refusal** (redirect to an escalation cap); if pushed, a hollow **price-only (list, pre-discount) MFN** with an impossible comparator, certificate-only, prospective-only, broad carve-outs, 12-mo sunset |
| **Typically lands** | One of three substitutes: **(1) most common — an escalation cap + locked multi-year pricing *instead of* parity**; (2) a narrow operable MFN (price-only, tight comparator, certificate + conditional audit; in only ~15–20% of >$500K-ACV deals); (3) benchmarking for multi-year managed-services (independent benchmarker, Year 2+, adjustment remedy) |

**Why it lands here:** The vendor gives a hard escalation cap (bounded, knowable) long before open-ended parity (an unknown, book-wide liability that makes it stop discounting), and the customer's real goal — protection from price drift — is mostly met by capped pre-locked pricing. So the cap, not the MFN, is the center of gravity. Antitrust bites only at the platform/market-power end (*BCBS Michigan*); an ordinary bilateral buyer MFN clears.
**Key levers:** **comparator definition (most outcome-determinative)** • list vs. net/effective price • carve-outs (channel/bundle most abused) • certificate vs. + audit • active-monitoring vs. passive covenant • prospective credit vs. retroactive true-up • sunset • **escalation cap as the real substitute** • benchmarking parameters • antitrust screen.

## IV. Term & Exit

### 11. Term & Auto-Renewal (Evergreen)
| | Position |
|---|---|
| **Vendor starts** | Multi-year initial term, **auto-renewal** (successive **1-year**; equal-length is the stretch), **60-day** non-renewal notice, "then-current pricing," uplift openers **7–10%+**, no convenience exit, silence = renewal |
| **Typically lands** | Evergreen usually **survives** but de-risked: equal-length → **1-year** renewals; notice **30–60 days** (60 modal), mutual + email; **uplift capped** (3–5%/CPI-ceiling) or year-2/3 fixed; renewal-reminder duty; convenience exit contested (traded away below enterprise); for-cause + cure is the floor |

**Why it lands here:** Each side trades what it values least. The vendor defends the auto-renew *default* (retention inertia) and pricing power; it concedes 1-year renewals and a 30–60 day window readily. The customer's priority isn't killing renewal but avoiding silent lock-in and an uncapped uplift — the uplift cap is highest-ROI because renewal leverage collapses once switching costs sink. Most state ARLs are consumer-facing; NY GOL 5-903's application to pure SaaS is contested — don't over-rely.
**Key levers:** initial term • **renewal length (1-yr vs. equal-length — biggest lock-in lever)** • notice window + trigger • auto-renew vs. opt-in • renewal pricing • pre-deadline reminder • convenience vs. for-cause • Order Form vs. MSA precedence • co-termination • NY GOL 5-903.

### 12. Termination
| | Position |
|---|---|
| **Vendor starts** | Asymmetric: **no customer convenience right**; cure mutual on 30-day breach **but non-payment hair-trigger (10 days/immediate suspension)**; prepaid non-refundable + acceleration; data export "on request within 30 days," proprietary format; "reasonable" T&M transition; ipso facto insolvency trigger |
| **Typically lands** | Customer rarely wins mid-term convenience; gets **trigger-based termination** (chronic SLA miss, uncured security/data breach, discontinuation, price-walk-away) + clean non-renewal; cure mutual (30-day breach, 10–15 day payment **with notice**) + dispute carve-out; **pro-rata refund** on vendor-cause; **export in non-proprietary, machine-readable format** + deletion cert; **transition assistance with rate card fixed at signing**; §365(n) escrow for on-prem |

**Why it lands here:** Vendors hold mid-term subscription convenience (it's the recognized ARR they're capitalized on); customers accept this because they get a clean exit on the vendor's *failure* plus a no-penalty non-renewal. Transition/portable export is where customers spend the most leverage — lock-in is the existential exit risk and pre-signature is the only cheap time to buy a clean exit. Ipso facto termination is generally unenforceable post-petition (§365(e)).
**Key levers:** who holds convenience • non-renewal reframe + uplift cap • exit-fee structure • cure length/symmetry + written notice before suspension • good-faith withholding carve-out • **pro-rata refund on vendor-cause** • trigger-based rights • **export format/window/cost** • deletion + cert • **transition rate card at signing** • survival • §365(n)/escrow.

### 13. Service Levels (SLA) & Uptime Credits
| | Position |
|---|---|
| **Vendor starts** | URL SLA (unilaterally amendable); **99.9%** single blended; monthly reset; credits **capped ~10–30% of one month** as **sole-and-exclusive remedy**; **30-day** claim; broad exclusions; **no SLA termination** |
| **Typically lands** | 99.9% usually **holds** (buyers win service-tiering — core 99.95%/secondary 99.5% — more than a higher blended number); top-tier credits **50–100%**; sole-remedy **narrowed to uptime + carved out of the cumulative-remedies clause**; **chronic-failure termination + pro-rata refund**; maintenance capped/pre-scheduled; claim window **60–90 days** or automatic credits |

**Why it lands here:** The uptime number rarely moves (99.9% is genuinely market; architecture is shared), so leverage shifts to the mechanics. Credits are a disguised second liability cap; the vendor concedes the chronic-failure termination right because it costs nothing if it performs and lets credits stay small. The **cumulative-remedies carve-out is non-negotiable drafting hygiene** — omit it and a court can read "remedies are cumulative" to defeat "sole remedy." The chronic-failure exit is also the FOEP pressure-release.
**Key levers:** uptime + tiering + locked-at-signing • window (monthly-reset vs. rolling) + method • "downtime" definition + min duration • credit shape + cap • **sole-remedy carved out of cumulative-remedies + N/A to security/IP/confidentiality** • **chronic-failure termination + refund** • maintenance caps • claim mechanics • P1/P2/P3 support SLOs.

## V. Operational / Boilerplate

### 14. Insurance
| | Position |
|---|---|
| **Vendor starts** | Thin/"customary"; floor limits (CGL $1M/$2M, **Tech E&O/Cyber blended on one $1–2M limit**); COI on request; refuses additional-insured beyond CGL; silent on subrogation/cancellation; insurance **decoupled from the cap** |
| **Typically lands** | Standalone schedule + 1–3yr tail: CGL $1M/$2M, **Tech E&O $2–5M, Cyber $3–5M floor ($5–10M+ regulated), unblended**; A-rated carriers; customer **AI on CGL** + primary-noncontributory + waiver of subrogation (endorsed); **vendor contractually owes 30-day cancellation notice**; "**insurance does not limit liability**" + cyber limit **floors the data-breach super-cap** |

**Why it lands here:** Insurance is the funding behind indemnity and the super-cap, so it's about money behind the promises that matter. The customer's leverage is high because most asks are cheap standard ISO endorsements (CG 20 10/20 37; CG 20 01) the vendor already carries. Vendors concede higher *limits* more readily than AI status on claims-made cyber/E&O forms (which resist AIs and erode the shared limit) — so the rational trade is robust separate limits + cyber-limit-floors-the-super-cap in exchange for dropping AI on those lines.
**Key levers:** **cyber limit** + ransomware/contingent-BI sub-limits • **unblending E&O from cyber** • AI beyond CGL • endorsement specificity • COI vs. actual endorsement • **vendor-owed 30-day cancellation notice (most over-promised term)** • carrier rating • claims-made tail • **"insurance ≠ cap" + cyber→super-cap link** • SIR cap • mutuality.

### 15. Assignment & Change of Control
| | Position |
|---|---|
| **Vendor starts** | Asymmetric: vendor gets affiliate + M&A carve-out **for itself only**; **CoC = deemed assignment** trigger **only against the customer**; consent "in vendor's sole discretion"; "null and void"; sometimes no-assign-to-competitor |
| **Typically lands** | Genuinely **mutual**; consent "**not to be unreasonably withheld, conditioned or delayed**"; **both** get affiliate + merger/sale-of-business carve-out (assignee assumes in writing, not a competitor); CoC trigger dropped/mutual; continuing-liability vs. release negotiated; receivables anti-assignment drops (UCC §§9-406/9-408) |

**Why it lands here:** Mutual + M&A/affiliate carve-out is one of the most standardized provisions; a sophisticated customer won't accept a one-way version. Each side fears being locked to a counterparty it didn't choose, so each accepts the same M&A-exit freedom it grants. "Not unreasonably withheld" preserves a check without a renegotiation weapon; the competitor exclusion is the residual fight. (Real: Duo World license confirms the carve-out structure; which party is freed varies with leverage.)
**Key levers:** **"not unreasonably withheld/conditioned/delayed"** • mutuality • M&A carve-out scope • affiliate definition + continuing liability vs. release • competitor conditions • CoC deemed-assignment trigger • reciprocal termination if vendor acquired by a customer competitor • assumption + notice • remedy (void vs. breach) • **receivables override (UCC §§9-406/9-408)**.

### 16. Governing Law, Venue & Dispute Resolution
| | Position |
|---|---|
| **Vendor starts** | Vendor **home-state** law + exclusive venue, **"substantive *and procedural*" law** (aggressive); jury waiver; class waiver; arbitration for click-through; one-way IP injunction carve-out; prevailing-party fees |
| **Typically lands** | **Neutral DE/NY** law (strike "procedural" overreach); enterprise deals **keep courts** (strike mandatory arbitration for appeal/discovery); arbitration reserved for publicity-sensitive/cross-border; **mutual** jury waiver survives; multi-tier escalation (30-day exec → mediation); IP injunction carve-out **mutual**; fees deleted/mutual; class waiver stays in B2B arbitration |

**Why it lands here:** Each side fears the other's home court more than a neutral one, so neutral DE/NY is the Coasean settling point. The forum fork splits by *industry/publicity-sensitivity, not pure leverage*: pure enterprise SaaS defaults to courts (appeal, discovery, public-pressure lever); arbitration is for publicity-averse/cross-border deals (New York Convention enforcement across ~170 states). (Real: SecureWorks/Dell subordinate the whole clause to the public-sector client contract.)
**Key levers:** governing law • **substantive-only vs. + procedural** • **courts vs. arbitration (central fork)** • institution/seat/panel • venue • jury waiver (mutual) • class waiver • escalation tiers • IP/equitable carve-out (mutual) • fee-shifting • FAA/delegation • limitations period • cross-border (NY Convention/Hague) • public-sector subordination.

### 17. Contractual Limitation Period for Claims
| | Position |
|---|---|
| **Vendor starts** | **1-year** time-bar (6 mo on aggressive clickwrap), anchored to **accrual/breach** (can run before the customer knows), one-sided (vendor payment carved out) |
| **Typically lands** | **Mutual 1 year** reset on three points: **(1) discovery rule** ("knew or reasonably should have known"); (2) **carve-outs** (IP indemnity, fraud/WM, confidentiality/data-breach, indemnity, payment); (3) genuinely mutual; often stretched to **2 years or struck**; "survival does not shorten the limitation period" added |

**Why it lands here:** Courts enforce a clearly-stated reasonable shortening (NY CPLR 201/*Kassner*; 1–2 yrs routinely upheld), so both prefer a clean number. The accrual-vs-discovery trade is the crux: the vendor gets a finite tail; the customer refuses to let a claim die before it could reasonably be discovered (latent defects, security incidents). UCC 2-725 floors goods at *not less than one year*; Louisiana prohibits shortening. Low-salience and frequently struck by a determined customer.
**Key levers:** length (6mo/1yr/2yr/silence) • **accrual vs. discovery trigger (most-fought)** • mutuality • carve-outs • "survival doesn't shorten" • interaction with claim-notice deadline • governing-law check (Louisiana; UCC 2-725) • non-waivable statutory claims excluded.

### 18. Force Majeure
| | Position |
|---|---|
| **Vendor starts** | Mutual-on-its-face; broad list + open catch-all; **payment NOT excused**; SLA credits suspended; **no/vendor-only** prolonged-event termination; soft mitigation; names pandemic/cyber/gov action as auto-excuses |
| **Typically lands** | Mutual; catch-all narrowed to "similar kind"; payment split — customer concedes payment isn't *excused* but wins **fee abatement/credit/pro-rata refund for unprovided service**; **DR/BCP carved out of FM relief**; SLA clock keeps running; **bilateral termination if event exceeds ~30 days** + refund of prepaid unused; firm mitigation; notice "as soon as reasonably practicable" |

**Why it lands here:** "No excuse for payment" is the US baseline and hard to overturn, so the customer's real win is reframing it as "pay for what you get." The 30-day bilateral termination right is the modern escape valve against indefinite limbo. The DR/BCP carve-out holds the vendor to its marketed resilience. NY law reads in unforeseeability and excuses only enumerated events — so the fight is over which events are *named*, not "whether or not foreseeable" boilerplate.
**Key levers:** mutuality • closed list vs. catch-all + named events • third-party/cloud failure • **DR/BCP carved out** • **payment: abatement/credit/refund (not whether excused)** • SLA clock runs vs. paused • security/breach/indemnity carved out • **bilateral termination trigger (30/60/90)** + refund • mitigation • notice • exclusions (own negligence, economic hardship, own-workforce strikes).

### 19. Audit / Compliance-Verification Rights
| | Position |
|---|---|
| **Vendor starts** | Broad self-help on-prem audit (short notice, uncapped frequency, vendor's staff); low cost-shift threshold; **true-up at undiscounted list**; reserved copyright-infringement remedies. SaaS: vendor-metered **overage** billing as the real regime |
| **Typically lands** | **≥30-day notice**, **1×/12 months** + for-cause; **independent third-party auditor** under NDA; scope limited, excluding regulated/other-tenant data; **cost-shift 5–10%**; **true-up at contract/discounted rate** + cure + **no auto copyright/termination escalation**; ~12-mo survival. SaaS: metered overage at contract (not list) rate + pre-bill notice |

**Why it lands here:** The conduct terms (notice, frequency, third-party auditor, data exclusions) are essentially free for a compliant vendor and fall early. The money fight is the cost-shift threshold and — more importantly — the **true-up rate** (a vendor that concedes a 5–10% threshold but holds list-price true-up still recovers a large premium). The copyright-infringement reservation gives aggressive on-prem licensors outsized leverage (statutory damages + fees), so subordinating it to cure-first is high-value. For SaaS the on-site audit is increasingly vestigial.
**Key levers:** notice/frequency • cost-shift threshold • **true-up at list vs. contract rate (the dollar lever) + cure** • **copyright-infringement reservation deletion** • self-certification-first • **SaaS overage rate + pre-bill notice** • scope/lookback + data exclusions • auditor independence/NDA • reciprocal audit of vendor fees/SLA • survival.

### 20. Publicity & Use of Name/Logo
| | Position |
|---|---|
| **Vendor starts** | Broad, **perpetual, self-executing** blanket grant (logo, lists, case studies, "any medium"); press release "**will issue**"; one-directional; no cease/remove |
| **Typically lands** | Gated/revocable: **bare logo/list listing** often conceded (brand guidelines, no implied endorsement); **PR/case studies/quotes require per-instance prior written consent** ("not unreasonably withheld," 5–10 business-day window); recharacterized as a **revocable** trademark license with **cease-use + remove within ~30 days** on termination; made **mutual**; investor/SEC carve-outs |

**Why it lands here:** The customer's brand is its asset — an unconsented logo reads as endorsement and can breach its own confidentiality — so it spends redline capital here. For the vendor, the bare logo listing delivers most marketing value at least sensitivity, so it trades away the blanket grant on PR/case studies (which need bespoke approval since the customer supplies the quotes). Buyers resist converting the response deadline into *deemed approval* (a published statement is hard to claw back).
**Key levers:** **blanket vs. per-instance prior written consent (biggest fight)** • channel tiering (logo/list vs. PR) • consent standard + deadline (escalation vs. deemed-approval) • one-way vs. mutual • **revocable** vs. perpetual • cease/remove on termination • brand guidelines + no-implied-endorsement • survival carve-outs • effective on signing vs. go-live • **AI/model-training use (new 2024–26 lever)**.

### 21. Acceptance / Acceptance Testing
| | Position |
|---|---|
| **Vendor starts** | "**Substantially conforms** to [vendor] Specifications"; **5–10 business-day** window; **deemed acceptance** on silence *and* on **production use**; unlimited "commercially reasonable" cure; **re-performance sole remedy**; SaaS = delete acceptance |
| **Typically lands** | "Conforms in all material respects to **mutually agreed objective criteria** set *before* testing"; **15–30 business-day** window (15 modal); deemed acceptance tamed (after written reminder; production-use narrowed to exclude pilot/DR); **structured reject-and-cure (≥2 cycles)**; **failure backstop — extend/price-reduce/terminate-and-refund**; re-coupled to a **10–20% holdback** (20–30% large/SI); punch-list for minor defects |

**Why it lands here:** Each side trades its least-valued for its most-feared. The customer concedes deemed acceptance and a bounded window (vendors can't carry indefinite unfunded acceptance risk; rev-rec needs a definite date) for objective up-front criteria, a real cure loop, and a termination/refund backstop. The failure backstop also forecloses the customer's UCC 2-719(2) FOEP argument. Custom-dev/SI work is often a services contract (common law, no UCC default acceptance), so the regime must be built in.
**Key levers:** standard + who owns the spec • **criteria agreed in writing *before* testing** • window + start point • deemed acceptance (reminder-gated?) • **production-use trigger narrowing** • cure period + **capped cycles** + re-test reset • **failure remedy stack** • sole-remedy + UCC 2-719(2) • **acceptance-based holdback** • severity tiering • downstream clocks • UCC vs. common-law characterization.

### 22. Compliance with Laws / Anti-Corruption
| | Position |
|---|---|
| **Vendor starts** | Thin one-way "comply with applicable laws"; ABAC/sanctions/AML usually **absent**; the one specific is a **one-way export/sanctions clause against the customer**; any anti-bribery line is a bare knowledge/materiality-qualified rep |
| **Typically lands** | **Mutual** compliance + vendor-side ABAC package: mutual anti-bribery rep covering **FCPA *and* UK Bribery Act** (no knowledge/materiality on the core "no bribe"), program covenant + flow-down, mutual trade-controls/sanctions + **not-a-Sanctioned-Person** rep, AML where money moves; breach = **material-breach (often no-cure) termination**; **carved out of the cap** alongside confidentiality/IP |

**Why it lands here:** The customer's driver is regulatory *defense*, not risk-shifting — the DOJ/SEC FCPA Resource Guide, DOJ's compliance-program guidance, and the UK Bribery Act s.7 "adequate procedures" defense all credit contractual third-party ABAC controls. The vendor concedes mutual ABAC/sanctions reps cheaply (true today, little new cost) and trades hardest on cost items — the audit right (conceded as a certification in SaaS) and a standalone dollar-one indemnity (not a reliable mid-market win).
**Key levers:** rep vs. warranty vs. covenant • mutual vs. one-way • statute scope (FCPA + UKBA; OFAC/EU/UK/UN; AML/ITAR if relevant) • knowledge/materiality qualifiers • affirmative program + flow-down • **audit (books-and-records vs. annual cert)** • **no-cure termination** • **liability treatment (carve-out; indemnity scope)** • Sanctioned-Person/50%-owner rep • debarment/exclusion-list reps (SAM/OIG/FDA) • survival.

### 23. Subcontracting / Personnel & Non-Solicitation
| | Position |
|---|---|
| **Vendor starts** | Broad self-granted subcontracting; prime responsibility narrow + under the cap; resists any **key-personnel** list; **one-way non-solicit** against the customer, 12–24 mo, whole workforce, **liquidated damages** |
| **Typically lands** | Subcontracting kept but new/data-touching subs need **consent not unreasonably withheld** (SaaS: DPA subprocessor notice-and-object); **vendor remains fully liable for subs** + flow-down (near non-negotiable); **named key-personnel list** (3–6 roles), 6–12mo lock, "equal-or-better" replacements + approval + overlap; non-solicit made **mutual**, narrowed to **engagement staff**, 12 mo, general-advertising carve-out, LDs shrink/drop; **void/severed as to CA staff** |

**Why it lands here:** "Delegate the work, not the responsibility" drives prime liability; the customer's leverage is data/regulated subs (Art. 28 regime, where a true veto is rare). On personnel, the customer is buying the continuity it pays a services premium for. Biggest current correction: employee non-solicits aren't merely "narrowed" in restrictive states — **California broadly voids them** (B&P 16600.5/SB 699, eff. Jan 1 2024, with fee-shifting; *AMN Healthcare*). The **FTC 2024 Non-Compete Rule was vacated (*Ryan v. FTC*), removed from the CFR eff. Feb 12 2026** — state law governs.
**Key levers:** subcontracting consent trigger • SaaS subprocessor veto vs. terminate-affected-service • **standalone prime liability + whether sub breaches reach the carve-outs** • flow-down • key-personnel list/lock + replacement • non-solicit reciprocity/scope/duration • carve-outs (general advertising, employee-initiated) • "solicit" vs. "hire" • remedy (LDs vs. injunctive) • **CA/ND/OK severability**.

### 24. Data Portability, Return & Transition / Escrow
| | Position |
|---|---|
| **Vendor starts** | Self-help export, **30-day** window then deletion, "vendor's standard format," **"Customer Data" drawn narrowly** (raw records only); transition = "reasonable cooperation at PS rates"; escrow silent or "source-code only, on bankruptcy" (useless for SaaS) |
| **Typically lands** | Machine-readable export (**CSV/JSON or documented API + schema**) free for normal volumes; definition broadened to **attachments/config/logs** (vendor keeps usage/derived/aggregated); **60–90-day** window + **retain-until-export**; **transition assistance with rate card locked at signing** (free-hours bucket in larger deals); **deletion + certification** + backup/legal-hold carve-outs; source-code escrow increasingly **dropped** for SaaS in favor of DR/SOC 2 assurances |

**Why it lands here:** The marginal items are cheap to the vendor, high-value to the customer (and dovetail with its own GDPR/CCPA portability/deletion duties), so vendors concede them to avoid looking like they're holding data hostage. What the vendor won't give up is usage/derived/aggregated data (analytics, benchmarks, training). The customer's real fear is the captive monopoly price at the worst moment — a signed rate card solves it. Source-code escrow is theater for SaaS (no servers/data/ops to run the code); true *continuity* escrow is reserved for critical dependencies and priced as a service.
**Key levers:** **scope of "Customer Data" (raw vs. + attachments/config/logs; vendor keeps derived)** • named format vs. "standard" • window + retain-vs-delete • export cost + "normal volume" • transition scope (the "reasonable assistance" trap) • **rate card locked at signing** • deletion + cert + legal-hold • **escrow existence/type (source-code refused vs. standby-hosting continuity)** • release triggers + verification • step-in rights (regulated) • survival.

### 25. Notices, Entire Agreement & Order-of-Precedence
| | Position |
|---|---|
| **Vendor starts** | Precedence ranks **Order Form + URL terms on top** (SaaS), URL terms "as updated from time to time" (unilateral-amendment lever); entire-agreement + **non-reliance** (parol-evidence); notices by email "deemed received on send," account-email enough for termination |
| **Typically lands** | **MSA controls on legal terms unless an Order Form/SOW expressly references the section it overrides and is signed**; DPA governs data matters; URL terms **pinned to a dated version**, no material adverse mid-term change; entire-agreement survives with **fraud carve-out** + preserved NDA/DPA/side-letters + narrowed non-reliance; notices split — **email for ordinary; courier/certified or confirmed-receipt for operative (termination/breach/claims)** + copy-to-counsel |

**Why it lands here:** Low-emotion, high-consequence — "whoever read the clause wins." The precedence clause is the rulebook for the whole stack: if a sales-drafted Order Form sits on top of *all* terms, a junior AE can silently overwrite the negotiated cap or IP grant, so customers insist on MSA-on-top-for-legal-terms with an explicit signed section-specific override. The fraud carve-out is effectively non-negotiable (US policy won't let a party contract out of its own fraud; non-reliance *can* bar negligent/innocent misrep under NY/DE — so scope it). Operative notices are strictly construed; a defective termination notice can render termination ineffective.
**Key levers:** precedence direction • **override only via express section reference + signature** • DPA ranking/survival • **URL terms pinned to dated version; bar mid-term adverse changes** • **fraud carve-out (cannot be excluded)** • scope of non-reliance • preserve NDA/DPA/side-letters • notice method by type • deemed-receipt timing + burden • mandatory copy-to-counsel • UCC 2-207 battle-of-the-forms.

## Reading the Leverage

The same clause lands in very different places depending on a handful of forces:

- **Relative size / who needs whom** — the dominant variable. SMB/self-serve = vendor paper holds verbatim; mid-market = the "typically lands" column; large enterprise = caps→super-caps/uncapped, escalators→3%/fixed, exit→real transition obligations. A marquee reference logo can flip leverage regardless of dollar size.
- **Competition / credible alternatives** — a displacement deal caves on escalation/parity/exit; an incumbent renewal with sunk switching costs holds. The buyer's strongest counter-lever is a documented, credible alternative.
- **Regulated buyer** — FFIEC/OCC, NYDFS Part 500, DORA, HIPAA/BAA, FAR/DFARS/FedRAMP import mandatory, often non-waivable terms (uncapped breach, $5–25M+ cyber, audit/step-in, continuity, forum constraints), usually via a separate addendum.
- **Data sensitivity** — more sensitive data pushes breach off the general cap into a high super-cap/uncapped, tightens the breach clock/subprocessor controls, and makes no-AI-training table stakes.
- **Multi-year / volume** — buys deeper discounts and price protection, but raises lock-in stakes, making uplift caps, portable export, and transition assistance more valuable to win pre-signature.
- **Who holds the pen** — on low-salience boilerplate (precedence, notices, limitation period, assignment), the party whose counsel actually read the mechanics wins. On the enterprise's own paper, defaults invert wholesale.

The through-line: vendors hold the lines tied to **insurability and one-paper economics** (the general 1× cap, the category-level consequential waiver, platform ownership, the auto-renew default, payment-not-excused) and concede **bounded, insurable, or self-controlled risks** (super-caps pegged to their cyber tower, uncapped IP/fraud/willful-misconduct heads, mutual carve-outs, capped escalators) — because those trades cost predictable money rather than betting the balance sheet.
