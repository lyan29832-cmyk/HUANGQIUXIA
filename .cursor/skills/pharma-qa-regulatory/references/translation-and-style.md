# Translation and QA style

For complaint translation/content review or complaint-triggered reporting clocks, also read [complaint-translation-and-content-review.md](complaint-translation-and-content-review.md), targeted review 2026-10-08.

For technology-transfer document translation or a module completeness review, also read [technology-transfer-translation-and-review.md](technology-transfer-translation-and-review.md), reviewed 2026-10-08.

## Core method

Translate for regulatory meaning, not superficial word matching. Preserve scope, conditions, exceptions, defined terms, and the source's level of obligation. Do not strengthen `should` into `shall/must`, weaken `shall/must`, or add a compliance claim absent from the source.

Use a mandatory two-pass process:

1. Produce a complete, faithful translation using consistent pharmaceutical QA and regulatory terminology.
2. Conduct an independent professional QA proofread for accuracy, terminology, consistency, grammar, logic, numbering, and Chinese-English correspondence; then correct the deliverable.

## Terminology source priority

Read [cs-terminology-guide.md](cs-terminology-guide.md) and search the controlled CS terminology TSVs for translation and terminology work. Apply sources in this order:

1. The user's explicit instruction for the current task and later user-approved terminology decisions.
2. The fixed user rules and approved distinctions in this file.
3. The governing approved template or task-specific terminology list, provided it does not conflict with items 1–2.
4. The exact or context-matched entry in the CS terminology snapshot.
5. Applicable official regulatory terminology and professional contextual usage, with any material conflict flagged rather than silently resolved.

Do not mechanically substitute a glossary hit without checking grammar, jurisdiction, document type, defined-term status, capitalization, singular/plural, and surrounding meaning. The CS snapshot contains `质量管理员` as `Quality Administrator`; this entry is superseded by the later approved term `Quality Management Specialist` below.

## Fixed user rules

- Translate `本规程` as `This SMP`.
- Translate `总则` as `General Principles` when it is a controlled-document heading.
- In ICH or regulatory contexts, translate `临床前研究` as `nonclinical research`.
- Interpret `其他产品生命周期适用的情况` as `other applicable situations at different stages of the product lifecycle`.
- For Purpose clauses, prefer `This SMP is established to...` when faithful to the source.
- Prefer established QA formulations such as `standardize`, `ensure compliance throughout`, `define clear workflows and responsibilities`, and `ensure that ... data are accurate, reliable, and meet specified requirements` when they convey the source accurately.
- Do not use Times New Roman as the default English font. Preserve an approved template's font; if no template governs, use a professional sans-serif font such as Aptos or Arial.
- When translating a Chinese document title enclosed in book-title marks `《 》`, remove the marks and italicize the translated title when the output format supports italics.

## Approved terminology and distinctions

Apply these established equivalents unless the source or governing template clearly requires a different term:

| Chinese | Approved English | Scope or caution |
| --- | --- | --- |
| 质量受权人 | `Qualified Person (QP)` | Use `QP` after first definition. Do not replace with an EU-specific certification concept unless EU law is actually in scope. |
| 飞行检查 | `unannounced inspection` | Use the plural `unannounced inspections` when referring to the inspection category or program generally. |
| 质量管理员 | `Quality Management Specialist` | In responsibilities, introduce `The Quality Management Specialist (hereinafter referred to as QA)` and then use `QA`. |
| 审核放行 | `batch review and release` | Use `Batch Review and Release Process` for `审核放行流程`. Reserve `release review` for the review step preceding release. |
| 临床试验用药放行 | `Clinical Release (CR)` | Define `CR` at first use. |
| 部门负责人 | `head of the department` | Preserve the organizational level. |
| 系统负责人 | `head of the organizational system` | Do not shorten to department head. |
| 部门或系统负责人 | `the head of the department or organizational system` | In a RACI column, use `Department/Organizational System Head`. |
| 控股公司 | `companies controlled by the Company` | Do not automatically translate as `subsidiaries`. |
| 子公司 | `subsidiaries` | The Company itself may be the group company; preserve the stated corporate structure. |

## Supplemental medical and product terminology (2026-09-29)

These entries supplement the controlled `CS Terminology 20260721` snapshot; they do not change that source workbook or its version.

| Chinese | Preferred English | Scope or caution |
| --- | --- | --- |
| 产品类型 | `Product Type` | Use exactly for the user's Chinese Pharmacopoeia-based field label; do not substitute `Product Category`. |
| 产品类别 | `Product Category` | Use only when the source actually says `产品类别` and the governing form has no different defined label. Distinguish from `产品类型`. |
| 抗肿瘤药 | `antineoplastic drug(s)` | Use `Antineoplastic Drugs` as a product-type value in the present context. This is a professional rendering; the exact wording in the Chinese Pharmacopoeia English edition was not independently verified. Preserve `anti-tumor drug(s)` when translating or quoting an established NMPA/CDE English title or approved bilingual text. If the reference is specifically WHO ATC L01, use its category name `Antineoplastic Agents`. Do not equate this broad category with cytotoxic chemotherapy alone. |

For the user's field: `产品类型：抗肿瘤药` → `Product Type: Antineoplastic Drugs`.

### Oncology indication wording

| Chinese | Preferred English | Scope or caution |
| --- | --- | --- |
| 复发或难治的外周T细胞淋巴瘤 | `relapsed or refractory peripheral T-cell lymphoma (PTCL)` | Preserve `relapsed or refractory` rather than changing to `relapsed and refractory`. |
| 全身化疗 | `systemic chemotherapy` | Do not broaden to `systemic therapy`. For `至少接受过一次全身化疗`, retain the `at least once` threshold; do not add `regimen`, `course`, or `line` unless the governing source defines that unit. |
| 芳香化酶抑制剂 | `aromatase inhibitor` | Use `an aromatase inhibitor` for an unspecified member of the class. |
| 激素受体阳性；人表皮生长因子受体2阴性 | `hormone receptor-positive (HR-positive); human epidermal growth factor receptor 2-negative (HER2-negative)` | Preserve the positive/negative status and expand abbreviations at first mention. |
| 局部晚期或转移性乳腺癌 | `locally advanced or metastatic breast cancer` | Preserve `or`. |
| 阿霉素；强的松 | `doxorubicin; prednisone` | In an R-CHOP expansion, use `rituximab, cyclophosphamide, doxorubicin, vincristine, and prednisone`. |
| MYC和BCL2表达阳性 | `positive expression of both MYC and BCL2` | Refers to expression; do not infer gene rearrangements or translate as `double-hit`. For `既往未经治疗的DLBCL`, attach `previously untreated` to the lymphoma rather than implying the patient has never received any treatment. |

Preserve lifecycle and approval distinctions:

| Chinese | Approved English |
| --- | --- |
| 临床试验批准前 | `prior to clinical trial authorization` |
| 注册批准前 | `prior to regulatory approval`; when specifically referring to a drug registration application, `prior to approval of the drug registration application` |
| 生产许可批准前 | `prior to approval of the manufacturing license` |
| 上市许可批准前 | `prior to marketing authorization` |

Do not collapse these expressions into a generic `pre-approval` label when the distinction affects scope or responsibility.

## Controlled-text preservation

- Preserve approved Chinese wording unless there is a substantive regulatory, logical, factual, or ambiguity issue. Do not rewrite merely for stylistic preference.
- When only the English needs clarification, keep the approved Chinese and explain the clarification in the translation or proofreading notes.
- For contract-quality responsibilities, preserve the direction of authority: the contract giver may base authorization for other product types on the extent to which it has audited and qualified the contract acceptor's quality management system. Do not reverse the audit, qualification, or authorization relationship.
- Distinguish `controlled by the Company`, `subsidiary`, and `group company` based on the actual corporate relationship rather than treating them as synonyms.

## Regulatory drafting conventions

- Use concise, controlled, auditable language. Prefer one requirement or action per sentence where practical.
- Use `shall` for mandatory internal requirements when that matches the governing document convention; use `should` for recommendations and `may` for permission or possibility. Do not change the source's normative force.
- Keep actor, action, timing, input, output, record, exception, and escalation clear.
- Expand an abbreviation at first use unless it is already defined, universally accepted in the document, or the user's template directs otherwise.
- Apply one English equivalent consistently for a defined Chinese term. Maintain a task-specific term list for long documents.
- Retain source numbering and cross-references. Flag an apparent source error instead of silently repairing its substance.
- For bilingual tables, verify row-by-row alignment and that negation, limits, units, dates, and acceptance criteria correspond.

## Final translation checks

Confirm all of the following before delivery:

- No sentence, note, table cell, heading, qualifier, or exception was omitted.
- Technical terms fit the applicable NMPA, EAEU/EEC, EU GMP, PIC/S, ICH, FDA, validation, quality-system, or laboratory context.
- Names of authorities, regulations, guidance, dosage forms, systems, and records are rendered consistently.
- Modal verbs, tense, singular/plural, logical connectors, and responsibility assignments preserve meaning.
- Chinese and English punctuation, capitalization, units, abbreviations, and document-title formatting are correct.
- The translation reads as an international pharmaceutical QA document, not as literal or promotional prose.
