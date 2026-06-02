# AGENTS.md — thinkpy.org (Python Programming)

## Base

Skill: `book-authoring` (from ai_shared)
Style: `guidelines/STYLE_GUIDE.md` in ai_shared

## Project Context

- College-level textbook for intermediate to advanced Python programming
- Data science as the application context; CS concepts are a priority
- Some math is fine, especially when it clarifies a concept — demonstrate mathematically when helpful
- Students should be prepared for technical interviews after completing the course
- Stay current with industry practices
- Published at thinkpy.org as a Jupyter Book

## Read First

1. `README.md` for repository structure
2. `authoring/BOOK_PLAN.md` for audience, scope, and chapter sequence
3. `_toc.yml` for the current notebook order
4. The target chapter's `MATERIALS.md` and `ORGANIZATION.md` before editing that chapter

## Chapter Structure

### Content notebooks

- Open with a section outline using the box-drawing style:

  ```
  ┌──────────────────────────────────────┐
  │ Outline                              │
  │                                      │
  │ Section One                          │
  │ Section Two                          │
  │   o Subsection A                     │
  └──────────────────────────────────────┘
  ```

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

## Semester Constraints

<!-- Update each semester. Example entries: -->
<!-- - Fall 2026: exercise placement is one per section (current rule) -->
<!-- - Next semester plan: consolidate exercises into one dedicated section per notebook -->
<!-- - Chapters 1–5 are stable; new chapters in scope for restructuring -->
