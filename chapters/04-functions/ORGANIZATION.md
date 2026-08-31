# Chapter 04 Organization (Functions)

This chapter is currently split into:

- `0400-functions.ipynb`
- `0401-functions.ipynb`
- `0402-function-design.ipynb`
- `0403-recursion.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `0400-functions.ipynb`
   - Chapter intro; learning goals; chapter flow; glossary
2. `0401-functions.ipynb`
   - Function motivation; turtle examples; defining and calling functions; parameters, arguments, default parameters, `*args`, `**kwargs`, return values, and basic type annotations
3. `0402-function-design.ipynb`
   - Scope, pure functions vs. side effects, small-function composition, docstrings as contracts, and basic lambda functions
4. `0403-recursion.ipynb`
   - Recursive functions; base cases; tracing recursive calls; return-value recursion; practical limits; memoization

## File Roles

- `0400-functions.ipynb`: Chapter landing page; intro, learning goals, chapter flow, glossary.
- `0401-functions.ipynb`: Function motivation; turtle examples; defining and calling functions; parameters, arguments, default parameters, `*args`, `**kwargs`, return values, and basic type annotations.
- `0402-function-design.ipynb`: Scope, pure functions vs. side effects, small-function composition, docstrings as contracts, and basic lambda functions.
- `0403-recursion.ipynb`: Recursive functions; base cases; tracing recursive calls; return-value recursion; practical limits; memoization.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/04-functions/*` as the only Chapter 04 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Add local `{contents}` navigation near the top of each section notebook.
- Ensure chapter outcomes align with any Chapter 04 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview
- `assignments/lab.ipynb` — Lab assignment
- `assignments/homework.ipynb` — Homework questions
