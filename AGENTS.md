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

- Preview
- Lab
- Homework

In `_toc.yml`, assignment child pages appear in this exact order: `Preview`, `Lab`, then `Homework`. Use those exact titles. Do not use `Preview Questions` for the preview assignment label.

Preview assignments should follow the DSM Chapter 01 preview model. They are short scored pre-class quizzes, not open-ended reflection prompts. Each `preview.ipynb` should:

- Start with `# Preview`.
- State the due date, point value, and that multiple submissions are allowed with the highest score kept.
- Focus on checking familiarity with the chapter glossary and core terms before class.
- Use multiple-choice questions with one correct answer per question.
- Include lightweight technical questions when the chapter section supports them, especially code-reading or output-prediction questions adapted from the chapter exercises or lab pattern. Keep these questions multiple choice; do not require students to write full code in the preview.
- Include SIS Login ID or Canvas identity handling when the book is connected to the quiz API.
- Provide Submit and Reset controls, save attempts through the quiz API where available, and show immediate per-question feedback after submission.

Lab assignments are extensions of the chapter's section exercises. Each `lab.ipynb` should contain exactly five lab questions that combine, extend, or apply the skills introduced in the chapter exercises. Do not introduce unrelated skills in the lab.

### Chapter Overview Slides

Overview slide decks must be substantive enough for lecture use. When creating or revising `_html_extra/chapters/XX-name/overview.md`, expand thin decks rather than leaving a short outline: include the chapter setup, the main ideas from each section, at least one worked code example or discussion prompt per major section, and a closing recap or checkpoint.

Each chapter overview deck should contain around 30 slides. Use fewer only for a genuinely short chapter, and add more when the chapter has enough examples, figures, tables, or activities to support them.

Slides should reuse the book's visual assets. Copy relevant figures, photos, diagrams, and table images from `figures/`, `_static/figures/`, chapter notebooks, or chapter material folders into a local slide asset folder such as `_html_extra/chapters/XX-name/assets/`, then reference the copied files from `overview.md`. Do not leave useful chapter figures or tables out of the deck when they clarify the concept.

After editing `overview.md`, regenerate and commit the matching `overview.html`.

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
