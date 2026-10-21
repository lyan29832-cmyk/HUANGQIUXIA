# QRM lifecycle application map - ICH Q9(R1) Annex II routing

## Purpose

Use this file after [quality-risk-management.md](quality-risk-management.md) when the task asks where QRM applies across the pharmaceutical lifecycle or how to route a concrete risk question to the correct quality-system domain.

The nine domains below follow ICH Q9(R1) Annex II. Annex II provides **illustrative, non-exhaustive applications**; it is not a separate list of mandatory procedures and does not replace the applicable GMP, dossier, pharmacovigilance or jurisdiction-specific requirement.

## Annex II domains and skill routing

| ICH Q9(R1) Annex II domain | Typical company questions | Load with QRM | Key QRM focus |
| --- | --- | --- | --- |
| **II.1 Integrated Quality Management** | Deviations, CAPA, change control, quality defects, complaints, recalls, internal audits, training, document systems, management review, periodic product review | [gmp-quality-workflows.md](gmp-quality-workflows.md); task-specific complaint/recall/change references | Risk-based investigation depth, CAPA priority, change impact, audit frequency, residual risk, risk review and management escalation. |
| **II.2 Regulatory Operations** | Submission/review risk, inspection planning/readiness, regulatory commitments, filing strategy supported by science/risk | [regulatory-evidence.md](regulatory-evidence.md); jurisdiction-specific source map | QRM may support prioritisation and evidence evaluation but cannot replace legal filing categories, inspections, approvals or authority communications. |
| **II.3 Development** | QTPP/CQAs/CPPs, formulation/process development, scale-up, comparability, control strategy, analytical development, clinical/registration CMC decisions | [rd-cmc-laboratory-quality-and-data-integrity.md](rd-cmc-laboratory-quality-and-data-integrity.md); [technology-transfer-and-process-validation.md](technology-transfer-and-process-validation.md); [qrm-ich-quality-guideline-interface-map.md](qrm-ich-quality-guideline-interface-map.md) | Use prior knowledge and development evidence to identify hazards/uncertainty and focus experiments. Do not use a risk score to substitute for necessary development data. |
| **II.4 Facilities, Equipment and Utilities** | Facility/equipment selection, qualification, utilities, maintenance, aging equipment, cleaning, contamination/cross-contamination, automation/computerised systems | [gmp-quality-workflows.md](gmp-quality-workflows.md); applicable PIC/S/EU/EAEU/China GMP source | Failure pathways, patient/product consequence, prevention versus detection, qualification/maintenance evidence, change impact and lifecycle review. |
| **II.5 Materials Management** | Supplier qualification, raw/packaging material controls, starting-material criticality, sourcing changes, sampling/testing, storage/transport | [gmp-quality-workflows.md](gmp-quality-workflows.md); [mah-holder-risk-management-regulatory-map.md](mah-holder-risk-management-regulatory-map.md); hold-time map when relevant | Supplier/material criticality, variability, detectability limits, outsourced oversight, supply continuity and change triggers. |
| **II.6 Production** | Process risk, IPCs, batch deviations, process parameters, hold time, process validation, CPV, rework/reprocessing, batch disposition support | [technology-transfer-and-process-validation.md](technology-transfer-and-process-validation.md); [process-validation-case-patterns.md](process-validation-case-patterns.md); hold-time references | State of control, failure modes, severity/probability, control effectiveness, process capability, residual risk and review using manufacturing experience. |
| **II.7 Laboratory Control and Stability Studies** | Method development/validation, OOS/OOT, reference standards, stability, sampling, laboratory controls, analytical lifecycle, data integrity | [rd-cmc-laboratory-quality-and-data-integrity.md](rd-cmc-laboratory-quality-and-data-integrity.md); [gmp-quality-workflows.md](gmp-quality-workflows.md); [qrm-ich-quality-guideline-interface-map.md](qrm-ich-quality-guideline-interface-map.md) | Analytical-procedure risk, representativeness, data quality, method performance, uncertainty, stability trends, OOS/OOT impact and risk review. |
| **II.8 Packaging and Labeling** | Printed component mix-ups, label issuance/reconciliation, pack design, line clearance, container/closure changes, packaging process controls | [gmp-quality-workflows.md](gmp-quality-workflows.md); jurisdictional GMP source | Patient consequence of mix-up/mislabeling, prevention hierarchy, line/vision controls, supplier/printed-material risk, change and complaint feedback. |
| **II.9 Supply Chain Control** | Contract manufacture/testing, supplier networks, transport/distribution, single-source risk, shortages, outsourced activities, supply reliability | [mah-holder-risk-management-regulatory-map.md](mah-holder-risk-management-regulatory-map.md); [qrm-jurisdictional-regulatory-map.md](qrm-jurisdictional-regulatory-map.md); complaint/recall map as applicable | Product-availability patient risk, supplier/service variability, quality agreements, oversight intensity, resilience, continuity and risk-based monitoring. |

## Lifecycle-stage overlay

Use the Annex II domain together with lifecycle stage; the same hazard can require a different evidence standard or decision route at different stages.

| Stage | Typical QRM emphasis |
| --- | --- |
| Discovery / early CMC | Knowledge gaps, preliminary hazards, platform knowledge, material/process uncertainty; often iterative and lower-data. |
| IND/CTA and clinical development | Patient protection, clinical-supply robustness, phase-appropriate controls, comparability/change impact, knowledge generation. |
| Technology transfer / scale-up | Transfer of product/process knowledge, receiving-unit capability, scale effects, equipment/site differences, control strategy and validation readiness. |
| Registration / late development | Commercial process maturity, validation strategy, dossier commitments, residual uncertainty, launch and supply reliability. |
| Commercial manufacture | State of control, deviations/CAPA, PQR/APR, CPV, complaints/recalls, supplier/outsourcing performance, changes and availability risks. |
| Discontinuation / site exit | Product continuity, retained samples/records, stability commitments, transfer/closure risks, regulatory commitments and knowledge retention. |

## Cross-domain questions

Do not force a complex problem into one Annex II category. Common combinations include:
- technology transfer = Development + Facilities/Equipment + Production + Laboratory Control;
- contract manufacture = Integrated Quality Management + Production + Supply Chain Control;
- supplier change = Materials Management + Supply Chain Control + Regulatory Operations;
- new analytical method = Development + Laboratory Control + Regulatory Operations;
- facility/equipment change = Facilities/Equipment + Production + Integrated Quality Management + Regulatory Operations;
- product shortage from manufacturing reliability = Production + Supply Chain Control + Product Availability risk;
- complaint/recall = Integrated Quality Management + Production/Laboratory/Supply Chain domains according to root cause.

## Application rule

For a substantive QRM task:
1. identify the Annex II domain(s);
2. identify lifecycle stage;
3. identify jurisdiction and product scope;
4. load the QRM core plus the relevant domain reference(s);
5. define the decision/risk question before selecting a tool;
6. keep Q9 examples separate from binding jurisdiction-specific requirements.
