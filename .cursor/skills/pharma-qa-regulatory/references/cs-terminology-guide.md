# CS pharmaceutical-quality terminology

## Controlled snapshot

The user-designated source is `CS制药质量翻译助手_术语20260721(4).xlsx`, identified by the user as the terminology set compiled through **2026-07-21**. The normalized searchable resources contain:

- [cs-terminology-20260721.tsv](cs-terminology-20260721.tsv): 724 main terminology entries with collection status, confirmation/collection date, and finalized-use context.
- [cs-terminology-abbreviations-20260721.tsv](cs-terminology-abbreviations-20260721.tsv): 348 non-empty bilingual terminology and abbreviation entries.
- [cs-standard-phrases-20260721.tsv](cs-standard-phrases-20260721.tsv): 49 standard formulations.

The workbook's `更新说明` sheet still labels the internal version `2026-07-16`, and the latest row-level confirmation date in the main table is `2026-06-25`. Treat `2026-07-21` as the user-designated snapshot date, not as a claim that every row was confirmed on that date.

During normalization, preserve cell wording while removing zero-width characters, trimming surrounding whitespace, and replacing embedded line breaks with spaces so the TSV files remain reliably searchable.

## Use the terminology

Search before drafting, then confirm the selected entry in context. Prefer exact Chinese-term matches; if none exists, search meaningful stems or nearby wording. Useful patterns include:

```bash
rg -n '^质量受权人\t' references/cs-terminology-20260721.tsv
rg -n '委托检验|contract analysis' references/cs-terminology-20260721.tsv
rg -n '^.*\t.*\tQP$' references/cs-terminology-abbreviations-20260721.tsv
rg -n '本规程旨在|This document is established' references/cs-standard-phrases-20260721.tsv
```

Apply [translation-and-style.md](translation-and-style.md) before accepting a hit. Later explicit user approvals override this snapshot. In particular, use `Quality Management Specialist` for `质量管理员`, not the snapshot's older `Quality Administrator` entry.

For long documents, build a task-specific term list from matched entries and check the completed document for consistent capitalization, abbreviation definition, singular/plural, and contextual meaning.

## Update rule

When the user supplies or identifies a later-dated CS terminology source:

1. Confirm the actual source date, filename, internal version label, sheet structure, and latest row-level confirmation date.
2. Compare it with this snapshot and identify additions, removals, changed translations, duplicates, and conflicts with later explicit user approvals.
3. Replace the normalized TSV resources with the latest confirmed content and update this guide's filename, date, counts, and discrepancy note.
4. Preserve later explicit user approvals unless the user expressly revises them.
5. Do not infer that a copy-number suffix such as `(4)` is a later content version without checking its contents or receiving the user's designation.

When the user asks whether the terminology is latest and access to their Library is available, search exact and broad title variants for `CS制药质量翻译助手` and compare source dates before answering. Do not treat upload or modification time alone as the terminology's content date.
