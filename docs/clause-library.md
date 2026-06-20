# Clause-Language Bank

Model language for the most-negotiated B2B (SaaS / technology + services) clauses, in three
variants — **🟥 Vendor-favorable**, **⚖️ Market (balanced)**, **🟦 Customer-favorable** — so
you can drop in a starting position and walk it with the [vendor-defense playbook](vendor-defense-playbook.md)
(opening → fallback ladder → red lines). This is the *drafting* complement to the
[negotiation playbook](negotiation-playbook.md) (which explains *why* each lands where it does).

**How to use:** pick the variant matching your posture and leverage, fill the `[bracketed]`
terms, and conform defined terms (`Provider`, `Customer`, `Services`, `Order Form`,
`Documentation`, `Customer Data`, `Confidential Information`) to your paper. Keep
ALL-CAPS where shown — limitation-of-liability, disclaimers, and the consequential-damages
waiver must be *conspicuous* (UCC 2-316 / 2-719).

> **General market-practice templates, not legal advice.** Have counsel adapt to your deal
> and jurisdiction before use.

*Part 1 covers the 9 core risk/IP/commercial clauses; Part 2 covers the remaining clauses
(DPA, commercial, operational) and standard boilerplate — the full set.*

---

## 1. Limitation of Liability (aggregate cap)

*Anchor: a single 1× trailing-12-month-fees cap; the fight is moving high-severity heads off the 1× number. See playbook §1.*

**🟥 Vendor-favorable**
> EXCEPT FOR CUSTOMER'S PAYMENT OBLIGATIONS, EACH PARTY'S TOTAL AGGREGATE LIABILITY ARISING OUT OF OR RELATED TO THIS AGREEMENT WILL NOT EXCEED THE FEES PAID BY CUSTOMER UNDER THE APPLICABLE ORDER FORM IN THE TWELVE (12) MONTHS PRECEDING THE EVENT GIVING RISE TO THE CLAIM. THIS LIMIT IS CUMULATIVE ACROSS ALL CLAIMS AND DOES NOT RESET.

**⚖️ Market (balanced)**
> EXCEPT FOR THE EXCLUDED MATTERS BELOW, EACH PARTY'S TOTAL AGGREGATE LIABILITY WILL NOT EXCEED THE FEES PAID OR PAYABLE IN THE TWELVE (12) MONTHS PRECEDING THE CLAIM (OR, FOR CLAIMS IN THE FIRST YEAR, THE GREATER OF FEES PAID OR THE FIRST-YEAR ANNUAL FEES). EACH PARTY'S LIABILITY FOR BREACH OF ITS DATA-PROTECTION/SECURITY OBLIGATIONS WILL NOT EXCEED 2× THAT AMOUNT. THE FOREGOING LIMITS DO NOT APPLY TO ("Excluded Matters"): (a) the indemnification obligations; (b) breach of confidentiality; (c) a party's gross negligence, willful misconduct, or fraud; (d) death or bodily injury or damage to tangible property; or (e) Customer's payment obligations.

**🟦 Customer-favorable**
> EACH PARTY'S AGGREGATE LIABILITY (EXCEPT FOR THE EXCLUDED MATTERS) WILL NOT EXCEED THE GREATER OF (a) [2×/3×] THE FEES PAID OR PAYABLE IN THE PRIOR 12 MONTHS OR (b) $[____]. PROVIDER'S LIABILITY FOR A DATA-SECURITY BREACH IS [UNCAPPED / CAPPED AT 5× FEES OR PROVIDER'S CYBER-INSURANCE LIMIT, WHICHEVER IS GREATER]. THE EXCLUDED MATTERS ARE NOT SUBJECT TO THIS CAP **OR** TO THE EXCLUSION OF CONSEQUENTIAL DAMAGES. Excluded Matters: indemnification; breach of confidentiality, security, or data-protection obligations; IP infringement; gross negligence, willful misconduct, or fraud; death/bodily injury; and payment obligations.

## 2. Exclusion of Consequential / Indirect Damages

*Anchor: mutual category waiver survives; the fight is named heads + carve-outs. See playbook §2.*

**🟥 Vendor-favorable**
> IN NO EVENT WILL EITHER PARTY BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY, OR PUNITIVE DAMAGES, OR FOR ANY LOST PROFITS, REVENUE, GOODWILL, BUSINESS, ANTICIPATED SAVINGS, OR LOSS OR CORRUPTION OF DATA, WHETHER IN CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE, EVEN IF ADVISED OF THE POSSIBILITY AND NOTWITHSTANDING THE FAILURE OF ESSENTIAL PURPOSE OF ANY REMEDY.

**⚖️ Market (balanced)**
> *Prepend:* EXCEPT WITH RESPECT TO THE EXCLUDED MATTERS (Section 1), IN NO EVENT WILL EITHER PARTY BE LIABLE FOR … [as above]. *(So the carve-outs escape the waiver, not just the dollar cap.)*

**🟦 Customer-favorable**
> *Add proviso:* … provided that this exclusion does not limit (a) amounts a party must pay to a third party under the indemnities, (b) damages arising from breach of confidentiality, security, or data-protection obligations, or (c) Customer's reasonable costs to procure substitute services or to recover, restore, or reconstruct lost or corrupted Customer Data.

## 3. Indemnification (IP infringement + third-party claims)

*Anchor: distinguish the consequential-exclusion carve-out (near-universal) from the dollar cap (the real fight). See playbook §3.*

**🟥 Vendor-favorable**
> Provider will defend Customer against any third-party claim alleging that the Services, used in accordance with this Agreement, infringe a U.S. patent issued as of the Effective Date or any copyright, and will pay damages finally awarded, provided Customer (a) promptly notifies Provider, (b) grants Provider sole control of the defense and settlement, and (c) reasonably cooperates. Provider has no obligation for claims arising from Customer Data, modifications not made by Provider, combination with non-Provider products, or use in breach of this Agreement. If the Services are or may be enjoined, Provider may, at its option, procure a license, modify the Services, or terminate and refund prepaid unused fees. THIS SECTION STATES PROVIDER'S SOLE LIABILITY AND CUSTOMER'S EXCLUSIVE REMEDY FOR INFRINGEMENT.

**⚖️ Market (balanced)**
> Each party (the "Indemnitor") will defend the other against third-party claims that (for Provider) the Services infringe or misappropriate any patent, copyright, trademark, or trade secret, or (for Customer) that the Customer Data or Customer's use in breach of this Agreement does so, and will indemnify against damages and reasonable costs finally awarded or agreed in settlement. Conditions: prompt notice (failure excuses the Indemnitor only to the extent prejudiced); Indemnitor controls defense; the indemnified party may participate with its own counsel at its expense; no settlement imposing non-monetary obligations or admissions on the indemnified party without consent. *Dollar treatment: subject to the data/IP super-cap and carved out of the consequential-damages exclusion.*

**🟦 Customer-favorable**
> *As Market, plus:* the IP indemnity is **uncapped** (or capped at [3×/5×] fees); on a conflict of interest the indemnified party may assume its own defense at the Indemnitor's expense; the remedy ladder (license / modify / terminate) applies only after the Indemnitor first uses commercially reasonable efforts to procure a license so Customer can continue using the Services; and the indemnity expressly covers open-source and AI-output infringement.

## 4. Warranties & Disclaimer

*Anchor: keep the AS-IS disclaimer; the customer wins the "except as expressly stated" subordination. See playbook §4.*

**🟥 Vendor-favorable**
> Provider warrants that the Services will perform substantially in accordance with the Documentation. Customer's sole and exclusive remedy for breach is, at Provider's option, re-performance or correction or, if Provider cannot do so within a commercially reasonable time, a refund of prepaid fees for the nonconforming Services. EXCEPT AS EXPRESSLY STATED, THE SERVICES ARE PROVIDED "AS IS," AND PROVIDER DISCLAIMS ALL OTHER WARRANTIES, EXPRESS OR IMPLIED, INCLUDING MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT, AND DOES NOT WARRANT THAT THE SERVICES WILL BE UNINTERRUPTED OR ERROR-FREE.

**⚖️ Market (balanced)**
> *As above but:* "materially in accordance with the Documentation" for the duration of the subscription term; add mutual warranties of authority and no-conflict, and Provider warranties that (a) the Services will not contain malicious code or disabling devices and (b) Provider will maintain the security measures in [Exhibit __]. The sole-remedy clause does not apply to breach of the security, confidentiality, or IP warranties.

**🟦 Customer-favorable**
> *As Market, plus:* Provider warrants the Services will conform in all material respects to the Documentation and the Order Form, that professional services will be performed in a professional and workmanlike manner by qualified personnel, and that Provider will comply with all applicable laws; **non-infringement and title are removed from the disclaimer**; and Customer may terminate the affected Services and receive a pro-rata refund if a material nonconformity is not cured within [30] days.

## 5. IP Ownership & License Grant

*Anchor: vendor keeps the platform; customer wins its data + custom work + training control. See playbook §5.*

**🟥 Vendor-favorable**
> As between the parties, Provider owns all right, title, and interest in and to the Services, the Provider Technology, and all modifications, enhancements, and derivatives, including any suggestions or feedback (which Customer hereby assigns to Provider). Provider grants Customer a non-exclusive, non-transferable, revocable license to access and use the Services during the Term solely for Customer's internal business purposes.

**⚖️ Market (balanced)**
> Each party retains all right, title, and interest in its pre-existing and independently developed IP. Provider grants Customer a non-exclusive, worldwide license to use the Services during the Term for its business purposes (non-revocable except for uncured material breach). As between the parties, Customer owns Customer Data and Confidential Information, which are not Provider IP. Customer grants Provider a license to use Customer Data solely to provide and secure the Services. Feedback is licensed (not assigned) to Provider on a perpetual, royalty-free basis, excluding Customer Confidential Information.

**🟦 Customer-favorable**
> *As Market, plus:* Provider hereby assigns to Customer all right, title, and interest in any Deliverables created specifically for Customer upon payment (with a work-made-for-hire recital and a present assignment backup); Provider will **not** use Customer Data to train, fine-tune, or improve any model except in [aggregated and de-identified] form [or: not at all] without Customer's prior written consent; Provider retains no residual-knowledge rights over Customer Confidential Information; and any AI output generated for Customer is owned by (or exclusively licensed to) Customer.

## 6. Confidentiality

*Anchor: low-leverage, resolves to market norms; the live points are the survival tail and trade-secret carve-out. See playbook §6.*

**🟥 Vendor-favorable**
> "Confidential Information" means non-public information disclosed by a party that is marked confidential or that should reasonably be understood to be confidential. The Receiving Party will protect it with at least reasonable care, use it only to perform under this Agreement, and not disclose it except to personnel with a need to know who are bound by confidentiality. Obligations last during the Term and for [three (3)] years thereafter, except trade secrets remain protected for as long as they qualify as trade secrets. Standard exclusions (public, already known, independently developed, rightfully received) apply; compelled disclosure permitted with notice.

**⚖️ Market (balanced)**
> *As above, mutual,* with recipients (including affiliates, advisors, and subcontractors) bound by terms at least as protective; Customer's personal/regulated data is protected for as long as the Receiving Party retains it; on termination, the Receiving Party will return or destroy Confidential Information and certify destruction (backup-retention and one-archival-copy carve-outs permitted).

**🟦 Customer-favorable**
> *As Market, plus:* objective standard (no marking required); survival tail of [five (5)] years (indefinite for trade secrets and for Customer's personal/regulated data); no residuals; the parties acknowledge that breach may cause irreparable harm and the disclosing party may seek injunctive relief without posting a bond; and breach of confidentiality is an Excluded Matter (uncapped or super-capped) under Section 1.

## 7. Payment Terms & Late Fees

*Anchor: keep the cash-flow architecture; concede the good-faith dispute carve-out. See playbook §8.*

**🟥 Vendor-favorable**
> Fees are due net thirty (30) days from the invoice date, payable annually in advance, non-refundable, and without set-off or deduction. Overdue amounts accrue interest at 1.5% per month (or the maximum permitted by law, if less) from the due date. Provider may suspend the Services on any past-due amount.

**⚖️ Market (balanced)**
> Fees are due net [thirty (30) / forty-five (45)] days from receipt of a valid invoice. Customer may withhold a reasonably and in-good-faith disputed amount if it pays the undisputed portion and notifies Provider with reasonable detail; disputed amounts are not "past due." Interest accrues only on undisputed past-due amounts and only after [10] days' written notice and opportunity to cure. Provider may suspend only for undisputed amounts that remain unpaid after such notice, and will restore the Services promptly on payment.

**🟦 Customer-favorable**
> *As Market, with:* net [forty-five (45) / sixty (60)] days; Customer may set off earned SLA credits [and any amount finally determined to be owed by Provider]; prepaid fees are refundable on a pro-rata basis on termination for Provider's uncured breach or discontinuation; and any late-fee/collection-cost provision is mutual.

## 8. Term & Auto-Renewal

*Anchor: defend the auto-renew default and pricing power; concede 1-year renewals + a shorter notice window. See playbook §11.*

**🟥 Vendor-favorable**
> The initial term is [__] years. This Agreement will automatically renew for successive periods equal to the initial term unless either party gives written notice of non-renewal at least sixty (60) days before the end of the then-current term. Renewals are at Provider's then-current pricing.

**⚖️ Market (balanced)**
> The initial term is [__] years, then automatically renews for successive one-year terms unless either party gives written notice of non-renewal at least [30–60] days before the end of the then-current term. Fees on renewal will not increase by more than the greater of [5%] or [CPI, capped at __%] over the prior term. Provider will send Customer a renewal reminder at least [__] days before the non-renewal deadline.

**🟦 Customer-favorable**
> The initial term is [__] years. **Renewal requires Customer's affirmative written agreement** (no automatic renewal) [or: auto-renews for one-year terms terminable on 30 days' notice]. Renewal pricing is fixed at the initial-term rates [or capped at 3% / CPI]; non-renewal notice is mutual and may be given by email to the other party's notice contact.

## 9. Termination

*Anchor: hold mid-term subscription convenience; give a clean exit on vendor failure + portability. See playbook §12.*

**🟥 Vendor-favorable**
> Either party may terminate for the other's material breach not cured within thirty (30) days of written notice (ten (10) days for non-payment). Customer has no right to terminate for convenience. On termination, prepaid fees are non-refundable and any committed fees become immediately due. Provider will make Customer Data available for export for thirty (30) days after termination, after which it may be deleted.

**⚖️ Market (balanced)**
> *As above, mutual,* with the payment cure period applying only after written notice and not to good-faith disputed amounts; on termination for Provider's uncured breach or discontinuation of the Services, Customer receives a pro-rata refund of prepaid, unused fees; Provider will, for [60–90] days, make Customer Data available for export in a documented, machine-readable format and, on request, provide transition assistance at the rate card in [Exhibit __]; on Customer's request Provider will certify deletion (backup/legal-hold carve-outs apply).

**🟦 Customer-favorable**
> *As Market, plus:* Customer may terminate for convenience on [30/60] days' notice with a pro-rata refund of prepaid unused fees [or: terminate the affected Services for a chronic SLA miss, an uncured security/data breach, a discontinuation, or a price increase above the cap]; transition assistance for up to [__] days at the locked rate card (with a bucket of [__] hours included); and a free export in non-proprietary format.

---

# Part 2 — remaining clauses

## 10. Data Protection, Privacy & Security (DPA)

*Anchor: usually a separate exhibit; the live points are the breach clock, subprocessor liability, and the super-cap. See playbook §7.*

**🟥 Vendor-favorable**
> Provider processes Customer Personal Data as a processor solely to provide the Services, per Customer's instructions and the DPA at [URL]. Provider maintains commercially reasonable technical and organizational measures, may engage the subprocessors listed at [URL], and will notify Customer of a confirmed Personal Data Breach without undue delay. Customer's audit right is satisfied by Provider's then-current SOC 2 report.

**⚖️ Market (balanced)**
> Provider maintains a written information-security program aligned to [SOC 2 Type II / ISO 27001] (Exhibit __); notifies Customer of a Personal Data Breach without undue delay and no later than seventy-two (72) hours after becoming aware, with the information Customer needs for its own notifications and reasonable assistance; gives advance notice of new subprocessors with a [30]-day objection right; and remains liable for its subprocessors. Cross-border transfers rely on the SCCs / IDTA / Data Privacy Framework. Liability for breach of this Section is subject to the data super-cap (Section 1) and carved out of the consequential-damages exclusion.

**🟦 Customer-favorable**
> *As Market, with:* breach notice within [48] hours of becoming aware; Provider maintains [SOC 2 Type II and ISO 27001] and promptly remediates any lapse or qualified finding; Customer (or its auditor) may audit for cause; new subprocessors require [Customer's prior approval / push notice + objection + right to terminate the affected Services]; Provider will **not** use Customer Personal Data to train or improve any model; and Provider's liability for a data-security breach is [uncapped / 5× fees or its cyber limit].

## 11. Price / Fee Escalation at Renewal

*Anchor: 3–5% is market; close the uncapped/"greater-of" tail and fix the discounted base. See playbook §9.*

**🟥 Vendor-favorable**
> On each renewal, fees increase by the greater of [5–7%] or the change in CPI over the prior term, applied to Provider's then-current list rates.

**⚖️ Market (balanced)**
> On renewal, fees will not increase by more than [5%] (or, if lower, the increase in the CPI-U over the prior twelve months), applied to the fees paid in the prior term. Provider will give at least [60] days' notice of any increase.

**🟦 Customer-favorable**
> Fees are fixed for the initial term, and no renewal increase will exceed [3%] over the prior term's fees [or: fees are fixed for [3] years]; any increase is calculated on Customer's actual discounted fees, not list, and does not compound retroactively.

## 12. Most-Favored-Customer / Benchmarking

*Anchor: vendors give a price cap before parity; a narrow MFN survives only when carve-outs make it symbolic. See playbook §10.*

**🟥 Vendor-favorable**
> *Decline; redirect to the escalation cap.* If pressed: Provider represents the list fees offered are no less favorable than its standard list fees for comparable volume; this excludes discounts, promotions, bundles, and channel/affiliate pricing.

**⚖️ Market (balanced)**
> If during the Term Provider grants a customer of comparable size and commitment more favorable per-unit fees for the same Services on substantially similar terms, Provider will offer Customer those fees prospectively for the remainder of the Term, verified by an officer's certificate on request. *(Frequently replaced entirely by a hard escalation cap.)*

**🟦 Customer-favorable**
> Provider warrants Customer's net effective per-unit pricing is and will remain at least as favorable as that offered to any comparable customer; on request an independent auditor may verify, and more-favorable pricing applies as a retroactive credit. *Multi-year alternative:* beginning in Year 2, Customer may engage an independent benchmarker; if fees exceed the [top-quartile] market range, the parties will adjust or Customer may terminate.

## 13. Service Levels (SLA) & Uptime Credits

*Anchor: the % rarely moves; win the mechanics — cumulative-remedies carve-out + chronic-failure exit. See playbook §13.*

**🟥 Vendor-favorable**
> Provider will use commercially reasonable efforts to make the Services available 99.9% of each calendar month, excluding scheduled maintenance and the exclusions in the SLA at [URL]. Service credits per that schedule are Customer's sole and exclusive remedy for availability failures, and must be requested within thirty (30) days.

**⚖️ Market (balanced)**
> Provider will meet 99.9% monthly uptime (tiered per Exhibit __). Credits (up to [30–50%] of the monthly fee) are Customer's sole and exclusive remedy **for availability failures only** and do not limit remedies for breach of security, IP, or confidentiality obligations. Maintenance is capped and pre-scheduled; claims within [60] days.

**🟦 Customer-favorable**
> 99.95% for [core] services; top-tier credit of [100%] of the monthly fee; **credits are without prejudice to Customer's other rights and remedies (not exclusive)**; if uptime falls below [95%] in any month or below [99.9%] for [3] consecutive months, Customer may terminate the affected Services and receive a pro-rata refund; credits are applied automatically.

## 14. Insurance

*Anchor: concede higher limits, not additional-insured on claims-made cyber/E&O. See playbook §14.*

**🟥 Vendor-favorable**
> Provider will maintain commercially reasonable insurance, including commercial general liability of at least $1M per occurrence / $2M aggregate, and will provide a certificate on request.

**⚖️ Market (balanced)**
> Provider will maintain, with carriers rated A- VII or better: CGL ($1M / $2M); Technology Errors & Omissions ($[2–5]M); Cyber/Privacy ($[3–5]M); and statutory workers' compensation. On request Provider will name Customer as additional insured on the CGL (primary and non-contributory) and provide certificates. This insurance does not limit Provider's liability.

**🟦 Customer-favorable**
> *As Market, with:* Cyber/Privacy of at least $[5–10]M (no sublimit below $[__] for ransomware/business interruption); E&O written separately from Cyber; Customer named additional insured on the CGL with waiver of subrogation; [30] days' notice of cancellation; and Provider's cyber limit floors the data-breach super-cap (Section 1).

## 15. Assignment & Change of Control

*Anchor: mutual + M&A/affiliate carve-out is standard; the fight is the competitor exclusion and CoC trigger. See playbook §15.*

**🟥 Vendor-favorable**
> Customer may not assign this Agreement without Provider's prior written consent. Provider may assign freely to an affiliate or in connection with a merger, acquisition, or sale of assets. Any prohibited assignment is void. A change of control of Customer is deemed an assignment requiring Provider's consent.

**⚖️ Market (balanced)**
> Neither party may assign without the other's prior written consent (not to be unreasonably withheld, conditioned, or delayed), except either party may assign, on notice, to an affiliate or in connection with a merger or sale of all or substantially all assets, provided the assignee assumes this Agreement in writing and is not a competitor of the other party. This Agreement binds permitted successors and assigns.

**🟦 Customer-favorable**
> *As Market, with:* the change-of-control "deemed assignment" trigger removed (or made mutual); if Provider is acquired by a Customer competitor, Customer may terminate on [30] days' notice; and nothing restricts a party's assignment of receivables (UCC §§9-406/9-408).

## 16. Governing Law, Venue & Dispute Resolution

*Anchor: neutral law; enterprise keeps courts; jury waiver survives. See playbook §16.*

**🟥 Vendor-favorable**
> This Agreement is governed by the laws of the State of [Provider's home state], excluding conflicts rules. The parties consent to the exclusive jurisdiction and venue of the courts located in [home state]. EACH PARTY WAIVES ANY RIGHT TO A JURY TRIAL.

**⚖️ Market (balanced)**
> Governed by the laws of the State of [Delaware / New York], excluding conflicts rules. The parties submit to the exclusive jurisdiction of the state and federal courts in [neutral venue], and will first attempt to resolve any dispute by escalation to senior executives within [30] days. EACH PARTY WAIVES TRIAL BY JURY. Either party may seek injunctive relief for IP or confidentiality breaches in any court of competent jurisdiction.

**🟦 Customer-favorable**
> Governed by the laws of [Customer's state / a neutral state]; disputes are resolved in court (not mandatory arbitration); the jury waiver and any fee-shifting are mutual; nothing limits either party's right to equitable relief. *(Arbitration alternative for cross-border/confidential deals: binding arbitration under [AAA/JAMS] rules, seat [city], before [one/three] arbitrator(s), with class actions waived.)*

## 17. Contractual Limitation Period

*Anchor: a clear, reasonable shortening is enforceable; the fight is accrual vs. discovery. See playbook §17.*

**🟥 Vendor-favorable**
> No claim arising out of or related to this Agreement may be brought more than one (1) year after the cause of action accrued.

**⚖️ Market (balanced)**
> No claim may be brought more than one (1) year after the party knew or reasonably should have known of the facts giving rise to it; this does not apply to claims for IP infringement, breach of confidentiality, indemnification, or payment.

**🟦 Customer-favorable**
> No claim may be brought more than two (2) years after discovery; this Section is mutual, subject to the carve-outs above, and does not shorten any statutory period that cannot be contractually reduced. *(Note: UCC 2-725 floors goods claims at one year; unenforceable in Louisiana.)*

## 18. Force Majeure

*Anchor: payment isn't excused, but pay-for-what-you-get + a 30-day termination valve. See playbook §18.*

**🟥 Vendor-favorable**
> Neither party is liable for any delay or failure (other than payment obligations) caused by events beyond its reasonable control, including acts of God, war, terrorism, pandemic, government action, labor disputes, and utility, internet, or supplier failures.

**⚖️ Market (balanced)**
> Neither party is liable for delay or failure (other than payment) due to events beyond its reasonable control and not its fault (the listed events and other similar events). The affected party will notify the other and use reasonable efforts to mitigate and resume. Payment is not excused, but Customer is entitled to a credit or pro-rata refund for Services not provided during the event, and Provider's disaster-recovery / business-continuity obligations are not excused.

**🟦 Customer-favorable**
> *As Market, with:* if the event continues more than [thirty (30)] days, either party may terminate the affected Services and Customer receives a refund of prepaid, unused fees; and security, confidentiality, and breach-notification obligations are never excused.

## 19. Audit / Compliance-Verification Rights

*Anchor: conduct terms are cheap; the money is the true-up rate, not just the threshold. See playbook §19.*

**🟥 Vendor-favorable**
> Provider may, on reasonable notice, audit Customer's use of the Services for compliance. If an audit reveals underpayment, Customer will pay the shortfall at list rates plus the audit costs.

**⚖️ Market (balanced)**
> On at least thirty (30) days' notice, no more than once per twelve (12) months (or for cause), an independent auditor under NDA may verify Customer's compliance during business hours, excluding other-tenant and regulated data. Underpayment exceeding [5%] is paid at contract rates plus reasonable audit costs, after Customer has [30] days to cure.

**🟦 Customer-favorable**
> *As Market, with:* true-up at contract (not list) rates; cost-shift only above [5–10%]; no automatic copyright-infringement or termination escalation; and a reciprocal right for Customer to audit Provider's fees, SLA performance, and security on the same terms.

## 20. Publicity & Use of Name/Logo

*Anchor: bare logo is cheap; PR/case studies need per-instance consent. See playbook §20.*

**🟥 Vendor-favorable**
> Customer grants Provider the right to use Customer's name and logo to identify Customer as a customer in Provider's marketing materials, customer lists, and website.

**⚖️ Market (balanced)**
> Provider may identify Customer as a customer using its name and logo per Customer's brand guidelines (no implied endorsement); any press release, case study, or quote requires Customer's prior written consent (not unreasonably withheld), with a [5–10] business-day review.

**🟦 Customer-favorable**
> Neither party will use the other's name, logo, or marks without prior written consent for each use; on termination Provider will cease use and remove Customer's marks within [30] days; carve-out for confidential disclosure to investors or advisors under NDA. Provider will not use Customer Data or this relationship to train any model.

## 21. Acceptance / Acceptance Testing

*Anchor: objective criteria set before testing + a real cure loop and failure backstop. See playbook §21.*

**🟥 Vendor-favorable**
> A Deliverable is deemed accepted if Customer does not give written notice of material non-conformity within five (5) business days of delivery, or on first production use. Provider's sole obligation is to correct confirmed non-conformities within a commercially reasonable time.

**⚖️ Market (balanced)**
> Customer will test each Deliverable against the mutually agreed acceptance criteria within fifteen (15) business days of delivery, and will accept or give written notice specifying the criteria not met. Provider will correct and re-deliver (up to [2] cycles, resetting the test period). If Customer does not respond, Provider may send a reminder and the Deliverable is deemed accepted [5] business days later. Production use other than agreed UAT is deemed acceptance.

**🟦 Customer-favorable**
> *As Market, with:* a thirty (30) business-day test period; on failure after [2] cure cycles Customer may extend, accept with an equitable price reduction, or terminate the affected SOW and receive a refund of fees paid for the Deliverable; and [10–20%] of the Deliverable fee is held back until acceptance.

## 22. Compliance with Laws / Anti-Corruption

*Anchor: mutual ABAC reps are cheap; the cost items are audit and a dollar-one indemnity. See playbook §22.*

**🟥 Vendor-favorable**
> Each party will comply with applicable laws. Customer will not use the Services in violation of export-control or sanctions laws, or by or for any sanctioned person or embargoed jurisdiction.

**⚖️ Market (balanced)**
> Each party will comply with applicable laws, including anti-corruption laws (the U.S. FCPA and the UK Bribery Act) and export-control and sanctions laws. Each represents that it has not and will not offer, pay, or accept any improper payment, maintains reasonable anti-corruption controls, and is not a Sanctioned Person or 50%-or-more owned by one.

**🟦 Customer-favorable**
> *As Market, with:* Provider maintains an anti-corruption compliance program and flows these obligations down to subcontractors; a violation is a material breach permitting termination without cure; and breach of this Section is an Excluded Matter (uncapped / super-capped) under Section 1.

## 23. Subcontracting, Personnel & Non-Solicitation

*Anchor: delegate the work, not the responsibility; non-solicits are void as to CA/ND/OK staff. See playbook §23.*

**🟥 Vendor-favorable**
> Provider may use subcontractors and remains responsible for their performance. During the Term and for [12] months after, Customer will not solicit for employment any Provider personnel involved in the Services.

**⚖️ Market (balanced)**
> Provider may subcontract but remains fully liable for its subcontractors and will flow down relevant terms; subcontractors with access to Customer Data are subject to the DPA subprocessor process. During the engagement and for [12] months after, neither party will solicit the other's personnel involved in the engagement; general advertising and responses to it are excluded.

**🟦 Customer-favorable**
> *As Market, with:* subcontractors with access to Customer Data or systems require Customer's prior approval; Provider names key personnel who will not be reassigned for [6–12] months without Customer's consent and an equal-or-better replacement; and the non-solicit is mutual and limited to active solicitation of engagement staff. **Employee non-solicits are void/unenforceable as to California (and North Dakota / Oklahoma) personnel — sever accordingly.**

## 24. Data Portability, Return & Transition

*Anchor: portability is cheap to concede; lock the transition rate card at signing. See playbook §24.*

**🟥 Vendor-favorable**
> On request within thirty (30) days after termination, Provider will make Customer Data available for export via the Services' standard export functionality, after which Provider may delete it.

**⚖️ Market (balanced)**
> For [60–90] days after termination, Provider will make Customer Data available for export in a documented, machine-readable format (e.g., CSV/JSON or a documented API), at no charge for normal volumes; thereafter Provider will delete it and, on request, certify deletion (backup and legal-hold carve-outs apply). On request, Provider will provide transition assistance at the rate card in [Exhibit __].

**🟦 Customer-favorable**
> *As Market, with:* "Customer Data" includes attachments, configuration, and logs; export is free; transition assistance for up to [__] days at the rate card locked at signing, with [__] hours included; and, for critical dependencies, Provider maintains a continuity arrangement ([standby hosting / source-code escrow]) released on insolvency, discontinuation, or chronic failure.

## 25. Boilerplate (standard single-version language)

**Notices.**
> Notices must be in writing to the addresses on the cover page. Routine notices may be given by email; notices of breach, termination, or a claim must be given by personal delivery, nationally recognized courier, or certified mail (or email with confirmed receipt), with a copy to the recipient's [Legal / General Counsel]. Notice is effective on receipt.

**Entire agreement & order of precedence.**
> This Agreement (including its Order Forms, SOWs, DPA, and exhibits) is the entire agreement and supersedes all prior or contemporaneous discussions. In a conflict, the following order controls: this MSA, then the DPA (for data-protection matters), then the applicable SOW or Order Form — except an Order Form or SOW prevails over the MSA only where it expressly identifies the superseded Section and is signed by both parties. Each party acknowledges it has not relied on any representation not set out in this Agreement; this does not exclude liability for fraud.

**Amendment.** > No amendment is effective unless in writing and signed by both parties.

**Waiver.** > No failure or delay in exercising a right is a waiver, and no waiver is effective unless in writing.

**Severability.** > If any provision is held unenforceable, it will be modified to the minimum extent necessary to make it enforceable, and the remaining provisions stay in effect.

**Counterparts / e-signature.** > This Agreement may be executed in counterparts and by electronic signature, each of which is deemed an original.

**Independent contractors.** > The parties are independent contractors; nothing creates a partnership, joint venture, agency, or employment relationship.

**Survival.** > Provisions that by their nature should survive termination — including accrued fees, IP ownership, confidentiality, warranty disclaimers, limitation of liability, indemnification, and governing law — survive.

**Third-party beneficiaries.** > There are no third-party beneficiaries, except indemnified parties may enforce the indemnities.

**Cumulative remedies.** > Except where a remedy is expressly stated to be sole and exclusive, all remedies are cumulative and in addition to any other remedies available at law or in equity.
