# Buyer-Redline Playbook: Open, Climb, Must-Haves

The **buyer-side mirror** of the [vendor-defense playbook](vendor-defense-playbook.md) — the
same 25 clauses from the **customer / procurement** seat. Per clause: where to **open** your
redline, the **fallback ladder** to climb (trade every *give* for a *get*) toward the market
landing, your **must-haves / walk-aways**, and where to **push hardest**.

Pairs with: the [negotiation playbook](negotiation-playbook.md) (where deals actually land),
the 🟦 *customer-favorable* language in the [clause bank](clause-library.md) (your opening
text), and the **Procurement** view in [persona-summaries.md](persona-summaries.md).

> **How to use:** open at your redline; climb the ladder only as far as you must, taking a
> *get* for every *give*; spend leverage where the money and risk are; concede the
> market-standard items; and **lock the exit and price protection pre-signature** — your
> leverage evaporates once switching costs sink. *General market-practice guidance, not legal
> advice.*

## I. Risk Allocation

### 1. Limitation of Liability (cap)
**Open:** mutual cap at the **greater of [2–3×] trailing-12-mo fees or $[floor]**; data-breach **uncapped** (or 5× / vendor's cyber limit); uncapped carve-outs (IP indemnity, confidentiality, gross negligence/willful misconduct/fraud, bodily injury) that escape **both** the cap **and** the consequential-damages exclusion.
**Ladder (give → get):**
1. **Give** accept a general cap at 1× fees **→ Get** data/privacy + IP indemnity lifted to a 2–3× supercap (or uncapped) and the uncapped carve-out list.
2. **Give** drop "uncapped" on data breach **→ Get** a hard supercap pegged to the vendor's cyber-insurance limit, so recovery tracks real collectible dollars.
🎯 **Must-have / walk:** data-breach and IP exposure must **not** sit at 1× fees; carve-outs must escape the consequential *exclusion* (a capped-and-excluded indemnity is worthless); the dollar cap is mutual.
💬 **Push hardest when:** data is sensitive/regulated, you're a large/strategic buyer, or you have a credible alternative.

### 2. Exclusion of Consequential Damages
**Open:** mutual waiver, but carve out (a) third-party amounts payable under the indemnities, (b) breach of confidentiality/security/data-protection, and (c) your costs to recover/restore/reconstruct data.
**Ladder (give → get):**
1. **Give** accept the category-level mutual waiver and lost-profits as a named exclusion **→ Get** the carve-out list above escapes the waiver (not just the dollar cap).
2. **Give** concede "value of lost data" stays excluded **→ Get** "costs to recover/restore data" + breach-response costs remain recoverable.
🎯 **Must-have / walk:** data-recovery and breach-response costs recoverable; carve-outs mirror the cap carve-outs.
💬 **Push hardest when:** the deal touches your sensitive data.

### 3. Indemnification
**Open:** mutual; covers patent/copyright/trademark **+ trade secret**; uncapped (or 3–5× supercap); carved out of the consequential exclusion; notice-and-prejudice; your own counsel on a conflict; vendor must first try to procure a license before modify/terminate.
**Ladder (give → get):**
1. **Give** let the vendor control the defense **→ Get** notice-and-prejudice (not strict notice), settlement consent for anything non-monetary/admission, separate counsel on conflict.
2. **Give** accept a 2–3× supercap instead of fully uncapped **→ Get** the supercap pegged to insurance, and the consequential-exclusion carve-out (non-negotiable).
🎯 **Must-have / walk:** the indemnity must escape the consequential exclusion; "**defend**" (pay as incurred), not just "indemnify"; trade-secret + AI-output/open-source covered.
💬 **Push hardest when:** your use of the product is broad or business-critical.

### 4. Warranties & Disclaimer
**Open:** "**materially** conforms to Documentation" for the full term; add anti-malware/no-disabling-code, security-per-exhibit, and compliance-with-law warranties; strike **non-infringement and title** from the disclaimer; sole-remedy non-exclusive for security/IP; chronic-failure termination + refund.
**Ladder (give → get):**
1. **Give** accept the AS-IS disclaimer of implied warranties and "no uninterrupted/error-free" **→ Get** the "**except as expressly stated**" subordination so the disclaimer can't gut the SLA/security/compliance promises.
2. **Give** accept re-performance as the first remedy **→ Get** a refund + chronic-failure termination backstop.
🎯 **Must-have / walk:** disclaimer subordinated to the express warranties; security/IP breaches escape the sole-remedy funnel.
💬 **Push hardest when:** the service is mission-critical.

## II. IP & Data

### 5. IP Ownership & License
**Open:** each retains background IP; your Data and Confidential Information are **never** vendor IP; **no AI training on your data without consent** (opt-in); custom deliverables assigned to you on payment; no residuals; feedback is a license only (excluding your CI); license non-revocable except for cause.
**Ladder (give → get):**
1. **Give** concede the vendor owns its platform/Services **→ Get** your data never becomes vendor IP, and no model-training on it without consent.
2. **Give** allow feedback as a license to the vendor **→ Get** your Confidential Information excluded; residuals deleted or trade-secret-carved.
🎯 **Must-have / walk:** no training on your data without consent; data/CI never vendor IP; custom work assigned to you.
💬 **Push hardest when:** your data is proprietary, sensitive, or a competitive asset.

### 6. Confidentiality
**Open:** mutual; objective standard; survival **5 yr** (indefinite for trade secrets and your regulated/personal data while retained); no residuals; return/destroy + certification; injunctive relief; breach super-capped or uncapped.
**Ladder (give → get):**
1. **Give** accept a term + 3-yr tail **→ Get** indefinite protection for trade secrets and your regulated/personal data.
2. **Give** accept the standard exclusions **→ Get** residuals deleted/narrowed.
🎯 **Must-have / walk:** your regulated/personal data protected as long as the vendor retains it; breach carved out of the cap.
💬 **Push hardest when:** you're disclosing trade secrets or regulated data.

### 7. Data Protection, Privacy & Security (DPA)
**Open:** breach notice **≤72h (push 48h) of awareness** + content + assistance; subprocessor approval, or push-notice + 30-day objection + right to terminate the affected Services; **vendor directly liable for subprocessors**; maintains SOC 2 Type II/ISO 27001 with lapse remediation; for-cause audit backstop; SCCs/IDTA/DPF for transfers; **no AI training on your data**; data-breach liability uncapped or 5×. *Bring this on your own DPA/addendum.*
**Ladder (give → get):**
1. **Give** accept general subprocessor authorization **→ Get** push-notice + objection + terminate-affected-service, and vendor direct liability for subs.
2. **Give** accept report-based audit (SOC 2) **→ Get** a for-cause on-site backstop + remediation on any lapse/qualified finding.
🎯 **Must-have / walk:** a defined breach clock (you owe your *own* regulator a 72h GDPR notice); no AI training on your data; data-breach off the general cap.
💬 **Push hardest when:** you're regulated or data-sensitive — these are compliance necessities, not asks.

## III. Commercial Terms

### 8. Payment Terms
**Open:** net **45–60**; good-faith dispute carve-out; interest only on undisputed amounts after notice; apply earned SLA credits as set-off; pro-rata refund of prepaid on termination for cause; fees mutual.
**Ladder (give → get):**
1. **Give** accept annual-in-advance and no general set-off **→ Get** the good-faith dispute carve-out (disputed amounts aren't "late," no suspension) + apply earned SLA credits.
2. **Give** accept net 30 **→ Get** the clock runs from a *conforming* invoice + 10–15 day cure before any interest/suspension.
🎯 **Must-have / walk:** good-faith dispute carve-out; suspension only for undisputed amounts after notice.
💬 **Push hardest when:** invoicing volume/complexity makes billing errors likely.

### 9. Price / Fee Escalation
**Open:** fixed renewal cap **[3%]** calculated **off your discounted rate**; first renewal flat (or fixed multi-year pricing); anti-compounding.
**Ladder (give → get):**
1. **Give** accept a 5% cap **→ Get** it's off your discounted rate (not list) and framed "lesser of CPI and 5%."
2. **Give** accept CPI indexing **→ Get** a *named* BLS index + a hard ceiling.
🎯 **Must-have / walk:** the increase is off the **discounted** base, not list (kills the silent year-1 clawback); a hard cap (no "greater of"/uncapped).
💬 **Push hardest when:** always — and **win it pre-signature**; renewal leverage is gone once you're locked in.

### 10. Most-Favored-Customer / Benchmarking
**Open:** net-effective pricing at least as favorable as comparable customers, verifiable, with retroactive credit; for multi-year, independent benchmarking with adjustment or termination.
**Ladder (give → get):**
1. **Give** drop a true MFN **→ Get** a hard escalation cap + locked multi-year pricing (the practical substitute vendors will actually give).
2. **Give** accept certificate-only verification **→ Get** a tight comparator definition + a prospective credit.
🎯 **Must-have / walk:** realistically, the **price cap** — parity is rarely conceded, so don't trade the cap away chasing it.
💬 **Push hardest when:** large ACV with real leverage.

## IV. Term & Exit

### 11. Term & Auto-Renewal
**Open:** **no auto-renewal** (affirmative opt-in), or 1-year renewals terminable on 30 days; renewal pricing fixed/capped; renewal reminder; mutual notice by email.
**Ladder (give → get):**
1. **Give** accept auto-renewal **→ Get** successive **1-year** terms (not equal-length), a 30–60-day window, and a pre-deadline reminder.
2. **Give** accept "then-current pricing" language **→ Get** the uplift cap from clause 9.
🎯 **Must-have / walk:** no silent multi-year lock-in; capped renewal uplift.
💬 **Push hardest when:** pre-signature, always.

### 12. Termination
**Open:** termination for convenience [or trigger-based: chronic SLA miss, uncured security/data breach, discontinuation, price-walk-away]; pro-rata refund; export in standard format; transition assistance at a **rate card locked now**.
**Ladder (give → get):**
1. **Give** drop mid-term convenience on the subscription **→ Get** trigger-based termination + a clean non-renewal + pro-rata refund on vendor-cause.
2. **Give** accept that prepaid is generally non-refundable **→ Get** a pro-rata refund specifically on the vendor's uncured breach or discontinuation.
🎯 **Must-have / walk:** a clean exit on vendor failure; portable-format export + **transition rate card locked at signing**.
💬 **Push hardest when:** pre-signature — lock-in is the existential exit risk.

### 13. Service Levels (SLA) & Credits
**Open:** 99.95% for core services; top-tier credit **100%** of the monthly fee; credits **non-exclusive** (without prejudice to other remedies); chronic-failure termination + refund; credits applied automatically.
**Ladder (give → get):**
1. **Give** accept 99.9% and the credit caps **→ Get** the **cumulative-remedies carve-out** (credits don't bar damages for security/IP/confidentiality) + a chronic-failure termination right.
2. **Give** accept monthly measurement **→ Get** automatic credits + a 60–90-day claim window.
🎯 **Must-have / walk:** chronic-failure exit; the sole-remedy doesn't reach security/IP breaches.
💬 **Push hardest when:** the service is business-critical.

## V. Operational / Boilerplate

### 14. Insurance
**Open:** Cyber/Privacy **$5–10M** (sublimits for ransomware/BI), E&O unblended, A-rated carriers, additional insured + waiver of subrogation, 30-day cancellation notice, and the cyber limit **floors the data super-cap**.
**Ladder (give → get):**
1. **Give** drop additional-insured on claims-made cyber/E&O **→ Get** higher separate limits + the cyber limit pegged to the data super-cap.
2. **Give** accept a COI (not endorsement) on some lines **→ Get** actual endorsements for CGL additional-insured + waiver of subrogation.
🎯 **Must-have / walk:** real cyber limits sized to your exposure; "**insurance ≠ cap**."
💬 **Push hardest when:** data-sensitive or regulated.

### 15. Assignment & Change of Control
**Open:** mutual; consent "**not unreasonably withheld/conditioned/delayed**"; both get the affiliate + M&A carve-out (assignee not a competitor, assumes in writing); drop the one-sided CoC-as-assignment trigger; if the vendor is acquired by your competitor, you may terminate.
**Ladder (give → get):**
1. **Give** accept the vendor's affiliate/M&A freedom **→ Get** the same freedom for you + drop the one-sided CoC trigger.
2. **Give** accept consent for assignment **→ Get** the "not unreasonably withheld" qualifier.
🎯 **Must-have / walk:** mutual; competitor-acquisition termination right.
💬 **Push hardest when:** the vendor competes with you or is an acquisition target.

### 16. Governing Law & Dispute Resolution
**Open:** neutral (DE/NY) or your state; **courts, not mandatory arbitration**; mutual jury waiver; mutual IP/equitable carve-out; no one-sided fee-shifting.
**Ladder (give → get):**
1. **Give** accept neutral law (not your home state) **→ Get** strike the "substantive *and procedural*" overreach + a neutral venue.
2. **Give** accept the jury waiver **→ Get** it's mutual, and you keep court access (no forced arbitration).
🎯 **Must-have / walk:** not the vendor's home court on the vendor's terms; mutual.
💬 **Push hardest when:** enterprise deal (keep courts for appeal/discovery).

### 17. Contractual Limitation Period
**Open:** **2 years from discovery**, mutual, with carve-outs (IP, confidentiality, data breach, indemnity, payment) — or strike it entirely.
**Ladder (give → get):**
1. **Give** accept a 1-year period **→ Get** a **discovery** trigger (not accrual) + the carve-outs.
🎯 **Must-have / walk:** the discovery rule (a claim can't expire before you could reasonably know); latent-defect/security carve-outs.
💬 **Push hardest when:** latent defects/security risk are plausible.

### 18. Force Majeure
**Open:** mutual; payment not excused but **credit/refund for unprovided service**; **DR/BCP carved out**; SLA clock keeps running; bilateral termination if the event exceeds 30 days + refund.
**Ladder (give → get):**
1. **Give** accept that payment isn't excused **→ Get** abatement/credit/refund for Services not provided during the event.
2. **Give** accept a broad event list **→ Get** DR/BCP obligations carved out + a 30-day termination valve.
🎯 **Must-have / walk:** pay-for-what-you-get; DR/BCP not excused; an exit if it drags on.
💬 **Push hardest when:** the service underpins your operations.

### 19. Audit Rights
**Open:** limit the vendor's audit of you (30-day notice, 1×/yr, third-party auditor, true-up at **contract rate**, cure first, no copyright escalation) **and add a reciprocal audit** of the vendor's fees/SLA/security.
**Ladder (give → get):**
1. **Give** accept a compliance-verification right **→ Get** third-party auditor under NDA, contract-rate true-up, 5–10% cost-shift threshold, and a cure period.
2. **Give** accept SaaS metered-overage billing **→ Get** overage at the contract rate + pre-bill notice.
🎯 **Must-have / walk:** true-up at **contract**, not list, rate; no automatic copyright-infringement/termination escalation.
💬 **Push hardest when:** on-prem/perpetual licensing (audit leverage is real there).

### 20. Publicity & Use of Name/Logo
**Open:** no use of your name/logo without **prior written consent for each use**; cease/remove on termination; mutual; no AI-training or marketing use of your data.
**Ladder (give → get):**
1. **Give** allow a bare logo / customer-list listing (per your brand guidelines) **→ Get** PR, case studies, and quotes require per-instance prior written consent (not deemed approval).
🎯 **Must-have / walk:** no published statement about you without consent; the license is revocable and ends on termination.
💬 **Push hardest when:** you're brand-sensitive, regulated, or in stealth.

### 21. Acceptance / Acceptance Testing
**Open:** objective criteria **agreed before testing**; 30-business-day window; reject-and-cure (≥2 cycles); failure backstop (price reduction / terminate + refund); 10–20% holdback.
**Ladder (give → get):**
1. **Give** accept deemed acceptance after a written reminder + a bounded window **→ Get** objective criteria fixed before testing + the production-use trigger narrowed to exclude pilot/UAT/DR.
2. **Give** accept re-performance as the primary remedy **→ Get** a terminate-and-refund backstop after failed cure cycles + a holdback.
🎯 **Must-have / walk:** objective criteria; a real failure exit; not deemed-accepted on mere pilot use.
💬 **Push hardest when:** custom development / systems-integration work.

### 22. Compliance with Laws / Anti-Corruption
**Open:** mutual compliance + ABAC (**FCPA + UK Bribery Act**), no knowledge/materiality on the core "no bribe"; program + flow-down; Sanctioned-Person rep; violation = termination; carve-out from the cap.
**Ladder (give → get):**
1. **Give** accept reps (rather than a standalone uncapped indemnity) **→ Get** mutual ABAC + flow-down + termination on violation.
2. **Give** accept an annual certification (not a books-and-records audit) for SaaS **→ Get** the certification right + the program covenant.
🎯 **Must-have / walk:** mutual ABAC reps + flow-down (for your own regulatory defense).
💬 **Push hardest when:** you're a regulated or public-facing buyer — this is your compliance posture.

### 23. Subcontracting, Personnel & Non-Solicitation
**Open:** consent for data-touching subs; vendor **fully liable** for subs; named key personnel + reassignment lock + equal-or-better replacement; non-solicit mutual, engagement-staff only, with a general-advertising carve-out.
**Ladder (give → get):**
1. **Give** accept that the vendor may subcontract **→ Get** the vendor remains fully liable + flows down terms + runs data subs through the DPA subprocessor process.
2. **Give** accept a mutual non-solicit **→ Get** it's limited to active solicitation of engagement staff, with general-advertising/employee-initiated carve-outs (and void as to CA/ND/OK staff).
🎯 **Must-have / walk:** vendor liable for its subs; key-personnel continuity (you're paying a services premium).
💬 **Push hardest when:** services/SI engagements where named people matter.

### 24. Data Portability, Return & Transition
**Open:** export in **non-proprietary, machine-readable format** (incl. attachments/config/logs), free, 60–90-day window + retain-until-export; transition assistance at a **rate card locked now**; deletion + certification; continuity escrow for critical dependencies.
**Ladder (give → get):**
1. **Give** concede the vendor keeps usage/derived/aggregated data **→ Get** documentation + your attachments/config/logs included in the export.
2. **Give** accept standard-functionality export **→ Get** a documented format/API + a 60–90-day window + a locked transition rate card.
🎯 **Must-have / walk:** portable-format export + a transition rate card **locked at signing** (avoid the captive-monopoly price at the worst moment).
💬 **Push hardest when:** pre-signature — lock-in is the existential exit risk.

### 25. Notices, Entire Agreement & Precedence
**Open:** the **MSA controls legal terms**; an Order Form overrides only by an express, signed, section-specific reference; the DPA governs data; URL terms pinned to a dated version (no unilateral mid-term change); fraud carve-out in the entire-agreement clause; operative notices need confirmed delivery + a copy to your counsel.
**Ladder (give → get):**
1. **Give** accept email for routine notices **→ Get** termination/breach/claim notices require confirmed delivery + copy-to-counsel.
2. **Give** accept incorporation of URL terms **→ Get** them pinned to a dated version with no material adverse mid-term change.
🎯 **Must-have / walk:** MSA-on-top for legal terms (stop a sales Order Form silently overwriting negotiated terms); URL terms pinned.
💬 **Push hardest when:** low-salience but high-consequence — whoever read the clause wins.

---

## Reading the leverage (buyer side)

- **Spend leverage where the money and risk are:** caps/supercaps, indemnity, data protection, price-escalation cap, and the exit. **Concede the unwinnable:** the AS-IS disclaimer, "no uninterrupted/error-free," the mutual consequential waiver, mid-term convenience on a subscription, and the 99.9% uptime number.
- **Pre-signature is peak leverage** — win uplift caps, portability, transition rates, and price before switching costs sink.
- **Insist on mutuality and real carve-outs** — make the cap/indemnity/assignment mutual, and ensure carve-outs escape the consequential *exclusion*, or the indemnity you "won" is worthless.
- **Regulated/data-sensitive?** Your own GDPR/CCPA/sector duties set the non-negotiables (breach clock, subprocessor controls, audit, no-AI-training) — bring them on your own addendum.
- **Your leverage drivers:** a documented credible alternative, deal size, and a multi-year/volume commitment (trade it for price protection and lower caps).
