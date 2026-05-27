# AGENTS.md — thinkpy.org (Python Programming)

## Base

Skill: `book-authoring` (from ai_shared)
Style: `guidelines/STYLE_GUIDE.md` in ai_shared

## Project Context

- College-level textbook for intermediate to advanced Python programming
- Data science as the application context; CS concepts are a priority
- Students should be prepared for technical interviews after completing the course
- Stay current with industry practices
- Published at thinkpy.org as a Jupyter Book

## Read First

1. `README.md` for repository structure
2. `_toc.yml` for the chapter and notebook sequence
3. The target chapter's folder before editing

## Chapter Structure

### Landing notebooks (`xx00*.ipynb`)

Each chapter landing notebook must include:
- One paragraph intro with 3–5 bullet points of the most essential concepts
- One video for the most important concept
- Learning goals
- Chapter table of contents
- Chapter glossary

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

  Box characters: `┌ ┐ └ ┘ ┬ ┴ │ ─ ▼`

- Headings are never underlined
- Keep `##` heading count to 5 or fewer per notebook
- Use `**Learning Goals**` (bold text), not a `## Learning Goals` heading
- Do not add a `## Setup` section; imports appear at the top without a heading
- Avoid `## Why … Matter` style headings

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
- Create one exercise per `##` or `###` section with essential content
- Questions should be simple practice of the content just covered
- Place each exercise at the end of its section
- Two code cells per exercise: question cell (`thebe-interactive`), solution cell (`hide-input`)
- Chapter intro notebooks (`CH00-*-intro.ipynb`) do not get exercises

## Semester Constraints

<!-- Update each semester. Example entries: -->
<!-- - Fall 2026: exercise placement is one per section (current rule) -->
<!-- - Next semester plan: consolidate exercises into one dedicated section per notebook -->
<!-- - Chapters 1–5 are stable; new chapters in scope for restructuring -->
