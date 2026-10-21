# Practical QRM methods and implementation notes

## Purpose and source status

Use this file only after [quality-risk-management.md](quality-risk-management.md). It converts selected practical lessons from the user's controlled technical references into reusable pharmaceutical QRM implementation guidance.

Secondary technical references reviewed for this update:
- Jayet Moon, *Foundations of Quality Risk Management: A Practical Approach to Effective Risk-Based Thinking*, Quality Press, 2020.
- Tim Sandle, *Risk Assessment and Management for Healthcare Manufacturing: Practical Tips and Case Studies*, 2016.

Both references predate the final ICH Q9(R1) Step 4 text adopted in 2023. They are not regulatory requirements and must not be used to override or dilute Q9(R1). Use their methods only where they remain consistent with Q9(R1) and the applicable pharmaceutical quality system.

For a task that also requires official R1 implementation context, Annex II lifecycle routing, cross-ICH guideline integration, or jurisdictional legal status, load the corresponding dedicated QRM map referenced directly from `SKILL.md`; do not expand this practical-methods file into a regulatory source hierarchy.

## Knowledge integration audit

| Topic from technical references | Integration decision | Q9(R1) alignment / correction |
| --- | --- | --- |
| Start with information gathering, assumptions, scope/boundaries, and a clear risk question | Retain | Strongly aligned with Q9(R1) initiation and risk-assessment framing. |
| Use multidisciplinary knowledge and competent facilitation | Retain with proportionality | Q9(R1) says QRM is usually, but not always, interdisciplinary; higher formality may justify cross-functional teams and an experienced facilitator. |
| Select a tool appropriate to the problem; a complex tool is not automatically better | Retain | Consistent with Q9(R1)'s flexible methodology and formality continuum. |
| Predefine scales and action/acceptance criteria | Retain with qualification | Useful control of subjectivity; criteria must be justified by evidence, science, knowledge, and context. |
| Use FMEA severity/occurrence/detection and RPN multiplication | Modify | FMEA is an accepted example tool, but Q9(R1) does not require S/O/D, 1-10 scales, multiplication, or a universal RPN threshold. Detectability is method-dependent. |
| Use a fixed RPN cutoff or a Pareto 80/20 rule as the decision rule | Do not generalize | Such thresholds are not ICH requirements. Use only if scientifically justified and governed for the specific context. |
| Use risk matrices for communication and prioritization | Retain with safeguards | Useful but vulnerable to scale design, compression, and subjectivity; do not treat ordinal categories as precise quantitative risk. |
| Record residual risk after treatment | Retain | Directly supports Q9(R1) risk control and residual-risk acceptance. |
| Check whether controls create secondary/new risks | Retain | Directly aligned with Q9(R1) requirement to consider new/increased risks introduced by risk reduction. |
| Use risk registers, KRIs, thresholds, and dashboards | Retain as optional implementation | Useful for persistent/lifecycle risks, but not universal Q9(R1) requirements. |
| Link risk management to PDCA, quality planning, and continual improvement | Retain as implementation architecture | Compatible with integration into the pharmaceutical quality system; do not present PDCA as a Q9(R1)-mandated format. |
| Use cognitive-bias and risk-perception concepts to challenge decisions | Retain as subjectivity control | Supports Q9(R1)'s explicit requirement to manage and minimize subjectivity; label psychological models as professional implementation methods, not regulatory text. |
| Apply broad enterprise concepts such as opportunity risk, executive risk appetite, or profit optimization | Use only when relevant and clearly separated | Q9(R1) is focused on pharmaceutical quality and patient protection. Do not import enterprise-risk objectives into a quality-risk conclusion without an explicit bridge. |

## Practical preparation sequence

For a material QRM exercise, use this preparation sequence before scoring:

1. **Decision statement:** What decision must this QRM support?
2. **Risk question:** What quality/patient outcome could be affected and through what system boundary?
3. **System map:** Map the process, product, equipment, interfaces, suppliers, data flow, or lifecycle stage at the level needed to expose hazards.
4. **Evidence pack:** Assemble requirements, process knowledge, historical data, deviations, complaints, trends, validation evidence, supplier performance, and relevant scientific literature.
5. **Assumption log:** Mark what is known, assumed, inferred, unknown, or disputed.
6. **Team design:** Select the smallest competent cross-functional team appropriate to the question; add facilitation or independent challenge when importance/uncertainty/complexity is high.
7. **Method choice:** Select the simplest method that can answer the question robustly.
8. **Criteria:** Define scales, evaluation rules, acceptance principles, and escalation rules before seeing the final scores where practicable.
9. **Review plan:** Define who can accept residual risk, how effectiveness will be checked, and what later evidence will trigger review.

## Risk statements that support analysis

Prefer a cause-event-consequence structure when it improves clarity:

`Because of [cause/hazard/source], [failure/event/exposure] may occur, leading to [quality/patient consequence].`

For FMEA, distinguish:
- item/process step or function;
- failure mode;
- failure effect/consequence;
- cause/mechanism;
- current prevention controls;
- current detection controls;
- evidence for occurrence/probability, severity, and detectability ratings;
- proposed action;
- post-action residual risk.

Do not collapse `cause`, `failure mode`, and `effect` into one vague phrase. Do not use `risk = contamination` when contamination is actually a hazard/event and the patient/product consequence remains unstated.

## Facilitation and team controls

Practical QRM can fail through group dynamics even when the tool is technically correct. For higher-impact decisions:
- use relevant expertise from quality, manufacturing, engineering, analytical, development, regulatory, clinical, supply chain, statistics, or other functions as applicable;
- state who is a subject-matter expert and who has decision authority;
- use a neutral facilitator when the discussion is complex or contentious;
- seek input from quieter participants before converging on a rating;
- record material dissent rather than forcing artificial consensus;
- consider an independent reviewer who did not construct the original scoring for consequential decisions;
- separate evidence gathering from final scoring when anchoring on an early number is a concern.

These are implementation controls for subjectivity, not mandatory team composition rules.

## Managing assumptions, uncertainty, and bias

Use an assumption/evidence table for consequential or uncertain assessments:

| Item | Status | Evidence | Uncertainty | Decision impact | Follow-up |
| --- | --- | --- | --- | --- | --- |
| Example parameter | Known / assumed / unknown / disputed | Source | Low / medium / high or narrative | Could / could not change outcome | Data/action needed |

Challenge common decision traps:
- anchoring on a legacy score or previous batch/site conclusion;
- availability bias after a recent deviation or audit observation;
- confirmation bias when evidence supporting a preferred conclusion receives more weight;
- familiarity bias because a process has operated for years without a known event;
- escalation of commitment to a previously approved design or control;
- authority bias when the most senior voice determines the score;
- false consensus when multidisciplinary disagreement is hidden by averaging scores.

When uncertainty is material, prefer a range, scenario comparison, or sensitivity analysis over an unsupported single point estimate.

## Tool-selection map

### Flowchart / process map
Use to expose interfaces, handoffs, control points, and where a failure can enter or propagate. Often useful before FMEA, HACCP, or HAZOP.

### Checklist / structured questions
Use for mature, lower-complexity processes when hazards and controls are already well understood. A checklist is not adequate if the question requires discovery of novel failure pathways.

### FMEA / FMECA
Use when the analysis is naturally organized by item/process step and failure mode. Keep the focus on failure mechanisms and action, not just RPN ranking.

### Fault tree analysis
Use when the top event is clear and the key question is which combinations of causes can produce it. Useful when logic pathways matter more than a long list of independent failure modes.

### HACCP
Use when a process-flow model and critical-control-point logic fit the hazard-control strategy. Avoid mechanically relabeling every pharmaceutical control as a CCP.

### HAZOP
Use for systematic deviations from design/operating intent using suitable guide words and current process knowledge. It is especially useful for complex process/equipment parameter deviations when competent facilitation is available.

### PHA / preliminary screening
Use early when information is incomplete to identify major hazards and decide where deeper work is needed. Revisit as knowledge matures.

### Risk ranking/filtering
Use to prioritize sites, suppliers, audits, products, changes, or issues. Make weighting and filtering logic explicit so priorities are not hidden inside a spreadsheet formula.

### Statistical / trend tools
Use when actual data can quantify variability, trend, capability, correlation, uncertainty, or signal changes. Check whether the data are representative and whether correlation is being mistaken for causation.

## Risk-matrix and scoring safeguards

Risk matrices improve visibility but can lose information. Apply these safeguards:

- Define the consequence represented by each row/item before scoring severity.
- Make occurrence/probability anchors relevant to the actual exposure window and population of opportunities.
- Define detectability in relation to the hazard/failure and timing of detection; distinguish prevention from detection.
- Do not award a favorable detectability score merely because final release testing exists when the test is insensitive, destructive, delayed, or cannot protect the affected patient/batch.
- Preserve the individual S/O/D components even when an RPN is calculated.
- Flag high-severity scenarios separately if different component combinations produce the same RPN.
- Do not describe a 1-10 ordinal score as `10 times` a score of 1 unless the scale truly supports that mathematical meaning.
- Avoid changing cutoffs after seeing the answer.
- If two reasonable experts can shift a rating by one category and cross the action threshold, treat that as a sensitivity/uncertainty issue requiring discussion or more evidence.
- Do not conclude `risk acceptable` solely because the number is below a threshold; confirm that the risk scenario and controls are acceptable in context.

## Risk response planning

For each prioritized risk, consider documenting:
- available treatment options;
- why the chosen option is preferred;
- how the treatment is expected to change the risk mechanism;
- implementation resources, owner, and timing;
- effectiveness evidence;
- possible new or secondary risks;
- post-treatment reassessment;
- residual-risk acceptance and authority;
- monitoring plan;
- contingency or escalation if the treatment fails.

Prefer controls that prevent or reduce the probability/severity of harm over reliance on detection alone when practicable. Do not assume risk can always be eliminated.

## Monitoring and lifecycle review

For risks that persist over time, define one or more signals that can demonstrate whether the risk profile is stable, worsening, or improving. Practical signal types include:
- event counts/frequencies;
- rates normalized to production/exposure;
- trend slopes;
- process capability/control signals;
- supplier performance indices;
- recurring defect or complaint categories;
- time-to-recovery or continuity measures for supply risk.

A useful indicator should be linked to the specific risk mechanism. A general KPI is not automatically a KRI. For each chosen indicator, define:
- data source and data-quality control;
- owner;
- review frequency;
- alert/action threshold when appropriate;
- expected response after breach;
- relationship to formal reassessment.

Use multiple indicators when one proxy can give a misleading picture.

## Risk register as an optional governance tool

A risk register can be useful for significant persistent risks across products, systems, suppliers, or sites. If used, link each register entry to the underlying assessment and include at least:
- risk statement/reference;
- current risk status;
- controls/actions;
- owner;
- residual risk/acceptance status;
- key indicators or review trigger;
- next review date or event;
- links to deviations, changes, CAPAs, audits, or other evidence.

Do not require a risk register merely because these technical references discuss one. Q9(R1) requires effective QRM and review, not a universal register format.

## Practical QRM audit red flags

Escalate review attention when you see any of the following:
- a preselected conclusion with a risk assessment written afterward to justify it;
- an undefined risk question or scope;
- scores with no evidence or rating definitions;
- universal RPN cutoffs carried across unrelated systems;
- `no historical event` used as the sole basis for low probability;
- detectability credited despite no timely or effective detection mechanism;
- a high-severity scenario hidden by a low aggregate score;
- resource limits used to explain why a significant risk received a lightweight assessment;
- a risk-reduction action that was never reassessed for effectiveness or new risks;
- no named decision authority for residual-risk acceptance;
- old risk assessments never revisited after changes, deviations, complaints, audits, or new knowledge;
- a risk register that contains status colors but no traceable assessments or evidence;
- enterprise/business opportunity language overriding product-quality or patient-protection priorities.

## Boundary between the technical books and Q9(R1)

When a conclusion is based on the technical references rather than the guideline, label it `Professional assessment` or `Practical implementation`. Never write `ICH requires` for:
- a fixed FMEA scale;
- a fixed RPN formula or cutoff;
- a Pareto 80/20 prioritization rule;
- a mandatory risk register;
- mandatory KRIs/dashboards;
- a specific facilitator or independent reviewer in every assessment;
- enterprise risk appetite or opportunity-risk optimization.

When old Q9-oriented text in a pre-2023 source conflicts with Q9(R1), follow Q9(R1) and note the reconciliation.
