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

*Part 1 below covers the 9 core risk/IP/commercial clauses. Part 2 (remaining clauses —
DPA, escalation, SLA, assignment, governing law, force majeure, audit, IP indemnity edge
cases, boilerplate) is listed at the end.*

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

## Part 2 — remaining clauses (to add)

These pair with the playbook but are either lower-frequency to redraft or more standardized;
say the word and I'll add them (with the same three-variant treatment where variants matter):

- **Data Protection, Privacy & Security (DPA)** — usually a separate exhibit; breach-notice clock, subprocessor terms, security standard, super-cap.
- **Price / fee escalation** · **Most-favored-customer / benchmarking** · **Service levels (SLA) & credits** · **Insurance**.
- **Assignment & change of control** · **Governing law, venue & dispute resolution** · **Contractual limitation period** · **Force majeure** · **Audit rights** · **Publicity** · **Acceptance** · **Compliance / anti-corruption** · **Subcontracting / non-solicit** · **Data portability / escrow**.
- **Boilerplate (single standard version):** notices · entire agreement & order of precedence · amendment · waiver · severability · counterparts / e-signature · independent contractor · survival · third-party beneficiaries · cumulative remedies.
