# Intermediate and bulk product hold-time study framework

## Contents

- Purpose and evidence-status guardrail
- Required inputs and hold-point inventory
- Risk assessment model
- Study strategy selection
- Batch/scale and time-point design
- Attribute, container and storage design
- Cross-site transfer, excursions and cumulative holds
- Acceptance/conclusion logic
- Exceeded hold-time investigation
- SOP/SMP design checklist
- Review output pattern and second-pass QA

## Purpose

Use this file after loading [intermediate-product-hold-time-regulatory-map.md](intermediate-product-hold-time-regulatory-map.md) when the task requires practical study design, protocol/SOP drafting, gap assessment, change-impact assessment, investigation of an exceeded hold, inspection readiness, or review of an existing hold-time validation package.

This file provides professional implementation structure. It does not create acceptance criteria or regulatory obligations beyond the cited jurisdictional sources.

## Evidence-status guardrail

Before designing the study, identify which statements are binding regulation/GMP, regional registration guidance, inspector guidance, company standard, or professional recommendation. In particular, do not use the 2025 ICH Q1 Step 2b/FDA draft as a current implemented requirement; use it only as an emerging harmonization reference until final adoption and applicable regional implementation. WHO TRS 992 Annex 4 can support scientific design but does not override a stricter or more specific market requirement.

## Required inputs

Collect or explicitly mark as unknown:

- product name, dosage form, strength(s), market(s), lifecycle stage;
- process flow and all proposed hold points;
- material state at each hold point;
- routine, target and maximum elapsed time;
- storage temperature/RH/light and controlled-area classification if relevant;
- temporary container, liner, closure, fill volume/headspace;
- whether transfer/transport occurs during the hold;
- prior development, validation, stability and deviation history;
- intermediate/bulk specifications and methods;
- downstream process sensitivities and finished-product CQAs;
- registered/approved manufacturing description and existing commitments.

Do not invent missing values. Use placeholders and identify which missing facts can change the regulatory conclusion.

## Hold-point inventory template

| Hold point ID | From event | To event | Material state | Routine hold | Proposed max hold | Storage conditions | Container/closure | Transport included? | Main risks | Existing evidence | Markets |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Define the time clock with objective events. Avoid vague wording such as `after blending` or `before compression` unless the batch record identifies the exact timestamp-generating event.

## Risk assessment model

Use QRM proportionate to uncertainty, importance and complexity. A numerical FMEA is optional, not mandatory. At minimum, evaluate:

### Chemical risk

- hydrolysis, oxidation, photolysis, isomerisation, deamidation or other plausible degradation;
- impurity growth and potency/assay change;
- interaction with excipients, container/liner, oxygen or moisture;
- solvent loss or concentration change.

### Physical risk

- particle-size shift, agglomeration, segregation or flow deterioration;
- density, compressibility, hardness/friability or coating behaviour changes;
- precipitation, phase separation, viscosity or rheology change;
- polymorphic/crystalline change;
- dissolution/release consequences.

### Microbiological risk

- water activity/moisture and nutrient potential;
- bioburden/endotoxin growth before sterilisation/filtration;
- preservative effectiveness where relevant;
- open versus closed processing;
- environmental exposure and container closure;
- aseptic/sterile boundary and maximum validated processing times.

### Processability and downstream risk

- effect on mixing, granulation, compression, coating, filtration or filling;
- impact on CPP-CQA relationships;
- equipment restart or extended campaign risk;
- additional sampling/testing causing contamination or segregation.

### Logistics risk

- storage-room variability;
- transport delay, vibration, temperature/RH excursion;
- partial container fill/headspace;
- staging and status-control errors;
- cumulative holds over weekends, maintenance or campaign scheduling.

## Study strategy selection

Use the governing-market requirement first, then the scientific risk.

### Route A: risk/science assessment without dedicated formal stability study

Use only where the applicable source permits and the evidence is adequate. This may fit chemically and physically stable US finished-dosage intermediates under FDA's CGMP Q&A, or low-risk holds where current product/process knowledge directly supports the period.

Document:

- why formal stability is unnecessary;
- data sources and representativeness;
- whether confirmatory sampling/testing is used;
- residual uncertainty and review triggers.

Do not use Route A to bypass an explicit product-scope requirement such as the China oral-solid >30-day study trigger or an applicable EU/EAEU prolonged-hold dossier expectation.

### Route B: dedicated hold-time study

Use when required by the applicable guidance, when material is unstable/sensitive, when the proposed hold exceeds a risk-derived period, when transport/conditions add uncertainty, or when development knowledge is insufficient.

The protocol should include:

1. objective and regulatory/scientific rationale;
2. material/stage and process linkage;
3. batch(es), scale and strength selection with rationale;
4. proposed maximum hold and study duration;
5. storage condition and monitoring;
6. container/closure/fill-level configuration;
7. time points;
8. sampling plan and sample protection;
9. test attributes/methods and acceptance criteria;
10. trend/statistical evaluation where relevant;
11. deviation/OOS/OOT handling;
12. downstream finished-product linkage;
13. conclusion rules and any commercial-scale confirmation commitment.

### Route C: process-validation challenge

Use where the jurisdiction accepts process-validation challenge as support and the commercial process can safely challenge the intended maximum hold. Predefine the hold in the validation protocol and assess both intermediate attributes and downstream/finished-product performance.

Do not assume PPQ automatically validates every possible hold if the actual validation batches did not challenge the defined maximum or representative worst case.

## Batch and scale decision table

| Framework | Study scale / batch principle |
| --- | --- |
| China CDE 2025 No. 6, chemical oral solids | At least pilot scale; at least one batch to determine hold time; if not commercial scale, confirm at commercial scale; use QRM for additional batches/strengths |
| EU finished-dosage-form guideline | Where relevant, stability support for prolonged hold on at least two pilot-scale batches; current EU Q.II.b.3(e) change route uses minimum two pilot or commercial batches |
| EAEU Recommendation No. 3 | Where relevant, at least two pilot-scale batches for hold-time stability support |
| PIC/S PE 009-18 finished dose | No universal fixed batch count for this purpose; justify extent through QRM/process knowledge and applicable product annex. PE 009-18 changes Annex 19, not this hold-time principle |
| PIC/S Part II / FDA Q7 API intermediates | No universal fixed hold-time study batch number in the cited time-limit clauses; justify scientifically and according to API stability/process knowledge |
| US 21 CFR 211.111 / FDA CGMP Q&A | No universal fixed batch count; evidence must be scientifically adequate for the proposed control |

## Time-point design

Do not copy a single global time-point pattern into every protocol.

China oral-solid guidance expressly expects at least beginning, intermediate, and end points. Elsewhere, select time points that can detect relevant change and support the proposed maximum.

Professional implementation options, to be justified, can include:

- T0, one or more intermediate points, proposed maximum;
- an additional challenge point beyond the intended maximum when scientifically useful and operationally safe;
- denser early sampling for microbiologically sensitive or rapidly changing materials;
- transport/excursion-specific points when a transfer forms part of the hold.

Do not state that an extra `+20%` or `+50%` challenge is a regulatory requirement unless a source/company standard requires it.

## Attribute-selection matrix

| Risk | Candidate attributes | Typical linkage |
| --- | --- | --- |
| moisture sensitivity | water/LOD, water activity, appearance, flow, hardness/friability | compression/coating/dissolution |
| oxidation/degradation | assay, related substances, specific degradants, oxygen/headspace where relevant | potency/safety/stability |
| segregation | blend uniformity, assay distribution, particle-size distribution, density | content uniformity |
| physical ageing | PSD, density, flow, hardness, friability, disintegration, dissolution/release | manufacturability/performance |
| aqueous/bioburden risk | microbial limits/bioburden, endotoxin as applicable, pH, appearance | sterile assurance/product safety |
| solution/suspension instability | pH, concentration/assay, viscosity, precipitation, particle size, homogeneity | filling/dose uniformity |
| polymorphic risk | solid-state/crystal-form test where justified | dissolution/stability |
| container interaction | appearance, moisture/oxygen-sensitive attributes, extractables/leachables only if scientifically relevant | quality during hold/transport |

This is a candidate matrix, not a mandatory test list. Select methods that are fit for the study objective and sufficiently sensitive to the expected change.

## Container and storage design

Use commercial temporary-storage configuration whenever feasible. If a smaller study container is used, justify equivalence in:

- material of construction;
- liner/contact surface;
- closure/seal;
- surface-area-to-volume relationship where relevant;
- headspace-to-product ratio;
- permeability to moisture/oxygen/light;
- fill level and orientation.

For oxidation-sensitive or moisture-sensitive materials, challenge the plausible worst case rather than automatically using the nominal fill volume.

## Cross-site transfer and excursions

Where the intermediate/bulk product is moved between sites:

- include transport time in the elapsed-time model if it consumes the approved hold window;
- identify transport temperature/RH and monitoring;
- evaluate seasonal and delay scenarios;
- consider vibration/agitation and container integrity;
- define excursion assessment using stability/process knowledge;
- ensure the destination can verify material status, elapsed time, conditions, and remaining approved hold time.

Do not restart the hold-time clock merely because the material changes site or container unless the validated process and approved procedure explicitly support a new independent clock.

## Cumulative hold-time evaluation

When a process contains several pauses, assess whether total elapsed exposure can affect the same degradation or microbiological mechanism. A series of individually acceptable holds is not automatically acceptable if cumulative exposure is relevant.

Use one of the following, with rationale:

- independent hold limits where mechanisms are demonstrably independent;
- a cumulative maximum manufacturing time;
- a combined worst-case challenge in process validation;
- a hybrid control with both local stage limits and a total process-time cap.

## Acceptance and conclusion logic

Before study execution, state how the evidence will support the conclusion.

A robust conclusion should address:

- all predefined acceptance criteria;
- trend direction and magnitude, not only specification pass/fail;
- batch-to-batch consistency;
- any OOS/OOT/atypical result;
- any storage-condition excursion;
- downstream process performance;
- finished-product quality/stability linkage where risk indicates;
- remaining uncertainty and commercial-scale confirmation.

If a parameter shows a consistent adverse trend while still within specification, do not automatically approve the full proposed hold. Assess the margin to specification, downstream impact, and whether a shorter operational limit is scientifically appropriate.

## Exceeded hold-time investigation framework

When an actual batch exceeds an established hold time:

1. quarantine/contain the affected material or batch as appropriate;
2. determine exact elapsed time and actual storage/transport conditions;
3. identify the applicable approved/registered maximum and source of the limit;
4. assess the mechanism-specific quality risk and downstream impact;
5. review original hold-time study margin, trend and representativeness;
6. determine whether additional testing can provide relevant evidence, without using testing to replace a required investigation;
7. assess related batches/process recurrence and scheduling/system causes;
8. perform regulatory assessment if disposition or process change could affect commitments;
9. document disposition, CAPA/change control and effectiveness follow-up.

Do not create a routine `grace period` after the validated maximum unless it is itself scientifically justified, procedurally controlled and consistent with regulatory commitments.

## SOP/SMP design checklist

A hold-time procedure should define:

- scope and material classifications;
- roles for CMC/process development, production, QA, QC, validation and RA as applicable;
- how hold points are identified;
- risk-assessment method and evidence hierarchy;
- study-trigger criteria;
- protocol/report requirements;
- controlled start/stop time definitions;
- routine recording and remaining-time calculation;
- storage/container/transport controls;
- warning/escalation before maximum time;
- exceeded-hold deviation and disposition route;
- change-control/reconfirmation triggers;
- regulatory assessment by market;
- PQR/CPV/trending linkage;
- document and raw-data retention.

## Review output pattern

For a protocol, report or SOP review, use an issue table such as:

| Location | Observed text/gap | Governing source / evidence | Regulatory vs professional status | Quality/compliance impact | Proposed revision/action | Fact to confirm |
| --- | --- | --- | --- | --- | --- | --- |

For a new hold-time strategy, use:

| Hold point | Risk basis | Proposed maximum | Conditions/container | Required evidence by market | Batch/scale strategy | Time points/tests | Downstream linkage | Change/regulatory action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Second-pass QA checks

Before finalising a hold-time deliverable, verify that:

- China, EU, EAEU, PIC/S and FDA positions have not been collapsed into one global number;
- the product type and material definition match each cited source;
- binding regulations are separated from scientific/regulatory guidance;
- the China 30-day statement is not presented as a universal GMP law;
- EU/EAEU `prolonged storage` markers are not mislabelled as absolute maximum limits;
- PIC/S Part I, Part II and Annex 1 scopes are not conflated;
- FDA 21 CFR 211.111 is distinguished from FDA Q&A and Q7 guidance;
- batch number, scale, time points and tests are justified from the correct source/risk;
- transport and cumulative holds are included where relevant;
- proposed operating limit, validated maximum and registered commitment are consistent or their differences are controlled;
- deviations, changes and post-approval filing implications are addressed.
