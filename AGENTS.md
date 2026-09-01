# AGENTS.md — thinkpy.org (Python Programming)

## Base

Skill: `book-authoring` (from ai_shared)
Style: `guidelines/STYLE_GUIDE.md` in ~/ai_shared

## Project Context

- College-level textbook for intermediate to advanced Python programming
- Data science as the application context
- Some math is helpful, especially when it clarifies a concept
- Stay current with industry practices in terms of tools and tech trends
- Published at thinkpy.org as a Jupyter Book

## Read First

1. `README.md` for repository structure
2. `authoring/BOOK_PLAN.md` for audience, scope, and chapter sequence
3. `_toc.yml` for the current notebook order
4. The target chapter's `MATERIALS.md` and `ORGANIZATION.md` before editing that chapter

## Shared Book Rules

Follow `book-authoring` for shared Jupyter Book conventions: landing page format, content notebook structure, glossary/index rules, assignment order, standard assignment descriptions, preview/lab/homework formats, submit panel behavior, student portal links, and chapter overview slides.

## Working Rules

### Content

- CS and data science cases are the primary context
- Use simple datasets (fruits, names, nums) for concept illustration; use business datasets when appropriate
- Reuse the same datasets across chapters for consistency
- Always show diffs when proposing changes to existing content

### Landing Pages

- Landing pages (first notebook in each chapter) are named `NNNN-title.ipynb` without "intro" suffix
  - Example: `0100-py.ipynb`, `0300-control-flow.ipynb`, `0600-collections.ipynb`
  - Landing pages introduce chapter scope and learning outcomes only
  - Landing pages do not contain exercises

### Sidebar Navigation

- Menu expand/collapse arrows must sit on the same visual baseline as the corresponding menu entry text. Do not leave arrows on a separate lower line or vertically offset from the entry they control.

### Assignment UI

- Homework question blocks should use the same simple bordered-card treatment as preview questions. Avoid busy, nested, or competing borders around the question content.
- Section `Interactive Exercise` labels should render in the same red used by lab interactive-exercise labels.

### Assignment Naming

- Assignment IDs, API IDs, Canvas gradebook column names, Canvas CSV score headers, and Canvas CSV filenames use the same hyphenated `chNN-type` convention: `ch01-preview`, `ch01-lab`, `ch01-homework`.
- Do not use assignment-first or underscore forms such as `preview_ch01`, `lab_ch01`, `homework_ch01`, `preview01`, `lab01`, or `homework01` for new assignment records or Canvas exports.
- Score reports and Canvas-ready CSV exports filtered to one assignment in best-score mode must include every active student except explicitly excluded admin/test accounts. Students without a submission show/export score `0`, attempts `0`, and blank `Last Submitted`.

### Exercises

- Landing page notebooks do not get exercises
- All exercises (preview, lab, homework) go in the `assignments/` folder

### Account Data

- Authentication events are research data for later research projects. Keep historical login timestamps for each user in a login-event table; do not rely only on an overwritten `last_login_at` field.

## Quality Audits

When asked to audit, read the corresponding prompt file first and follow its instructions exactly.

| Invocation | Prompt | Scope |
| --- | --- | --- |
| `audit ch08` | `~/ai_shared/prompts/quality-check.md` | Per-chapter deep audit |
| `audit structure` | `~/ai_shared/prompts/audit-structure.md` | Project-wide file/folder check |
| `audit content [chNN]` | `~/ai_shared/prompts/audit-content.md` | Chapter depth and thinness |
| `audit style [chNN]` | `~/ai_shared/prompts/audit-style.md` | Prose style conformance |
| `audit assignments [chNN]` | `~/ai_shared/prompts/audit-assignments.md` | Assignment quality |
| `audit sync [chNN]` | `~/ai_shared/prompts/audit-sync.md` | Slides and assignments vs. current content |

## Semester Constraints

Update before each semester. No major changes during the semester.
