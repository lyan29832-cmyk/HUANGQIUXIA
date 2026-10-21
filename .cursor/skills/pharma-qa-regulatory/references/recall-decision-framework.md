# Recall decision, execution, and closure framework

## Table of contents

1. Purpose and status
2. Recall activation gates
3. Risk assessment and classification controls
4. Jurisdictional clock matrix
5. Recall strategy and depth
6. Regulatory communication package
7. Supply-chain execution and evidence
8. Effectiveness checks and reconciliation
9. Product disposition
10. Termination and quality-system closure
11. MAH / contract manufacturer / commercial / PV / RA interface
12. Mock recall and readiness testing
13. Case-routing examples
14. SOP/SMP drafting checklist

## 1. Purpose and status

Use this file after [recall-regulatory-map.md](recall-regulatory-map.md) when a task requires an operational recall decision, SOP/SMP design, case triage, recall-clock table, recall strategy, authority/consignee communication, effectiveness checks, reconciliation, termination, or recall-readiness audit.

This framework is a professional implementation model. Jurisdiction-specific requirements come from [recall-regulatory-map.md](recall-regulatory-map.md) and the current official source. Do not present company-design choices in this framework as law unless the cited source expressly requires them.

## 2. Recall activation gates

Run Gates 0-6 in parallel. A case can trigger more than one route.

### Gate 0 - distributed product?

Determine whether the product:

- remains under direct company control;
- has left the manufacturing site but remains in a controlled affiliate warehouse;
- has entered wholesaler/distributor control;
- has reached pharmacies, hospitals, investigators, patients, or consumers;
- has crossed borders or been exported.

This distinction can change whether the action is a recall, stock recovery, correction, market withdrawal, stop-ship, or another market action.

### Gate 1 - immediate patient/product protection?

Assess whether to implement immediately:

- quarantine / stop ship;
- stop sale / stop use;
- production or release suspension;
- pharmacy/hospital notification;
- patient-level communication;
- public warning;
- authority contact;
- emergency medical advice;
- supply-continuity or shortage mitigation.

Do not wait for final root cause when immediate controls are justified.

### Gate 2 - suspected quality defect or safety hazard?

Define the defect and potential mechanism, including:

- identity/mix-up/labeling;
- contamination or sterility assurance;
- potency/content/dissolution/degradation;
- particulate/foreign matter;
- packaging/container-closure integrity;
- counterfeit/falsification/tampering;
- temperature/storage/transport failure;
- manufacturing/process/control failure;
- incorrect patient information or dosing instructions;
- unapproved or uncontrolled change;
- quality defect linked to adverse event or lack of efficacy.

### Gate 3 - time-critical parallel regulatory report?

Check separately for:

- China PV or serious-quality/safety reporting;
- US FAR, BPDR, postmarketing safety reporting;
- EU quality-defect notification / rapid alert route;
- shortage/supply-disruption notification where applicable;
- national competent-authority reporting;
- foreign-market notification.

A recall decision does not replace these reports.

### Gate 4 - recall threshold met?

Ask:

- Is distributed product potentially harmful, noncompliant, unsafe, ineffective, mislabeled, deteriorated, contaminated, or otherwise subject to market removal?
- Has the issue been confirmed or is the suspicion sufficiently serious to justify recall before confirmation?
- Can risk be controlled without recall, and is that legally/clinically acceptable?
- Is the defect limited to identifiable units/lots or potentially systemic?
- Has product reached patients?

### Gate 5 - formal classification route

Apply only the governing jurisdiction's system:

- China: Level I/II/III under the NMPA Recall Measures.
- US: FDA Class I/II/III; company health-hazard assessment can support a proposal but FDA assigns the classification.
- EU: use the current Union/NCA quality-defect risk classification and recall/rapid-alert process; do not invent a China/US class equivalence.

### Gate 6 - cross-market / cross-product scope?

Assess shared:

- API, excipient, component, packaging material;
- equipment, line, room, HVAC, water or computerized system;
- analytical method or laboratory cause;
- contract manufacturer / testing laboratory / logistics provider;
- process change or supplier;
- production date window;
- destination country;
- product family or strength;
- stability or cold-chain excursion mechanism.

Document why related lots/products/markets are included or excluded.

## 3. Risk assessment and classification controls

Use a health-hazard narrative before relying on a numeric risk score.

At minimum evaluate:

1. observed or plausible harm;
2. severity of harm;
3. probability/likelihood;
4. reversibility or duration;
5. time to harm / urgency;
6. exposure amount and duration;
7. population size;
8. vulnerable groups;
9. clinical detectability before harm;
10. availability and risk of alternative treatment;
11. defect detectability by user/health professional;
12. possibility that unaffected-looking units are affected;
13. geographic/distribution extent;
14. uncertainty and evidence quality;
15. consequences of not recalling;
16. consequences of recalling, including shortage risk.

A shortage concern can influence recall strategy, but it does not justify leaving known unsafe product in the market without documented authority/risk governance.

## 4. Jurisdictional clock matrix

### 4.1 China core clocks

After the MAH decides recall under the 2022 Drug Recall Administrative Measures:

| Action | Level I | Level II | Level III |
| --- | ---: | ---: | ---: |
| Send recall notice + file investigation/risk report, plan, notice | 1 day | 3 days | 7 days |
| Progress report | Daily | Every 3 days | Every 7 days |

Additional China clocks:

- Recall and disposition completion report: within **10 working days after recall completion**.
- Specified foreign recall by foreign MAH: domestic responsible entity reports specified information within **10 working days after overseas recall initiation**.
- Provincial regulator effectiveness review after summary report: within **10 working days after receipt**.

Always verify the current rule before copying clocks into a controlled SOP.

### 4.2 United States core clocks

There is no single universal statutory `Class I = 24h / Class II = 48h / Class III = 72h` company recall clock in 21 CFR Part 7.

Controls:

- Under 21 CFR 7.46, a firm that removes/corrects distributed product because it believes it is violative is requested to notify the appropriate FDA office **immediately**.
- Do not delay recall initiation while FDA reviews the firm's strategy or assigns classification.
- Under 21 CFR 7.53, FDA specifies recall-status report frequency based on urgency; the regulation states a **generally 2-4 week** reporting interval unless otherwise specified.
- Separate FAR, BPDR, and safety-report clocks from recall clocks.

### 4.3 European Union core clocks

Do not invent one EU-wide MAH recall clock where the source gives a risk-based or authority-route requirement.

Controls:

- EU GMP / Directive 2017/1572 require a system capable of **prompt recall at any time** and notification of defects that could result in recall or abnormal supply restriction.
- Directive 2001/83/EC Article 123 requires specified MAH market actions to be notified **forthwith**.
- Article 117a requires rapid alert transmission without delay for suspected serious public-health risk and urgent public announcements within **24 hours** where the medicinal product is deemed to have reached patients.
- For centrally authorised products, follow EMA's current quality-defect reporting instructions, including interim-report requirements when final reports are not available.
- Nationally authorised products follow the competent authority's national route and operational timelines.
- The 2026 Union quality-defect procedure's 1-working-day classification target and 3/5/10-working-day risk-management limits are **NCA operating targets**, not generic MAH recall deadlines. Do not copy them into a company SOP as legal recall clocks.

## 5. Recall strategy and depth

Before execution, or contemporaneously for an urgent recall, create a controlled **Recall Decision Record** that captures at minimum: trigger/source; first-awareness date/time; distributed status; affected product/lot/markets; current evidence and uncertainty; health-hazard assessment; immediate containment; recall vs non-recall rationale; jurisdiction-specific classification or proposed classification; recall depth/scope; regulator-contact route and clock; PV/FAR/BPDR/quality-defect parallel reports; shortage/continuity impact; decision authority; and date/time of approval. Update the record when scope, risk, classification, or strategy changes.

Do not delay urgent protective action solely to complete the record.


Document the strategy before or contemporaneously with execution; do not delay urgent initiation merely to perfect the document.

Include:

- product/strength/dosage form/presentation;
- affected lot(s)/serial/code/time window;
- recall reason and defect mechanism;
- health-hazard assessment;
- geographic markets/countries;
- distribution quantities and dates;
- recall level/class or proposed classification;
- recall depth;
- stop-sale/use instructions;
- downstream notification requirement;
- public warning decision;
- medical advice / patient communication if relevant;
- action required for stock on hand;
- return/correction/destruction route;
- special storage/transport requirements;
- effectiveness-check approach;
- reporting cadence;
- shortage/alternative-treatment plan;
- owner and 24/7 escalation contacts.

### 5.1 US recall depth

Under 21 CFR 7.42, use consumer/user, retail, or wholesale level as appropriate. FDA reviews adequacy of the firm's strategy and may recommend changes.

### 5.2 China recall scope

Define the units, batches, distribution areas, and recall time limit in the recall plan. If the recall is incomplete, expand the scope or re-recall and update the regulator as required.

### 5.3 EU recall scope

Use QRM and competent-authority coordination. Cross-border quality defects may require Rapid Alert Network coordination. Confirm whether the product is centrally authorised or nationally authorised before selecting the reporting route.

## 6. Regulatory communication package

Maintain a controlled recall data pack that can be generated rapidly.

### Core data set

- legal product name and identifiers;
- MAH/applicant/manufacturer/recalling firm;
- lot/batch and expiry;
- strength, dosage form, pack;
- defect description;
- discovery date/time/source;
- distribution start/end dates;
- total manufactured/released/distributed/on-hand;
- markets/countries;
- direct accounts and downstream chain;
- adverse events/complaints known;
- investigation status;
- health-hazard/risk assessment;
- proposed recall classification and depth;
- draft recall communication/public warning;
- immediate controls;
- CAPA known at that time;
- contact people and 24/7 number.

### Communication-control rules

- Use one controlled fact set across QA, PV, RA, commercial, medical, legal/public affairs, and supply chain.
- For multi-market recalls, maintain a jurisdictional action matrix showing each market's legal actor, authority, classification terminology, notification route, clock, consignee/public communication, progress/final-report requirement, and closure status. Do not force all markets into the most familiar market's recall class or deadline.
- Timestamp all regulator and consignee communications.
- Preserve original communications and revised versions.
- Do not make unsupported statements that the defect is isolated or harmless.
- Do not imply regulator endorsement unless expressly received.
- Reconcile translated recall notices to the approved source text for international recalls.

## 7. Supply-chain execution and evidence

### Distribution traceability

The recall system should rapidly produce:

- direct account list;
- shipment dates/quantities;
- lot numbers and expiry;
- consignee addresses/contacts;
- downstream customers where available/required;
- export destinations;
- inventory remaining under company control;
- known patient/user-level distribution where applicable.

US finished drugs: 21 CFR 211.150(b) expressly requires a system by which distribution of each lot can be readily determined to facilitate recall.

China: use statutory traceability and the Recall Measures' purchase/sales-record requirements.

EU: use GMP/GDP distribution records and the applicable recall/rapid-alert route.

### Returned/recalled stock

Maintain:

- receipt date/time;
- consignee/source;
- quantity;
- lot/pack identity;
- storage condition;
- quarantine status;
- tamper/seal condition;
- investigation sample status;
- disposition authorization;
- destruction/rework/correction evidence.

## 8. Effectiveness checks and reconciliation

### 8.1 Effectiveness-check design

Define what constitutes an effective response:

- recall notice received;
- notice understood;
- distribution/use stopped;
- downstream consignees notified where required;
- affected inventory identified;
- return/correction/disposition instruction executed;
- response evidence documented.

Escalate nonresponders based on risk. Do not count an undelivered email as a successful notification.

### 8.2 United States

Under 21 CFR 7.42, effectiveness checks verify that consignees at the specified recall depth received notification and took appropriate action. FDA may use Levels A-E for the percentage/intensity of effectiveness checks in the recall strategy.

Do not map FDA Effectiveness Check Level A-E to recall Class I-III.

### 8.3 China

The MAH must evaluate recall effectiveness during execution. If incomplete, revise the plan, broaden the recall, or conduct a renewed recall; regulators can also require re-recall after effectiveness review.

### 8.4 Reconciliation

Maintain a quantity reconciliation:

`released/distributed quantity = recovered + corrected + destroyed + confirmed consumed/used + confirmed on-hand + other explained disposition + unresolved quantity`

Investigate material unexplained quantities and risk-significant nonresponders.

## 9. Product disposition

Do not assume recalled product can be reworked or returned to sale.

Assess:

- legal/regulatory acceptability;
- approved dossier and GMP status;
- product identity and traceability;
- storage/transport history;
- tamper evidence;
- defect mechanism;
- validation/qualification;
- labeling/packaging change controls;
- expiry implications;
- need for authority agreement.

China Recall Measures permit specified corrective handling in certain circumstances, but such handling must comply with applicable quality-management requirements and may not extend expiry/shelf life.

For US/EU product, use the applicable CGMP/GMP, approved application/marketing authorisation, and regulator instructions before rework/relabel/re-release.

## 10. Termination and quality-system closure

Keep four decisions separate:

1. **Recall execution complete** — planned market actions have been performed.
2. **Regulatory recall terminated/closed** — regulator termination/acceptance obtained where applicable.
3. **Investigation complete** — scope, root cause, and impact assessment are adequate.
4. **CAPA/change closure** — actions implemented and effectiveness demonstrated where required.

A recall can be operationally complete before CAPA effectiveness is finished. Conversely, a CAPA plan does not terminate a recall.

### China

Submit completion/disposition reporting within the rule's timeframe; regulator assesses recall effectiveness and can require renewed recall.

### United States

FDA terminates the recall when reasonable efforts have been made and appropriate removal/correction/disposition has occurred. A firm may request termination with current status and disposition information.

### EU

Follow the applicable NCA/EMA closeout route. Ensure investigation, defect assessment, CAPA, market action, distribution/reconciliation, and final authority communications are complete.

## 11. MAH / contract manufacturer / commercial / PV / RA interface

Map at minimum:

| Activity | MAH / applicant / recalling firm | Contract manufacturer | QA | PV | RA | Supply chain / commercial | Medical / legal / public affairs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Initial defect intake | Accountable for market-safety governance | Provide manufacturing facts | Lead quality triage | Screen safety info | Screen regulatory reports | Provide distribution data | Support patient/public communication |
| Recall risk assessment | Approve/own market decision according to legal role | Technical input | Lead quality assessment | Safety assessment | Authority-route advice | Supply/shortage input | Risk communication input |
| Recall classification | Jurisdiction-specific responsibility | Consulted | Prepare rationale | Consulted | Verify regulatory framework | Informed | Informed |
| Authority notification | Legal-role dependent | Provide data; direct notification if source requires | Content owner for quality | PV reports in parallel | Submission/coordination | Supply data | Communication review |
| Recall execution | Ensure overall governance | Support affected-site actions | Control records/reconciliation | Safety follow-up | Regulator updates | Notify/recover through channel | Public/patient materials as needed |
| Closeout | Ensure regulatory and quality closure | CAPA/site closure | Investigation/CAPA/PQR | Safety reconciliation | Final authority closeout | Final stock reconciliation | Final communication if needed |

Do not allow quality agreements to obscure statutory responsibility. Define 24/7 notification, first-awareness clocks, data access, lot genealogy, authority-contact ownership, recall-letter approval, returned-product handling, and CAPA responsibility.

## 12. Mock recall and readiness testing

A mock recall is a readiness control, not a substitute for an actual recall procedure.

Define:

- test product/lot and scenario;
- announced or unannounced mode;
- scope and markets;
- distribution-list generation time;
- traceability completeness;
- escalation/decision simulation;
- recall-letter generation;
- consignee response simulation;
- reconciliation accuracy;
- data integrity and evidence retention;
- gaps, CAPA, and retest criteria.

Do not invent a universal regulator-mandated mock-recall frequency. Set frequency according to applicable GMP/GDP expectations, product/distribution complexity, prior performance, and company risk governance.

## 13. Case-routing examples

### Example A - China wrong-strength product distributed

Facts: labeled 5 mg product contains 10 mg tablets; multiple provinces distributed.

Route:

- immediate stop sale/use and distribution containment;
- MAH investigation and health-risk assessment;
- assess Level I/II recall according to plausible clinical harm; do not assign level by defect name alone;
- once recall decision is made, apply the 1/3/7-day notice/filing clock according to the final recall level;
- publish recall information; Level I/II also use provincial regulator website route;
- report progress at required frequency;
- reconcile stock, assess adverse events in parallel, investigate mix-up root cause;
- submit completion/disposition report within 10 working days after completion;
- PQR/CAPA/change-control feedback.

### Example B - US NDA product fails release specification after distribution

Facts: distributed batch later confirmed OOS against application specification.

Route:

- immediate product/lot risk assessment and stop-ship;
- assess FAR under 21 CFR 314.81(b)(1) independently of recall;
- assess firm-initiated recall under Part 7 and notify FDA immediately if removing/correcting because firm believes product violative;
- provide product/distribution/risk/communication/strategy package;
- do not wait for FDA classification to begin protective action;
- FDA assigns recall Class I/II/III;
- conduct recall communications/effectiveness checks/status reports;
- seek FDA termination when criteria met;
- complete 211.192 investigation/CAPA and annual-review feedback.

### Example C - EU centrally authorised sterile product with contamination signal

Facts: sterility/contamination concern in distributed batches across several Member States.

Route:

- immediate containment and patient-risk assessment;
- notify EMA through current quality-defect route and relevant authorities; do not wait for final root cause where recall/market action may be needed;
- use 2026 Union quality-defect risk/classification procedure and Rapid Alert Network route where serious cross-border risk warrants it;
- if products have reached patients and serious public-health risk criteria are met, Article 117a urgent public-announcement requirements become relevant;
- provide interim/final investigation and health-hazard information per EMA CAP instructions;
- coordinate recall depth/countries, reconcile product, complete CAPA, and close with the applicable authority route.

### Example D - US warehouse-only stock recovery

Facts: mislabeled units discovered before any portion of affected lot left direct company control.

Route:

- confirm distribution status and direct control;
- apply 21 CFR 7.3 definition of stock recovery rather than automatically calling it a recall;
- still investigate the CGMP deviation and assess whether any other lot entered distribution;
- assess FAR or other reporting only if the separate trigger is met.

## 14. SOP/SMP drafting checklist

A globally usable recall SOP should include:

- definitions by jurisdiction;
- legal roles and market-specific appendices;
- 24/7 escalation;
- initial containment authority;
- health-hazard/risk assessment method;
- classification rules and authority ownership;
- recall decision approval;
- market/country scope assessment;
- distribution-data retrieval;
- recall strategy/depth;
- regulator communication and clocks;
- consignee/public/patient communication;
- returned-product controls;
- effectiveness checks;
- quantity reconciliation;
- status/progress reports;
- final report/termination;
- investigation/CAPA/change/PQR link;
- mock recall/readiness testing;
- records and retention;
- contract-manufacturer/distributor/logistics interfaces;
- foreign-recall assessment;
- shortage/continuity assessment;
- PV/FAR/BPDR/quality-defect-reporting parallel routes.

For a controlled procedure, place jurisdiction-specific legal clocks in a controlled appendix or regulatory matrix that can be updated without rewriting the entire procedural sequence, unless the company's document hierarchy requires otherwise.
