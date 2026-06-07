# Chapter Quality Checklist — thinkpy.org overrides

Canonical audit prompts live in `~/ai_shared/prompts/`. This file records only overrides and project-specific rules that apply to thinkpy.org.

## Audit prompts

| Invocation                 | Prompt                                     |
|----------------------------|--------------------------------------------|
| `audit ch08`               | `~/ai_shared/prompts/quality-check.md`     |
| `audit structure`          | `~/ai_shared/prompts/audit-structure.md`   |
| `audit content [chNN]`     | `~/ai_shared/prompts/audit-content.md`     |
| `audit style [chNN]`       | `~/ai_shared/prompts/audit-style.md`       |
| `audit assignments [chNN]` | `~/ai_shared/prompts/audit-assignments.md` |
| `audit sync [chNN]`        | `~/ai_shared/prompts/audit-sync.md`        |

## Project-specific overrides

### Datasets

- Use `fruits`, `names`, `nums` as the default illustration datasets across all chapters
- Use business/domain datasets when the professional context adds value
- Reuse the same named datasets across chapters — do not invent new toy data per chapter

### Exercises

- Chapter intro notebooks (`XX00-*.ipynb`) never get exercises

### Content

- Data science is the primary application context throughout; prefer DS examples over generic CS examples where both would work
