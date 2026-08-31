# Chapter 02 Organization (Variables and Basics)

This chapter is split into:

- `0200-py-basics.ipynb`
- `0201-variables-and-objects.ipynb`
- `0202-expressions-and-operators.ipynb`
- `0203-types-and-builtins.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `0200-py-basics.ipynb` — chapter overview, learning goals, glossary, and chapter flow. No exercises.
2. `0201-variables-and-objects.ipynb` — names and assignment; objects, values, types, and identity; mutation vs. reassignment; f-strings.
3. `0202-expressions-and-operators.ipynb` — expressions and statements; arithmetic; comparison and Boolean logic; membership and identity; assignment updates and precedence.
4. `0203-types-and-builtins.ipynb` — scalar types; type checking and conversion; common built-in functions; light collection-type preview; type hints.

Detailed collection behavior belongs in Chapter 06 and dictionaries in Chapter 07. Chapter 02 should introduce collection types only far enough for students to recognize them and use small examples.

## Archived Files

The previous six-notebook split was archived in `materials/_archived/02-overfragmented/` because it made the chapter feel like a reference sequence instead of a paced foundation chapter.

## Source of Truth

Use `chapters/02-basics/*` as the only Chapter 02 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Add local `{contents}` navigation near the top of each section notebook.
- Ensure chapter outcomes align with any Chapter 02 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview
- `assignments/lab.ipynb` — Lab assignment
- `assignments/homework.ipynb` — Homework questions
