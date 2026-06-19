# Vendor-Defense Playbook: Opening, Fallbacks, Red Lines

> Internal negotiation cheat-sheet for the **vendor side** of a B2B SaaS / technology + services deal. Per clause: where to **open**, the **fallback ladder** to walk down (trade every *give* for a *get*), the **red line** you hold or escalate on, and **who signs off**. Companion to [`negotiation-playbook.md`](negotiation-playbook.md).
>
> **How to use:** open at the Opening; walk *down* the ladder only as far as the deal needs; never give a rung away without taking its *get*; escalate the moment an ask crosses an **Escalate when** trigger; never cross a **Red line** without the named approver. Entries marked **†** are first-pass drafts (the second review pass was interrupted) — sound, but provisional.
>
> *General market-practice reference, not legal advice — adapt with counsel.*


## I. Risk Allocation


### 1. Limitation of Liability — Aggregate Cap + Supercaps

**Opening.** On our paper, open with a SINGLE one-sided aggregate cap on Vendor's total liability equal to 1x the fees PAID by Customer to Vendor in the trailing twelve (12) months preceding the event giving rise to the claim, calculated PER ORDER FORM (not across the whole MSA).


**Fallback ladder:**

1. **Give** Make the dollar cap MUTUAL (applies symmetrically to both parties), and confirm the consequential-damages exclusion is mutual. → **Get** Customer accepts our cap STRUCTURE — the single aggregate cap, the anti-stacking sentence, and the consequential-damages exclusion with lost…
2. **Give** Concede the MARKET-STANDARD uncapped carve-outs that no cap survives at law or that are universally granted: a party's gross negligence, willful… → **Get** (a) The carve-out list is CLOSED to these heads at this rung (IP, confidentiality, and data stay inside the dollar treatment for now);
3. **Give** Move the cap metric from 'fees paid' to 'fees paid OR PAYABLE' in the trailing 12 months, and add a year-one floor of 'the greater of… → **Get** Customer holds the multiplier at 1x for the GENERAL cap and agrees the trailing-12-month look-back window keyed to the EVENT (not 'all amounts ever…
4. **Give** Concede a DATA/PRIVACY/SECURITY SUPERCAP at 2x trailing-12-month fees for losses arising from breach of the security/DPA obligations or unauthorized… → **Get** (a) The supercap is the SOLE elevated number for those heads — no uncapped data liability;
5. **Give** Concede an IP-INDEMNITY SUPERCAP at 2–3x trailing-12-month fees (the IP indemnity is carved out of the consequential-damages exclusion —… → **Get** (a) Customer drops any demand for an UNCAPPED data-breach figure and an UNCAPPED IP indemnity, accepting that IP and data sit at bounded 2–3x…


🛑 **Red line.** Do NOT agree to (1) an UNCAPPED general liability cap, or a general multiplier above roughly 2x trailing-12-month fees (1x is the target; ~2x is the absolute ceiling — anything over 1x is a GC item, not freely available); (2) an UNCAPPED data/privacy/security-breach figure;

⬆️ **Escalate when.** Deal-desk / junior counsel may sign WITHIN the ladder down to and including rung 5 — i.e. mutual 1x general cap with a 'greater of fees or [¼-year then full first-year ACV]' floor, the standard uncapped heads (gross negligence, willful…


**Talking points:**

- Twelve months of fees is the common market anchor for the GENERAL cap — comparable enterprise SaaS deals cluster there, usually expressed as prior-12-month fees or roughly one…
- A liability cap proportionate to fees is what makes the price possible: liability is priced into the fee.
- We are not asking you to bear catastrophic risk uncapped — we're moving the high-severity heads (your data and privacy, IP infringement, our willful misconduct and fraud) OFF the…
- A data/privacy supercap pegged to our cyber tower ties your recovery to real, collectible dollars.


*Drafting:* - Default the cap metric to fees "PAID" (not "paid or payable") and to amounts paid in the trailing 12 months PER ORDER FORM — "paid" and per-order both shrink the base;


### 2. Exclusion of Consequential / Indirect Damages

**Opening.** Put on our paper a broad, MUTUAL waiver in conspicuous ALL CAPS: "EXCEPT AS EXPRESSLY SET FORTH HEREIN, NEITHER PARTY WILL BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, EXEMPLARY OR PUNITIVE DAMAGES, OR FOR ANY LOST PROFITS, LOST REVENUES, LOST OR DAMAGED DATA, LOSS OF GOODWILL, LOSS OF BUSINESS, OR COST OF SUBSTITUTE/COVER SERVICES…


**Fallback ladder:**

1. **Give** Confirm the waiver is facially reciprocal (it already is) and keep the customary 'EXCEPT AS EXPRESSLY SET FORTH HEREIN' lead-in so it visibly does… → **Get** Customer accepts that the abstract category waiver (indirect/incidental/special/punitive/exemplary) survives in full and is reciprocal, and that the…
2. **Give** Concede that the customer's reasonable, documented out-of-pocket COSTS TO RECOVER AND RESTORE customer data, and reasonable third-party… → **Get** Customer agrees these recoverable amounts remain subject to the data/privacy SUPERCAP (2-3x) — not uncapped — and agrees the VALUE of lost data and…
3. **Give** Agree that THIRD-PARTY amounts the customer is legally obligated to PAY OUT (settlements, judgments, statutory fines/penalties where insurable and… → **Get** Customer agrees those amounts stay subject to the applicable dollar cap/supercap and to 'legally obligated to pay' (excluding voluntary/unapproved…
4. **Give** Agree that lost profits / revenue may be recovered ONLY when they flow THROUGH a specifically carved-out breach (IP indemnity, confidentiality… → **Get** Customer agrees lost profits remain an EXPRESSLY NAMED EXCLUDED HEAD for everything else (ordinary performance/SLA failures, downtime, defects) AND…
5. **Give** As the final retreat, accept the customer's preferred conspicuousness formatting (e.g., bold rather than full ALL-CAPS) and delete the standalone… → **Get** Customer agrees the named-head exclusions (lost profits, lost-data value, cover) survive as independent exclusions, recovery through carve-outs stays…


🛑 **Red line.** Do NOT accept (a) deletion of the lost-profits exclusion as a GENERAL matter — i.e., the customer recovering its own lost profits for ordinary performance failures, downtime, or defects, outside the carve-outs;

⬆️ **Escalate when.** Deal-desk/junior counsel may grant Rung 1 (reciprocity framing + dropping the 'regardless of characterization' gloss). Senior contracts counsel may grant Rungs 2-4 — capped data-recovery/breach-response costs, third-party pay-out amounts…


**Talking points:**

- This waiver is facially reciprocal and is standard between sophisticated commercial parties — it runs against both of us on the same terms.
- Consequential-damages waivers between sophisticated businesses are routinely enforced as a matter of freedom of contract;
- The carve-outs you actually need are already addressed: costs to recover and restore your data, and third-party breach-response and forensics costs, come back to you as…
- Where it matters most to you — a security incident, a confidentiality breach, an IP problem — lost profits are NOT off the table;


*Drafting:* List lost profits, lost revenue, lost/corrupted data, loss of goodwill, loss of business, and cost of cover/substitute services as their OWN enumerated excluded heads — never only as examples of 'indirect' damages — so they are barred even…


### 3. Indemnification (IP infringement + third-party claims)

**Opening.** One-way only: Vendor indemnifies Customer against third-party claims that the unmodified Service, used in accordance with the Documentation and this Agreement, directly infringes an ISSUED patent, a registered copyright, or a registered trademark in the United States (no trade-secret misappropriation, no pending/continuation/provisional patents, no foreign…


**Fallback ladder:**

1. **Give** Carve the IP indemnity (defense costs, settlements, court-awarded damages) OUT of the consequential/indirect-damages exclusion so it is not barred as… → **Get** In the same breath, lock the structural concession that the DOLLAR cap is a SEPARATE question that survives this carve-out — i.e., get Customer's…
2. **Give** Extend scope to issued patents and registered copyrights/trademarks in the territory where the Service is licensed and used (drop 'U.S.-only'); → **Get** Hold the 1x general cap as the dollar treatment for now, and keep the remaining exclusions intact.
3. **Give** Convert the absolute exclusions to 'to the extent' (proportional) carve-outs, so a partially-excluded claim isn't wholly forfeited. → **Get** Customer accepts a notice-and-prejudice standard (late notice cuts off the indemnity only to the extent Vendor is actually prejudiced) AND keeps…
4. **Give** Make the indemnity MUTUAL — Customer indemnifies Vendor for third-party claims arising from Customer Data, Customer-provided content/specs, and… → **Get** Reciprocity on BOTH the obligation and the dollar treatment: whatever cap the Vendor indemnity ultimately carries, Customer's mirrors it.
5. **Give** Lift the dollar treatment off the 1x general cap to a SUPERCAP of 2x trailing-12-month fees (open at 2x). → **Get** Vendor retains sole control of the defense and authority to settle WITHOUT Customer consent only where the settlement (a) is solely for money, (b) is…


🛑 **Red line.** Do NOT agree to a fully UNCAPPED IP/third-party indemnity, and do not tie the indemnity to — or let it exceed — the company's actual cyber/E&O/media-liability tower, in ANY deal tier without sign-off.

⬆️ **Escalate when.** Crossing a red line requires sign-off: (a) UNCAPPED IP/third-party indemnity (at ANY tier), any cap above 3x trailing-12-month fees, OR pegging/tying the indemnity to the cyber/E&O/media limit — requires GC + CFO (CFO because it is a…


**Talking points:**

- On the dollar cap: 'A supercap at 2-3x your annual fees is genuinely above-market for this deal size.
- On defense control: 'We keep control of the defense because we are the only party that can fix the root cause across the product — procure a license, re-engineer the feature, or…
- On the remedy ladder being exclusive: 'Procure-modify-or-terminate-and-refund is the industry-standard remedy because it actually solves your problem — it keeps you compliant and…
- On notice-and-prejudice: 'We are agreeing that late notice reduces our obligation only to the extent it actually harms our ability to defend — that is more generous than the…


*Drafting:* "1) Keep the two cap questions in SEPARATE sentences: one carving the indemnity out of the CONSEQUENTIAL-DAMAGES EXCLUSION, a different one stating the DOLLAR cap (supercap).


### 4. Warranties & Disclaimers

**Opening.** On our paper, scope the express warranty as narrowly as the market will bear and disclaim everything else. Draft: "Vendor warrants that, for thirty (30) days following initial provisioning (the 'Warranty Period'), the Service will perform SUBSTANTIALLY in accordance with the then-current Documentation." Sole and exclusive remedy = Vendor will use…


**Fallback ladder:**

1. **Give** Change the performance standard from 'substantially' to 'materially in accordance with the Documentation,' and pin Documentation to the version in… → **Get** Customer accepts the AS-IS / implied-warranty disclaimer in substance (merchantability + fitness disclaimed).
2. **Give** Make the conformity warranty CONTINUOUS for the full subscription term rather than a 30-day window (this is the SaaS market norm — there is no… → **Get** Customer agrees the SLA/service-credit regime is the SOLE remedy for availability/uptime, and the conformity warranty is the sole remedy for…
3. **Give** Add standard bilateral warranties: (a) mutual authority/due-organization; (b) Vendor warrants the Service does not contain malware, time-bombs, or… → **Get** These are bilateral (customer reps the same on authority and on lawful use of the Service), and the compliance-with-law warranty is scoped to…
4. **Give** Concede the 'except as expressly stated in this Agreement' subordination so the AS-IS disclaimer cannot be read to gut the SLA, the security… → **Get** Customer accepts that 'uninterrupted / error-free / secure' stays expressly disclaimed (uptime is the SLA's job, not a warranty) and that the…
5. **Give** Make the sole-remedy clause NON-EXCLUSIVE for breaches of the security warranty, the IP/non-infringement obligations, and confidentiality (those… → **Get** This is the floor and the deal-closer. In exchange: the conformity warranty's exclusive remedy stays re-perform/refund for ordinary functional bugs;


🛑 **Red line.** Do NOT agree to: (1) any open-ended fitness-for-Customer's-particular-purpose warranty, or a warranty that the Service will meet Customer's specific business requirements or regulatory obligations — that converts a product warranty into an uninsurable, fact-specific performance guarantee tied to a customer environment we don't control;

⬆️ **Escalate when.** Escalate when the customer demands any of the following (route as noted; routine, market-standard language below these thresholds should be handled by the deal lead WITHOUT escalation — including accepting a 'to the extent permitted by…


**Talking points:**

- The AS-IS disclaimer of implied warranties is standard, mutually-understood market practice between sophisticated commercial parties — it appears in essentially every enterprise…
- We are not disclaiming our actual promises. The 'except as expressly stated in this Agreement' carve-out means the disclaimer never touches the SLA, the security commitments, the…
- 'Uninterrupted and error-free' is disclaimed because no software meets that strict-liability standard — even Oracle's paper expressly states it does not guarantee programs will be…
- A continuous full-term conformity warranty (not a 30-day window) is genuinely customer-favorable and the correct SaaS construction — in a subscription there's no single 'delivery'…


*Drafting:* ["Keep 'substantially in accordance with the Documentation' on the first draft and only retreat to 'materially' as a traded concession — both are defensible, and starting at 'substantially' gives a free rung to spend.","Always define the…


## II. IP & Data


### 5. IP Ownership & License Grant

**Opening.** On our paper, draft maximally vendor-favorable: (1) Vendor owns and reserves all right, title and interest in the Service, platform, software, models, APIs, documentation, and "all enhancements, modifications, configurations, templates, methodologies, know-how, and derivative works of the Service" — define "Vendor Technology" broadly to include "any…


**Fallback ladder:**

1. **Give** Narrow 'Vendor Technology' so it no longer sweeps in Customer Data or Customer-provided materials; → **Get** Customer accepts that Vendor retains all platform/Service IP including 'all enhancements, modifications, configurations, and derivative works of the…
2. **Give** Concede that Customer owns Output: replace 'Vendor owns Output' with 'As between the parties, Customer owns the Output it generates,' and Vendor… → **Get** (a) Vendor's only obligation as to Output is to deliver it; we give NO warranty of accuracy, non-infringement, or fitness of AI-generated Output, and…
3. **Give** Convert Feedback assignment to a perpetual, irrevocable, royalty-free, sublicensable LICENSE to use Feedback for any purpose (drop the 'hereby… → **Get** Feedback license expressly survives termination and explicitly EXCLUDES Customer Confidential Information and Customer Data from its scope.
4. **Give** For bespoke/custom deliverables built and separately paid for under an SOW, agree Customer owns them via present-tense 'Vendor hereby assigns ... → **Get** (a) A broad, perpetual, irrevocable, worldwide, royalty-free, sublicensable license-BACK to Vendor for any Background IP, tools, libraries, and…
5. **Give** Delete the residuals clause entirely (or narrow it to exclude trade secrets and any Customer Confidential Information). → **Get** Tie the deletion to the confidentiality clause's existing objective-standard / 'unaided memory' mechanics so we're not double-conceding the same…


🛑 **Red line.** Do NOT (a) assign, co-own, or grant exclusivity in the Service, platform, models, or any underlying Vendor Technology; and (b) do NOT agree to a blanket prohibition on using DE-IDENTIFIED, aggregated usage/telemetry data for operating, securing, and abuse-protecting the Service. Reason: platform ownership is the entire enterprise.

⬆️ **Escalate when.** (a) Co-ownership of the platform: a customer's opening redline merely ASKING for joint ownership is routine — the reviewer (Deal Desk + supporting counsel) rejects it at the table; do NOT auto-escalate first asks.


**Talking points:**

- 'Each party keeps what it brought.' We are not asking to own anything of yours — your data and your confidential information are expressly carved out and can never become our IP…
- On custom work you pay for under an SOW, you get it — by present-tense assignment, not a promise to assign later, and title transfers on full payment.
- You own your Output. As between us, the Output you generate is yours; we keep only the license we need to host, process, and display it while running the Service.
- The Feedback term is a license, not a grab of your ideas. We need the freedom to ship roadmap features without a later claim that an improvement traces to something you said — but…


*Drafting:* ["Define 'Vendor Technology' affirmatively AND add an express negative carve-out: 'Notwithstanding anything to the contrary, Customer Data and Customer Confidential Information are not Vendor Technology and shall not constitute Vendor IP.'…


### 6. Confidentiality

**Opening.** Mutual-but-tilted NDA on our paper. Definition: an objective "all non-public information that the receiving party knows or reasonably should understand to be confidential given its nature or the circumstances of disclosure" — NO marking or written-summary requirement (we disclose pricing, architecture, roadmap and security posture orally and in demos…


**Fallback ladder:**

1. **Give** Drop the residuals clause entirely (or, as a first step, narrow it to 'unaided memory, excluding trade secrets and any personally identifiable or… → **Get** Spend this chip to buy ONE core anchor, not several — realistically the customer's acceptance of the objective no-marking definition (the…
2. **Give** Confirm/strengthen the standard of care to fully mutual 'reasonable care' and an express 'no less protective' flow-down covenant making each party… → **Get** Customer drops any push for a heightened/strict standard or a fixed-dollar care metric, and drops any 'our security program must independently…
3. **Give** Add an express carve-out protecting the customer's personal/regulated data 'for as long as it is retained,' overriding the 3-year tail for that… → **Get** Tie it to keeping the general 3-year tail for ordinary business confidential information (don't let them ratchet the whole tail to 5 years on the…
4. **Give** Move the survival tail from term+3 to term+5 years for ordinary confidential information. → **Get** Only in exchange for something of value — e.g., the customer accepting the objective no-marking standard, or withdrawing a demand to put a fixed…
5. **Give** Firm up return-or-destroy: on termination or written request, return or destroy and, if requested, certify destruction in writing. → **Get** Preserve the backup/archival and legal-hold carve-out and an express statement that archived copies remain subject to the confidentiality obligations…


🛑 **Red line.** Do NOT agree to fully uncapped liability for ALL confidentiality breaches (a blanket carve-out of the entire confidentiality section from the dollar cap), and do NOT let an uncapped 'any Security Incident' exception sneak in through the NDA.

⬆️ **Escalate when.** Any customer demand for uncapped liability for confidentiality breaches beyond the trade-secret-misappropriation/willful-breach pair, OR a confidentiality-specific super-cap above 3x fees, requires Deal Desk + GC sign-off (it changes our…


**Talking points:**

- Confidentiality is one of the most symmetric clauses in the agreement — both parties disclose sensitive information, so the right answer is market-standard mutual protection, not…
- The objective 'reasonably understood to be confidential' standard without a marking requirement is the market norm and protects both sides.
- Keeping trade secrets protected indefinitely is the legally correct treatment, not a grab. Under the Defend Trade Secrets Act and the UTSA, information qualifies as a trade secret…
- Term-plus-3-years is the modal market tail for ordinary business confidential information; 5 years is at the customer-favorable end.


*Drafting:* Define Confidential Information with an objective trigger ('knows or reasonably should understand to be confidential given the nature of the information or circumstances of disclosure') and explicitly state 'no marking, legending, or…


### 7. Data Protection, Privacy & Security (DPA)

**Opening.** Put our own form DPA on the table by incorporated URL (our paper, not the customer's, and not as a separately negotiated exhibit). Core openers: (1) Breach notice "without undue delay after [Vendor] confirms a Security Incident affecting Customer Personal Data" — trigger pegged to confirmation by our incident-response function, no fixed hour-clock;


**Fallback ladder:**

1. **Give** Convert breach trigger from 'after Vendor confirms' to 'without undue delay, and in any event within 72 hours, after Vendor becomes aware of a… → **Get** DEFINE 'becomes aware' as confirmation by Vendor's security/incident-response team (not any employee's hunch), and keep 'confirmed' (not 'suspected')…
2. **Give** Tighten the clock to 48 hours from confirmed awareness and add a duty to reasonably assist Customer with its own Art. → **Get** Assistance is at Customer's reasonable expense beyond a defined included threshold (e.g., first 8-10 hours per incident free, then T&M), and Customer…
3. **Give** Keep general subprocessor authorization but add (a) advance notice of new subprocessors via a subscribe-able mechanism (email/RSS), (b) a 30-day… → **Get** Objection right is limited to bona fide data-protection grounds (not commercial preference);
4. **Give** Accept direct, flow-through liability for our subprocessors' acts/omissions as if our own, and replace 'commercially reasonable measures' with a… → **Get** All subprocessor liability flows through the SAME liability cap and carve-out architecture as the rest of the agreement (no separate or stacked…
5. **Give** Grant a report-first audit right (current SOC 2 Type II / ISO 27001 plus a reasonable annual security questionnaire), with an on-site/third-party… → **Get** On-site audits: no more than once per 12 months absent a qualifying cause event, on 30 days' notice, during business hours, under NDA, by a mutually…


🛑 **Red line.** Do NOT agree to: (a) uncapped liability for any privacy/security losses, or a data-breach super-cap exceeding ~3x trailing-12-month fees, or a super-cap with no connection to our cyber-insurance tower (insurance should anchor the figure as a floor;

⬆️ **Escalate when.** Escalate to the CISO + GC jointly for: any breach-notice clock BELOW 48 hours (48h itself is pre-approved as the floor — do NOT escalate at 48h), any "suspected"-incident trigger or any awareness trigger not anchored to the IR team, OR any…


**Talking points:**

- GDPR sets the equilibrium in our favor: Article 33(1) gives the CONTROLLER (you) the obligation to notify your supervisory authority within 72 hours, while Article 33(2) requires…
- A trigger keyed to a CONFIRMED incident, with 'awareness' defined as confirmation by our incident-response team, protects you as much as us: premature notice on every…
- Article 28(2) GDPR expressly contemplates 'general written authorization' for subprocessors coupled with a right to object — that IS the statutory model, not a vendor-friendly…
- We accept DIRECT, flow-through liability for our subprocessors as if their acts were our own — so you get a single accountable counterparty and never have to chase a downstream…


*Drafting:* Define 'Security Incident' as a CONFIRMED unauthorized access to, or disclosure of, Customer Personal Data, and expressly exclude unsuccessful attempts, pings/scans, and routine events that do not compromise data security — this keeps the…


## III. Commercial Terms


### 8. Payment Terms & Late Fees

**Opening.** Put on our paper: all fees invoiced annually in advance, due Net 30 from invoice date; all fees non-cancelable, nonrefundable, and payable "without any deduction, withholding, set-off, or counterclaim." Late amounts accrue interest automatically (no notice required) at the lesser of 1.5% per month (18% p.a.) or the maximum rate permitted by applicable law.


**Fallback ladder:**

1. **Give** Move the interest clock so it runs from receipt of a conforming invoice (correct PO, entity, line items) rather than invoice date; → **Get** Customer commits to a fixed validated-invoice/PO process and a hard deadline to dispute invoice FORM, i.e., facial defects in the invoice itself such…
2. **Give** Add a good-faith dispute carve-out: interest and suspension do not apply to amounts the customer disputes in good faith with reasonable written… → **Get** Carve-out is tightly bounded: (a) undisputed portion of every invoice paid in full on time regardless of any dispute;
3. **Give** Soften suspension: written past-due notice plus a 10–15 day cure period before any suspension; suspension limited to undisputed, post-cure amounts; → **Get** Once suspension is permitted (post-notice, post-cure, undisputed), the right is unconditional and reinstatement fees apply;
4. **Give** Extend net period to Net 45 (Net 60 only for large or regulated/government buyers with documented AP cycles). → **Get** Tie the longer terms to either annual-in-advance billing being retained, or a multi-year commitment / prepay discount;
5. **Give** Retain no-set-off as the default, but permit the customer to apply earned, finalized SLA service credits against the next invoice. → **Get** Set-off is limited to SLA credits actually accrued and finalized under the SLA's own claim mechanics — not unliquidated damages, indemnity claims, or…


🛑 **Red line.** Do not accept (a) a customer right to withhold or set off the ENTIRE invoice — or to net unliquidated/indemnity/breach/damages claims against fees — which converts our receivable into a self-help bargaining chip and is fatal to receivables-based financing and clean revenue recognition;

⬆️ **Escalate when.** Net terms beyond Net 60, or monthly/quarterly billing in arrears replacing annual-in-advance → CFO / VP Finance (revrec and cash-flow impact).


**Talking points:**

- Annual-in-advance, non-cancelable, nonrefundable, no-set-off is a well-established SaaS posture, not an outlier — major enterprise vendors' order documents recite that the fee is…
- Our 1.5%/month late charge is expressly the lesser of that rate 'or the maximum rate permitted by applicable law' — so by its own terms it can never be usurious;
- The good-faith dispute carve-out protects you on the thing that actually goes wrong — a billing error: you never owe interest or face suspension on an amount you contest in…
- No-set-off protects the integrity of the subscription, not just us — it keeps a single contested support ticket or a downstream claim from being used to starve the service of the…


*Drafting:* Always pair any stated late-fee percentage with "or the maximum rate permitted by applicable law, whichever is less" — it makes the number self-curing against usury/penalty challenges and avoids a court voiding the whole clause.


### 9. Price / Fee Escalation at Renewal

**Opening.** On our paper, each renewal term's fees increase by "the greater of seven percent (7%) or the increase in CPI over the prior twelve (12) months," applied to our then-current list rates (NOT the discounted rate the customer pays in the initial term), compounding year over year, with CPI generic and uncapped on the high side.


**Fallback ladder:**

1. **Give** Flip 'greater of 7% or CPI' to a fixed 6% annual cap and drop the CPI floor entirely (no index tracking, no 'whichever is greater'). → **Get** Customer accepts our then-current LIST rate as the escalation base AND a 3-year initial term.
2. **Give** Lower the fixed cap to 5% per year, expressly a hard ceiling. → **Get** 3-year minimum commitment AND the escalator stays calculated off then-current/list rather than the discounted rate.
3. **Give** Re-base the escalator to the customer's actual discounted/net rate paid in the prior term (kill the silent list-rate reset), keep the 5% cap. → **Get** Removal of any benchmarking/MFN ask AND confirmation the 60-day auto-renewal mechanic stays intact.
4. **Give** Convert to 'lesser of CPI or 5%' (so a low-inflation year costs the customer less than 5%), pin CPI to the named BLS series CPI-U, All Items, U.S. → **Get** First renewal term increase is reciprocally capped/locked AND the customer pre-commits to the first renewal term (waives convenience non-renewal for…
5. **Give** Year-1 of the FIRST renewal term only is flat (0% uplift), then 'lesser of CPI or 4-5%' thereafter, with overage/added units priced at the contracted… → **Get** Longer total commitment (4-5 years) AND expansion/upsell rights OR a named case study/reference. The flat first year is the classic closer;


🛑 **Red line.** Do NOT agree to: (a) a hard freeze of fees for the entire term and all renewals — no escalator at all; (b) a cap CEILING below 3% off the discounted base for anything other than our largest strategic accounts with CFO sign-off (a CPI-linked result that lands below 3% in a low-inflation year is acceptable because it is bounded by a known…

⬆️ **Escalate when.** Deal desk can approve, WITHOUT escalation, anything down to and including rung 4: a fixed hard cap of 5% or lower-but-not-below-5%, the discounted/net rate base (re-basing off list is market-standard — do not escalate it), 'lesser of CPI…


**Talking points:**

- A 3-5% annual escalator, pegged to CPI or a fixed percentage, is the documented enterprise-software norm — not an aggressive ask.
- With CPI running near 3% in 2026, a fixed 5% cap with NO CPI floor protects YOU: it caps your exposure in a catastrophic inflation year, which an uncapped or pure-CPI clause would…
- We pin the escalator to a named, verifiable index — CPI-U, All Items, U.S. City Average, with a successor-index clause if the BLS discontinues it.
- The escalator only offsets our own rising input costs over a multi-year term — hosting, third-party licenses, security and compliance investment, and engineering comp all rise…


*Drafting:* ["State the escalation base as 'Customer's then-current Fees as set forth in the applicable Order Form' ONLY after you have conceded the discounted-rate base;


### 10. Most Favored Customer / Pricing-Parity & Benchmarking

**Opening.** Open with SILENCE: put no MFN, parity, or benchmarking clause on our paper. Our standard Order Form/MSA states the negotiated fees and the renewal-escalation cap (Clause 9) and says nothing about what other customers pay. If the customer raises parity, do not draft toward it — redirect first: \"We don't grant MFNs.


**Fallback ladder:**

1. **Give** Drop the MFN/parity request entirely and instead grant a hard renewal-escalation cap (lesser of CPI and 3-5%, off the customer's discounted rate per… → **Get** Customer withdraws the MFN/parity ask completely and accepts that capped, pre-locked pricing IS their price-protection mechanism — trade a bounded…
2. **Give** Add a multi-year price lock with a small extra discount (e.g., 2-3 points) in exchange for a longer commitment (3 yr vs. → **Get** Longer term + prepay (cash and retention), and the parity conversation is closed because the customer now has contractually fixed pricing for the…
3. **Give** Concede the narrow price-only LIST-price MFN from the opening draft (stacked comparator, certificate-only, prospective credit, broad carve-outs… → **Get** Customer accepts that 'price' means published list price, accepts the full carve-out list, and accepts a vendor certificate in lieu of audit.
4. **Give** Tighten 'price' from list to NET/effective price. This is a real economic concession — flag it as such to the customer and extract for it. → **Get** In exchange, lock a true 'identical material terms' comparator (identical SKU, same committed volume/tier band, same term length, same region) and a…
5. **Give** Add a conditional, narrow audit right on top of the certificate. → **Get** Audit is by an independent third-party auditor (not the customer or its counsel), once per 12 months, on reasonable notice, at the CUSTOMER's expense…


🛑 **Red line.** Never agree to ANY of the following — these are walk / hard-escalate, not negotiable drafting points: (1) parity measured against NET/effective price WITHOUT the full carve-outs for promo/pilot/channel/bundle/co-sell/design-partner/strategic deals — that turns a single negotiated discount anywhere in the book into a book-wide ratchet and…

⬆️ **Escalate when.** VP Sales (deal desk) may sign off UNILATERALLY only on rungs 1-2 (renewal cap, price lock, extra discount, prepay terms) — pure pricing mechanics with NO MFN language.


**Talking points:**

- What you actually need is protection from price drift over time. A hard renewal cap plus locked multi-year pricing gives you that as a known, bankable number — whereas an MFN…
- An MFN backed by our officer's certificate is fully enforceable — a false certificate is a breach with fraud exposure.
- Net-price comparisons are only meaningful between deals with identical material terms — same SKU, volume, term length, region, and timing — because net price bakes in all of…
- We discount aggressively for pilots, references, multi-year prepay, and channel/co-sell deals.


*Drafting:* Define 'price' as 'the published list price for the identical Product SKU' and resist any drift to 'net price,' 'effective price,' 'total cost,' or 'economic value' — the comparator definition is the single most outcome-determinative term…


## IV. Term & Exit


### 11. Term & Auto-Renewal (Evergreen)

**Opening.** On our paper, lead with a multi-year initial term (36 months preferred, 24 acceptable) that auto-renews for successive renewal terms unless either party gives written notice of non-renewal at least 60 days before the end of the then-current term. Open with equal-length renewals (another 36/24 months);


**Fallback ladder:**

1. **Give** Drop equal-length renewals to successive 1-year renewals (keep the multi-year initial term, the 60-day window, the auto-renew default, and… → **Get** Hold the multi-year initial term firm and keep auto-renew as the default (opt-out, not opt-in).
2. **Give** Cap the renewal uplift — open at CPI + 3%, settle at the greater of 5% or trailing-12-month CPI (CPI-U, a named published index), replacing… → **Get** Tie the cap to the 1-year renewal cadence. Protect against down-sell by anchoring the cap to per-unit/list price (so the cap on rate survives even if…
3. **Give** Add an affirmative renewal-reminder duty: we email the billing/notice contact 30-90 days before the non-renewal deadline. → **Get** In exchange, keep the auto-renewal mechanism itself intact and explicitly agree that the reminder is a notice courtesy, not a condition of renewal…
4. **Give** Tighten the non-renewal notice window from 60 to 30-45 days (this favors the customer — less runway committed to the next term) and make it mutual… → **Get** Concede only down to 30 days (60 is modal; 30 is the floor we'll reach). Keep notice mutual so the symmetry argument neutralizes the 'adhesion'…
5. **Give** Where the customer signs multiple Order Forms, agree to co-terminate all active Order Forms to the master subscription end date. → **Get** Co-termination is a retention win for us (everything renews together, one larger renewal event) and we frame it as admin simplicity for them — trade…


🛑 **Red line.** Do not agree to (a) convert auto-renewal to affirmative opt-in / opt-in re-signature ('renewal requires the customer's affirmative written election'); (b) a customer termination-for-convenience right during the initial term or any in-progress renewal term;

⬆️ **Escalate when.** Escalate before agreeing to any of: (1) Opt-in / affirmative-renewal in place of auto-renewal, OR a customer termination-for-convenience right inside the initial term or a renewal term -> VP Sales + GC jointly (touches…


**Talking points:**

- The multi-year commitment is what funds your discount. The rate on your Order Form is priced against the committed term and the renewal default;
- You are protected against the thing you actually care about — silent lock-in — by the renewal reminder plus the non-renewal window.
- The uplift cap is the real protection against price drift, and we are giving it to you: the greater of 5% or trailing-12-month CPI, tied to a named published index.
- Notice is mutual and by email — the obligation runs both ways, so this is a symmetric administrative window, not a one-sided lock-in.


*Drafting:* Define 'then-current pricing' and the uplift cap in the SAME sentence so a later reader can't read the cap as overriding nothing, and word the cap as 'the lesser of [vendor's then-current list increase] and the greater of 5% or the…


### 12. Termination

**Opening.** Put an asymmetric termination scheme on our paper. (1) NO customer termination for convenience mid-term — the subscription term is fixed and the committed fees are an unconditional, non-cancelable payment obligation. (2) Termination for cause only on a material breach uncured after 30 days' written notice, mutual on its face.


**Fallback ladder:**

1. **Give** Make the for-cause cure right explicitly mutual and symmetrical: either party may terminate on 30 days' uncured material breach. → **Get** Customer drops its push for a standalone convenience right. Symmetry is cheap — we rarely breach — and framing the trade as 'you already have a…
2. **Give** Soften non-payment to a 10-day cure WITH written notice (drop 'immediate' termination) and limit suspension to the affected Order Form, with 5… → **Get** Customer accepts that good-faith disputed amounts must be (a) limited to the specific line item disputed, (b) accompanied by timely payment of the…
3. **Give** Add concrete trigger-based customer termination rights: (a) chronic SLA failure (e.g., below the committed uptime in 3 consecutive months or any 3 in… → **Get** These are tied to OUR failure or OUR election, cost nothing if we perform, and let us hold the line on no free-form convenience exit.
4. **Give** Replace proprietary export with export in a non-proprietary, machine-readable format (CSV/JSON or documented API) within a defined window (30 days… → **Get** Customer accepts (a) export is of Customer Data only, not our configurations, models, derived/aggregated analytics, or usage data;
5. **Give** Offer transition assistance beyond raw export at a rate card FIXED AT SIGNING (not 'then-current'), capped at a defined number of hours/days, for a… → **Get** Customer agrees transition services are (a) scoped in a mutually agreed statement of work, (b) contingent on the customer being current on all…


🛑 **Red line.** Do NOT grant a customer termination for convenience that refunds or relieves prepaid/committed fees mid-term, and do NOT relieve a customer of committed/accrued fees on a customer-cause termination (customer breach).

⬆️ **Escalate when.** Any customer termination-for-convenience right that waives the early-termination fee or refunds/relieves prepaid/committed fees mid-term requires VP Sales + CFO sign-off (it directly impairs recognized/committed ARR).


**Talking points:**

- You have a complete exit on our failure: 30-day cure on material breach, plus express triggers for chronic SLA misses, uncured security breaches, and discontinuation.
- The committed term is the consideration for the rate. Our list-to-contract discount and the fixed price are funded by the certainty of the term;
- On data lock-in, we'll commit in writing to export your data in a non-proprietary, machine-readable format with a deletion certificate.
- Fixing the transition rate card at signing protects you, not us — you lock in today's rates instead of paying 'then-current' rates years from now when you have the least leverage.


*Drafting:* ["Define the term in the Order Form and make committed fees an 'unconditional and non-cancelable payment obligation' there, not just in the MSA — Order Form precedence then carries it even if the MSA termination clause is softened in…


### 13. Service Levels (SLA) & Uptime Credits

**Opening.** Put the SLA on a vendor-hosted URL incorporated by reference and amendable by us. Commit to a single blended **99.9% monthly uptime** target (≈43 min/month allowance), measured per calendar month with a hard monthly reset (no carry-over, no rolling window).


**Fallback ladder:**

1. **Give** Lock the SLA to the version attached as an Exhibit / incorporated as of the Effective Order Date; → **Get** Customer drops the demand to raise the 99.9% number itself and accepts that 99.9% blended is the committed figure.
2. **Give** Administrative goodwill: convert credit claims to vendor-issued **automatic** credits once we detect/confirm a miss, OR extend the claim window to… → **Get** Customer keeps monthly-reset measurement (no rolling/quarterly window), accepts our monitoring/records as the basis of record, and the aggregate…
3. **Give** Raise the headline worst-band credit in two steps — first to **50%**, then if pressed to **100%**, of the affected month's fee for the worst outage… → **Get** Aggregate dollar ceiling stays at **one month's** fees and never higher; credits remain **sole-and-exclusive** for availability;
4. **Give** Add **service tiering** instead of a higher blended number — core/production API at **99.95%**, secondary/batch components at **99.5%** — and add… → **Get** Customer treats tiering as the substitute for pushing the overall % to 99.99%, and accepts that support-response SLOs carry **no separate financial…
5. **Give** Cap and pre-schedule maintenance: scheduled maintenance limited to a defined off-peak window with advance notice (e.g., ≤8 hrs/month, ≥48 hrs… → **Get** Emergency maintenance and customer/third-party/force-majeure causes remain excluded from the calculation;


🛑 **Red line.** Do NOT (a) let an SLA breach trigger a **general breach or termination of the entire Agreement**, or open the door to **uncapped or consequential damages** (lost profits, cover costs) for downtime;

⬆️ **Escalate when.** **GC sign-off** required to: make an SLA breach a termination/breach trigger for the whole Agreement; remove the sole-and-exclusive-remedy designation; allow availability damages outside credits;


**Talking points:**

- 99.9% monthly availability is a defensible market-standard floor for single-region, multi-tenant SaaS — a large share of enterprise SaaS commits at 99.9%, with 99.95% common for…
- Service credits are a meaningful, contractually certain remedy that aligns our interests with yours — we lose money the moment we underperform.
- The sole-and-exclusive-remedy structure is what lets us offer competitive, predictable pricing: availability risk is priced into the subscription on the assumption it is bounded…
- We give you a real exit, not just credits: if we chronically miss the committed level, you can terminate the affected service after notice and a cure period and recover your…


*Drafting:* ["Put the sole-and-exclusive-remedy sentence inside the SLA AND add an express carve-out in the general 'remedies are cumulative' clause: '...except that Service Credits are the Customer's sole and exclusive remedy for any failure to meet…


## V. Operational / Boilerplate


### 14. Insurance †

**Opening.** Put a short, "customary"-style clause on our paper: "Each party shall maintain, at its own expense, commercially reasonable insurance customary for its business, including Commercial General Liability of $1M per occurrence / $2M aggregate, and Technology Errors & Omissions / Cyber liability on a combined/blended limit of $1–2M.


**Fallback ladder:**

1. **Give** Unblend into a standalone insurance schedule with named lines and modestly raised limits: CGL $1M/$2M, Tech E&O $2M, Cyber $3M, A-/A.M. → **Get** Customer confirms insurance stays expressly DECOUPLED from the liability cap (no 'insurance does not limit liability,' no cyber-floors-the-super-cap…
2. **Give** Raise Cyber to a $5M floor (and to $5–10M if Customer is in a regulated vertical — healthcare/PHI, financial, payment-card) and add a… → **Get** Drop additional-insured on the claims-made Cyber/E&O forms entirely (AIs erode the shared limit and most carriers won't endorse them cleanly), and…
3. **Give** Customer named as Additional Insured on the CGL line only, via standard ISO endorsement (CG 20 10 / CG 20 37), plus primary-and-non-contributory (CG… → **Get** AI/primary-noncontributory/waiver is strictly limited to CGL — never E&O or Cyber. We provide the actual endorsement, not a redrafted bespoke one.
4. **Give** We contractually owe 30-day advance written notice of cancellation or material reduction (10 days for non-payment), and provide COI evidencing the… → **Get** Notice obligation is 'to the extent we receive it from our carrier / commercially reasonable efforts' framing is replaced only for the notice timing…
5. **Give** Accept a narrow, mutual 'insurance is in addition to and does not limit either party's liability or obligations' acknowledgment, AND a Self-Insured… → **Get** This acknowledgment stays severed from the liability cap and the indemnity — it confirms coverage exists alongside the cap, it does NOT raise or…


🛑 **Red line.** Do NOT agree to any of the following: (1) Additional-insured status on the claims-made Cyber or Tech E&O policies — carriers generally won't endorse it cleanly, it dilutes a shared aggregate limit across customers, and it can void our own coverage; this is an insurability limit, not a negotiating posture.

⬆️ **Escalate when.** Escalate before agreeing when the customer asks for: (a) any AI/primary-noncontributory/waiver-of-subrogation on the Cyber or E&O lines, OR cyber limits above $5M (or above $10M for regulated verticals) — CISO/Risk + CFO sign-off, because…


**Talking points:**

- Our limits are minimums and floors, not a cap on available coverage or a representation of our total tower — you get the benefit of whatever coverage actually responds.
- Additional-insured status on a claims-made Cyber or E&O policy is a coverage problem for both of us: it draws down a shared aggregate limit across our whole customer base, so a…
- Insurance and the liability cap do different jobs: insurance funds the indemnities and the data-breach exposure; the cap allocates residual risk.
- Cancellation notice: we'll commit to 30 days' advance written notice and to maintaining comparable replacement coverage if a policy changes — that's the enforceable promise.


*Drafting:* ["State limits as 'minimum limits' that 'shall not be construed as a limitation on, or representation of, the limits of [Vendor]'s liability or available coverage' — and add 'satisfaction of this Section constitutes full performance of…


### 15. Assignment & Change of Control

**Opening.** Open on our paper with an asymmetric clause, presented as standard boilerplate so it reads administrative, not as a grab: "Customer may not assign, delegate, or transfer this Agreement or any right or obligation hereunder, in whole or in part, whether voluntarily, by operation of law, or otherwise (including by merger, consolidation, sale of all or…


**Fallback ladder:**

1. **Give** Confirm our consent standard over the customer's assignment is 'not to be unreasonably withheld, conditioned, or delayed,' and add a… → **Get** Keep the clause one-way at this rung (we still assign freely on notice; CoC remains a deemed-assignment trigger against the customer only).
2. **Give** Carve out the customer's true ordinary-course events from the consent requirement: assignment to an affiliate, or to a successor in a merger or sale… → **Get** Tie any such customer transfer to three conditions: (1) assignee assumes all obligations in writing as a condition precedent to effectiveness, (2)…
3. **Give** Drop the standalone change-of-control deemed-assignment trigger against the customer for non-competitor acquirers (so the customer simply getting… → **Get** In exchange, add a reciprocal protective right: if [Vendor] is acquired by or undergoes a change of control to a direct competitor of Customer…
4. **Give** Accept reciprocal continuing liability, or — if the customer pushes hard — a release of the assigning party upon the assignee's written assumption… → **Get** Use the release as the chip to lock the competitor-exclusion and written-assumption-as-condition-precedent, and to keep our own notice-only…
5. **Give** On the customer's insistence, narrow or delete the anti-assignment override as applied to accounts receivable / payment rights, so the clause does… → **Get** Concede this gracefully because the restriction is largely unenforceable anyway — UCC 9-406 and 9-408 make contractual bans on assigning receivables…


🛑 **Red line.** Two genuine walk/hard-escalate lines: (1) We will NOT permit the customer to make a VOLUNTARY DIRECT assignment of this Agreement to a direct competitor of [Vendor] without our consent, with full release and no written-assumption condition;

⬆️ **Escalate when.** Escalate to the GC (VP Sales informed) before agreeing to: (a) any customer right to make a VOLUNTARY DIRECT assignment to a [Vendor] competitor without our consent;


**Talking points:**

- Mutual M&A and affiliate assignment carve-outs are one of the most standardized provisions in B2B SaaS — neither of us wants to be permanently locked to a counterparty we didn't…
- 'Not to be unreasonably withheld, conditioned, or delayed' is a real, enforceable check — courts read a genuine reasonableness obligation into it, so it's not a renegotiation…
- We're not blocking your ability to be acquired. If you're bought by a non-competitor, that's notice-only — no consent, no breach.
- The written-assumption requirement protects you as much as us: it guarantees whoever ends up holding this contract is actually bound to perform and stands behind the obligations —…


*Drafting:* Keep our own assignment sentence SEPARATE from the customer's restriction, and phrase ours as a right we 'may' exercise 'including without limitation' to affiliates, acquirers, successors, and lenders/financing parties — explicitly…


### 16. Governing Law, Venue & Dispute Resolution

**Opening.** On our paper: "This Agreement, and all disputes arising out of or relating to it, shall be governed by the substantive laws of the State of [Vendor home state], without regard to conflict-of-laws rules and excluding the UN Convention on Contracts for the International Sale of Goods.


**Fallback ladder:**

1. **Give** If we open with 'and procedural' (or the customer raises it): drop it. Clause governs by Vendor home-state SUBSTANTIVE law only, conflicts rules… → **Get** Near-free concession — a court applies its own procedural rules (lex fori) regardless, so 'procedural' adds almost nothing and is the first thing…
2. **Give** Move governing law to a neutral jurisdiction — Delaware or New York substantive law. → **Get** Only in exchange for venue staying neutral and tied to that same state, AND the customer dropping its push for its own home court.
3. **Give** Make the jury waiver and the IP/equitable-relief carve-out expressly mutual and bilateral. → **Get** Customer agrees the mutual jury waiver survives termination and the carve-out stays bilateral but unchanged in substance (either party may run to…
4. **Give** Replace single-step litigation with a multi-tier escalation: 30-day good-faith executive negotiation, then non-binding mediation, before either party… → **Get** Customer accepts that the escalation clock does NOT toll any applicable statute of limitations or contractual limitation period (cross-ref Clause 17)…
5. **Give** For enterprise deals, strike mandatory arbitration and keep the dispute in court (litigation). → **Get** Customer keeps the exclusive jurisdiction + venue in our neutral DE/NY forum, and the mutual jury waiver and class/collective/representative-action…


🛑 **Red line.** Do NOT agree to the customer's own home-state law AND home-state exclusive venue COMBINED where that state is hostile to our standard risk terms — i.e., a forum that voids or narrows contractual liability caps, mutual jury waivers, or contractual shortening of the limitations period (e.g., California's non-enforcement of pre-dispute jury…

⬆️ **Escalate when.** GC sign-off required for: (1) accepting the customer's home-state law where that jurisdiction is on our 'hostile forum' list (CA waiver/consumer issues, LA limitations bar, or any state that won't enforce our LoL cap or mutual jury waiver)…


**Talking points:**

- Neutral ground cuts both ways: 'Neither of us wants to litigate in the other's backyard. Delaware and New York are the two most commercially sophisticated benches in the country —…
- On dropping 'and procedural': 'You're right to push on this — we'll govern by substantive law only.
- On the mutual jury waiver: 'It's mutual and it benefits both sides. Commercial disputes turn on documents and expert testimony, not jury sympathy — a bench trial before a judge…
- On multi-tier escalation: 'A 30-day executive window plus mediation before anyone files costs nothing and resolves the large majority of disputes faster and cheaper than a…


*Drafting:* See the structured drafting_tips field above.


### 17. Contractual Limitation Period for Claims †

**Opening.** On our paper, put down a 1-year contractual limitation period (drop to 6 months only on self-service / clickwrap, where no human negotiates): "No action, regardless of form, arising out of or relating to this Agreement may be brought by Customer more than one (1) year after the cause of action accrued." Anchor the clock to ACCRUAL (the breach/event), not…


**Fallback ladder:**

1. **Give** Make the period genuinely mutual (applies to both parties' claims, not just the customer's), keeping 1 year and the accrual trigger. → **Get** Customer drops the demand to lengthen the period or move to discovery; mutuality costs us little because we sue almost exclusively for fees, which we…
2. **Give** Keep 1 year + accrual, but carve OUT our fee/payment-collection claims so the bar never runs against our own collections. → **Get** Frame the carve-out as 'reciprocal' by also excluding the customer's payment-dispute and refund claims;
3. **Give** Move the trigger from pure accrual to a HYBRID: the clock starts on accrual but tolls until the customer 'knew or reasonably should have known' of… → **Get** In exchange, hold the headline period at 1 year from that discovery point and get the customer to accept the 2-year outside backstop so we still have…
4. **Give** Concede the standard carve-outs the customer's counsel always wins: IP indemnity, fraud/willful misconduct, breach of confidentiality / data-security… → **Get** In return, the limitation period stays at 1 year (discovery-triggered, 2-year longstop) for the bulk of ordinary contract/warranty/service claims —…
5. **Give** Stretch the headline period to 2 years (still discovery-triggered, carve-outs in place) and add 'expiration of a survival period does not shorten… → **Get** Get the customer to keep an EXPRESS contractual limitation period at all (a clean number we can plead) rather than reverting to the open statute, and…


🛑 **Red line.** Do not agree to language that effectively gives us UNLIMITED time exposure on core service/warranty claims with no finite outside backstop AND no liability cap interaction — e.g., a pure discovery trigger with no longstop, applied to all claims, combined with "this period shall not be shorter than any applicable statute." That recreates…

⬆️ **Escalate when.** Sub-floor or void-risk terms (shortening below UCC 2-725's one-year goods floor, any shortening under Louisiana or other anti-shortening governing law, or barring non-waivable statutory claims) require GC sign-off — these are…


**Talking points:**

- A clearly-worded, reasonable contractual shortening is routinely enforced — New York CPLR 201 permits parties to agree to a shorter period (Kassner v.
- A finite limitation period benefits BOTH parties: it lets each side close its books, release reserves, and avoid stale-evidence disputes years after the facts.
- This is a SaaS subscription, not a perpetual-defect product. You are continuously monitoring the service month to month;
- We are not trying to time-bar the things that actually matter to you: IP indemnity, fraud, confidentiality and data-security breaches, and indemnification all sit OUTSIDE the…


*Drafting:* ["Anchor to 'accrual' in the first draft, not 'discovery' — accrual silently starts (and can expire) the clock before the customer knows of the claim.


### 18. Force Majeure †

**Opening.** On our paper: a clause that reads mutual but is engineered to favor us as the performing party. (1) Excused-performance trigger covering any event "beyond the affected party's reasonable control," followed by a broad enumerated list (acts of God, war/terrorism, civil unrest, fire/flood/earthquake/severe weather, epidemic/pandemic and government…


**Fallback ladder:**

1. **Give** Confirm the clause is genuinely mutual (symmetric trigger and relief for both parties). → **Get** Free concession — costs us nothing because the customer's only real performance obligation is to pay, and we hold the line that payment is never…
2. **Give** Narrow the catch-all from open-ended to ejusdem generis: 'any other cause of a similar kind beyond the affected party's reasonable control' and drop… → **Get** Customer keeps the full enumerated list intact — including the load-bearing named events (pandemic/government order, and especially…
3. **Give** Add firm mitigation: 'use commercially reasonable efforts to mitigate, work around, and resume performance' plus notice 'as soon as reasonably… → **Get** We keep the cloud/third-party-supplier event in the list and keep DR optional at this rung.
4. **Give** Reframe payment: customer concedes that payment is NOT legally excused, but for prospective SaaS subscription fees covering a service we are not… → **Get** We preserve the US baseline that FM never discharges the debt (protects already-earned fees, one-time/implementation fees, and committed minimums)…
5. **Give** Carve disaster recovery / business continuity OUT of FM relief: an event we are contractually or per our SOC 2 / published DR commitments required to… → **Get** Only offer this once the customer pushes hard on cloud-dependency risk. We get to keep true catastrophic / wide-area events (war, genuine…


🛑 **Red line.** Two positions we do not cross. (1) FM must NEVER excuse, suspend, or cap (a) the confidentiality/data-security obligations, (b) the data-breach notification and incident-response duties, or (c) the indemnification obligations of either party — a vendor that can stop protecting customer data because 'a pandemic happened' is uninsurable…

⬆️ **Escalate when.** Escalate before agreeing to any of: (1) cash refund/clawback of EARNED or prepaid one-time fees, or any FM relief that touches the payment-not-excused baseline beyond a prospective service credit — CFO sign-off.


**Talking points:**

- 'No excuse for payment' is simply the US baseline, not a vendor power grab — under UCC and common law a force majeure event does not discharge a buyer's payment obligation;
- Real executed agreements carve payment out of FM relief expressly — e.g., language that relieves a party of its obligations during a force majeure event 'other than a failure to…
- Mutuality cuts both ways and protects you: if your data center or staff are hit by the same hurricane or outage, the symmetric clause relieves you too.
- On cloud/third-party failure: we run on the same hyperscale infrastructure (AWS/Azure/GCP) you would use directly.


*Drafting:* ["Make it mutual on its face but asymmetric in effect: the only obligation the clause excuses for the customer is timely cooperation;


### 19. Audit / Compliance-Verification Rights

**Opening.** On vendor paper, lead with two parallel regimes and make the SaaS-metering regime the real workhorse. (1) On-prem/licensed software: Vendor may audit Customer's deployment and usage records on 10 business days' notice, during business hours, up to once per 12 months and additionally any time Vendor reasonably suspects non-compliance.


**Fallback ladder:**

1. **Give** Drop self-help audit by Vendor's own staff; agree the audit will be conducted by an independent third-party auditor (not a competitor, not… → **Get** Hold once-per-12-months + for-cause cadence and the undiscounted list-price true-up (for-the-tier);
2. **Give** Cap routine cadence at once per 12 months with a narrow, documented for-cause exception, and limit the lookback/records scope to the most recent 24… → **Get** Preserve the right to invoice discovered overage on the documented audit findings, subject only to a short good-faith dispute notice (not a full…
3. **Give** Move the true-up rate off undiscounted list to Customer's contract / then-current renewal rate for the deficient units (applied at the applicable… → **Get** Hold the cost-shift threshold at 5% of fees properly due for the period (Customer pays Vendor's reasonable audit costs above that), and keep accrued…
4. **Give** Subordinate the copyright-infringement / breach escalation to cure-first: no termination or infringement claim if Customer trues up and pays within… → **Get** Preserve all copyright remedies expressly for willful, knowing, or repeated overuse and for failure to remit the true-up amount within the cure…
5. **Give** Make the audit/verification right mutual in form (Customer may verify Vendor's fee accuracy and SLA credits via the same independent-auditor… → **Get** Lock each party to bear its own audit costs (subject only to the 5–10% under-licensing cost-shift), keep Vendor's metering/billing systems…


🛑 **Red line.** Do not agree to: (a) true-up at the discounted/contract rate with NO cost-shift AND no ability to recover undiscounted value for willful, knowing, or repeated overuse — conceding contract-rate true-up generally is fine (rung 3), but stripping BOTH the cost-shift and the undiscounted backstop for bad-faith overuse turns the audit into a…

⬆️ **Escalate when.** CISO sign-off (with GC) required for ANY customer-directed or customer-conducted audit, inspection, or penetration testing of Vendor's production/multi-tenant systems or source code, or any security commitment beyond the standard SOC 2…


**Talking points:**

- The conduct terms cost a compliant customer nothing: an independent third-party auditor under NDA, 30 days' notice, business hours, once a year, 24-month lookback…
- Excluding regulated data, other customers' data, source code, and privileged material from audit scope protects the CUSTOMER as much as us — we are not asking to see, and they…
- The cost-shift is self-correcting and proportionate: it is keyed to under-licensing of more than 5% of fees properly due for the period, so a compliant customer never trips it and…
- Metered SaaS overage billed at the contract rate is the least intrusive verification regime that exists — no on-site visit, no auditor, just the customer paying the agreed…


*Drafting:* ["Define the audit-cost cost-shift as triggered by 'under-licensing of more than five percent (5%) of fees properly due for the audited period' — basing it on a percentage of fees (not a flat dollar amount) keeps the trigger scaling with…


### 20. Publicity & Use of Name/Logo †

**Opening.** On our paper, lead with a broad, royalty-free, perpetual, self-executing grant: "Customer grants Vendor a non-exclusive, worldwide, royalty-free license to use Customer's name, logo, and trademarks (a) to identify Customer as a customer in Vendor's customer lists, website, investor and sales materials, and (b) to develop and publish a case study, quote, and…


**Fallback ladder:**

1. **Give** Split the grant into two channels and drop the request for any marketing credit / mandatory reference quota — keep the bare logo + customer-list… → **Get** Customer accepts the logo/list right survives as long as Customer remains a paying customer, with no per-instance approval for that channel.
2. **Give** Subject even the bare logo/list use to Customer's brand guidelines and a 'no implied endorsement / no disparagement' statement, and add that we'll… → **Get** Customer keeps the logo right standing (not per-instance-consent) and agrees the cease obligation is prospective only — we are not required to…
3. **Give** Move PR / case studies / attributed quotes to per-instance prior written consent, 'not to be unreasonably withheld, conditioned, or delayed,' and… → **Get** A defined response window — Customer responds within 10 business days; pair the consent standard with an escalation-on-silence path (a written…
4. **Give** Drop true 'deemed approval' on silence; replace with: if Customer does not respond within 10 business days, the request escalates to a named Customer… → **Get** Tighten the window to 5-7 business days for pre-approved formats (logo on a slide, a one-line list entry) and reserve the 10-day track for net-new…
5. **Give** Recharacterize the whole thing as a revocable trademark license — Customer may revoke prospectively on notice; → **Get** Carve out from both the revocation and the removal obligation: (i) materials already distributed or printed;


🛑 **Red line.** Do not agree to (a) retroactive recall/destruction of already-distributed or published materials, (b) revocation that reaches consent already given for a specific published asset (a live case study or issued press release), or (c) any indemnity or uncapped/cap-excluded liability tied to publicity/trademark use, or liquidated damages for…

⬆️ **Escalate when.** Any of the following requires sign-off before agreeing: (1) Publicity/trademark breach carved OUT of the liability cap, or any indemnity, liquidated damages, or specific-performance/injunction-with-fee-shifting remedy attached -> GC (this…


**Talking points:**

- Bare logo/list listing carries no implied endorsement when it is governed by your brand guidelines and an express 'no endorsement' statement — and we are happy to put both in…
- We are making the clause fully mutual — the same protections you want for your brand, you get to assert against ours. This is reciprocal brand hygiene, not a one-way grab.
- On PR, case studies, and quotes we are not asking for blanket rights — those require your prior written consent on a per-instance basis, because you supply the quote and control…
- Consent 'not to be unreasonably withheld, conditioned, or delayed' is the market standard for this clause — your own customer agreements almost certainly use the same formulation…


*Drafting:* ["Define the standing right against 'Customer's name and logo in Vendor's customer lists and identification of Customer as a customer,' and put PR/case studies/quotes in a SEPARATE sentence with its own consent standard — so a customer…


### 21. Acceptance / Acceptance Testing †

**Opening.** On our paper, acceptance is a formality, not a gate. Draft: Deliverables/Services are deemed accepted if they "substantially conform to Vendor's then-current Documentation/Specifications." Customer has a 5-business-day inspection window from delivery.


**Fallback ladder:**

1. **Give** Tighten the standard from 'substantially conforms' to 'conforms in all material respects to the Specifications,' and agree the… → **Get** The criteria must be the criteria existing/agreed BEFORE testing begins, frozen at SOW signature or by a dated Acceptance Test Plan — no unilateral…
2. **Give** Extend the inspection/testing window from 5 to 15 business days (offer 30 only for genuinely complex/SI deliverables). → **Get** Keep deemed-acceptance on silence, and keep production use as a deemed-acceptance trigger.
3. **Give** Gate deemed-acceptance on a written reminder: if Customer is silent at window's end, Vendor sends a notice and Customer gets a short tail (5 business… → **Get** Production use OTHER than agreed pilot/UAT/DR testing still = immediate deemed acceptance, expressly carved into the clause.
4. **Give** Replace 'commercially reasonable cure' with a structured reject-and-cure loop: on a conforming rejection notice (specifying the failed criteria)… → **Get** (1) A conforming rejection must identify the specific criterion failed; defects Customer doesn't call out are waived.
5. **Give** Add a failure backstop after the capped cure cycles fail: Customer may elect to (a) extend cure, (b) accept with an equitable, pre-agreed price… → **Get** This menu is Customer's SOLE AND EXCLUSIVE remedy for non-acceptance, expressly displacing UCC 2-719(2) failure-of-essential-purpose and any…


🛑 **Red line.** Do not agree to: (1) open-ended acceptance with NO deemed-acceptance mechanism and no outer date — revenue recognition under ASC 606 needs a determinable point of control transfer, and indefinite unfunded acceptance risk means we carry a delivered, un-paid asset on the books with no certainty it ever converts;

⬆️ **Escalate when.** Escalate to GC + CFO jointly if the customer demands either (a) a refund-the-entire-contract / cross-Deliverable clawback on acceptance failure, (b) deletion of the sole-remedy + UCC 2-719(2) displacement language (i.e., surviving…


**Talking points:**

- 'Objective criteria agreed in writing before testing protects both of us — you get certainty the product will be measured against what you actually need, and we get certainty…
- 'Deemed acceptance isn't a trick — it's the rev-rec discipline our auditors require under ASC 606. We need a determinable acceptance date to recognize revenue.
- 'Production use as an acceptance trigger is simple fairness: if the deliverable is good enough to run your live business on, it's good enough to be accepted.
- 'The two-cycle cure loop with a reset clock is a real, enforceable quality gate — you reject with specifics, we fix, you re-test from zero.


*Drafting:* ["Anchor acceptance to 'the Specifications' as a defined term that points to Vendor's Documentation/an agreed Acceptance Test Plan — never let an undefined 'requirements' or 'Customer's expectations' creep in.


### 22. Compliance with Laws / Anti-Corruption †

**Opening.** On our paper, lead with a thin, one-way frame and let the customer build it up. Draft: (1) a single mutual-sounding-but-bare line — "Each party shall comply with all laws applicable to it in the performance of this Agreement" — with NO statute names, no program covenant, no audit, no flow-down;


**Fallback ladder:**

1. **Give** Make the bare compliance line genuinely mutual and add a clean, mutual anti-bribery representation naming both the U.S. → **Get** Strict reciprocity (customer makes the identical rep), and the clause stays inside the general 1x cap with ordinary notice-and-cure termination.
2. **Give** Convert the one-way export/sanctions clause to MUTUAL trade-controls compliance (OFAC, EAR, plus EU/UK where the customer operates) and add a mutual… → **Get** Customer accepts that trade-controls/sanctions obligations are mutual and that either party may suspend performance without liability if continued…
3. **Give** Add an affirmative ABAC program covenant ('maintains commercially reasonable anti-corruption policies, training, and books-and-records appropriate to… → **Get** Program described as 'commercially reasonable' and 'appropriate to size and risk' (not a prescriptive checklist), flow-down is…
4. **Give** Agree the anti-bribery and sanctions reps are CARVED OUT OF THE GENERAL 1x CAP, sitting alongside confidentiality and IP, and that a proven violation… → **Get** Termination requires a 30-day cure period for any breach that is curable (e.g., a lapsed policy, a flow-down gap);
5. **Give** TRUE FLOOR — accept no-cure immediate termination for a proven core bribe, an officer-certification model with a narrow 'records reasonably necessary… → **Get** Audit stays a documented-suspicion, scope-limited, confidential, third-party-auditor, look-only right (NOT a roaming annual books-and-records audit);


🛑 **Red line.** Do NOT agree to: (a) a standalone, dollar-one, uncapped anti-corruption/sanctions INDEMNITY — that is the line insurers and reserves cannot price; corruption/sanctions exposure (treble FCPA penalties, OFAC strict-liability fines into the tens of millions) is exactly the open-ended, often un-insurable tail the single cap exists to…

⬆️ **Escalate when.** Escalate before agreeing to any of: (1) ANY anti-corruption or sanctions INDEMNITY, whether dollar-one or supercapped, or any uncapped liability head beyond the standard carve-out list — GC sign-off (and CFO if uncapped, because it hits…


**Talking points:**

- 'We're giving you the substance you actually need.' The customer's real driver is regulatory DEFENSE, not shifting money to us.
- 'An officer's annual certification is stronger evidence than a one-off audit, and it's how SaaS does it.' A signed officer certification is a recurring, dated, attributable…
- 'The carve-out already solves your real fear.' Pulling the anti-bribery and sanctions reps out of the general cap means a breach claim isn't limited to one year's fees — you have…
- 'Cure rights only bite on curable breaches.' We agree an actual proven bribe is no-cure and terminable immediately — that conduct can't be undone.


*Drafting:* ["Keep knowledge/materiality qualifiers OFF the core 'has not and will not pay, offer, promise, or authorize a bribe' sentence (that's the part the customer's counsel will check and the part that's true anyway), but DO attach 'to its…


### 23. Subcontracting / Personnel & Non-Solicitation †

**Opening.** On our paper, three moves bundled into one clause: (1) Subcontracting — "Vendor may engage affiliates, contractors and subprocessors of its choosing to perform the Services; Vendor's responsibility for subcontractor performance is limited to using reasonable care in selection, and any subcontractor breach is subject to the same limitation of liability and…


**Fallback ladder:**

1. **Give** Drop the carve-out that lets subcontractor breaches hide behind the cap as a separate event; → **Get** In exchange, keep unilateral discretion to ENGAGE subcontractors (no per-sub consent), and confirm that all liability — ours or a sub's — runs…
2. **Give** Add a consent gate, but only for NEW subcontractors that will access Customer Confidential Information or personal data: 'consent not to be… → **Get** Existing/incumbent subs and all non-data-touching subs (infra, support tooling) stay pre-approved with no gate.
3. **Give** Agree a named key-personnel list of 3–6 roles with a 6–12 month commitment, advance notice of voluntary departures, and replacements of 'equal or… → **Get** Replacements are subject to Customer approval 'not to be unreasonably withheld' with a 5-business-day deemed-approval clock;
4. **Give** Make the non-solicitation MUTUAL and narrow it to personnel who were directly involved in the engagement (not the whole workforce), drop the duration… → **Get** Reciprocity (it now also protects us when the customer's people see our delivery team), and we keep 'solicit AND hire' rather than 'solicit only' for…
5. **Give** Replace liquidated damages with a fixed recruiting-cost reimbursement (e.g., 25–30% of first-year base salary as an agreed pre-estimate of placement… → **Get** The clause survives as a mutual, enforceable provision everywhere it can be — the severability language is what keeps a court from blue-penciling or…


🛑 **Red line.** Do not accept a per-subcontractor consent VETO over our general delivery, infrastructure or support stack (as opposed to data-touching subs), and do not accept an absolute prohibition on subcontracting.

⬆️ **Escalate when.** Escalate to the GC if the customer demands (a) a per-subcontractor consent veto extending beyond data-touching subs, (b) standalone subcontractor liability OUTSIDE the MSA cap (an uncapped second liability pool), or (c) any non-solicit…


**Talking points:**

- 'We delegate the work, not the responsibility.' We will remain fully liable for our subcontractors as if their acts were our own — you get a single counterparty to hold…
- A consent veto over our infrastructure and delivery subprocessors isn't something we can give any single customer — they're shared across our platform, and a one-off carve-out…
- On personnel: we'll name and commit the key roles for 6–12 months and give you approval over replacements.
- A one-way non-solicit only protects us; making it mutual protects you too — your people work alongside our delivery team.


*Drafting:* ["Define 'Subcontractor' to expressly INCLUDE affiliates and subprocessors, so the broad engagement right and the prime-liability language both clearly reach the shared platform stack rather than leaving affiliates as a contested…


### 24. Data Portability, Return & Transition / Escrow †

**Opening.** On our paper, open narrow and self-help on all four sub-issues. (1) Return/export: Customer may self-serve export its data via the standard in-product export during the subscription term; on termination, Customer has a 30-day window to export, after which Vendor may delete.


**Fallback ladder:**

1. **Give** Name the export format and make it free: machine-readable CSV/JSON, or a documented API plus the data schema/dictionary, for Customer Data at no… → **Get** 'Normal volume' ceiling stays numeric and Vendor-defined; bulk/full-history extracts or repeated re-exports above the ceiling billed at the PS rate…
2. **Give** Broaden 'Customer Data' to include Customer-supplied attachments, and Customer-authored configuration, plus an export of activity/audit logs… → **Get** Hard line preserved in the definition: usage/telemetry, derived, aggregated, benchmarked, de-identified, and any model-training data remain Vendor IP…
3. **Give** Extend the post-termination export window to 60 days, and add a 'retain-until-export' commitment: we will not delete Customer Data during the window… → **Get** Window applies only if Customer's account is paid current (no export assistance while fees are in dispute/arrears).
4. **Give** Provide transition assistance under a rate card whose rates are locked at signing for the duration of the term (so the customer is not exposed to a… → **Get** Assistance is scoped and capped (defined deliverables: one standard-format export, schema/data-dictionary handover, up to N hours of migration Q&A) —…
5. **Give** On termination, certify deletion of Customer Data in writing within 30 days of the window closing. → **Get** Standard carve-outs survive: (i) data in routine backups deleted on the ordinary backup-rotation cycle rather than on demand;


🛑 **Red line.** Do not agree to (a) return or escrow of usage/derived/aggregated/de-identified/model-training data, or any commitment that lets the customer extract or replicate the platform, analytics, benchmarks, or models — that is the company's core IP and the asset base across the entire customer install base;

⬆️ **Escalate when.** Escalate for sign-off when the customer asks to cross a red line or materially re-prices the deal: (1) any return/escrow of derived, aggregated, de-identified, usage, or model-training data, or any audit/inspection of those datasets — GC +…


**Talking points:**

- 'We're not holding your data hostage — you can self-serve export it in machine-readable CSV/JSON or via our documented API and schema, throughout the term and for 60 days after.
- 'A signed rate card locked at signing removes the only real exit risk that matters — being charged a captive price at the worst moment.
- 'Raw data comes back; analytics, benchmarks, and models stay ours. Those derived datasets are built from the whole customer base, not your records alone — returning them would…
- 'Source-code escrow is theatre for SaaS — even if you held the code, you'd have no servers, data pipeline, secrets, or ops to run it.


*Drafting:* ["Define 'Customer Data' affirmatively and narrowly ('data Customer or its Users submit to the Service'), then add an express exclusion sentence: 'Customer Data does not include Usage Data, Aggregated Data, De-identified Data, or any data…


### 25. Notices, Entire Agreement & Order-of-Precedence †

**Opening.** Put all three mechanics on our paper, ranked our way. (1) ORDER OF PRECEDENCE — "In the event of conflict, the following control in descending order: (a) the Order Form, (b) the online terms at [vendor.com/terms] as updated from time to time, (c) this MSA, (d) the DPA, (e) any SOW." This floats sales-drafted Order Forms and our unilaterally-updatable URL…


**Fallback ladder:**

1. **Give** PRECEDENCE: flip to 'MSA controls on all legal terms; Order Form/SOW controls only on commercial terms (fees, quantities, term length, named… → **Get** Keep the Order Form on top for everything commercial, and require that ANY override of an MSA legal term be (i) by express reference to the specific…
2. **Give** URL/ONLINE TERMS: pin the incorporated online terms to a specific dated version ('the terms at [URL] as of the Order Form Effective Date') and drop… → **Get** Reserve the right to update online terms prospectively at renewal, and keep unilateral update rights for the AUP/security-and-privacy docs and any…
3. **Give** NOTICES — split by type. Email stays valid for ORDINARY notices (routine, support, general comms). → **Get** Strict reciprocity — the same elevated method binds the customer's notices to us, so they cannot effect termination-for-breach by a buried email…
4. **Give** ENTIRE AGREEMENT — add the fraud carve-out ('nothing herein limits liability for fraud or fraudulent misrepresentation') and expressly preserve the… → **Get** Keep the integration clause and no-oral-modification intact, and narrow the non-reliance survivor to bar only claims for NEGLIGENT or INNOCENT…
5. **Give** DEEMED-RECEIPT / NON-RELIANCE FINAL TRIM (large or regulated buyer only): accept that operative notices are deemed received only on actual documented… → **Get** This is the floor for boilerplate. In exchange, hold the integration clause, the signed-writing amendment requirement, the section-specific override…


🛑 **Red line.** Do NOT agree to either of these: (1) leaving the Order Form / customer PO on top of ALL terms (legal + commercial) without the express-section-reference-plus-signature override gate.

⬆️ **Escalate when.** Escalate to the GC (Legal) for sign-off when the customer demands EITHER: (a) Order Form / customer-PO precedence over MSA legal terms WITHOUT the express-section-reference-plus-signature override gate, or any deletion of the fraud…


**Talking points:**

- 'MSA-controls-on-legal-terms' protects YOU as much as us. If a sales-drafted Order Form floated over everything, either side's junior staff could bury a one-sided term in an…
- Pinning the online terms to a dated version is a reasonable ask and we'll do it for the committed term.
- On notices: courts construe operative notices strictly, so a defective termination or breach notice can be held INEFFECTIVE.
- The fraud carve-out is not a concession we're 'giving' — it's mandatory. Neither of us can contract out of our own fraud under US law (and specifically under New York and Delaware…


*Drafting:* Quiet protections that hold without a fight: (1) Order the precedence list so the DPA outranks the MSA on DATA matters but the MSA outranks the DPA on liability/cap — split by subject matter, not a flat stack, so the DPA can't import an…


---

## Approval / Escalation Matrix

| # | Clause | Escalate when (→ approver) |
|---|---|---|
| 1 | Limitation of Liability — Aggregate Cap + Supercaps | Deal-desk / junior counsel may sign WITHIN the ladder down to and including rung 5 — i.e. |
| 2 | Exclusion of Consequential / Indirect Damages | Deal-desk/junior counsel may grant Rung 1 (reciprocity framing + dropping the 'regardless of characterization' gloss). |
| 3 | Indemnification (IP infringement + third-party claims) | Crossing a red line requires sign-off: (a) UNCAPPED IP/third-party indemnity (at ANY tier), any cap above 3x trailing-12-month fees, OR pegging/tying the… |
| 4 | Warranties & Disclaimers | Escalate when the customer demands any of the following (route as noted; routine, market-standard language below these thresholds should be handled by the deal… |
| 5 | IP Ownership & License Grant | (a) Co-ownership of the platform: a customer's opening redline merely ASKING for joint ownership is routine — the reviewer (Deal Desk + supporting counsel)… |
| 6 | Confidentiality | Any customer demand for uncapped liability for confidentiality breaches beyond the trade-secret-misappropriation/willful-breach pair, OR a… |
| 7 | Data Protection, Privacy & Security (DPA) | Escalate to the CISO + GC jointly for: any breach-notice clock BELOW 48 hours (48h itself is pre-approved as the floor — do NOT escalate at 48h), any… |
| 8 | Payment Terms & Late Fees | Net terms beyond Net 60, or monthly/quarterly billing in arrears replacing annual-in-advance → CFO / VP Finance (revrec and cash-flow impact). |
| 9 | Price / Fee Escalation at Renewal | Deal desk can approve, WITHOUT escalation, anything down to and including rung 4: a fixed hard cap of 5% or lower-but-not-below-5%, the discounted/net rate… |
| 10 | Most Favored Customer / Pricing-Parity & Benchmarking | VP Sales (deal desk) may sign off UNILATERALLY only on rungs 1-2 (renewal cap, price lock, extra discount, prepay terms) — pure pricing mechanics with NO MFN… |
| 11 | Term & Auto-Renewal (Evergreen) | Escalate before agreeing to any of: (1) Opt-in / affirmative-renewal in place of auto-renewal, OR a customer termination-for-convenience right inside the… |
| 12 | Termination | Any customer termination-for-convenience right that waives the early-termination fee or refunds/relieves prepaid/committed fees mid-term requires VP Sales +… |
| 13 | Service Levels (SLA) & Uptime Credits | **GC sign-off** required to: make an SLA breach a termination/breach trigger for the whole Agreement; remove the sole-and-exclusive-remedy designation; |
| 14 | Insurance | Escalate before agreeing when the customer asks for: (a) any AI/primary-noncontributory/waiver-of-subrogation on the Cyber or E&O lines, OR cyber limits above… |
| 15 | Assignment & Change of Control | Escalate to the GC (VP Sales informed) before agreeing to: (a) any customer right to make a VOLUNTARY DIRECT assignment to a [Vendor] competitor without our… |
| 16 | Governing Law, Venue & Dispute Resolution | GC sign-off required for: (1) accepting the customer's home-state law where that jurisdiction is on our 'hostile forum' list (CA waiver/consumer issues, LA… |
| 17 | Contractual Limitation Period for Claims | Sub-floor or void-risk terms (shortening below UCC 2-725's one-year goods floor, any shortening under Louisiana or other anti-shortening governing law, or… |
| 18 | Force Majeure | Escalate before agreeing to any of: (1) cash refund/clawback of EARNED or prepaid one-time fees, or any FM relief that touches the payment-not-excused baseline… |
| 19 | Audit / Compliance-Verification Rights | CISO sign-off (with GC) required for ANY customer-directed or customer-conducted audit, inspection, or penetration testing of Vendor's production/multi-tenant… |
| 20 | Publicity & Use of Name/Logo | Any of the following requires sign-off before agreeing: (1) Publicity/trademark breach carved OUT of the liability cap, or any indemnity, liquidated damages… |
| 21 | Acceptance / Acceptance Testing | Escalate to GC + CFO jointly if the customer demands either (a) a refund-the-entire-contract / cross-Deliverable clawback on acceptance failure, (b) deletion… |
| 22 | Compliance with Laws / Anti-Corruption | Escalate before agreeing to any of: (1) ANY anti-corruption or sanctions INDEMNITY, whether dollar-one or supercapped, or any uncapped liability head beyond… |
| 23 | Subcontracting / Personnel & Non-Solicitation | Escalate to the GC if the customer demands (a) a per-subcontractor consent veto extending beyond data-touching subs, (b) standalone subcontractor liability… |
| 24 | Data Portability, Return & Transition / Escrow | Escalate for sign-off when the customer asks to cross a red line or materially re-prices the deal: (1) any return/escrow of derived, aggregated, de-identified… |
| 25 | Notices, Entire Agreement & Order-of-Precedence | Escalate to the GC (Legal) for sign-off when the customer demands EITHER: (a) Order Form / customer-PO precedence over MSA legal terms WITHOUT the… |

## Deal-Breaker Red Lines (quick reference)

| # | Clause | Red line |
|---|---|---|
| 1 | Limitation of Liability — Aggregate Cap + Supercaps | Do NOT agree to (1) an UNCAPPED general liability cap, or a general multiplier above roughly 2x trailing-12-month fees (1x is the target; |
| 2 | Exclusion of Consequential / Indirect Damages | Do NOT accept (a) deletion of the lost-profits exclusion as a GENERAL matter — i.e., the customer recovering its own lost profits for ordinary performance failures, downtime, or defects, outside the… |
| 3 | Indemnification (IP infringement + third-party claims) | Do NOT agree to a fully UNCAPPED IP/third-party indemnity, and do not tie the indemnity to — or let it exceed — the company's actual cyber/E&O/media-liability tower, in ANY deal tier without… |
| 4 | Warranties & Disclaimers | Do NOT agree to: (1) any open-ended fitness-for-Customer's-particular-purpose warranty, or a warranty that the Service will meet Customer's specific business requirements or regulatory obligations —… |
| 5 | IP Ownership & License Grant | Do NOT (a) assign, co-own, or grant exclusivity in the Service, platform, models, or any underlying Vendor Technology; |
| 6 | Confidentiality | Do NOT agree to fully uncapped liability for ALL confidentiality breaches (a blanket carve-out of the entire confidentiality section from the dollar cap), and do NOT let an uncapped 'any Security… |
| 7 | Data Protection, Privacy & Security (DPA) | Do NOT agree to: (a) uncapped liability for any privacy/security losses, or a data-breach super-cap exceeding ~3x trailing-12-month fees, or a super-cap with no connection to our cyber-insurance… |
| 8 | Payment Terms & Late Fees | Do not accept (a) a customer right to withhold or set off the ENTIRE invoice — or to net unliquidated/indemnity/breach/damages claims against fees — which converts our receivable into a self-help… |
| 9 | Price / Fee Escalation at Renewal | Do NOT agree to: (a) a hard freeze of fees for the entire term and all renewals — no escalator at all; |
| 10 | Most Favored Customer / Pricing-Parity & Benchmarking | Never agree to ANY of the following — these are walk / hard-escalate, not negotiable drafting points: (1) parity measured against NET/effective price WITHOUT the full carve-outs for… |
| 11 | Term & Auto-Renewal (Evergreen) | Do not agree to (a) convert auto-renewal to affirmative opt-in / opt-in re-signature ('renewal requires the customer's affirmative written election'); |
| 12 | Termination | Do NOT grant a customer termination for convenience that refunds or relieves prepaid/committed fees mid-term, and do NOT relieve a customer of committed/accrued fees on a customer-cause termination… |
| 13 | Service Levels (SLA) & Uptime Credits | Do NOT (a) let an SLA breach trigger a **general breach or termination of the entire Agreement**, or open the door to **uncapped or consequential damages** (lost profits, cover costs) for downtime; |
| 14 | Insurance | Do NOT agree to any of the following: (1) Additional-insured status on the claims-made Cyber or Tech E&O policies — carriers generally won't endorse it cleanly, it dilutes a shared aggregate limit… |
| 15 | Assignment & Change of Control | Two genuine walk/hard-escalate lines: (1) We will NOT permit the customer to make a VOLUNTARY DIRECT assignment of this Agreement to a direct competitor of [Vendor] without our consent, with full… |
| 16 | Governing Law, Venue & Dispute Resolution | Do NOT agree to the customer's own home-state law AND home-state exclusive venue COMBINED where that state is hostile to our standard risk terms — i.e., a forum that voids or narrows contractual… |
| 17 | Contractual Limitation Period for Claims | Do not agree to language that effectively gives us UNLIMITED time exposure on core service/warranty claims with no finite outside backstop AND no liability cap interaction — e.g., a pure discovery… |
| 18 | Force Majeure | Two positions we do not cross. (1) FM must NEVER excuse, suspend, or cap (a) the confidentiality/data-security obligations, (b) the data-breach notification and incident-response duties, or (c) the… |
| 19 | Audit / Compliance-Verification Rights | Do not agree to: (a) true-up at the discounted/contract rate with NO cost-shift AND no ability to recover undiscounted value for willful, knowing, or repeated overuse — conceding contract-rate… |
| 20 | Publicity & Use of Name/Logo | Do not agree to (a) retroactive recall/destruction of already-distributed or published materials, (b) revocation that reaches consent already given for a specific published asset (a live case study… |
| 21 | Acceptance / Acceptance Testing | Do not agree to: (1) open-ended acceptance with NO deemed-acceptance mechanism and no outer date — revenue recognition under ASC 606 needs a determinable point of control transfer, and indefinite… |
| 22 | Compliance with Laws / Anti-Corruption | Do NOT agree to: (a) a standalone, dollar-one, uncapped anti-corruption/sanctions INDEMNITY — that is the line insurers and reserves cannot price; |
| 23 | Subcontracting / Personnel & Non-Solicitation | Do not accept a per-subcontractor consent VETO over our general delivery, infrastructure or support stack (as opposed to data-touching subs), and do not accept an absolute prohibition on… |
| 24 | Data Portability, Return & Transition / Escrow | Do not agree to (a) return or escrow of usage/derived/aggregated/de-identified/model-training data, or any commitment that lets the customer extract or replicate the platform, analytics, benchmarks… |
| 25 | Notices, Entire Agreement & Order-of-Precedence | Do NOT agree to either of these: (1) leaving the Order Form / customer PO on top of ALL terms (legal + commercial) without the express-section-reference-plus-signature override gate. |
