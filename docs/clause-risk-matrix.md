# MSA Clause Risk Matrix

Every MSA clause as a **risk-tiered escalation grid**, written to make the tug-of-war obvious.

**Who's who**
- **🟥 Seller** = the **Vendor / Provider / Supplier** — the party providing the product or service (and, usually, the one whose paper the MSA starts on).
- **🟦 Buyer** = the **Customer / Client** — the party paying for it.

**How to read each clause**
1. **Risky for the Buyer / Risky for the Seller** — the specific exposure each side faces, i.e. *why this clause is worth fighting over*.
2. **Balanced (market)** — the neutral position in real language.
3. The **grid** — a position is **🟥 seller-leaning** when it favors the seller and **pushes risk onto the buyer**, or **🟦 buyer-leaning** when it favors the buyer and **pushes risk onto the seller**, at three escalating levels. The **approver** named in each cell is whoever — on the side *being asked to accept that risk* — must sign off.
4. **🚩 Walkaway** — the position past L3 that the risk-bearing side won't accept, and why.

**Risk levels:** *L1* minor/market-adjacent · *L2* moderate shift · *L3* aggressive/off-market (concentrated, often uninsurable). **Approver ladder:** *Deal Desk / Procurement* (L1) → *Legal* (L2) → *GC* + functional exec — *CFO* (money), *CISO/DPO* (data), *GC* (legal/IP) (L3) → *Exec/CEO* or walk (beyond).

> *General market-practice guidance, not legal advice. "Risk level" is directional — calibrate to your own risk posture and deal.*

---

## I. Risk Allocation

### 1. Limitation of Liability (cap)
- **Risky for the Buyer 🟦:** a low/narrow cap means real losses (data breach, IP, downtime damage) are mostly **unrecoverable** — the buyer eats them.
- **Risky for the Seller 🟥:** a high/uncapped cap means one incident can **exceed the deal's total revenue** and isn't insurable — it bets the balance sheet.

**Balanced:** mutual cap = 1× trailing-12-mo fees (paid-or-payable); 2–3× data/IP supercap; uncapped carve-outs for IP indemnity, confidentiality, gross negligence/willful misconduct/fraud, bodily injury, payment.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | cap on "fees **paid**" basis; standard carve-outs — *Procurement* | add a modest year-one "$ floor" — *Deal Desk* |
| **L2** | data breach folded **inside** the 1× cap (no supercap) — *Legal* | data/IP supercap raised to 3–5× — *Legal* |
| **L3** | carve-outs trimmed to payment only; per-order anti-stacking — *GC + CISO* | **uncapped** data-breach liability — *GC + CFO* |

🚩 **Walkaway:** seller walks if the general cap is uncapped/>2× or carve-outs swallow it; buyer walks if data/IP/fraud sit inside a 1× cap. **Why:** each extreme is uninsurable (seller) or makes catastrophic loss unrecoverable (buyer).

### 2. Exclusion of Consequential Damages
- **Risky for the Buyer 🟦:** its biggest losses (lost business, breach-response, data recovery) are typically labeled "indirect" and **waived** → unrecoverable.
- **Risky for the Seller 🟥:** open-ended exposure to the buyer's **downstream business losses** it can't foresee or price.

**Balanced:** mutual waiver; carve out indemnity third-party amounts, confidentiality/security/data breach, and data-recovery costs.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | lost profits named as its own excluded head — *Procurement* | data-recovery/breach-response costs recoverable — *Deal Desk* |
| **L2** | **no carve-outs** to the waiver — *Legal* | lost profits recoverable *through* carved-out breaches — *Legal* |
| **L3** | waiver also bars direct damages "however characterized" — *GC* | broad direct lost-profits recovery preserved — *GC* |

🚩 **Walkaway:** buyer walks if breach-response/data-recovery costs are waived; seller walks if its downstream/business-loss exposure is open-ended. **Why:** the waiver only works if catastrophic-but-foreseeable losses are handled by carve-outs, not erased.

### 3. Indemnification
- **Risky for the Buyer 🟦:** if the product **infringes a third party's IP**, the buyer gets sued and — without an indemnity — pays its own defense and damages.
- **Risky for the Seller 🟥:** it agrees to **defend and pay** for claims about its product — potentially large, and ruinous if uncapped.

**Balanced:** mutual; patent/copyright/TM + trade secret; carved out of the consequential exclusion; 2–3× supercap; notice-and-prejudice; substance-based settlement consent.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | issued patents + copyright only; vendor-controlled defense — *Procurement* | add trade-secret + "defend from tender" — *Deal Desk* |
| **L2** | indemnity capped at the **1× general cap** — *Legal* | supercap to 5× + separate counsel on conflict — *Legal* |
| **L3** | one-way (vendor→customer only); absolute exclusions — *GC* | **uncapped** IP indemnity + AI/open-source covered — *GC* |

🚩 **Walkaway:** buyer walks if the indemnity is **capped-and-excluded** (defense costs barred as "indirect" → illusory); seller walks at fully uncapped IP across all heads. **Why:** an illusory indemnity is worthless to the buyer; unlimited IP exposure is unpriceable for the seller.

### 4. Warranties & Disclaimer
- **Risky for the Buyer 🟦:** an "AS-IS" disclaimer can leave it with **no recourse** if the product underperforms.
- **Risky for the Seller 🟥:** broad warranties create **ongoing performance obligations** and liability whenever the product falls short.

**Balanced:** "materially conforms to Documentation" for the term; AS-IS disclaimer of implied warranties, subordinated to express terms; security/anti-malware warranties added.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | "substantially conforms"; short warranty window — *Procurement* | full-term coverage; anti-malware warranty — *Deal Desk* |
| **L2** | re-performance is the **sole** remedy for everything — *Legal* | non-infringement/title struck from disclaimer — *Legal* |
| **L3** | disclaimer not subordinated (can gut the SLA/security) — *GC* | broad fitness-for-purpose + chronic-failure refund — *GC* |

🚩 **Walkaway:** buyer walks if the AS-IS disclaimer overrides the express SLA/security promises; seller walks at an uncapped fitness-for-Customer's-purpose warranty. **Why:** an unsubordinated disclaimer makes the warranties meaningless; a subjective fitness warranty is open-ended.

## II. IP & Data

### 5. IP Ownership & License
- **Risky for the Buyer 🟦:** its **data or custom-built work** could become the vendor's IP or fuel model training, or it loses access to deliverables it paid for.
- **Risky for the Seller 🟥:** giving away ownership of its **platform / background IP** would hand over its core business.

**Balanced:** each retains background IP; customer data/CI never vendor IP; custom work assigned on payment; feedback licensed; no model-training without consent.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | broad feedback license to vendor — *Procurement* | custom deliverables assigned on payment — *Deal Desk* |
| **L2** | vendor may train on **de-identified** customer data — *Legal* | no model-training on customer data (opt-in) — *Legal* |
| **L3** | residuals clause (no trade-secret carve-out); feedback assigned — *GC* | vendor assigns customer-specific IP; AI output to customer — *GC* |

🚩 **Walkaway:** buyer walks if its data can train models or becomes vendor IP; seller walks if asked to assign its core platform/background IP. **Why:** data-as-training-fuel is an existential governance risk for the buyer; platform IP is the seller's whole business.

### 6. Confidentiality
- **Risky for the Buyer 🟦:** its **sensitive/regulated data** could be exposed or under-protected (e.g., protection expiring on a short clock).
- **Risky for the Seller 🟥:** open-ended/**uncapped liability** for an inadvertent disclosure, plus exposure of its own roadmap.

**Balanced:** mutual; objective standard; term + 3 yrs (indefinite for trade secrets); return/destroy + certification.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | marking required to qualify; 2-yr tail — *Procurement* | objective standard; 3-yr tail — *Deal Desk* |
| **L2** | residuals clause included — *Legal* | 5-yr tail; regulated data protected while retained — *Legal* |
| **L3** | short fixed expiry even for trade secrets — *GC* | breach uncapped; residuals deleted — *GC* |

🚩 **Walkaway:** buyer walks if regulated/personal data loses protection on a fixed clock; seller walks at uncapped exposure for an inadvertent slip. **Why:** premature expiry forfeits trade-secret status and breaches the buyer's own duties; an uncapped slip is uninsurable.

### 7. Data Protection & Security (DPA)
- **Risky for the Buyer 🟦:** as the data **controller**, a vendor breach triggers the **buyer's own** regulator fines/notifications — and a slow breach clock makes it miss its 72h GDPR duty.
- **Risky for the Seller 🟥:** as **processor**, uncapped breach liability plus heavy security, subprocessor, and audit obligations.

**Balanced:** processor terms; breach notice ≤72h of awareness; subprocessor notice + objection + vendor liability; SOC 2/ISO maintained; 2–3× data super-cap.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | notice "without undue delay"; SOC 2 satisfies audit — *Procurement* | 72h clock + assistance — *Deal Desk* |
| **L2** | "commercially reasonable" security (no named standard) — *Legal/CISO* | 48h clock; maintains SOC 2 II + lapse remediation — *Legal* |
| **L3** | breach notice only after vendor **confirms**; privacy loss inside 1× cap — *GC + CISO* | no AI training; for-cause on-site audit; uncapped breach — *GC + CFO* |

🚩 **Walkaway:** buyer (esp. regulated) walks without a defined breach clock + super-cap + no-AI-training; seller walks at fully uncapped privacy liability. **Why:** the buyer owes its own regulator a 72h notice; uncapped breach is uninsurable for the seller.

## III. Commercial Terms

### 8. Payment Terms
- **Risky for the Buyer 🟦:** a billing dispute or error can trigger **interest or suspension** of a business-critical service.
- **Risky for the Seller 🟥:** slow pay, set-off, and refunds disrupt the **cash flow** it has financed against.

**Balanced:** net 30–45; good-faith dispute carve-out; interest on undisputed after notice; suspension only post-notice.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | net 30, annual-in-advance — *Procurement* | dispute carve-out; SLA-credit set-off — *Deal Desk* |
| **L2** | no set-off; suspension on any past-due — *Legal* | net 45–60 — *Legal/CFO* |
| **L3** | pay-first-dispute-later; immediate suspension; 18% interest — *Legal/CFO* | broad set-off of finally-determined amounts — *CFO* |

🚩 **Walkaway:** buyer walks if a contested invoice can suspend a critical service; seller walks at open-ended set-off against its receivables. **Why:** suspension-on-dispute weaponizes billing errors; broad set-off breaks the seller's cash-flow/financing model.

### 9. Price / Fee Escalation
- **Risky for the Buyer 🟦:** **uncapped renewal price hikes** once it's locked in and switching costs are sunk.
- **Risky for the Seller 🟥:** a **price freeze** that erodes margin against inflation/cost growth.

**Balanced:** renewal cap ~3–5% off the discounted rate; named index if CPI-linked; anti-compounding.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | 5% cap off discounted rate — *Procurement* | first renewal flat; 3% cap — *Deal Desk* |
| **L2** | cap applied to **list** rate (discount clawback) — *Legal/CFO* | fixed multi-year pricing — *Legal/CFO* |
| **L3** | "greater of 7% or CPI," uncapped CPI — *CFO* | 0% / price locked for term + renewals — *CFO* |

🚩 **Walkaway:** buyer walks at uncapped / "greater-of" escalation off list; seller walks at a multi-year hard price freeze in an inflationary market. **Why:** uncapped uplift is the buyer's worst post-lock-in surprise; a long freeze erodes the seller's margin.

### 10. Most-Favored-Customer / Benchmarking
- **Risky for the Buyer 🟦:** **paying more** than comparable customers for the same thing.
- **Risky for the Seller 🟥:** a **book-wide parity obligation** — an unknown liability that forces it to stop discounting anyone.

**Balanced:** usually replaced by a hard escalation cap; narrow price-only MFN with tight comparator if any.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | no MFN; rely on the escalation cap — *Procurement* | escalation cap + locked pricing (the substitute) — *Deal Desk* |
| **L2** | list-price-only MFN, broad carve-outs, certificate-only — *Legal* | net-effective MFN, tight comparator — *Legal/CFO* |
| **L3** | (no seller-favorable MFN — seller's posture is to decline) — *—* | active-monitoring MFN + retroactive credit + audit — *CFO* |

🚩 **Walkaway:** seller walks at a true book-wide, audited, retroactive MFN. **Why:** open-ended parity is an unknown, book-wide liability that forces the seller to stop discounting entirely.

## IV. Term & Exit

### 11. Term & Auto-Renewal
- **Risky for the Buyer 🟦:** **silent multi-year lock-in** that auto-renews at higher prices before it can act.
- **Risky for the Seller 🟥:** losing **predictable recurring revenue** / easy churn at each renewal.

**Balanced:** auto-renew for successive 1-yr terms; 30–60-day notice; capped uplift; renewal reminder.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | 1-yr auto-renewal, 60-day notice — *Procurement* | 30-day notice + renewal reminder — *Deal Desk* |
| **L2** | equal-length (multi-yr) auto-renewal — *Legal* | renewal pricing fixed/capped — *Legal* |
| **L3** | 90-day notice + then-current (uncapped) pricing — *Legal/CFO* | no auto-renewal (affirmative opt-in) — *Deal Desk* |

🚩 **Walkaway:** buyer walks at silent multi-year lock-in with uncapped uplift. **Why:** renewal leverage collapses once switching costs sink — this is where margin is quietly recovered.

### 12. Termination
- **Risky for the Buyer 🟦:** **no exit when the vendor underperforms**, data held hostage, and forfeited prepaid fees.
- **Risky for the Seller 🟥:** a **convenience exit** that destroys the recognized ARR it's capitalized on.

**Balanced:** mutual for-cause + cure; pro-rata refund on vendor-cause; data export + transition rate card; trigger-based buyer exits.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | mutual 30-day cure; export window 30 days — *Procurement* | trigger-based exits (chronic SLA/breach) — *Deal Desk* |
| **L2** | prepaid non-refundable; payment hair-trigger — *Legal* | pro-rata refund on vendor-cause; locked transition rate card — *Legal* |
| **L3** | no buyer exit at all; acceleration of committed fees — *Legal/CFO* | termination **for convenience** mid-term + refund — *GC + CFO* |

🚩 **Walkaway:** buyer walks with no exit on vendor failure + no data portability; seller walks at a free mid-term convenience exit on a subscription. **Why:** no-exit + lock-in is the buyer's existential risk; convenience exit destroys the seller's recognized ARR.

### 13. Service Levels (SLA) & Credits
- **Risky for the Buyer 🟦:** downtime hurts its business, but **credits are tiny and the "sole remedy."**
- **Risky for the Seller 🟥:** **uncapped damages** for outages, and an easy SLA-based termination trigger.

**Balanced:** 99.9% uptime; tiered credits; sole remedy for *availability only* + cumulative-remedies carve-out; chronic-failure exit.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | 99.9%; credits ≤30% of monthly fee — *Procurement* | service-tiered SLOs; auto-applied credits — *Deal Desk* |
| **L2** | credits are the **sole & exclusive** remedy (all heads) — *Legal* | credits non-exclusive; chronic-failure termination — *Legal* |
| **L3** | URL SLA unilaterally amendable; no termination right — *Legal* | top-tier credit 100% + refund on chronic miss — *Legal/CFO* |

🚩 **Walkaway:** buyer walks if SLA credits are the only remedy for a security/data failure; seller walks at uncapped damages for downtime. **Why:** credits as sole remedy turn a breach into a rounding error; uncapped downtime damages are unpriceable.

## V. Operational / Boilerplate

### 14. Insurance
- **Risky for the Buyer 🟦:** if the vendor causes a loss, there's **no funded coverage** standing behind the indemnity/cap.
- **Risky for the Seller 🟥:** the cost of carrying high limits, and additional-insured status that **erodes its own coverage**.

**Balanced:** CGL + Tech E&O ($2–5M) + Cyber ($3–5M), A-rated; additional insured on CGL; "insurance ≠ cap."

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | "commercially reasonable"/CGL only — *Procurement* | named E&O + Cyber limits — *Deal Desk* |
| **L2** | E&O/Cyber **blended** on one low limit — *Legal/CISO* | Cyber $5–10M; cyber limit floors the data super-cap — *Legal/CFO* |
| **L3** | COI on request only; no AI/waiver of subrogation — *Risk/CFO* | additional insured on claims-made cyber/E&O — *Risk/CFO* |

🚩 **Walkaway:** buyer (data-sensitive) walks without real, separate cyber limits; seller walks at additional-insured status that erodes its claims-made cyber tower. **Why:** insurance is the money behind the promises; AI status on cyber drains the shared limit.

### 15. Assignment & Change of Control
- **Risky for the Buyer 🟦:** getting **stuck with an assignee/acquirer it didn't choose** (including a competitor).
- **Risky for the Seller 🟥:** the mirror — and being **blocked from its own M&A or financing**.

**Balanced:** mutual; consent not unreasonably withheld; affiliate + M&A carve-out (assignee not a competitor).

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | mutual + M&A carve-out — *Procurement* | "not unreasonably withheld" qualifier — *Deal Desk* |
| **L2** | CoC of buyer = deemed assignment (one-way) — *Legal* | competitor-acquisition termination right — *Legal* |
| **L3** | vendor assigns freely; buyer needs consent (sole discretion) — *GC* | buyer assigns freely to affiliates incl. on CoC — *GC* |

🚩 **Walkaway:** buyer walks at a one-way assignment right + a CoC trip-wire only against it. **Why:** asymmetric assignment can strand a party with a counterparty (or competitor) it never chose.

### 16. Governing Law & Dispute Resolution
- **Risky for the Buyer 🟦:** litigating on the **seller's home turf and terms**, and losing court access to forced arbitration.
- **Risky for the Seller 🟥:** the mirror — the **buyer's home forum** and procedure.

**Balanced:** neutral DE/NY law; courts; mutual jury waiver; IP/equitable carve-out.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | neutral DE/NY law + venue — *Procurement* | mutual jury waiver; escalation tier — *Deal Desk* |
| **L2** | seller's home-state law + venue — *Legal* | buyer's home-state law + venue — *Legal* |
| **L3** | "substantive **and procedural**" home law + forced arbitration — *GC* | mandatory arbitration on buyer's terms — *GC* |

🚩 **Walkaway:** either walks at the other's home court on the other's procedural terms. **Why:** forum + procedure can decide outcomes regardless of the merits.

### 17. Contractual Limitation Period
- **Risky for the Buyer 🟦:** a **short clock from accrual** kills claims before latent defects/breaches even surface.
- **Risky for the Seller 🟥:** a **long tail** of open liability and uncertainty.

**Balanced:** 1–2 yrs from discovery; mutual; carve-outs for IP/confidentiality/data/indemnity/payment.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | 1 yr from discovery — *Procurement* | 2 yrs; mutual — *Deal Desk* |
| **L2** | 1 yr from **accrual** (can run before discovery) — *Legal* | carve-outs (IP/data/fraud) excluded from the bar — *Legal* |
| **L3** | 6-month bar from accrual, one-sided — *GC* | no shortened period (full statute) — *GC* |

🚩 **Walkaway:** buyer walks at a sub-1-yr accrual-based bar (claims die before discovery). **Why:** latent defects/security incidents surface after the clock would expire.

### 18. Force Majeure
- **Risky for the Buyer 🟦:** **paying for a service it isn't receiving** during a disruption, with no exit.
- **Risky for the Seller 🟥:** being held **liable for events beyond its control**.

**Balanced:** mutual; payment not excused but credit/refund for unprovided service; DR/BCP carved out; 30-day termination valve.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | mutual, closed list + "similar events" — *Procurement* | abatement/refund for unprovided service — *Deal Desk* |
| **L2** | SLA credits suspended during the event — *Legal* | DR/BCP obligations carved out of FM — *Legal* |
| **L3** | payment continues, no relief, no buyer exit — *Legal* | 10-day bilateral termination + full refund — *GC* |

🚩 **Walkaway:** buyer walks if it keeps paying indefinitely for an unavailable service with no exit. **Why:** FM should excuse performance, not convert into open-ended payment for nothing.

### 19. Audit Rights
- **Risky for the Buyer 🟦:** as the audited licensee — **surprise audits + list-price true-ups + infringement claims** (audit-as-revenue).
- **Risky for the Seller 🟥:** under-licensing / usage leakage going undetected (and, in reverse, being audited by the buyer).

**Balanced:** 30-day notice, 1×/yr, third-party auditor; true-up at contract rate; 5–10% cost-shift; reciprocal vendor audit.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | 30-day notice, annual, third-party auditor — *Procurement* | reciprocal audit of vendor fees/SLA/security — *Deal Desk* |
| **L2** | true-up at **list** rate; low cost-shift threshold — *Legal/CFO* | true-up at contract rate + cure period — *Legal* |
| **L3** | self-help, no-notice audit + auto copyright-infringement claim — *GC + CFO* | no audit (rely on SaaS metering) — *Deal Desk* |

🚩 **Walkaway:** buyer walks at no-notice self-help audits with list-price true-up + infringement escalation. **Why:** that combination is an audit-as-revenue weapon, not compliance verification.

### 20. Publicity & Use of Name/Logo
- **Risky for the Buyer 🟦:** **unconsented use of its name/logo** implies endorsement or breaches its own confidentiality.
- **Risky for the Seller 🟥:** losing the **marketing/reference rights** it values.

**Balanced:** bare logo/list listing allowed; PR/case studies need per-instance consent; revocable.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | logo/customer-list listing (brand guidelines) — *Procurement* | per-instance consent for PR/case studies — *Deal Desk* |
| **L2** | press release "will issue" on signing — *Legal/Marketing* | cease-use + remove on termination — *Legal* |
| **L3** | perpetual, blanket, self-executing publicity grant — *Marketing/GC* | no use of name/logo at all without consent — *Marketing* |

🚩 **Walkaway:** buyer (brand-sensitive/stealth/regulated) walks at a blanket perpetual grant. **Why:** unconsented use reads as endorsement and can breach the buyer's own obligations.

### 21. Acceptance / Acceptance Testing
- **Risky for the Buyer 🟦:** **deemed-accepting (and paying for) a non-conforming deliverable** with no exit.
- **Risky for the Seller 🟥:** **indefinite unfunded acceptance risk** — it can't recognize revenue and carries a delivered, unpaid asset.

**Balanced:** objective criteria set before testing; 15–30-day window; reject-and-cure; failure backstop; holdback.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | 15-day window; reminder-gated deemed acceptance — *Procurement* | objective criteria fixed before testing — *Deal Desk* |
| **L2** | deemed acceptance on any production use — *Legal* | 2 cure cycles + price-reduction option — *Legal* |
| **L3** | 5-day window; "substantially conforms"; sole remedy re-perform — *Legal/CFO* | terminate-and-refund backstop + 20% holdback — *CFO* |

🚩 **Walkaway:** buyer walks at deemed acceptance on pilot use with no failure exit; seller walks at open-ended acceptance with no deemed date. **Why:** the buyer can be locked into a non-conforming build; the seller can't carry indefinite unfunded acceptance risk (rev-rec).

### 22. Compliance / Anti-Corruption
- **Risky for the Buyer 🟦:** a supplier's **bribery/sanctions violation** creates the buyer's *own* regulatory and criminal exposure.
- **Risky for the Seller 🟥:** an **uncapped, dollar-one compliance indemnity** plus heavy program/audit obligations.

**Balanced:** mutual compliance + ABAC (FCPA + UKBA); program + flow-down; violation = termination.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | mutual "comply with laws" — *Procurement* | mutual ABAC reps (FCPA + UKBA) — *Deal Desk* |
| **L2** | one-way export/sanctions clause against buyer only — *Legal* | ABAC program covenant + flow-down — *Legal/Compliance* |
| **L3** | no ABAC terms at all — *GC/Compliance* | standalone uncapped anti-corruption indemnity — *GC + CFO* |

🚩 **Walkaway:** a regulated buyer walks without mutual ABAC + flow-down; seller walks at a dollar-one uncapped ABAC indemnity. **Why:** the buyer needs supplier controls for its own regulatory defense; uncapped indemnity here is unpriceable.

### 23. Subcontracting & Non-Solicitation
- **Risky for the Buyer 🟦:** **losing key people**, or a subcontractor mishandling its data with no recourse to the prime; and an over-broad non-solicit *against* it.
- **Risky for the Seller 🟥:** **losing its staff** to the customer, and constrained delivery flexibility.

**Balanced:** vendor fully liable for subs; key-personnel continuity; mutual non-solicit of engagement staff.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | vendor may subcontract, remains liable — *Procurement* | flow-down + DPA process for data subs — *Deal Desk* |
| **L2** | one-way non-solicit against buyer, 24 mo, whole workforce — *Legal* | named key personnel + reassignment lock — *Legal* |
| **L3** | LD-backed non-solicit; no prime liability for subs — *GC* | buyer approval required for all subcontractors — *GC* |

🚩 **Walkaway:** buyer walks if the vendor isn't liable for its subs; non-solicit walks if it's one-way/whole-workforce (and is void as to CA/ND/OK staff). **Why:** "delegate the work, not the responsibility"; over-broad non-solicits are unenforceable in key states.

### 24. Data Portability, Return & Transition
- **Risky for the Buyer 🟦:** **lock-in** — it can't get its data out in usable form, and faces captive transition pricing.
- **Risky for the Seller 🟥:** the **cost/effort** of transition and giving up its derived/aggregated data.

**Balanced:** portable-format export (incl. attachments/config/logs); 60–90-day window; transition rate card locked at signing; deletion + cert.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | standard-functionality export, 30-day window — *Procurement* | documented format/API; 60–90-day window — *Deal Desk* |
| **L2** | "Customer Data" defined narrowly (raw records only) — *Legal/CISO* | attachments/config/logs included; free export — *Legal* |
| **L3** | transition only "as reasonable" at uncapped PS rates — *Legal/CFO* | continuity/source-code escrow for critical deps — *GC + CFO* |

🚩 **Walkaway:** buyer walks without portable export + a transition rate card locked at signing. **Why:** lock-in is the existential exit risk; the captive-monopoly price gets quoted at the worst moment.

### 25. Notices, Entire Agreement & Precedence
- **Risky for the Buyer 🟦:** a **sales-drafted Order Form silently overriding** the negotiated MSA protections, or fraud being contracted out.
- **Risky for the Seller 🟥:** **ambiguity over which terms control**, and operative notices being mis-served.

**Balanced:** MSA controls legal terms; Order Form overrides only by express signed reference; URL terms pinned; fraud carve-out; operative notices need confirmed delivery.

| Level | 🟥 Seller-leaning (risk → buyer) → *buyer approves* | 🟦 Buyer-leaning (risk → seller) → *seller approves* |
|---|---|---|
| **L1** | email for routine notices — *Procurement* | confirmed delivery for operative notices + copy-to-counsel — *Deal Desk* |
| **L2** | Order Form + URL terms sit **on top** of all terms — *Legal* | URL terms pinned to a dated version — *Legal* |
| **L3** | URL terms "as updated"; non-reliance excludes fraud — *GC* | MSA supreme on all terms; no unilateral changes — *GC* |

🚩 **Walkaway:** buyer walks if a sales-drafted Order Form can silently override the MSA, or if fraud is contracted out. **Why:** precedence is the rulebook for the whole stack — and no one can contract out of their own fraud.
