# Chapter 03 Organization (Control Flow)

This chapter is currently split into:

- `0300-control-flow.ipynb`
- `0301-conditionals.ipynb`
- `0302-iteration.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `0300-control-flow.ipynb`
   - Motivation and overview of conditional and loop constructs
2. `0301-conditionals.ipynb`
   - control-structure overview; if / elif / else; nested conditionals; Boolean expressions; conditional expressions (ternary)
3. `0302-iteration.ipynb`
   - for and while loops; break, continue; accumulator pattern

## Planned Additions

Topics from the 2026-09-25 coverage review. Status: planned, not yet written. When a topic is written, move it into the sequence above and delete it here.

- **`0301-conditionals.ipynb`**: `match`/`case` (Python 3.10+): matching literal values, `case _` as the default, `|` for alternatives, and capture patterns; when a plain `if`/`elif` chain is still clearer.
  *Why:* current Python syntax; the book uses it only in passing (7.1, 10.2).

## File Roles

- `0300-control-flow.ipynb`: Motivation and overview of conditional and loop constructs.
- `0301-conditionals.ipynb`: Control-structure overview; if / elif / else; nested conditionals; Boolean expressions; conditional expressions (ternary).
- `0302-iteration.ipynb`: for and while loops; break, continue; accumulator pattern.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/03-control-flow/*` as the only Chapter 03 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Add local `{contents}` navigation near the top of each section notebook.
- Ensure chapter outcomes align with any Chapter 03 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview
- `assignments/lab.ipynb` — Lab assignment
- `assignments/homework.ipynb` — Homework questions
