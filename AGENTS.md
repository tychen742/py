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
- Include about 10 multiple-choice questions and be scored out of 10 total points.
- Focus on checking familiarity with the chapter glossary and core terms before class.
- Use glossary terms in multiple-choice form, with one correct answer per question.
- Do not include code-reading, output-prediction, full-code-writing, or other technical exercise questions in `preview.ipynb`; those belong in labs or homework.
- Include SIS Login ID or Canvas identity handling when the book is connected to the quiz API.
- Provide Submit and Reset controls, save attempts through the quiz API where available, and show immediate per-question feedback after submission.

Lab assignments are extensions of the chapter's section exercises. Each `lab.ipynb` should contain about five lab questions. Format lab questions the same way section exercise questions are formatted in the chapter notebooks. Lab questions are technical: they should be runnable coding questions that combine, extend, or apply the skills introduced in the chapter exercises. Do not introduce unrelated skills or purely conceptual prompts in the lab.

Homework assignments should contain about 5 true/false questions covering essential concepts in the chapter and about 5 coding questions providing technical practice for the chapter. Score homework out of 10 total points, with each question worth 1 point unless a chapter-specific reason requires a different split. True/false questions should provide visible radio buttons for `True` and `False` in each question, not just prose prompts. For homework, true/false questions should be framed as short management, workplace, or decision cases that require applying the concept; avoid direct definition statements that merely contain the target term.

Auto-graded assignment submission panels should keep instructional headings, explanatory copy, and feedback/result rows hidden before submission. Show only the input fields and controls students need to submit. Reveal per-question feedback/results only after a submission returns, and allow multiple submissions by re-enabling the submit control after each attempt.

Student account menu links for `Account` and `My Scores` should open in new tabs. Keep `Log Out` in the current tab.

Student portal top navigation should sit close to the top of the browser tab. Keep scores pages compact: left-align the shell, avoid excess top padding, use tight section spacing, and keep table rows dense enough for scanning many attempts.

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
