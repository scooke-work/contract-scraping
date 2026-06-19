# MSA Review Checklist

The full anatomy of a master services agreement with the **specific sub-points to check or
flag** in review, in the order terms typically appear. An MSA is the **master framework** —
it holds the legal/risk terms once; commercial specifics (scope, price, timeline,
deliverables) live in **SOWs / Order Forms** issued under it.

The clauses that consume the most negotiation time are detailed in the companion playbooks:
[`negotiation-playbook.md`](negotiation-playbook.md) (where vendors start vs. where deals
land) and [`vendor-defense-playbook.md`](vendor-defense-playbook.md) (opening → fallback
ladder → red lines). Sections 1–10 below assume a SaaS / technology + professional-services
MSA; **Section 11** adds the goods/supply (UCC Article 2) terms for non-SaaS deals.

> *General market-practice reference, not legal advice — adapt with counsel.*

## 1. Front matter
- **Parties** · correct *contracting* legal entity (not parent/affiliate) · entity type + state/country of incorporation · signatory authority · notice address.
- **Dates** · effective date vs. signature date vs. SOW/subscription start.
- **Recitals** · accurate, "background only," create no obligations.
- **Definitions** · every capitalized term defined, no circularity · scope of *Confidential Information, Customer Data, Deliverables, Services, Affiliate, Documentation* · "including" = "without limitation."
- **Order of precedence** · which document wins · whether an Order Form / URL terms sit on top · override only by express, signed, section-specific reference.

## 2. Framework & structure
- **Structure** · MSA = legal terms, SOW/Order Form = commercial · what controls on conflict.
- **SOW / Order Form** · who may issue · required form + signature · do unsigned POs bind.
- **Affiliates** · which may order/use · prime vs. per-affiliate liability · flow-down of terms.
- **Change control** · written change orders · price/schedule impact · no work pre-approval · how disputed changes resolve.

## 3. Scope & delivery
- **Scope / deliverables** · specified in SOW · assumptions + exclusions stated.
- **Acceptance** · "materially conforms" vs. "substantially" · criteria agreed *before* testing · window length + start point · deemed-acceptance triggers (silence; production use) · capped cure cycles + re-test reset · failure backstop (price reduction / terminate + refund) · holdback %.
- **SLA** · uptime % + tiering · measurement window + method · "downtime" definition + exclusions · credit schedule + cap · sole-remedy **+ cumulative-remedies carve-out** + not-applicable-to-security/IP · chronic-failure termination + refund · claim mechanics (auto vs. request; days).
- **Customer responsibilities / dependencies** · what customer must provide · vendor relief/excuse for customer delay.
- **Key personnel** · named roles · reassignment lock · "equal-or-better" replacement + approval · background checks.
- **Subcontracting** · consent for new/data-touching subs · prime remains liable · flow-down · subprocessor list (→ DPA).
- **Governance** · meeting/reporting cadence · escalation path.

## 4. Commercial
- **Fees** · amounts/units/currency · one-time vs. recurring · ramp/tiers.
- **Invoicing & payment** · net term + invoice-date vs. *conforming*-invoice clock · e-invoice/PO precondition · **good-faith dispute carve-out** · late interest + "or max by law" usury qualifier · suspension notice/cure/undisputed-only · no-set-off vs. SLA-credit set-off.
- **Expenses** · pre-approval · travel-policy cap · pass-through (no markup).
- **Taxes** · who bears sales/VAT · exemption certs · withholding gross-up.
- **Escalation** · cap % · "lesser of CPI and X" vs. "greater of" · *named* BLS index · base = **discounted** vs. list rate · first-year flat · anti-compounding · advance notice.
- **MFN / benchmarking** · comparator definition · list vs. net price · carve-outs (channel/bundle) · verification (cert vs. audit) · remedy (prospective credit).

## 5. Term & termination
- **Term & renewal** · initial length · auto-renew vs. opt-in · renewal length (**1-yr vs. equal**) · non-renewal notice window + method · pre-deadline reminder.
- **Termination** · convenience (who/notice/fees) · for cause + cure (length + **symmetry**) · payment hair-trigger + notice · good-faith dispute carve-out · insolvency (§365 reality).
- **Effects / transition** · data **export format + window** + retain-until-export · deletion + certification · **transition assistance + rate card locked at signing** · pro-rata refund on vendor-cause · escrow · survival list.

## 6. IP & data
- **IP ownership** · background IP each retains · deliverables "**hereby assigns**" + work-for-hire backup · "reusable/residual" sweep narrowed · feedback **license** (not assignment) · payment-conditioned assignment · no joint ownership · strike "revocable at vendor discretion."
- **Data rights** · customer data never vendor IP · usage/derived/aggregated/de-identified rights · **AI training opt-in/opt-out** · AI **output** ownership.
- **Confidentiality** · definition + marking standard · survival tail + **indefinite trade-secret carve-out** · standard exclusions · residuals (delete/narrow) · recipients "at least as protective" · compelled-disclosure mechanics · return/destroy + cert + backup carve-out · injunctive relief/no-bond.
- **DPA / security** · controller/processor roles · **breach-notice clock** (aware vs. confirm; 48–72h) + content + assist · subprocessor model + objection window + **vendor direct liability** · security standard ("**maintains** SOC 2/ISO" + lapse hook) · audit (report vs. on-site) · SCCs/IDTA/DPF + cross-border · return/deletion + DSR assistance · **super-cap + consequential-waiver carve-out** · **no-AI-training covenant**.

## 7. Warranties & risk allocation
- **Reps & warranties** · authority/no-conflict (mutual) · performance/conformity · anti-malware/no-disabling-code · security · compliance-with-law · survival periods.
- **Disclaimers** · implied warranties (merchantability/fitness/title/**non-infringement**) · "uninterrupted/error-free" · "**except as expressly stated**" subordination · ALL-CAPS conspicuousness · beta/AI AS-IS.
- **Indemnification** · who→who (**mutual?**) · scope (patent/copyright/TM + **trade-secret**) · exclusions "to the extent" · defend from tender · procure/modify/terminate ladder · notice-and-prejudice · defense control + separate counsel on conflict · settlement consent · **two cap questions** (escape the consequential *exclusion* AND the dollar super-cap) · AI-output/open-source.
- **Limitation of liability** · cap multiple **+ metric** (paid vs. paid-or-payable; period; per-order vs. aggregate) · anti-stacking · **mutuality of the dollar cap** · data/IP **super-caps** · uncapped carve-outs (IP/confi/GN/WM/fraud/bodily injury/payment) · **carve-outs escape the consequential exclusion** · UCC 2-719(2) FOEP survival.
- **Consequential-damages waiver** · mutual · named heads (lost profits/revenue/data) · carve-outs mirroring the cap · "costs to recover data" recoverable vs. "value of data" excluded · FOEP-survives language · conspicuousness.
- **Insurance** · coverage types + limits (CGL; **Tech E&O; Cyber — unblended**) · ransomware/contingent-BI sub-limits · carrier rating (A- VII+) · additional-insured + primary-noncontributory + waiver-of-subrogation (endorsed) · 30-day cancellation notice · "**insurance ≠ cap**" · cyber limit floors the data super-cap.

## 8. Compliance & legal
- **Compliance with laws** · mutual · scope.
- **Anti-corruption** · **FCPA + UK Bribery Act** · no knowledge/materiality on the core "no bribe" · program covenant + flow-down · violation = termination · carve-out from cap.
- **Export / sanctions** · OFAC/EAR · **Sanctioned-Person + 50%-owner rep** · screening · ITAR if relevant.
- **Sector** · HIPAA/BAA, GLBA · debarment/exclusion-list reps (SAM/OIG/FDA).

## 9. General / boilerplate
- **Governing law & disputes** · law (neutral DE/NY?) · **substantive-only vs. + procedural** · **courts vs. arbitration** · venue · jury waiver (mutual) · class waiver · escalation tiers · IP/equitable carve-out (mutual) · fee-shifting · public-sector subordination.
- **Limitation period** · length (1–2 yr) · **accrual vs. discovery** trigger · mutual · carve-outs · "survival ≠ shorten" · UCC 2-725 one-year floor / Louisiana.
- **Assignment & change of control** · "**not unreasonably withheld/conditioned/delayed**" · mutual · M&A/affiliate carve-out · competitor exclusion · CoC = deemed-assignment trigger · continuing liability vs. release · receivables override (UCC 9-406/9-408).
- **Force majeure** · mutual · closed list vs. catch-all + named events · payment not excused **but abatement/refund for unprovided service** · **DR/BCP carved out** · SLA clock runs vs. pauses · **bilateral termination at ~30 days** + refund · mitigation · notice.
- **Audit** · ≥30-day notice · 1×/12 mo + for-cause · third-party auditor + NDA · scope/data exclusions · cost-shift threshold (5–10%) · **true-up at contract vs. list rate** · copyright-infringement reservation deletion · SaaS overage rate + pre-bill notice.
- **Publicity** · **blanket vs. per-instance consent** · logo/list vs. PR/case-study tiering · **revocable** trademark license · cease/remove on termination · mutual · AI/model-training use.
- **Non-solicitation** · mutual · engagement staff only · duration · general-advertising carve-out · "solicit" vs. "hire" · LDs vs. injunctive · **CA/ND/OK void**.
- **Notices & entire agreement** · method by type (email ordinary; **certified/confirmed for operative** notices) + copy-to-counsel · deemed-receipt timing · entire-agreement + **fraud carve-out** + non-reliance scope · preserve NDA/DPA/side-letters.
- **Relationship** · independent contractor; no agency/partnership/JV.
- **Mechanics** · amendments (written + signed) · waiver (no implied) · severability · counterparts/e-sign · **survival** list · cumulative remedies · third-party beneficiaries (none) · further assurances.

## 10. Exhibits & schedules
- All present, current, cross-referenced, **no "[TBD]"/blanks** · SOW/Order Form templates · **DPA** (current) · SLA · **security/InfoSec exhibit** specifics · pricing/rate card · insurance schedule · **BAA** if healthcare · acceptable-use policy.

---

## 11. Goods / Supply add-ons (UCC Article 2 deals)

For a sale-of-goods or supply agreement, the framework above still applies, but several
SaaS/services clauses change shape and the following are added. (Article 2 of the UCC
governs the sale of goods — many defaults below are UCC gap-fillers you are confirming or
overriding.)

**Clauses that change shape vs. SaaS/services:**
- **Acceptance → Inspection & rejection** · the SaaS "acceptance test" becomes UCC inspection + **perfect-tender** rejection (2-601).
- **No SLA/uptime** · replaced by product warranty + epidemic-failure terms.
- **Limitation period** · the UCC default is **4 years** (2-725); confirm any contractual shortening (floor: 1 year).

**Added clauses / sub-points to look for:**
- **Forecasts & ordering** · binding vs. non-binding forecast · min/max order quantities · requirements/output commitment · blanket vs. firm POs · lead times · rolling forecast windows.
- **Delivery & Incoterms** · delivery term (FOB/FCA/DDP per **Incoterms 2020**) · delivery location · partial/installment shipments · delivery schedule · "time is of the essence" · late-delivery remedy.
- **Title & risk of loss** · when **title** passes · when **risk of loss** passes (often at the Incoterm delivery point) — *these can differ; confirm both explicitly*.
- **Inspection, acceptance & rejection** · inspection period · right to reject non-conforming goods (**2-601 perfect tender**) · revocation of acceptance (**2-608**) · seller's right to cure (**2-508**) · return/restocking + freight on rejected goods.
- **Quantity / shortage / overage** · tolerance band · handling of over-/under-shipment.
- **Packaging, labeling & shipping** · packaging spec · labeling/marking · country-of-origin marking · HAZMAT handling · freight/carrier + transit insurance.
- **Pricing & price adjustment** · firm price vs. raw-material/index pass-through · surcharge mechanics · most-favored pricing.
- **UCC warranties** · express warranty (conformity to spec/sample/model) · implied **merchantability** (2-314) · implied **fitness for a particular purpose** (2-315) · warranty of **title & against infringement** (2-312) · disclaimers must be **conspicuous** and (for merchantability) name "merchantability" or use "as is" (**2-316**) · warranty period · remedy (repair/replace/refund) within 2-719 limits.
- **Product warranty & defects** · warranty period + start (ship vs. install) · repair/replace/refund remedy · **latent-defect** handling · **epidemic/systemic failure** clause (threshold %, root-cause analysis, remedy, expanded recall).
- **Recall** · who bears recall costs · cooperation · trigger + control.
- **Continuity of supply / EOL** · capacity/allocation-on-shortage + priority · **last-time-buy** + end-of-life notice · spare-parts availability period.
- **Quality & change control** · quality system (e.g., **ISO 9001**) · incoming inspection · facility audit/inspection rights · corrective action (CAPA) · **no unapproved change** to spec/process/component source/site.
- **Product compliance** · regulatory conformity (CE/FCC/UL) · **RoHS/REACH/conflict minerals** · Prop 65 · country-specific standards.
- **Product liability** · indemnity for personal injury / property damage from defective goods · **product-liability insurance** coverage + limits.
- **Tooling** · ownership of tooling/molds · who funds · return/access on termination.
