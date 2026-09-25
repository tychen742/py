# Chapter 01 Organization (Introduction to Python)

This chapter is currently split into:

- `0100-py.ipynb` (landing page)
- `0101-programming.ipynb`
- `0102-basic-syntax.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `0100-py.ipynb` (landing page)
   - What Python is, where it runs, how to use Jupyter, chapter flow, glossary
2. `0101-programming.ipynb`
   - Programming learning habits, what programs and algorithms are, abstraction, binary/hex/ASCII basics
3. `0102-basic-syntax.ipynb`
   - Syntax rules, comments, print statements, built-in functions, module imports, first programs, and runnable exercises that feed into Lab 01

## Planned Additions

Topics from the 2026-09-25 coverage review. Status: planned, not yet written. When a topic is written, move it into the sequence above and delete it here.

- **`0102-basic-syntax.ipynb`, Input and Output: make this the single home for output formatting** (between semesters): f-strings; the format-spec mini-language (`.2f`, `>10`, `,`, `%`); `str.format()` with positional placeholders, including reordering and reuse (for example `'{0} {1} cost ${2}'.format(6, 'bananas', 1.74)` and `'{1}, {1}!'`), and with keyword placeholders; a short note that `%`-formatting is legacy. Move this material here from 8.1's String Formatting section.
  *Why:* output formatting is split between 1.2 and 8.1, and it belongs with output. Scheduled between semesters because students who have finished Chapter 1 would not see it.

## File Roles

- `0100-py.ipynb`: Landing page — What Python is, where it runs, how to use Jupyter, chapter flow, glossary.
- `0101-programming.ipynb`: Programming learning habits, what programs and algorithms are, abstraction, binary/hex/ASCII basics.
- `0102-basic-syntax.ipynb`: Syntax rules, comments, print statements, built-in functions, module imports, first programs, and technical section exercises aligned with the Lab 01 coding questions.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Material Files

- `materials/01-intro-text_file.txt`: text file used by introductory examples.

## Source of Truth

Use `chapters/01-intro/*` as the only Chapter 01 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Add local `{contents}` navigation near the top of each section notebook.
- Ensure chapter outcomes align with any Chapter 01 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
- Keep `_html_extra/chapters/01-intro/overview.md` at about 30 slides with section checkpoints, worked code examples, and local slide assets.

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview
- `assignments/lab.ipynb` — Lab assignment with about five technical runnable coding questions extending the section exercises
- `assignments/homework.ipynb`: post-class homework with five management/case-framed true/false concept checks and five technical coding questions that extend the lab or cover essential gaps, including syntax debugging, running-count updates, type inspection after conversion, stakeholder messages, and combined audit tags. True/false homework questions use the DSM two-cell format: one visible markdown question/radio-button cell followed by one hidden solution cell, with compact bold question labels instead of markdown headings. Technical homework questions use the lab-style two-cell format: one interactive code prompt cell followed by one hidden solution cell.
