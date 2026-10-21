# Complaint decision matrices and operating controls

**Targeted complaint review, 2026-10-08:** Read [complaint-translation-and-content-review.md](complaint-translation-and-content-review.md) for translation plus content review, source-by-source currentness, China urgent safety routes, PIC/S/EAEU scope and FDA contractor-aware FAR day 0. Earlier verification dates below are historical.

## Table of contents

1. Purpose and regulatory boundary
2. Complaint taxonomy and first-pass classification
3. Immediate triage gates
4. Internal risk-severity model
5. Investigation-depth model
6. Regulatory clock and escalation matrix
7. MAH / product owner / contract manufacturer operating model
8. Investigation evidence matrix
9. Complaint-sample and retain-sample controls
10. Root cause, CAPA, and closure gates
11. Trending, signals, and management review
12. SOP/SMP design controls
13. Audit and inspection readiness questions
14. Worked routing examples
15. Current-source checkpoints

## 1. Purpose and regulatory boundary

Use this reference after [complaints-quality-defects-and-recalls.md](complaints-quality-defects-and-recalls.md) when the task requires an operational decision, procedure design, case triage, complaint classification, investigation-depth decision, regulatory-reporting assessment, market-action assessment, or MAH/contract-manufacturing responsibility analysis.

This file deliberately separates three layers:

- `Regulatory requirement`: a duty, trigger, timeline, record, or responsibility traceable to current applicable law, regulation, GMP/GDP/GVP requirement, or competent-authority procedure.
- `Regulatory interpretation`: application of that requirement to the facts and scope.
- `Professional operating model`: a company control proposed to make the system executable. Internal classifications, target times, decision gates, matrices, and KPIs in this file are not automatically legal requirements.

Do not equate an internal complaint severity rating with a statutory or regulatory recall classification. In particular:

- an internal `Critical / Major / Minor` complaint model is not the same as China's Level I / II / III recall classification;
- it is not the same as FDA Class I / II / III recall classification;
- it is not the same as any EU competent-authority quality-defect or rapid-alert classification.

Apply the jurisdiction-specific classification only when its legal/regulatory criteria are met and the applicable current source has been checked.

## 2. Complaint taxonomy and first-pass classification

Classify the incoming communication by all applicable pathways; a single complaint may belong to multiple pathways.

| Pathway | Typical signal | Required routing question |
| --- | --- | --- |
| Product Quality Complaint (PQC) | identity, strength, quality, purity, appearance, contamination, deterioration, packaging, labeling, performance, specification, integrity | Could this represent a product quality defect or a failure to meet approved/registered/specification requirements? |
| Safety / pharmacovigilance | adverse reaction, serious event, medically important event, exposure, medication error, lack of efficacy where reportable | Does the information meet the applicable safety-intake/reporting criteria? Route to PV without waiting for quality investigation completion. |
| Distribution / logistics | temperature excursion, damaged shipment, delay, mishandling, incorrect storage, delivery issue | Is the issue only service-related, or could it have affected product quality, traceability, or patient safety? |
| Falsification / tampering | suspected counterfeit, altered packaging, unknown supply chain, seal tampering, abnormal coding | Is there a credible falsification or tampering concern requiring immediate escalation to quality, regulatory/security, and competent authorities as applicable? |
| Labeling / mix-up | wrong product, wrong strength, wrong label, wrong leaflet, carton/blister mismatch | Does the event trigger a market-quality notification, FAR, recall, or immediate patient-protection action? |
| Medical information / use question | expected use, administration, compatibility, general information | Is there embedded quality or safety information that must be captured before routing as a medical-information request? |
| Service / commercial | pricing, availability, delivery communication, customer service | Is there any product-quality, safety, supply-integrity, or regulatory signal hidden in the complaint? |
| Mixed | more than one of the above | Open parallel workstreams with one master complaint record and linked quality/PV/regulatory/recall records. |

Do not use `invalid complaint` merely because a retain sample passes testing or the event cannot be reproduced. Distinguish:

- `complaint received and documented`;
- `complaint allegation substantiated / not substantiated / indeterminate`;
- `quality defect confirmed / not confirmed / cannot be excluded`;
- `root cause confirmed / probable / not established`.

These are different conclusions and should not be collapsed into one field.

## 3. Immediate triage gates

Apply the following gates as soon as the complaint is received. Record date/time of receipt and escalation because regulatory clocks can begin before the investigation is complete.

### Gate 0 - Identity and traceability

Capture, where available:

- product name, strength, dosage form, pack, presentation;
- batch/lot and expiry;
- market/country and authorization route;
- complainant/source and date/time received;
- purchase/distribution channel;
- complaint description in the complainant's own words;
- sample, photo, video, packaging, shipping container, or device availability;
- patient exposure and current product disposition.

A missing batch number does not by itself justify closing or refusing the complaint. Document attempts to establish traceability and assess whether the allegation still creates a market-wide or product-wide signal.

### Gate 1 - Patient and public-health protection

Ask immediately:

1. Has death, life-threatening injury, hospitalization, permanent impairment, medically significant harm, or another serious outcome been alleged?
2. Could the alleged defect plausibly cause serious harm even if no harm has yet occurred?
3. Does the patient still possess or use the suspect product?
4. Is immediate medical advice, stop-use communication, quarantine, stop-ship, or other interim risk control needed?

Quality and medical/PV teams may need to act in parallel. Do not make medical causality conclusions from the quality investigation alone.

### Gate 2 - High-concern quality signals

Escalate without waiting for routine complaint review when the allegation credibly involves, as applicable:

- wrong product, wrong strength, wrong label, or product/label mix-up;
- microbial or other contamination, especially for sterile/high-risk products;
- foreign matter with plausible patient risk;
- significant deterioration, abnormal odor/color/physical change with possible quality impact;
- specification failure in distributed product;
- tampering, falsification, counterfeit, or supply-chain integrity concern;
- critical container-closure failure;
- repeated similar complaints suggesting systemic or multi-batch failure;
- defect affecting multiple countries/markets;
- quality defect associated with a serious adverse event;
- defect that may require recall, market restriction, or urgent authority communication.

These examples are escalation signals, not a universal regulatory definition of `critical complaint`.

### Gate 3 - External regulatory clock

Assess on receipt and re-assess when new facts emerge:

- China: pharmacovigilance reporting; quality/safety risk control; recall triggers and recall-process timelines; other applicable NMPA/provincial reporting.
- United States: 21 CFR 314.81(b)(1) FAR; 21 CFR 314.80 or 600.80 safety reporting; 21 CFR 600.14 BPDR where applicable; recall/other product-specific requirements.
- European Union: suspected quality-defect notification to the appropriate authority/EMA route; pharmacovigilance ICSR reporting; recall/rapid-alert and national requirements.

Do not use the company's complaint closure target as the start or end point for a statutory reporting clock.

### Gate 4 - Scope and containment

Determine whether to:

- quarantine stock;
- pause distribution or shipment;
- place related batches/products on hold;
- preserve complaint and retain/reference samples;
- protect electronic and paper evidence;
- notify contract manufacturer, testing laboratory, logistics provider, distributor, or supplier;
- broaden the assessment to related batches, products, components, sites, markets, or time periods.

### Gate 5 - Governance and decision authority

Identify who owns each decision:

- complaint record ownership;
- quality investigation;
- PV case handling;
- regulatory assessment/submission;
- market action / recall decision;
- customer/healthcare communication;
- CAPA and effectiveness verification;
- complaint closure.

A quality agreement can allocate execution, but cannot remove statutory responsibilities that remain with the regulated entity.

## 4. Internal risk-severity model

Use this only as a professional company model when the user needs an internal complaint classification. Do not present these definitions as China, FDA, or EU statutory categories.

### 4.1 Critical - internal model

Consider `Critical` when credible available information indicates a defect could result in death, life-threatening harm, serious or irreversible health consequences, or another high-consequence public-health risk; or when the issue represents an extreme product-identity/integrity failure requiring immediate senior escalation.

Illustrative signals may include wrong product/strength, serious labeling mix-up, high-risk contamination, major sterility assurance failure, potent cross-contamination, or falsification with patient exposure. Product type, route, population, dose, detectability, and actual exposure must be considered.

Default operating response:

- immediate Quality Head / designated senior quality escalation;
- immediate PV and Regulatory Affairs screening;
- same-cycle assessment of external reporting and market action;
- urgent containment;
- full/systemic investigation unless a stricter or different regulatory path applies.

### 4.2 Major - internal model

Consider `Major` when the defect could cause clinically meaningful but generally non-catastrophic harm, significant loss of intended quality/performance, substantial compliance concern, or a material risk of recurrence or market impact.

Illustrative signals may include clinically meaningful potency/performance concern, significant packaging-integrity failure, recurring tablet/coating defect with quality implication, material transport excursion, or a labeling/packaging defect with meaningful use risk.

Default operating response:

- prompt quality investigation;
- PV/regulatory screening;
- related-batch and trend review;
- documented market-action assessment;
- CAPA as supported by root/contributing causes.

### 4.3 Minor - internal model

Consider `Minor` when available evidence indicates no meaningful impact on identity, strength, quality, purity, safety, efficacy/performance, traceability, or correct use, and no meaningful systemic/recurrence signal is present.

Examples may include cosmetic or service issues with demonstrated absence of product-quality impact. Do not classify as Minor solely because no injury occurred.

### 4.4 Mandatory safeguards for internal classification

- Severity must be based on potential consequence as well as actual outcome.
- Low frequency does not automatically mean low severity.
- A single complaint can be Critical.
- A recurring Minor complaint can become a significant systemic signal.
- Classification must be revisited when new evidence emerges.
- Classification cannot cancel a separate FAR, PV, BPDR, quality-defect notification, or recall trigger.

## 5. Investigation-depth model

Use the following three-level model as a professional operating framework. It is not itself a regulatory classification.

### Level A - screening / documented assessment

Appropriate only when the applicable regulation permits it and the available evidence supports a limited assessment. Typical elements:

- complaint data and traceability review;
- batch release/specification review as relevant;
- recent similar-complaint/trend check;
- PV/regulatory/recall screening;
- documented rationale for no further investigation, if legally permissible;
- responsible reviewer/approver.

Do not use Level A for convenience or because the complaint sample is unavailable.

### Level B - focused investigation

Use when a plausible quality issue requires targeted evidence but available facts do not indicate a broader systemic failure. Typical elements:

- batch manufacturing/packaging/testing records relevant to allegation;
- deviations, OOS/OOT, changes, maintenance, line clearance, reconciliation, and release data as applicable;
- complaint sample and/or retain/reference sample examination where scientifically useful;
- storage/distribution evidence;
- comparison with historical complaints/trends;
- supplier/component review as indicated;
- root/contributing cause assessment;
- impact on related batches/products/markets;
- CAPA and effectiveness plan where needed.

### Level C - full / systemic investigation

Use when risk, recurrence, distributed-product status, regulatory trigger, or systemic evidence warrants broad investigation. Typical drivers include:

- serious/high-consequence patient risk;
- credible wrong product/strength/label or significant contamination;
- distributed batch failing specification;
- FAR/BPDR/serious quality-defect notification or recall assessment;
- recurring or clustered complaints;
- multi-batch/product/site/market signal;
- data-integrity or falsification concern;
- failure of a prior CAPA;
- evidence that the cause may lie in a shared process, supplier, system, utility, equipment train, or distribution network.

Typical additional work:

- cross-batch/product/site/market scope extension;
- structured chronology;
- cross-functional investigation team;
- process/equipment/supplier/distribution data reconstruction;
- statistical/trend analysis where useful;
- formal health-hazard/quality-risk assessment;
- interim and final regulatory updates as required;
- executive/management review;
- CAPA effectiveness and recurrence monitoring.

## 6. Regulatory clock and escalation matrix

Always revalidate the current official source before placing a mandatory number in a controlled SOP. The values below are routing checkpoints verified for this package on 2026-09-18, not a perpetual currentness guarantee.

### 6.1 China

| Trigger | Routing checkpoint | Clock / control |
| --- | --- | --- |
| Serious suspected adverse reaction / valid report within China PV scope | Current China GVP | Report as soon as possible and no later than 15 days from knowledge/receipt as applicable under the current rule. Verify case validity and route. |
| Non-serious suspected adverse reaction / valid report within China PV scope | Current China GVP | No later than 30 days under the current rule. Verify case validity and route. |
| Foreign regulatory action because of adverse reaction, where current GVP trigger applies | Current China GVP | Assess the 24-hour reporting requirement in the current rule; verify exact trigger and recipient before controlled use. |
| Death case under Order 81 | Articles 21–22; targeted review 2026-10-08 | Immediate reporting; manufacturer investigation report within 15 days. Map actor and reporting destination; not a routine 15-day intake allowance. |
| Drug group adverse event under Order 81 | Articles 27–29; targeted review 2026-10-08 | Immediate reporting to the specified local bodies; manufacturer investigation report within 7 days; individual case reports also required as applicable. |
| Recall decision under NMPA 2022 No. 92 | China recall measures | Level I: notice/file within 1 day; Level II: 3 days; Level III: 7 days, subject to exact current text. |
| Recall progress | China recall measures | Level I daily; Level II every 3 days; Level III every 7 days. |
| Recall completion | China recall measures | Generally report within 10 working days after completion of recall under the current rule. |
| Quality/safety issue that may require risk control before recall decision | China GMP / MAH responsibility / recall framework | Do not wait for a recall classification to begin investigation, containment, regulator assessment, or PV routing. |

Do not use the 1/3/7-day recall notice periods as complaint investigation timelines.

### 6.2 United States

| Trigger | Regulatory route | Clock / control |
| --- | --- | --- |
| Qualifying distributed NDA/ANDA information | 21 CFR 314.81(b)(1), with 314.98 as applicable | FAR within 3 working days of receipt of the information by the applicant when triggered. Do not wait for completed RCA. |
| Serious and unexpected postmarketing adverse drug experience under applicable NDA/ANDA rule | 21 CFR 314.80 | Submit as soon as possible and no later than 15 calendar days after initial receipt, subject to current applicability. |
| Serious and unexpected postmarketing adverse experience for licensed biologic | 21 CFR 600.80 | Submit as soon as possible and no later than 15 calendar days after initial receipt, subject to current applicability. |
| Qualifying biological product deviation associated with distributed product | 21 CFR 600.14 | Report as soon as possible and no later than 45 calendar days from discovery of information reasonably suggesting a reportable event, subject to rule applicability. |
| Complaint indicating possible specification failure | 21 CFR 211.198 / 211.192 | QCU review and investigation decision; no universal numeric CFR complaint-closure deadline. |
| Recall consideration | 21 CFR Part 7 Subpart C plus product-specific authority | Assess health hazard, classification/strategy, FDA communication, effectiveness and disposition. Do not turn a company target into a statutory clock. |

FDA Final July 2021 FAR Q&A III.3(a) interprets day 0 to include contractor discovery of qualifying information. Internal forwarding does not restart the clock. Use Monday–Friday excluding US Federal holidays; the NDA/ANDA applicant remains responsible. Preserve this distinction from the CFR's applicant-receipt text when citing law versus FDA interpretation.

For 21 CFR 211.198 records, preserve the exact current retention rule: at least one year after expiration or one year after complaint receipt, whichever is longer, with the specific OTC exception in the current text. Recheck exact wording before controlled use.

### 6.3 European Union

| Trigger | Regulatory route | Clock / control |
| --- | --- | --- |
| Suspected product quality defect that could result in market action | EU GMP Chapter 8 + competent-authority route | Notify the competent authority before market action unless urgent action is needed to protect health. Do not wait for defect confirmation or full investigation when the available information and initial risk assessment support reporting. |
| Centrally authorised product quality defect that could result in recall or abnormal restriction on supply | EMA quality-defect route | Notify EMA and applicable authorities through the current route; verify current form/channel and national requirements. |
| Serious valid ICSR | Directive 2001/83/EC Article 107(3) / current GVP Module VI | Submit within 15 days from receipt/knowledge as defined by the applicable framework. |
| Non-serious valid ICSR | Directive 2001/83/EC / current GVP Module VI | Submit within 90 days under the current framework. |
| Recall / urgent market action | EU GMP Chapter 8 + current Union/national procedure | Follow competent-authority coordination, rapid-alert and local requirements; do not invent one EU-wide numeric complaint-closure deadline. |

EMA's current GMP/GDP Q&A states that suspected quality-defect notification should begin when information supports detection of the issue and the initial patient/animal risk assessment indicates it could result in market action; completion of the investigation is not required before reporting.

## 7. MAH / product owner / contract manufacturer operating model

This section is a professional governance model. Confirm legal responsibility separately for each market and authorization type.

### 7.1 Core principle

Use one master complaint record with linked workstreams. The company with marketing/application/license responsibility should maintain end-to-end visibility even when technical investigation work is performed by a contract manufacturer, contract laboratory, distributor, logistics provider, or affiliate.

Do not write a quality agreement so that both parties assume the other will perform the regulatory assessment.

### 7.2 Responsibility interface matrix

| Activity | MAH / applicant / product owner | Contract manufacturer / testing site | PV | Regulatory Affairs | Commercial / customer / distribution interface |
| --- | --- | --- | --- | --- | --- |
| Receive complaint | Ensure all channels feed the controlled complaint system or are forwarded | Forward any complaint received directly and preserve original information/evidence | Receive safety information immediately through defined route | Be informed of potential reportable quality/regulatory issue | Capture original complaint without filtering out quality/safety information |
| Preserve evidence | Ensure traceability and governance | Preserve batch, sample, manufacturing/testing and site evidence | Preserve safety source data | Preserve regulatory correspondence/submission evidence | Preserve customer communications, distribution and return evidence |
| Initial quality triage | Own/oversee product and market impact assessment as applicable | Provide rapid technical assessment and site facts | Determine safety case/reportability path | Determine quality-regulatory notification pathway | Support batch/channel/market traceability |
| Manufacturing investigation | Provide oversight and market context | Lead detailed site investigation for operations performed at site; comply with own GMP duties | Provide safety facts relevant to quality assessment | Advise on registered commitments and notification expectations | Provide distribution/storage/customer facts |
| Related-batch / product scope | Ensure end-to-end scope is not limited to contractor's site view | Assess shared equipment, process, materials, other batches/products at site | Assess safety clustering | Assess multi-market regulatory impact | Assess affected customers, markets and stock |
| External quality reporting | Ensure legally responsible entity makes required submission/notification | Provide information fast enough to meet external clocks; submit only if its legal role requires it | Make/coordinate applicable PV submissions | Coordinate quality/regulatory notifications and authority communication | Do not independently assure customer of regulatory conclusions unless authorized |
| Recall / market action | Lead or coordinate decision and governance when legally responsible; ensure effectiveness | Execute site actions, traceability, technical support and disposition within role | Assess patient-safety implications | Coordinate competent-authority reporting | Execute customer/consignee communication and product recovery as assigned |
| CAPA | Ensure systemic adequacy and cross-party actions | Implement site CAPA for root/contributing causes under site control | Implement PV-system CAPA if needed | Implement regulatory-process CAPA if needed | Implement distribution/customer-process CAPA if needed |
| Closure | Ensure all linked workstreams are reconciled | Provide final investigation evidence | Confirm PV obligations complete | Confirm regulatory obligations/update commitments complete | Confirm customer response/recovery evidence complete |

### 7.3 Quality-agreement controls for complaints

For contract manufacture or contract testing, ensure the quality agreement or equivalent controlled agreement addresses:

- which party can receive complaints and how the original record is preserved;
- forwarding/escalation expectations for routine versus potentially serious complaints;
- immediate escalation of death/serious harm, wrong product/strength/label, contamination, falsification, distributed-specification failure, or potential recall;
- complaint sample/retain/reference sample custody and testing;
- access to batch, laboratory, deviation, change, stability, environmental, maintenance and distribution records as applicable;
- investigation lead and approval/review roles;
- right to request investigation expansion or additional testing with scientific justification;
- FAR/BPDR/PV/EU quality-defect/China recall assessment information exchange;
- authority communication and who submits what;
- market-action and recall execution support;
- CAPA, effectiveness, trend and PQR/APR information exchange;
- data-integrity, confidentiality and record-retention expectations;
- escalation when parties disagree about root cause, reportability, severity, or recall need.

Do not assume a contract can shift away a manufacturer's own CGMP obligations or an MAH/applicant/license holder's statutory obligations.

## 8. Investigation evidence matrix

Tailor the evidence to the allegation. Do not mechanically test everything.

| Complaint type | Key evidence to consider | Common scope-extension questions |
| --- | --- | --- |
| Wrong product / wrong strength / mix-up | line clearance, component issuance, reconciliation, vision/inspection, label controls, batch/packaging records, retain samples, returned sample, other products on line | Were adjacent products/strengths/batches packed on same line/time window? Any reconciliation discrepancy? |
| Tablet/capsule appearance, breakage, chipping | complaint sample, retains, IPC, compression/encapsulation/coating parameters, hardness/friability/moisture, equipment setup, packaging protection, transport | Similar trend by lot/equipment/market? Could shipping damage explain but not exclude manufacturing contribution? |
| Color/odor/physical change | sample/retains, stability, impurities/degradation, moisture/light/temperature exposure, packaging integrity, raw materials | Is deterioration plausible across distribution, shelf life, market climate, or affected component lots? |
| Foreign matter / contamination | sample identification, microscopy/chemistry/microbiology as appropriate, environmental/cleaning data, line/equipment inspection, raw materials, packaging components, pest controls | Could same source affect other batches/products/equipment? Is contamination intrinsic or post-opening? |
| Microbial concern | sample integrity, retain/reference testing, environmental monitoring, water/utilities, bioburden/sterility controls, cleaning/sanitation, container closure | Could other batches or shared utilities/areas be affected? |
| Missing/extra units / fill count | packaging records, counters/checkweighers, reconciliation, reject logs, equipment alarms, complaint pack | Is the issue isolated to handling or systematic counter/reconciliation failure? |
| Blister/bottle seal or closure failure | package integrity, leak/torque/seal data, packaging parameters, components, maintenance, transport | Could moisture/oxygen/contamination affect product quality? Other batches/components? |
| Label/carton/leaflet defect | approved artwork, issuance, reconciliation, line clearance, print/vision systems, master data, change control | Could the defect cause wrong use? Is there mix-up across products/markets/languages? |
| Assay/dissolution/specification concern | complaint sample suitability, retain/reference sample, release/stability data, method performance, manufacturing parameters, OOS/OOT, changes | Distributed batch FAR/quality-defect trigger? Other lots/product strengths? Stability trend? |
| Temperature/storage excursion | logger evidence, lane qualification, excursion duration/range, stability knowledge, packaging, distribution records | Other shipments/consignees affected? Does approved stability support continued quality? |
| Suspected counterfeit/tampering | coding/serialization, packaging security, supply chain, distributor/source, sample authenticity, law-enforcement/security evidence | Broader market/channel exposure? Need authority/MAH/anti-falsification escalation? |

For complaint-sample testing, define the question before testing. Testing should generate evidence, not create an appearance of investigation completeness.

## 9. Complaint-sample and retain-sample controls

### 9.1 Complaint sample

Document:

- chain of custody and condition on receipt;
- whether package has been opened/used/altered;
- storage/transport conditions after complaint event if known;
- photo and unique identification;
- requested examination/testing and scientific rationale;
- sample quantity limitations;
- destructive versus nondestructive testing sequence;
- reserve quantity where feasible;
- final disposition.

Do not assume a consumer-returned sample remains representative of the released batch after uncontrolled storage or use.

### 9.2 Retain/reference sample

Use retain/reference samples to answer defined hypotheses, not as the sole basis for rejecting the complaint. A passing retain sample can support evidence that the retained unit meets tested attributes; it does not prove that every distributed unit was defect-free or that no distribution/packaging/event-specific failure occurred.

### 9.3 Testing strategy

Avoid `test until pass` behavior. Predetermine, as far as practicable:

- test purpose;
- sample identity and representativeness;
- methods and acceptance criteria;
- replicate rationale;
- comparison population;
- handling of atypical/OOS/OOT results;
- decision rule for additional testing.

## 10. Root cause, CAPA, and closure gates

### 10.1 Root-cause standard

Use evidence to distinguish:

- direct cause;
- root/system cause;
- contributing factors;
- unconfirmed hypotheses.

Do not close as `operator error` without explaining the mechanism and why the system allowed or failed to detect the error.

If root cause is not established, state that clearly. Do not create a false definitive cause merely to close the complaint. Define risk controls and enhanced monitoring proportionate to the residual uncertainty.

### 10.2 CAPA decision

CAPA is not automatically required for every complaint, but the decision must be defensible. Consider:

- confirmed or probable root cause;
- severity/patient risk;
- recurrence and trend;
- systemic scope;
- detectability;
- prior similar CAPA;
- regulatory commitment;
- supplier/contractor/system weakness.

Separate:

- correction / immediate remediation;
- corrective action against cause;
- preventive/systemic action where justified;
- market action / recall, which is not merely a CAPA.

### 10.3 Closure gates

Do not close a complaint until, as applicable:

1. allegation and evidence are adequately documented;
2. investigation or no-investigation rationale is approved under the applicable rule;
3. related-batch/product/market scope is resolved;
4. PV case/reporting obligations are reconciled;
5. FAR/BPDR/quality-defect/other regulatory obligations are reconciled;
6. recall/market-action assessment is documented and updated with final facts;
7. root/contributing cause conclusion is evidence-based or uncertainty is explicitly documented;
8. CAPA/other actions are assigned and closure state is governed;
9. complainant/customer response is handled as required;
10. trend coding is complete and suitable for periodic review;
11. linked records and authority correspondence are cross-referenced.

Complaint record closure can be administratively separated from long-term CAPA effectiveness completion if the company's procedure defines the linkage and no regulatory obligation is obscured. Do not mark CAPA effective before the predefined effectiveness evidence exists.

## 11. Trending, signals, and management review

Use normalized and contextual trends rather than raw counts alone. The following are professional PQS metrics, not universal regulatory thresholds:

- complaints per million units/packs/batches distributed, where denominator is meaningful;
- product/strength/presentation/market trend;
- complaint category and defect mode;
- internal severity distribution;
- confirmed / probable / not substantiated / indeterminate outcomes;
- recurrence by root/contributing cause;
- batch/site/equipment/supplier/component clustering;
- complaints associated with adverse events;
- complaints triggering FAR/BPDR/quality-defect notification/recall;
- time to initial triage, investigation, customer response, and closure;
- external reporting timeliness;
- overdue investigations and CAPA;
- repeat complaint after CAPA;
- complaint sample return rate and evidence adequacy.

Do not use a fixed statistical signal threshold without considering product risk, distribution volume, clinical consequence, detectability, reporting behavior, and historical baseline.

Escalate meaningful signals into PQR/APR, management review, QRM, supplier oversight, validation/CPV, change control, and regulatory strategy as appropriate.

## 12. SOP/SMP design controls

A robust complaint procedure should define at least:

1. purpose and scope;
2. definitions and distinctions among complaint, PQC, quality defect, adverse event, falsification, distribution complaint, and recall;
3. complaint channels and receipt timestamp;
4. required minimum intake data and handling of incomplete information;
5. original-information preservation and data integrity;
6. immediate triage and high-concern escalation;
7. internal classification model, if used, with explicit statement that it is not regulatory recall classification;
8. PV screening and forwarding;
9. market-by-market regulatory-reporting assessment;
10. investigation/no-investigation criteria;
11. investigation-depth and scope-extension rules;
12. complaint/retain/reference sample controls;
13. root-cause and CAPA requirements;
14. recall/market-action interface;
15. MAH/contract manufacturer/distributor responsibilities;
16. external and internal communication controls;
17. complainant response requirements;
18. trend review and PQR/APR feed;
19. record retention;
20. closure criteria and reopened-complaint process;
21. periodic effectiveness review of the complaint system;
22. forms/templates and controlled decision records.

Do not set one global internal target if it would make shorter jurisdictional clocks invisible. Use explicit escalation timers or a regulatory-clock field in the complaint record.

## 13. Audit and inspection readiness questions

Use these questions to test whether the system works in practice:

- Can every complaint channel, including calls, email, sales, medical, distributors, social/customer-service routes where applicable, enter the controlled process?
- Can staff identify and timestamp safety information immediately?
- Can the organization demonstrate that FAR assessment occurs within the 3-working-day US window when applicable?
- Can the organization demonstrate that EU suspected quality-defect reporting is considered before market action and without waiting for final RCA?
- Can the organization distinguish China complaint handling from China recall classification and recall-process timing?
- Can the MAH obtain contractor records fast enough to make its own regulatory decisions?
- Are contractor complaint-forwarding obligations tested, not only written in the quality agreement?
- Are related batches/products assessed when the cause could be shared?
- Are complaint samples handled with chain-of-custody and representativeness limitations documented?
- Are `not substantiated` complaints still trended?
- Do repeat complaints trigger escalation even when each individual complaint was initially classified low risk?
- Are PV, regulatory, recall, deviation, CAPA, and change-control records cross-linked?
- Can management see overdue external reporting decisions separately from overdue investigation completion?
- Can the company prove that recall/market-action decisions were updated as new evidence emerged?

## 14. Worked routing examples

These examples are hypothetical and illustrate process routing only. They are not legal conclusions for a real product.

### Example A - US NDA tablet: distributed batch later fails dissolution

Facts: A marketed NDA tablet complaint alleges lack of effect. During the complaint investigation, a distributed batch is found to fail an application specification for dissolution.

Route:

1. Preserve complaint and safety information; route lack-of-effect information to PV if it meets the applicable safety/reporting criteria.
2. Open/expand the quality investigation under 21 CFR 211.198 / 211.192.
3. Assess FAR immediately because a distributed batch failing an application specification is within the 21 CFR 314.81(b)(1) route; the 3-working-day clock is not postponed until root cause is known.
4. Assess related batches/products and market distribution.
5. Perform health-hazard/recall assessment under applicable FDA framework.
6. Reconcile PV, FAR, recall, investigation and CAPA before final complaint closure.

### Example B - China tablet: wrong strength alleged with serious adverse event

Facts: A patient reports that tablets in a pack appear to be a different strength and reports a serious clinical event.

Route:

1. Escalate immediately as a potential high-concern quality defect and safety case.
2. Route safety information to PV without waiting for quality confirmation; apply current China GVP reporting clock if the report is valid/reportable.
3. Secure sample/photos/packaging and distribution traceability.
4. Investigate packaging line clearance, component issuance/reconciliation, vision systems, artwork, batch records and adjacent products/strengths.
5. Assess other batches/products and immediately evaluate risk-control/recall need.
6. If recall is decided, apply the current Level I/II/III recall criteria and corresponding 1/3/7-day process timelines; do not use internal complaint severity as the recall classification.

### Example C - EU centrally authorised product: packaging mix-up signal

Facts: A complaint provides credible photos showing a carton/blister mismatch that could lead to incorrect use. Investigation is not yet complete.

Route:

1. Escalate as suspected quality defect and perform immediate patient-risk assessment.
2. If the available information and initial risk indicate that market action could be required, notify the applicable competent authorities and EMA route without waiting for full investigation; coordinate market action before implementation unless urgent patient protection requires immediate action.
3. Route any associated adverse reaction to PV and assess ICSR reporting independently.
4. Extend investigation to line clearance, reconciliation, artwork/master data, other products/strengths/markets and adjacent packaging operations.
5. Reassess recall/market action and authority updates as evidence develops.

### Example D - Complaint sample passes; allegation cannot be reproduced

Facts: Consumer reports chipped tablets. Returned sample is partially used; retain samples pass appearance/friability testing.

Route:

1. Do not automatically label the complaint invalid.
2. Assess sample representativeness and post-distribution handling.
3. Review manufacturing/packaging IPC, transport protection, similar complaints, equipment and lot history.
4. Conclude separately whether the allegation is substantiated, whether a product defect is confirmed, and whether root cause is established.
5. Trend the complaint even if no defect is confirmed.

## 15. Current-source checkpoints

Reopen current sources before controlled use of exact reporting obligations.

### China

- China GMP (2010 Revision) official/government checkpoint: `https://www.beijing.gov.cn/zhengce/zhengcefagui/qtwj/201102/t20110212_781359.html`
- Drug Recall Administrative Measures, NMPA Announcement No. 92 of 2022: `https://www.nmpa.gov.cn/xxgk/fgwj/xzhgfxwj/20221026164304199.html`
- Good Pharmacovigilance Practice, NMPA Announcement No. 65 of 2021 government checkpoint: `https://www.beijing.gov.cn/zhengce/zhengcefagui/qtwj/202204/t20220407_2656162.html`
- China GSP current SAMR text: `https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/bgt/art/2023/art_bc07ffdb7a1c4e46be371ac5a4a65f9c.html`
- NMPA MAH primary-responsibility framework: verify current NMPA text for Announcement No. 126 of 2022 and later applicable amendments/notices.

### United States

- eCFR Title 21 current index: `https://www.ecfr.gov/current/title-21`
- 21 CFR 211.198: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-J/section-211.198`
- 21 CFR 211.192: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211/subpart-J/section-211.192`
- 21 CFR 314.81: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-D/part-314/subpart-B/section-314.81`
- 21 CFR 314.80: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-D/part-314/subpart-B/section-314.80`
- 21 CFR 600.80: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-F/part-600/subpart-D/section-600.80`
- 21 CFR 600.14: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-F/part-600/subpart-B/section-600.14`
- 21 CFR Part 7 Subpart C: `https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-7/subpart-C`
- FDA Field Alert Reports: `https://www.fda.gov/drugs/surveillance/field-alert-reports`
- FDA Contract Manufacturing Arrangements for Drugs: Quality Agreements (final guidance, Nov 2016): `https://www.fda.gov/regulatory-information/search-fda-guidance-documents/contract-manufacturing-arrangements-drugs-quality-agreements-guidance-industry`
- FDA Q7 GMP Guidance for APIs: `https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q7-good-manufacturing-practice-guidance-active-pharmaceutical-ingredients-guidance-industry`

### European Union

- EudraLex Volume 4 current index: `https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en`
- EMA GMP/GDP Q&A, Chapter 8 quality-defect reporting: `https://www.ema.europa.eu/en/human-regulatory-overview/research-development/compliance-research-development/good-manufacturing-practice/guidance-good-manufacturing-practice-good-distribution-practice-questions-answers`
- EMA Quality defects and recalls: `https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/compliance-post-authorisation/quality-defects-recalls`
- EMA Compilation of Union Procedures: `https://www.ema.europa.eu/en/human-regulatory-overview/research-development/compliance-research-development/good-manufacturing-practice/compilation-union-procedures-inspections-exchange-information`
- Directive 2001/83/EC current consolidated EUR-Lex record, especially Article 107 for PV reporting and Articles relevant to quality defects/market actions.
- EMA GVP current index and Module VI: `https://www.ema.europa.eu/en/human-regulatory-overview/post-authorisation/pharmacovigilance-post-authorisation/good-pharmacovigilance-practices-gvp`

At the 2026-09-18 checkpoint, EMA's GVP page continued to list Module VI Rev. 2 while also noting ongoing GVP updates following newer EU pharmacovigilance implementing changes. Revalidate before controlled use of detailed PV procedures.
