# R&D CMC laboratory quality and data integrity

**October 2026 update routing:** Read [regulatory-update-2026-10.md](regulatory-update-2026-10.md) for the latest scoped version/status and applicability updates; earlier checkpoints below are historical. For qualification/validation use [pics-pi006-4-validation-map.md](pics-pi006-4-validation-map.md). Do not extend clinical electronic-data guidance to all CMC laboratories or sterile/advanced-product GMP to all oral-solid products.

## Purpose, source status, and use boundary

Use this reference for risk- and purpose-based quality controls for CMC data generated in research and development laboratories, particularly supportive data used across the lifecycle of biological products. It converts a user-provided technical article into original assessment logic and reusable case patterns.

Source article:

- Brent S. Kendrick et al., *Quality risk management and data integrity in R&D laboratories supporting CMC lifecycle of biological products*, *Journal of Pharmaceutical Sciences*, corrected proof, 2024, DOI `10.1016/j.xphs.2024.09.013`.
- User-supplied file SHA-256: `6f35eac58425c50138e41c37f46b31d7d1f83ed3bcd436436ec27e6321e0a6cf`.

Apply these controls:

- Treat the article as secondary industry commentary, not a statute, regulation, regulator-issued guidance, compendial standard, or binding inspection criterion.
- The article's `Tier 0`, `Tier 1`, and `Tier 2` categories are author-proposed labels. A company may adapt the logic, but must define and govern its own categories, criteria, controls, and reclassification process.
- Use the synthesized knowledge only within the account for which the article was supplied. Do not bundle, reproduce, redistribute, upload, or quote substantial portions of the source PDF through the Skill.
- The source PDF is not part of the Skill. If exact wording, figures, tables, or page-specific evidence is required, ask the user to provide the relevant source copy or excerpt in the current task and respect its use restrictions.
- Regulatory requirements, dossier commitments, predicate-rule records, approved company procedures, and contract or quality-agreement obligations take precedence. Revalidate current regulatory propositions against official primary sources at execution time.
- Official checkpoints reviewed for this synthesis on 2026-09-08 include the FDA's current Preapproval Inspections Compliance Program 7346.832, ICH Q14, WHO TRS 1033 Annex 4, and PIC/S PI 041-1. This focused verification does not change the Skill's global regulatory baseline date.

## Core operating rule

Select the rigor of an R&D data package from its **intended use, consequence of error, uncertainty, and applicable requirements**, not merely from the department that generated it, a development-phase label, or a fixed tier name.

Use the following practical categories when the company has no controlled scheme. These are professional assessment categories, not legal classifications:

| Working category | Typical intended use | Control implication |
| --- | --- | --- |
| Exploratory internal work | Scouting, feasibility, or hypothesis generation not intended to support a regulated decision or submission | Maintain enough identity, provenance, scientific integrity, and retention to prevent misuse and support learning; label limitations and non-filing status. |
| Supportive R&D data | Development decisions or filing-supportive information with moderate product, patient, regulatory, or business consequence if wrong | Use planned studies, fit-for-purpose methods, traceable samples/materials, contemporaneous raw data, competent review, documented deviations and transformations, and controlled retention. |
| Critical supportive R&D data | Pivotal, registration-enabling, regulator-facing, post-PPQ, comparability, reference-standard, control-strategy, validation-support, or other high-consequence decisions | Apply enhanced prospective governance, independent verification, complete source-to-report-to-dossier traceability, stronger equipment/system assurance, explicit data-exclusion rules, and Quality or other independent oversight proportionate to risk. |
| GxP or predicate-rule data | Data required by applicable GxP, used for batch disposition, PPQ, release, formal stability, method validation/verification, or another governed record | Apply the governing quality system and regulatory requirements. Do not downgrade these data through an R&D category. |

The article's Tier 0 generally informs the exploratory category, Tier 1 the supportive category, and Tier 2 the critical-supportive category. Do not assume a one-to-one mapping without assessing the actual intended use.

## Assigning the level of rigor

Document the assessment prospectively where practicable. Consider:

1. whether the data, report, conclusion, or selected subset will be submitted to or inspected by a regulator;
2. whether it supports product or process design, a control strategy, acceptance criteria, reference-standard qualification, analytical validation, PPQ, comparability, clinical bridging, biosimilar similarity, or a GMP investigation;
3. potential impact of an erroneous or incomplete result on patient safety, product quality, clinical interpretation, lot disposition, regulatory conclusions, supply, or irreversible project decisions;
4. method maturity, measurement uncertainty, data complexity, manual processing, transformation, modeling, and susceptibility to analyst judgment or confirmation bias;
5. sample uniqueness, replaceability, chain of custody, storage/shipping sensitivity, and the ability or cost to repeat the study;
6. external-laboratory, vendor, software, instrument, interface, or data-hosting dependencies;
7. the development stage, but only as one input; a pre-PPQ study can still be critical, and a post-PPQ activity can be exploratory;
8. existing knowledge, platform applicability, uncertainty, deviations, atypical observations, failed work, omitted data, and legacy-data limitations;
9. applicable laws, guidance, filing commitments, approved protocols, quality-system procedures, and contractual requirements.

Record the classification rationale, required controls, accountable owner, reviewer/approver, retention decision, and reclassification trigger. A label alone is not a control.

## Proportionate control matrix

Tailor the matrix to the study. `Enhanced` does not mean full GMP by default, and `supportive` does not mean informal or undocumented.

| Control area | Supportive R&D data | Critical supportive R&D data | GxP or predicate-rule data |
| --- | --- | --- | --- |
| Study plan and report | Defined purpose, design, methods, decision use, limitations, and scientific review | Approved prospective protocol or equivalent; predefined criteria, deviations, exclusions, statistics, verification, and conclusion authority | Governed protocol/report and approvals required by the applicable quality system |
| Samples and chain of custody | Unique identity, receipt/condition/date, storage location and conditions, and traceable handling | Reconciliation, custody transfers, shipment/environmental monitoring where critical, excursion assessment, and heightened controls for irreplaceable or licensed-reference materials | Governed sample management and records |
| Materials, reagents, and standards | Grade/suitability, lot, expiry or use period, preparation, storage, and justification of atypical use | Stronger pedigree, bridging, qualification/stability, inventory/reconciliation, and critical-consumable traceability | Applicable GMP/compendial/company controls |
| Personnel | Demonstrable competence for the assigned work | Documented training or equivalent evidence, supervisory assessment, and independent competence challenge where warranted | Required controlled training and qualification |
| Equipment and environment | Installation/fitness, maintenance/calibration as applicable, relevant system suitability or controls | Risk-based qualification/assurance, critical environmental or temperature monitoring, maintenance status, and failure-impact assessment | Applicable qualification, calibration, maintenance, and computerized-system controls |
| Analytical method | Fit for the study purpose; capability and limitations understood | Qualification evidence, predefined performance expectations, reference/control suitability, and linkage to later validation or comparability decisions | Required validation, verification, transfer, or approved-method controls |
| Raw data and metadata | Contemporaneous attributable records; original or verified true copies; raw, processed, and supporting data retained | Complete data set; stronger metadata/audit-trail review; source-to-result verification; preserved processing history | Applicable data-integrity and record controls |
| Processing and transformation | Scientific justification; raw data and parameters preserved; reproducible calculation or processing | Predefined or independently challenged processing, software/code/version control, before-and-after lineage, and bias review | Validated/configured system and governed processing as applicable |
| Review and verification | Scientific peer review plus targeted source checks based on risk | Independent verification from key conclusions to sources and from submission/report back to complete data; selective reprocessing checks where justified | Review and approval defined by the governing system |
| Deviations, repeats, and exclusions | Explain departures, repeats, invalidations, missing data, and exclusions | Prospective rules where practicable; independent challenge of aberrant/negative data; full decision traceability | Governed deviation, OOS/OOT, investigation, and change processes |
| Retention, backup, and recovery | Defined retention and protected storage suited to intended use and study duration | Documented backup/restore and recovery assurance based on loss tolerance, criticality, and legal/business need | Applicable record-retention, archive, backup, and recovery requirements |
| External laboratory/vendor | Defined deliverables, method/data access, responsibilities, and performance evidence | Quality/technical agreement as appropriate, right to underlying data, change/deviation notice, audit or oversight, chain-of-custody and data-hosting controls | Applicable outsourced-activity and sponsor/MAH oversight requirements |

## Data-integrity and scientific-integrity rules

Apply ALCOA+ principles as appropriate to the data's intended use and risk. Preserve a traceable chain from sample and instrument through raw data, metadata, processing, review, report, and any dossier or decision that relies on the result.

Require that:

- complete sequences, controls, failed or aborted work, negative and aberrant observations, repeated analyses, reprocessing, omitted results, and excluded data remain visible and scientifically assessed;
- data selection is governed by the question and predefined or justified criteria, not by whether a result supports the desired conclusion;
- raw data and critical metadata are retained together with processing methods, software or code version, parameters, manual interventions, calculations, and the identity and timing of changes;
- transformations such as baseline correction, smoothing, normalization, interpolation, integration, spectral processing, image processing, or model-based output are scientifically suitable, reproducible, and incapable of concealing a meaningful signal without detection;
- custom scripts, spreadsheets, macros, models, and pipelines have version control, tested intended-use fitness, protected inputs/outputs, review, and change governance proportionate to risk;
- advanced or very large data sets use risk-based verification of key evidence, data lineage, processing logic, completeness, and exceptions rather than an impracticable claim that every data point was manually rechecked;
- scientific peer review, data verification, Quality oversight, method qualification, method validation, and regulatory approval are kept distinct.

Never fabricate, falsify, delete, selectively suppress, or manipulate data to obtain a desired outcome. Never change integration, calibration, settings, algorithms, inclusion criteria, or presentation merely to pass criteria or mask an impurity, signal, trend, or uncertainty.

## Regulatory firewall for potentially permissive article recommendations

Do not import the following article-derived practices as blanket permissions:

- **Accounts and attribution:** use unique individual accounts as the default. A shared or generic account is acceptable only when the system technically cannot support individual access and a documented risk assessment demonstrates equivalent attribution and traceability, restricted privileges, independent review, procedural controls, and a prioritized replacement or remediation plan. Never treat an administrator-like shared account as routine convenience.
- **Audit trails and metadata:** do not state that audit trails are unnecessary for a category. Determine audit-trail generation, retention, review, and metadata controls from data criticality, intended use, system capability, applicable requirements, and the risk of undetected change.
- **Backups:** do not copy a monthly, 30-day, quarterly, or other fixed cadence from the article. Define backup frequency, retention, off-site or resilient storage, restore testing, and recovery objectives from study duration, data criticality, loss tolerance, cybersecurity, and applicable record requirements.
- **Training evidence:** competence must be demonstrable. The documentation formality may be proportionate, but absence of a formal training record is not proof that no evidence is needed.
- **Quality oversight:** do not state that formal Quality oversight is never needed for R&D data. Determine independence, Quality involvement, approvals, audits, and escalation from consequence, intended use, company procedure, filing or contract commitments, and applicable requirements.
- **Electronic-record requirements:** do not claim that 21 CFR Part 11 or another electronic-record rule is categorically inapplicable because a laboratory is called R&D. First establish whether the record is required under a predicate rule or otherwise relied upon for a regulated activity, and assess regional scope and current official guidance.

These safeguards reflect current official data-integrity expectations reviewed for this synthesis and take precedence over a more permissive reading of the secondary article.

## Case-informed applications

The following patterns help select controls; they are not fixed tier assignments.

| Application | Typical assessment direction | Special controls and questions |
| --- | --- | --- |
| Structure/function and impurity characterization | Often supportive; elevate when pivotal, regulator-facing, or central to a CQA/control-strategy conclusion | Use orthogonal evidence, identify sample-preparation artifacts and method limitations, retain complete spectral/chromatographic/imaging data, and explain conflicting results. |
| Forced degradation | Supportive for early method understanding; critical when it supports stability-indicating claims, comparability, or biosimilar assessment | Justify stress conditions, prevent selective presentation, distinguish generated artifacts from product-relevant pathways, and link conclusions to method capability. |
| Product reference standards | Early interim standards may be supportive; primary/master and working-standard establishment, stability, qualification, and bridging are usually high consequence | Preserve pedigree, inventory, qualification, potency/attribute links, bridging history, storage/excursions, expiry or requalification, and continuity between generations. |
| R&D method qualification | Rigor depends on the decision supported; elevate when qualification data support method validation, PPQ, comparability acceptance criteria, or a critical CMC package | Define intended purpose and performance characteristics. Do not equate fit-for-purpose qualification with formal validation, verification, or transfer. Avoid claiming a universal definition of `method qualification`. |
| Process development and optimization | Early screening often supportive; late-stage control-strategy, range, clearance, column-lifetime, cleaning, or validation-support work may be critical | Demonstrate scale/model relevance, material and equipment comparability, method fitness, variability, predefined decisions, and applicability to the commercial process. |
| Small-scale model qualification | Usually high consequence when it replaces or informs commercial-scale evidence | Establish model purpose, input/output comparability, representative ranges, bias and uncertainty, challenge conditions, acceptance criteria, maintenance, and change triggers. |
| Formulation, presentation, handling, and shipping studies | Early screening may be supportive; confirmatory, post-PPQ, in-use, device/container, or filing-critical work often needs enhanced controls | Assess representative materials/configurations, time/temperature/agitation/light stresses, transport monitoring, stability linkage, and product-specific failure modes. |
| Analytical comparability | Elevate when criteria or conclusions will be submitted, support a process/site change, or involve PPQ/post-approval data | Establish method capability and precision, prospective protocol/criteria, lot/sample representativeness, complete data disclosure, orthogonal methods, and scientific/statistical relevance. |
| Biosimilar comparative analytical assessment | Normally high consequence and regulator-facing | Control licensed-reference-product sourcing, authenticity, storage, chain of custody, lot inventory/reconciliation, vendor activities, method fitness, full data lineage, and avoidance of cherry-picking. |
| R&D support for GMP OOS/OOT or nonconformance | Exploratory hypotheses and orthogonal/scale-down studies can be useful but may become high-consequence supportive evidence | Keep the formal GMP investigation in control. R&D work may support hypothesis testing but cannot replace required original-laboratory assessment, manufacturing investigation, impact assessment, or authorized lot-disposition evidence. |

## Legacy data and change of intended use

Classify data prospectively whenever possible. If exploratory or lower-control data are later proposed for a pivotal, regulator-facing, validation, comparability, reference-standard, or GMP decision:

1. define the new intended use and applicable requirements;
2. inventory the available raw data, metadata, samples, methods, systems, personnel evidence, equipment status, deviations, repeats, transformations, review, and retention;
3. compare the existing controls with those that would have been required prospectively;
4. assess gaps, uncertainty, bias, completeness, traceability, and the consequence of an erroneous conclusion;
5. perform justified independent verification, reanalysis, sensitivity analysis, bridging, confirmation, or regeneration of data;
6. document whether the data are accepted, conditionally accepted with limitations, or rejected for the new use, with approval by the proper authority;
7. update the classification, knowledge record, retention, and future controls.

Do not retrospectively relabel weak data as high-quality evidence without closing or transparently accepting the gaps. If a critical conclusion cannot be adequately verified, regenerate the evidence.

## Required assessment output

For an R&D CMC laboratory quality or data-integrity assessment, provide:

1. `Decision and intended use`: what the data will support and who owns the decision.
2. `Applicable status`: exploratory, supportive, critical supportive, or GxP/predicate-rule, with rationale and applicable jurisdiction.
3. `Evidence map`: samples/materials, methods, instruments/systems, people, raw data/metadata, processing, reports, submissions, and custody/data lineage.
4. `Controls expected`: prospective controls matched to consequence, uncertainty, and requirements.
5. `Observed evidence and gaps`: facts separated from assumptions; completeness, atypical results, exclusions, transformations, and legacy limitations visible.
6. `Regulatory text`: current official requirements with precise citations when the conclusion depends on them.
7. `Regulatory interpretation`: what the requirements mean for this use.
8. `Professional assessment`: application of this article-derived framework, explicitly labeled as nonbinding technical judgment.
9. `Actions and disposition`: verify, bridge, repeat, regenerate, restrict use, escalate, or accept with documented limitations; include owners and timing only when provided or authorized.
10. `Lifecycle follow-through`: retention, knowledge-management update, reclassification trigger, vendor oversight, change control, and future review.

## Official verification record

Official sources reviewed on 2026-09-08 for the regulatory safeguards in this synthesis:

- FDA, *Compliance Program Guidance Manual 7346.832, Preapproval Inspections*, issued 29 June 2026 and implemented 10 August 2026: `https://www.fda.gov/media/193382/download?attachment=`. Use it to support current FDA inspection attention to pharmaceutical-development documentation, raw data, application-data comparison, data integrity, and potential omission or selective use of data.
- ICH Q14, *Analytical Procedure Development*, current ICH-hosted text checked 2026-09-08: `https://database.ich.org/sites/default/files/ICH_Q14_Guideline_2023_1130_ErrorCorrection_2025.pdf`. Use it for phase-appropriate analytical development, prior knowledge, risk assessment, analytical procedure control strategy, and suitability considerations.
- WHO TRS 1033 Annex 4, *Guideline on data integrity*: `https://www.who.int/docs/default-source/medicines/norms-and-standards/guidelines/inspections/trs1033-annex4-guideline-on-data-integrity.pdf`. Use it for the unique-account default and the limited, justified exception when a system cannot support individual logins.
- PIC/S PI 041-1, *Good Practices for Data Management and Integrity in Regulated GMP/GDP Environments*: `https://picscheme.org/layout/publication.php?id=588`. Use it as current official inspection guidance within its scope; verify adoption and jurisdictional applicability before presenting it as binding law.

The review date records a focused verification for this article integration. It is not proof that every linked source remains current and does not replace execution-time currentness checks.
