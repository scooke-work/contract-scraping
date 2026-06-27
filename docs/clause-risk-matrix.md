# MSA Clause Risk Matrix

Every MSA clause as a **risk-tiered escalation grid**, written to make the tug-of-war obvious.

**Who's who**
- **🟥 Seller** = the **Vendor / Provider / Supplier** — the party providing the product or service (usually the one whose paper the MSA starts on).
- **🟦 Buyer** = the **Customer / Client** — the party paying for it.

**How to read each clause**
1. **Risky for the Buyer / Risky for the Seller** — the specific exposure each side faces (why the clause is worth fighting over).
2. The **table** — each row is a position on the spectrum: **🟥 seller-leaning** (L1–L3) pushes risk *onto the buyer*; **⚖️ balanced** is the market middle; **🟦 buyer-leaning** (L1–L3) pushes risk *onto the seller*; **🚩 walkaway** is past the point either side signs. Columns:
   - **Escalates to** — who, on the side *being asked to accept that risk*, must sign off.
   - **Summary** — the position in a phrase.
   - **Example clause language** — illustrative drop-in text (`[brackets]` to fill); not legal advice.

**Risk levels:** *L1* minor/market-adjacent · *L2* moderate shift · *L3* aggressive/off-market (concentrated, often uninsurable). **Approver ladder:** *Deal Desk / Procurement* (L1) → *Legal* (L2) → *GC* + functional exec — *CFO* (money), *CISO/DPO* (data), *GC* (legal/IP) (L3) → *Exec/CEO* or walk (beyond).

> *General market-practice guidance, not legal advice. Calibrate to your own risk posture and deal.*

---

## I. Risk Allocation

### 1. Limitation of Liability (cap)
- **Risky for the Buyer 🟦:** a low/narrow cap leaves real losses (data breach, IP, downtime) unrecoverable. **Risky for the Seller 🟥:** a high/uncapped cap can exceed total deal revenue and isn't insurable.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Cap on "fees **paid**" basis; standard carve-outs | "…aggregate liability will not exceed the fees **paid** by Customer in the 12 months before the claim." |
| 🟥 Seller L2 | Buyer · Legal | Data breach folded into the 1× cap | "…all liability, **including for any data breach**, is subject to the single cap in this Section." |
| 🟥 Seller L3 | Buyer · GC + CISO | Carve-outs trimmed to payment; per-order anti-stacking | "…the cap is the aggregate maximum **per Order Form**; the only excluded matter is Customer's payment obligations." |
| ⚖️ **Balanced** | Market | Mutual 1× cap + 2–3× data/IP supercap + uncapped carve-outs | "Neither party's aggregate liability will exceed 1× the fees paid or payable in the prior 12 months; liability for a data-protection breach will not exceed 2×; and these limits do not apply to indemnification, confidentiality, gross negligence, willful misconduct, fraud, or payment." |
| 🟦 Buyer L1 | Seller · Deal Desk | Add a first-year dollar floor | "…or, for claims in the first year, the **greater of** the fees paid or $[___]." |
| 🟦 Buyer L2 | Seller · Legal | Data/IP supercap raised to 3–5× | "…liability for data-protection or IP-indemnity claims will not exceed [3–5]× the prior-12-month fees." |
| 🟦 Buyer L3 | Seller · GC + CFO | Uncapped data-breach liability | "Notwithstanding the cap, each party's liability for a data-security breach is **unlimited**." |
| 🚩 **Walkaway** | Exec / walk | Seller: any uncapped general cap. Buyer: data/IP/fraud inside a 1× cap. | *(no agreed language — past the point either side signs)* |

### 2. Exclusion of Consequential Damages
- **Risky for the Buyer 🟦:** its biggest losses (lost business, breach response, data recovery) get labeled "indirect" and waived. **Risky for the Seller 🟥:** open-ended exposure to the buyer's downstream business losses.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Lost profits named as their own excluded head | "…neither party is liable for indirect or consequential damages, **including lost profits, revenue, or data**." |
| 🟥 Seller L2 | Buyer · Legal | No carve-outs to the waiver | "…this exclusion applies to **all** claims, with no exception." |
| 🟥 Seller L3 | Buyer · GC | Waiver bars direct damages "however characterized" | "…lost profits and similar losses are excluded **whether characterized as direct or indirect**." |
| ⚖️ **Balanced** | Market | Mutual waiver with carve-outs | "Neither party is liable for indirect, consequential, or punitive damages or lost profits; except this does not limit indemnity third-party amounts, breach of confidentiality/security, or Customer's costs to recover lost data." |
| 🟦 Buyer L1 | Seller · Deal Desk | Data-recovery / breach-response costs recoverable | "…costs to recover, restore, or reconstruct Customer Data are recoverable as direct damages." |
| 🟦 Buyer L2 | Seller · Legal | Lost profits recoverable through carved-out breaches | "…the exclusion does not apply to damages arising from breach of the confidentiality, security, or IP obligations." |
| 🟦 Buyer L3 | Seller · GC | Broad direct lost-profits recovery preserved | "…nothing in this Section limits Customer's recovery of direct damages, including lost profits." |
| 🚩 **Walkaway** | Exec / walk | Buyer: breach-response/data-recovery waived. Seller: open-ended business-loss exposure. | *(no agreed language)* |

### 3. Indemnification
- **Risky for the Buyer 🟦:** if the product infringes a third party's IP, the buyer is sued and (without indemnity) pays. **Risky for the Seller 🟥:** it agrees to defend and pay claims about its product — ruinous if uncapped.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Issued patents + copyright only; vendor controls defense | "Provider will defend claims that the Services infringe an issued U.S. patent or copyright, and controls the defense and settlement." |
| 🟥 Seller L2 | Buyer · Legal | Indemnity capped at the 1× general cap | "…Provider's indemnity obligations are subject to the limitation of liability in Section [X]." |
| 🟥 Seller L3 | Buyer · GC | One-way; absolute exclusions | "Provider has no obligation for any claim arising from Customer Data, combinations, or modifications." |
| ⚖️ **Balanced** | Market | Mutual; broad IP; carved out of the consequential exclusion; 2–3× supercap | "Each party will defend the other against third-party claims that its technology infringes or misappropriates any patent, copyright, trademark, or trade secret; subject to a [2–3]× cap and carved out of the consequential-damages exclusion." |
| 🟦 Buyer L1 | Seller · Deal Desk | Add trade-secret + "defend from tender" | "…the indemnity covers misappropriation of trade secrets, and Provider will defend from tender of the claim." |
| 🟦 Buyer L2 | Seller · Legal | Supercap to 5× + separate counsel on conflict | "…the indemnity cap is [5]× fees, and Customer may engage separate counsel at Provider's expense on a conflict." |
| 🟦 Buyer L3 | Seller · GC | Uncapped IP indemnity; AI/open-source covered | "Provider's IP-infringement indemnity (including AI output and open-source components) is **uncapped**." |
| 🚩 **Walkaway** | Exec / walk | Buyer: a capped-and-excluded (illusory) indemnity. Seller: fully uncapped IP across all heads. | *(no agreed language)* |

### 4. Warranties & Disclaimer
- **Risky for the Buyer 🟦:** an "AS-IS" disclaimer can leave it with no recourse. **Risky for the Seller 🟥:** broad warranties create ongoing obligations and liability for any shortfall.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | "Substantially conforms"; short window | "Provider warrants the Services will **substantially** conform to the Documentation for [30] days after delivery." |
| 🟥 Seller L2 | Buyer · Legal | Re-performance is the sole remedy for everything | "…re-performance is Customer's **sole and exclusive remedy** for any breach of warranty." |
| 🟥 Seller L3 | Buyer · GC | Disclaimer not subordinated (can gut SLA/security) | "EXCEPT AS STATED, THE SERVICES ARE PROVIDED AS IS AND ALL OTHER TERMS ARE DISCLAIMED." |
| ⚖️ **Balanced** | Market | "Materially conforms" for the term; AS-IS subordinated to express terms | "Provider warrants the Services will **materially** conform to the Documentation throughout the term; **except as expressly stated**, the Services are provided AS IS and implied warranties are disclaimed." |
| 🟦 Buyer L1 | Seller · Deal Desk | Full-term coverage + anti-malware warranty | "…Provider warrants the Services contain no malicious code or disabling devices." |
| 🟦 Buyer L2 | Seller · Legal | Non-infringement / title struck from disclaimer | "…the disclaimer does not extend to the warranties of title and non-infringement." |
| 🟦 Buyer L3 | Seller · GC | Broad fitness-for-purpose + chronic-failure refund | "Provider warrants the Services are fit for Customer's stated purposes; Customer may terminate and obtain a refund for chronic non-conformity." |
| 🚩 **Walkaway** | Exec / walk | Buyer: disclaimer overrides express SLA/security. Seller: uncapped fitness-for-Customer's-purpose warranty. | *(no agreed language)* |

## II. IP & Data

### 5. IP Ownership & License
- **Risky for the Buyer 🟦:** its data/custom work could become vendor IP or fuel model training, or it loses paid-for deliverables. **Risky for the Seller 🟥:** giving away its platform/background IP hands over its business.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Broad feedback license to vendor | "Customer grants Provider a perpetual license to use any feedback or suggestions." |
| 🟥 Seller L2 | Buyer · Legal | Vendor may train on de-identified customer data | "Provider may use **de-identified** Customer Data to improve its services and models." |
| 🟥 Seller L3 | Buyer · GC | Residuals clause; feedback assigned | "Provider may use residual knowledge retained in unaided memory; Customer assigns all feedback to Provider." |
| ⚖️ **Balanced** | Market | Each retains background IP; data never vendor IP; no training without consent | "Each party retains its pre-existing IP; Customer Data is not Provider IP; Provider will not train models on Customer Data without consent; custom deliverables are assigned to Customer on payment." |
| 🟦 Buyer L1 | Seller · Deal Desk | Custom deliverables assigned on payment | "Provider assigns to Customer all right, title, and interest in the Deliverables upon payment." |
| 🟦 Buyer L2 | Seller · Legal | No model-training on customer data (opt-in) | "Provider will **not** use Customer Data to train or fine-tune any model." |
| 🟦 Buyer L3 | Seller · GC | Customer-specific IP assigned; AI output to customer | "All output generated for Customer, and all Customer-specific developments, are owned by Customer." |
| 🚩 **Walkaway** | Exec / walk | Buyer: data trains models / becomes vendor IP. Seller: asked to assign core platform IP. | *(no agreed language)* |

### 6. Confidentiality
- **Risky for the Buyer 🟦:** its sensitive/regulated data could be exposed or under-protected. **Risky for the Seller 🟥:** uncapped liability for an inadvertent slip, plus exposure of its roadmap.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Marking required; 2-yr tail | "Information qualifies as confidential only if **marked**; obligations last [2] years after disclosure." |
| 🟥 Seller L2 | Buyer · Legal | Residuals clause included | "The receiving party may use residual ideas retained in unaided memory." |
| 🟥 Seller L3 | Buyer · GC | Short fixed expiry even for trade secrets | "All confidentiality obligations expire [2] years after termination." |
| ⚖️ **Balanced** | Market | Mutual; objective standard; term + 3 yrs (indefinite for trade secrets) | "Each party will protect the other's Confidential Information using reasonable care; obligations last the term plus three years, and indefinitely for trade secrets." |
| 🟦 Buyer L1 | Seller · Deal Desk | Objective standard; 3-yr tail | "Information that would reasonably be understood to be confidential is protected, whether or not marked." |
| 🟦 Buyer L2 | Seller · Legal | 5-yr tail; regulated data protected while retained | "…obligations last [5] years, and Customer's personal/regulated data is protected for as long as it is retained." |
| 🟦 Buyer L3 | Seller · GC | Breach uncapped; residuals deleted | "Breach of confidentiality is not subject to the liability cap; no residual-use rights are granted." |
| 🚩 **Walkaway** | Exec / walk | Buyer: regulated data loses protection on a fixed clock. Seller: uncapped exposure for an inadvertent slip. | *(no agreed language)* |

### 7. Data Protection & Security (DPA)
- **Risky for the Buyer 🟦:** as controller, a vendor breach triggers *its own* regulator fines/notifications; a slow clock makes it miss its 72h duty. **Risky for the Seller 🟥:** as processor, uncapped breach liability + heavy security/audit duties.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Notice "without undue delay"; SOC 2 satisfies audit | "Provider will notify Customer of a breach without undue delay; Customer's audit right is met by Provider's SOC 2 report." |
| 🟥 Seller L2 | Buyer · Legal / CISO | "Commercially reasonable" security (no named standard) | "Provider will maintain commercially reasonable administrative and technical safeguards." |
| 🟥 Seller L3 | Buyer · GC + CISO | Notice only after vendor confirms; privacy loss inside 1× cap | "Provider will notify Customer after it **confirms** a breach; such liability is subject to the general cap." |
| ⚖️ **Balanced** | Market | ≤72h notice; subprocessor objection + vendor liability; SOC 2/ISO; data super-cap | "Provider will notify Customer within 72 hours of becoming aware of a breach, remains liable for subprocessors, maintains SOC 2 Type II / ISO 27001, and its data-breach liability is capped at [2–3]× and carved out of the consequential exclusion." |
| 🟦 Buyer L1 | Seller · Deal Desk | 72h clock + assistance | "…notice within 72 hours of awareness, with the information Customer needs for its own notifications." |
| 🟦 Buyer L2 | Seller · Legal | 48h clock; maintains SOC 2 II + lapse remediation | "…notice within 48 hours; Provider will promptly remediate any lapse in its SOC 2 / ISO certification." |
| 🟦 Buyer L3 | Seller · GC + CFO | No AI training; for-cause on-site audit; uncapped breach | "Provider will not use Customer Personal Data to train models; Customer may audit for cause; breach liability is uncapped." |
| 🚩 **Walkaway** | Exec / walk | Buyer (regulated): no defined clock / super-cap / no-AI-training. Seller: fully uncapped privacy liability. | *(no agreed language)* |

## III. Commercial Terms

### 8. Payment Terms
- **Risky for the Buyer 🟦:** a billing dispute can trigger interest or suspension of a critical service. **Risky for the Seller 🟥:** slow pay, set-off, and refunds disrupt cash flow it has financed against.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Net 30, annual-in-advance | "Fees are due net 30 days, payable annually in advance, and non-refundable." |
| 🟥 Seller L2 | Buyer · Legal | No set-off; suspension on any past-due | "Payments are without set-off; Provider may suspend the Services on any past-due amount." |
| 🟥 Seller L3 | Buyer · Legal / CFO | Pay-first-dispute-later; immediate suspension; 18% interest | "Customer must pay in full and dispute afterward; overdue amounts accrue interest at 1.5%/month." |
| ⚖️ **Balanced** | Market | Net 30–45; good-faith dispute carve-out; suspension only post-notice | "Fees are due net [30–45] days; Customer may withhold a good-faith disputed amount if it pays the rest; interest and suspension apply only to undisputed amounts after notice and a cure period." |
| 🟦 Buyer L1 | Seller · Deal Desk | Dispute carve-out + SLA-credit set-off | "Disputed amounts are not 'past due'; Customer may apply earned SLA credits." |
| 🟦 Buyer L2 | Seller · Legal / CFO | Net 45–60 | "Fees are due net [45–60] days from receipt of a valid invoice." |
| 🟦 Buyer L3 | Seller · CFO | Broad set-off of finally-determined amounts | "Customer may set off any amount finally determined to be owed by Provider." |
| 🚩 **Walkaway** | Exec / walk | Buyer: a contested invoice can suspend a critical service. Seller: open-ended set-off against receivables. | *(no agreed language)* |

### 9. Price / Fee Escalation
- **Risky for the Buyer 🟦:** uncapped renewal hikes once it's locked in. **Risky for the Seller 🟥:** a price freeze that erodes margin against inflation.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | 5% cap off discounted rate | "Renewal fees may increase by up to 5% over the prior term." |
| 🟥 Seller L2 | Buyer · Legal / CFO | Cap applied to list rate (discount clawback) | "Renewal fees revert to Provider's then-current **list** rates, plus the annual increase." |
| 🟥 Seller L3 | Buyer · CFO | "Greater of 7% or CPI," uncapped | "Renewal fees increase by the **greater of** 7% or the change in CPI." |
| ⚖️ **Balanced** | Market | ~3–5% cap off the discounted rate; named index | "Renewal fees will not increase by more than [3–5]% (or, if lower, CPI-U) over the fees paid in the prior term." |
| 🟦 Buyer L1 | Seller · Deal Desk | First renewal flat; 3% cap | "The first renewal is at the same fees; thereafter, increases are capped at 3%." |
| 🟦 Buyer L2 | Seller · Legal / CFO | Fixed multi-year pricing | "Fees are fixed for the initial term and the first [two] renewals." |
| 🟦 Buyer L3 | Seller · CFO | 0% / price locked for term + renewals | "Fees will not increase for the duration of this Agreement, including renewals." |
| 🚩 **Walkaway** | Exec / walk | Buyer: uncapped / "greater-of" off list. Seller: long hard price freeze in an inflationary market. | *(no agreed language)* |

### 10. Most-Favored-Customer / Benchmarking
- **Risky for the Buyer 🟦:** paying more than comparable customers. **Risky for the Seller 🟥:** a book-wide parity obligation that forces it to stop discounting.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | No MFN; rely on the escalation cap | "Pricing is governed by the escalation cap in Section [9]; no most-favored-pricing applies." |
| 🟥 Seller L2 | Buyer · Legal | List-price-only MFN, broad carve-outs | "Provider's **list** fees are no less favorable than for comparable customers, excluding discounts, bundles, and promotions." |
| 🟥 Seller L3 | Buyer · — (seller declines) | (no seller-favorable MFN — posture is to decline) | *(seller offers a price cap instead of parity)* |
| ⚖️ **Balanced** | Market | Hard escalation cap as the practical substitute | "The parties rely on the renewal cap and locked multi-year pricing in lieu of a most-favored-customer right." |
| 🟦 Buyer L1 | Seller · Deal Desk | Escalation cap + locked pricing (the substitute) | "Fees are locked for the term and capped on renewal, as Customer's price protection." |
| 🟦 Buyer L2 | Seller · Legal / CFO | Net-effective MFN, tight comparator | "If Provider offers a customer of comparable size and term more favorable net pricing, it will offer Customer the same prospectively." |
| 🟦 Buyer L3 | Seller · CFO | Active-monitoring MFN + retroactive credit + audit | "Provider will proactively monitor and grant Customer any more-favorable pricing as a retroactive credit, verifiable by audit." |
| 🚩 **Walkaway** | Exec / walk | Seller: a true book-wide, audited, retroactive MFN. | *(no agreed language)* |

## IV. Term & Exit

### 11. Term & Auto-Renewal
- **Risky for the Buyer 🟦:** silent multi-year lock-in auto-renewing at higher prices. **Risky for the Seller 🟥:** losing predictable recurring revenue / easy churn.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | 1-yr auto-renewal, 60-day notice | "This Agreement auto-renews for successive 1-year terms unless either party gives 60 days' notice." |
| 🟥 Seller L2 | Buyer · Legal | Equal-length (multi-yr) auto-renewal | "…renews for successive periods **equal to the initial term**." |
| 🟥 Seller L3 | Buyer · Legal / CFO | 90-day notice + then-current (uncapped) pricing | "…renews at Provider's then-current pricing unless 90 days' notice is given." |
| ⚖️ **Balanced** | Market | 1-yr renewals; 30–60-day notice; capped uplift; reminder | "This Agreement renews for successive 1-year terms unless either party gives [30–60] days' notice; renewal increases are capped per Section [9]; Provider will send a renewal reminder." |
| 🟦 Buyer L1 | Seller · Deal Desk | 30-day notice + renewal reminder | "…either party may decline renewal on 30 days' notice; Provider will remind Customer beforehand." |
| 🟦 Buyer L2 | Seller · Legal | Renewal pricing fixed/capped | "Renewal fees are fixed at the initial-term rates [or capped at 3%]." |
| 🟦 Buyer L3 | Seller · Deal Desk | No auto-renewal (affirmative opt-in) | "This Agreement does **not** auto-renew; renewal requires Customer's written agreement." |
| 🚩 **Walkaway** | Exec / walk | Buyer: silent multi-year lock-in with uncapped uplift. | *(no agreed language)* |

### 12. Termination
- **Risky for the Buyer 🟦:** no exit when the vendor underperforms, data held hostage, prepaid forfeited. **Risky for the Seller 🟥:** a convenience exit that destroys recognized ARR.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Mutual 30-day cure; 30-day export window | "Either party may terminate for uncured material breach (30 days); data is exportable for 30 days after." |
| 🟥 Seller L2 | Buyer · Legal | Prepaid non-refundable; payment hair-trigger | "Prepaid fees are non-refundable; Provider may terminate on 10 days' non-payment." |
| 🟥 Seller L3 | Buyer · Legal / CFO | No buyer exit; acceleration of committed fees | "Customer has no termination right; on early termination, all committed fees become due." |
| ⚖️ **Balanced** | Market | Mutual for-cause + cure; pro-rata refund on vendor-cause; export + transition | "Either party may terminate for uncured breach; on Provider's breach Customer receives a pro-rata refund; Provider provides data export and transition assistance at the agreed rate card." |
| 🟦 Buyer L1 | Seller · Deal Desk | Trigger-based exits | "Customer may terminate the affected Services for a chronic SLA miss or an uncured security breach." |
| 🟦 Buyer L2 | Seller · Legal | Pro-rata refund + locked transition rate card | "On termination for Provider's breach or discontinuation, Customer receives a pro-rata refund and transition help at the rate card agreed at signing." |
| 🟦 Buyer L3 | Seller · GC + CFO | Termination for convenience mid-term + refund | "Customer may terminate for convenience on [30/60] days' notice with a pro-rata refund." |
| 🚩 **Walkaway** | Exec / walk | Buyer: no exit on failure + no portability. Seller: free mid-term convenience exit on a subscription. | *(no agreed language)* |

### 13. Service Levels (SLA) & Credits
- **Risky for the Buyer 🟦:** downtime hurts its business but credits are tiny and the "sole remedy." **Risky for the Seller 🟥:** uncapped downtime damages and an easy termination trigger.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | 99.9%; credits ≤30% of monthly fee | "Provider targets 99.9% uptime; credits are capped at 30% of the monthly fee." |
| 🟥 Seller L2 | Buyer · Legal | Credits are the sole & exclusive remedy (all heads) | "Service credits are Customer's **sole and exclusive remedy** for any failure of the Services." |
| 🟥 Seller L3 | Buyer · Legal | URL SLA unilaterally amendable; no termination right | "The SLA at [URL] may be updated by Provider; chronic failure does not give a termination right." |
| ⚖️ **Balanced** | Market | 99.9%; sole remedy for *availability only* + cumulative-remedies carve-out; chronic-failure exit | "Provider meets 99.9% uptime; credits are the sole remedy for availability **and do not limit remedies for security/IP/confidentiality breaches**; Customer may terminate for chronic failure." |
| 🟦 Buyer L1 | Seller · Deal Desk | Service-tiered SLOs; auto-applied credits | "Uptime is tiered by service criticality; credits are applied automatically." |
| 🟦 Buyer L2 | Seller · Legal | Credits non-exclusive; chronic-failure termination | "Credits are without prejudice to other remedies; Customer may terminate for chronic SLA failure." |
| 🟦 Buyer L3 | Seller · Legal / CFO | Top-tier credit 100% + refund on chronic miss | "The top credit is 100% of the monthly fee, and Customer may obtain a refund on chronic failure." |
| 🚩 **Walkaway** | Exec / walk | Buyer: credits the only remedy for a security/data failure. Seller: uncapped downtime damages. | *(no agreed language)* |

## V. Operational / Boilerplate

### 14. Insurance
- **Risky for the Buyer 🟦:** no funded coverage standing behind the indemnity/cap. **Risky for the Seller 🟥:** cost of high limits; additional-insured status erodes its own coverage.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | "Commercially reasonable" / CGL only | "Provider maintains commercially reasonable insurance, including CGL of $1M/$2M." |
| 🟥 Seller L2 | Buyer · Legal / CISO | E&O/Cyber blended on one low limit | "Provider maintains combined Tech E&O and Cyber coverage of $[1–2]M." |
| 🟥 Seller L3 | Buyer · Risk / CFO | COI on request only; no AI / waiver of subrogation | "Provider will provide a certificate on request; no additional-insured or subrogation waiver is granted." |
| ⚖️ **Balanced** | Market | CGL + Tech E&O ($2–5M) + Cyber ($3–5M); AI on CGL; "insurance ≠ cap" | "Provider maintains CGL, Tech E&O ($[2–5]M), and Cyber ($[3–5]M) with A-rated carriers, names Customer additional insured on the CGL, and this insurance does not limit liability." |
| 🟦 Buyer L1 | Seller · Deal Desk | Named E&O + Cyber limits | "Provider maintains Tech E&O of $[2–5]M and Cyber of $[3–5]M." |
| 🟦 Buyer L2 | Seller · Legal / CFO | Cyber $5–10M; floors the data super-cap | "Provider maintains Cyber coverage of at least $[5–10]M, which sets the floor for the data-breach super-cap." |
| 🟦 Buyer L3 | Seller · Risk / CFO | Additional insured on claims-made cyber/E&O | "Customer is named additional insured on Provider's Cyber and E&O policies." |
| 🚩 **Walkaway** | Exec / walk | Buyer (data-sensitive): no real, separate cyber limits. Seller: AI status that drains its claims-made cyber tower. | *(no agreed language)* |

### 15. Assignment & Change of Control
- **Risky for the Buyer 🟦:** getting stuck with an assignee/acquirer it didn't choose (incl. a competitor). **Risky for the Seller 🟥:** the mirror — and being blocked from its own M&A/financing.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Mutual + M&A carve-out | "Neither party may assign without consent, except either may assign in a merger or sale of assets." |
| 🟥 Seller L2 | Buyer · Legal | CoC of buyer = deemed assignment (one-way) | "A change of control of **Customer** is deemed an assignment requiring Provider's consent." |
| 🟥 Seller L3 | Buyer · GC | Vendor assigns freely; buyer needs consent (sole discretion) | "Provider may assign freely; Customer may not assign without Provider's consent, in its sole discretion." |
| ⚖️ **Balanced** | Market | Mutual; "not unreasonably withheld"; affiliate + M&A carve-out | "Neither party may assign without the other's consent (not unreasonably withheld), except to an affiliate or in a merger/sale to a non-competitor that assumes this Agreement." |
| 🟦 Buyer L1 | Seller · Deal Desk | "Not unreasonably withheld" qualifier | "Consent to assignment will not be unreasonably withheld, conditioned, or delayed." |
| 🟦 Buyer L2 | Seller · Legal | Competitor-acquisition termination right | "If Provider is acquired by a Customer competitor, Customer may terminate on 30 days' notice." |
| 🟦 Buyer L3 | Seller · GC | Buyer assigns freely (incl. on CoC) to affiliates | "Customer may assign to an affiliate or successor, including on a change of control, without consent." |
| 🚩 **Walkaway** | Exec / walk | Buyer: one-way assignment right + a CoC trip-wire only against it. | *(no agreed language)* |

### 16. Governing Law & Dispute Resolution
- **Risky for the Buyer 🟦:** litigating on the seller's home turf/terms, losing court access. **Risky for the Seller 🟥:** the mirror — the buyer's home forum.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Neutral DE/NY law + venue | "Governed by the laws of [Delaware/New York]; venue in [neutral city]." |
| 🟥 Seller L2 | Buyer · Legal | Seller's home-state law + venue | "Governed by the laws of [Provider's state]; exclusive venue there." |
| 🟥 Seller L3 | Buyer · GC | Home substantive + procedural law + forced arbitration | "Governed by [Provider's state] substantive **and procedural** law; disputes resolved by binding arbitration there." |
| ⚖️ **Balanced** | Market | Neutral law; courts; mutual jury waiver | "Governed by [Delaware/New York] law; the parties submit to the courts of [neutral venue] and waive trial by jury; either may seek injunctive relief for IP/confidentiality." |
| 🟦 Buyer L1 | Seller · Deal Desk | Mutual jury waiver + escalation tier | "The parties will escalate disputes to executives for 30 days before litigation; both waive a jury trial." |
| 🟦 Buyer L2 | Seller · Legal | Buyer's home-state law + venue | "Governed by the laws of [Customer's state]; venue there." |
| 🟦 Buyer L3 | Seller · GC | Mandatory arbitration on buyer's terms | "Disputes resolved by arbitration under [Customer's chosen] rules and seat." |
| 🚩 **Walkaway** | Exec / walk | Either party: the other's home court on the other's procedural terms. | *(no agreed language)* |

### 17. Contractual Limitation Period
- **Risky for the Buyer 🟦:** a short clock from accrual kills claims before defects surface. **Risky for the Seller 🟥:** a long tail of open liability.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | 1 yr from discovery | "No claim may be brought more than one year after it was or should have been discovered." |
| 🟥 Seller L2 | Buyer · Legal | 1 yr from accrual (can run before discovery) | "No claim may be brought more than one year after the cause of action **accrued**." |
| 🟥 Seller L3 | Buyer · GC | 6-month bar from accrual, one-sided | "No claim against Provider may be brought more than six months after accrual." |
| ⚖️ **Balanced** | Market | 1–2 yrs from discovery; mutual; carve-outs | "No claim may be brought more than [1–2] years after discovery; this does not apply to IP, confidentiality, data-breach, indemnity, or payment claims." |
| 🟦 Buyer L1 | Seller · Deal Desk | 2 yrs; mutual | "Either party must bring any claim within two years of discovery." |
| 🟦 Buyer L2 | Seller · Legal | Carve-outs (IP/data/fraud) excluded from the bar | "…the limitation period does not apply to claims for IP infringement, data breach, or fraud." |
| 🟦 Buyer L3 | Seller · GC | No shortened period | "The parties rely on the applicable statutory limitation periods." |
| 🚩 **Walkaway** | Exec / walk | Buyer: a sub-1-yr accrual-based bar (claims die before discovery). | *(no agreed language)* |

### 18. Force Majeure
- **Risky for the Buyer 🟦:** paying for a service it isn't receiving, with no exit. **Risky for the Seller 🟥:** being held liable for events beyond its control.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Mutual, closed list + "similar events" | "Neither party is liable for delays caused by events beyond its reasonable control." |
| 🟥 Seller L2 | Buyer · Legal | SLA credits suspended during the event | "Service-level commitments and credits are suspended during a force-majeure event." |
| 🟥 Seller L3 | Buyer · Legal | Payment continues; no relief; no buyer exit | "Customer remains obligated to pay in full during a force-majeure event, with no termination right." |
| ⚖️ **Balanced** | Market | Mutual; credit/refund for unprovided service; DR/BCP carved out; 30-day exit | "Neither party is liable for force-majeure delays (other than payment); Customer receives a credit for Services not provided; Provider's BCP duties are not excused; either may terminate if the event exceeds 30 days." |
| 🟦 Buyer L1 | Seller · Deal Desk | Abatement/refund for unprovided service | "Fees abate for the period the Services are not provided due to the event." |
| 🟦 Buyer L2 | Seller · Legal | DR/BCP obligations carved out of FM | "Force majeure does not excuse Provider's disaster-recovery and business-continuity obligations." |
| 🟦 Buyer L3 | Seller · GC | 10-day bilateral termination + full refund | "Either party may terminate if the event exceeds 10 days; Customer receives a refund of prepaid unused fees." |
| 🚩 **Walkaway** | Exec / walk | Buyer: pays indefinitely for an unavailable service with no exit. | *(no agreed language)* |

### 19. Audit Rights
- **Risky for the Buyer 🟦:** surprise audits + list-price true-ups + infringement claims (audit-as-revenue). **Risky for the Seller 🟥:** undetected under-licensing (and, in reverse, being audited).

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | 30-day notice, annual, third-party auditor | "Provider may audit Customer's use on 30 days' notice, once per year, via an independent auditor." |
| 🟥 Seller L2 | Buyer · Legal / CFO | True-up at list rate; low cost-shift threshold | "Any shortfall is payable at **list** rates, plus audit costs if usage is understated." |
| 🟥 Seller L3 | Buyer · GC + CFO | Self-help, no-notice audit + auto copyright claim | "Provider may audit without notice; unlicensed use constitutes copyright infringement." |
| ⚖️ **Balanced** | Market | 30-day notice, annual; third-party auditor; contract-rate true-up; reciprocal | "On 30 days' notice, an independent auditor may verify compliance annually; shortfalls over [5%] are paid at **contract** rates after a cure period; Customer has a reciprocal right to audit fees/SLA/security." |
| 🟦 Buyer L1 | Seller · Deal Desk | Reciprocal audit of vendor fees/SLA/security | "Customer may audit Provider's invoicing, SLA performance, and security controls." |
| 🟦 Buyer L2 | Seller · Legal | True-up at contract rate + cure period | "Any true-up is at the contracted rate, after a [30]-day opportunity to cure." |
| 🟦 Buyer L3 | Seller · Deal Desk | No audit (rely on SaaS metering) | "Usage is measured by the platform; no manual audit applies." |
| 🚩 **Walkaway** | Exec / walk | Buyer: no-notice self-help audits + list-price true-up + infringement escalation. | *(no agreed language)* |

### 20. Publicity & Use of Name/Logo
- **Risky for the Buyer 🟦:** unconsented use implies endorsement / breaches its confidentiality. **Risky for the Seller 🟥:** losing marketing/reference rights it values.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Logo/customer-list listing (brand guidelines) | "Provider may identify Customer as a customer using its name and logo per Customer's brand guidelines." |
| 🟥 Seller L2 | Buyer · Legal / Marketing | Press release "will issue" on signing | "The parties **will** issue a joint press release announcing the relationship." |
| 🟥 Seller L3 | Buyer · Marketing / GC | Perpetual, blanket, self-executing grant | "Customer grants Provider a perpetual right to use its name and logo in any medium." |
| ⚖️ **Balanced** | Market | Logo/list allowed; PR/case studies need per-instance consent; revocable | "Provider may list Customer's logo; any press release, case study, or quote requires Customer's prior written consent (not unreasonably withheld)." |
| 🟦 Buyer L1 | Seller · Deal Desk | Per-instance consent for PR/case studies | "Each public reference to Customer requires its prior written approval." |
| 🟦 Buyer L2 | Seller · Legal | Cease-use + remove on termination | "On termination, Provider will stop using and remove Customer's marks within 30 days." |
| 🟦 Buyer L3 | Seller · Marketing | No use of name/logo at all without consent | "Provider will not use Customer's name, logo, or marks without prior written consent for each use." |
| 🚩 **Walkaway** | Exec / walk | Buyer (brand-sensitive/stealth/regulated): a blanket perpetual publicity grant. | *(no agreed language)* |

### 21. Acceptance / Acceptance Testing
- **Risky for the Buyer 🟦:** deemed-accepting (and paying for) a non-conforming deliverable. **Risky for the Seller 🟥:** indefinite unfunded acceptance risk (rev-rec).

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | 15-day window; reminder-gated deemed acceptance | "A Deliverable is accepted if Customer does not object within 15 business days of a reminder." |
| 🟥 Seller L2 | Buyer · Legal | Deemed acceptance on any production use | "Use of a Deliverable in production constitutes acceptance." |
| 🟥 Seller L3 | Buyer · Legal / CFO | 5-day window; "substantially conforms"; sole remedy re-perform | "Deliverables are accepted after 5 days; re-performance is the sole remedy for non-conformity." |
| ⚖️ **Balanced** | Market | Objective criteria set before testing; reject-and-cure; failure backstop; holdback | "Customer tests against agreed criteria within [15–30] days; Provider corrects and re-delivers (up to 2 cycles); on continued failure Customer may reduce price or terminate and refund; [10–20%] is held back until acceptance." |
| 🟦 Buyer L1 | Seller · Deal Desk | Objective criteria fixed before testing | "Acceptance is measured against the criteria agreed in writing before testing begins." |
| 🟦 Buyer L2 | Seller · Legal | 2 cure cycles + price-reduction option | "Provider gets up to two cure cycles; Customer may accept with an equitable price reduction." |
| 🟦 Buyer L3 | Seller · CFO | Terminate-and-refund backstop + 20% holdback | "On failed acceptance Customer may terminate the SOW and recover fees paid; 20% is withheld until acceptance." |
| 🚩 **Walkaway** | Exec / walk | Buyer: deemed acceptance on pilot use with no failure exit. Seller: open-ended acceptance with no deemed date. | *(no agreed language)* |

### 22. Compliance / Anti-Corruption
- **Risky for the Buyer 🟦:** a supplier's bribery/sanctions violation creates *its own* regulatory/criminal exposure. **Risky for the Seller 🟥:** an uncapped dollar-one compliance indemnity + heavy program duties.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Mutual "comply with laws" | "Each party will comply with all laws applicable to its performance." |
| 🟥 Seller L2 | Buyer · Legal | One-way export/sanctions clause against buyer only | "Customer will not use the Services in violation of export-control or sanctions laws." |
| 🟥 Seller L3 | Buyer · GC / Compliance | No ABAC terms at all | *(no anti-corruption or sanctions representations included)* |
| ⚖️ **Balanced** | Market | Mutual ABAC (FCPA + UKBA); program + flow-down; violation = termination | "Each party complies with anti-corruption (FCPA, UK Bribery Act) and sanctions laws, maintains reasonable controls, and is not a Sanctioned Person; a violation is a material breach." |
| 🟦 Buyer L1 | Seller · Deal Desk | Mutual ABAC reps (FCPA + UKBA) | "Each party represents it has not made and will not make any improper payment." |
| 🟦 Buyer L2 | Seller · Legal / Compliance | ABAC program covenant + flow-down | "Provider maintains an anti-corruption compliance program and flows these terms down to subcontractors." |
| 🟦 Buyer L3 | Seller · GC + CFO | Standalone uncapped anti-corruption indemnity | "Provider indemnifies Customer, without limit, for losses arising from its violation of anti-corruption or sanctions laws." |
| 🚩 **Walkaway** | Exec / walk | Buyer (regulated): no mutual ABAC + flow-down. Seller: a dollar-one uncapped ABAC indemnity. | *(no agreed language)* |

### 23. Subcontracting & Non-Solicitation
- **Risky for the Buyer 🟦:** losing key people / a sub mishandling its data with no recourse to the prime; an over-broad non-solicit against it. **Risky for the Seller 🟥:** losing staff to the customer; constrained delivery.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Vendor may subcontract, remains liable | "Provider may use subcontractors and remains responsible for their performance." |
| 🟥 Seller L2 | Buyer · Legal | One-way non-solicit, 24 mo, whole workforce | "During the term and 24 months after, Customer will not solicit any Provider employee." |
| 🟥 Seller L3 | Buyer · GC | LD-backed non-solicit; no prime liability for subs | "Customer will pay liquidated damages of [__] per solicited employee; Provider is not liable for subcontractor acts." |
| ⚖️ **Balanced** | Market | Vendor fully liable for subs; key-personnel continuity; mutual non-solicit | "Provider remains fully liable for subcontractors and flows down terms; data subs follow the DPA process; neither party will solicit the other's engagement personnel for 12 months (general advertising excluded)." |
| 🟦 Buyer L1 | Seller · Deal Desk | Flow-down + DPA process for data subs | "Subcontractors with access to Customer Data are engaged under the DPA subprocessor process." |
| 🟦 Buyer L2 | Seller · Legal | Named key personnel + reassignment lock | "Provider will not reassign the named key personnel for [6–12] months without Customer's consent and an equal-or-better replacement." |
| 🟦 Buyer L3 | Seller · GC | Buyer approval required for all subcontractors | "Provider will not use any subcontractor without Customer's prior written approval." |
| 🚩 **Walkaway** | Exec / walk | Buyer: vendor not liable for its subs. Non-solicit: one-way/whole-workforce (and void as to CA/ND/OK staff). | *(no agreed language)* |

### 24. Data Portability, Return & Transition
- **Risky for the Buyer 🟦:** lock-in — can't get its data out in usable form; captive transition pricing. **Risky for the Seller 🟥:** cost/effort of transition; giving up derived/aggregated data.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Standard-functionality export, 30-day window | "Customer may export its data via the standard export feature for 30 days after termination." |
| 🟥 Seller L2 | Buyer · Legal / CISO | "Customer Data" defined narrowly (raw records only) | "'Customer Data' means the records Customer uploads, excluding configuration, logs, and derived data." |
| 🟥 Seller L3 | Buyer · Legal / CFO | Transition only "as reasonable" at uncapped PS rates | "Provider will provide reasonable transition assistance at its then-current professional-services rates." |
| ⚖️ **Balanced** | Market | Portable-format export (incl. attachments/config/logs); 60–90-day window; rate card locked at signing | "For [60–90] days, Provider will export Customer Data in a documented machine-readable format at no charge, then delete and certify; transition assistance is available at the rate card in Exhibit [__]." |
| 🟦 Buyer L1 | Seller · Deal Desk | Documented format/API; 60–90-day window | "Export is available via a documented API/format for at least 60 days after termination." |
| 🟦 Buyer L2 | Seller · Legal | Attachments/config/logs included; free export | "'Customer Data' includes attachments, configuration, and logs; export is provided at no charge." |
| 🟦 Buyer L3 | Seller · GC + CFO | Continuity / source-code escrow for critical deps | "Provider will maintain a continuity escrow ([standby hosting / source code]) released on insolvency, discontinuation, or chronic failure." |
| 🚩 **Walkaway** | Exec / walk | Buyer: no portable export + no transition rate card locked at signing. | *(no agreed language)* |

### 25. Notices, Entire Agreement & Precedence
- **Risky for the Buyer 🟦:** a sales-drafted Order Form silently overriding negotiated MSA protections; fraud contracted out. **Risky for the Seller 🟥:** ambiguity over which terms control; operative notices mis-served.

| Level | Escalates to | Summary | Example clause language |
|---|---|---|---|
| 🟥 Seller L1 | Buyer · Procurement | Email for routine notices | "Notices may be given by email to the parties' designated contacts." |
| 🟥 Seller L2 | Buyer · Legal | Order Form + URL terms sit on top of all terms | "In a conflict, the Order Form and referenced online terms control over this Agreement." |
| 🟥 Seller L3 | Buyer · GC | URL terms "as updated"; non-reliance excludes fraud | "Online terms apply as updated from time to time; Customer has relied on no statement outside this Agreement." |
| ⚖️ **Balanced** | Market | MSA controls legal terms; Order Form overrides only by express signed reference; fraud carve-out | "This MSA controls; an Order Form overrides it only where it expressly identifies the superseded Section and is signed; online terms are pinned to a dated version; nothing excludes liability for fraud." |
| 🟦 Buyer L1 | Seller · Deal Desk | Confirmed delivery for operative notices + copy-to-counsel | "Notices of breach, termination, or a claim require confirmed delivery, with a copy to Legal." |
| 🟦 Buyer L2 | Seller · Legal | URL terms pinned to a dated version | "Online terms apply as of the Effective Date and will not change to Customer's material detriment during the term." |
| 🟦 Buyer L3 | Seller · GC | MSA supreme on all terms; no unilateral changes | "This MSA controls over all Order Forms and exhibits; no term changes without a signed amendment." |
| 🚩 **Walkaway** | Exec / walk | Buyer: a sales-drafted Order Form can silently override the MSA, or fraud is contracted out. | *(no agreed language)* |
