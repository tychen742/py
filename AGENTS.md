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

## Chapter Structure

### Content notebooks

- Open with a local table of contents generated from `##` headings:

  ````markdown
  ```{contents}
  :local:
  :depth: 2
  ```
  ````

### Assignment section (per chapter)

Three assignment types per chapter, appearing in the Jupyter Book left menu under Assignments:

- Preview questions
- Homework questions
- Lab assignment

## Working Rules

### Content

- CS and data science cases are the primary context
- Use simple datasets (fruits, names, nums) for concept illustration; use business datasets when appropriate
- Reuse the same datasets across chapters for consistency
- Always show diffs when proposing changes to existing content

### Exercises

- Chapter intro notebooks (`CH00-*-intro.ipynb`) do not get exercises

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