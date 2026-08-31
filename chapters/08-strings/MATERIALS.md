# Chapter 08 Materials (Strings and Text)

This checklist is for building and delivering the string, regex, and text-analysis notebooks listed in `ORGANIZATION.md`.

## Chapter 08 Delivery Order (Recommended)

1. `0800-strings.ipynb` — String and text overview, learning objectives, glossary, and chapter flow
2. `0801-strings.ipynb` — String creation/access, methods, comparison, looping/sorting, word lists, and checkpoint exercises
3. `0802-regex.ipynb` — Escape sequences, raw strings, the `re` module, regex syntax, advanced regex, applications, and checkpoint exercises
4. `0803-text-analysis.ipynb` — Cleaning text, word frequencies (manual dict + `Counter`), random text, Markov generation, and checkpoint exercises

Previous split subsection notebooks are preserved in `materials/_archived/ch09-strings-split/`.

Chapter 08 planning and delivery are scoped to `chapters/08-strings/` only.

## Material Files

- `materials/08-strings/datasss/pg345.txt` — raw Project Gutenberg text used in regex/text examples
- `materials/08-strings/datasss/pg345_cleaned.txt` — cleaned text example

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview
- `assignments/lab.ipynb` — Lab assignment (built, graded, wired to the lab submission API): clean/normalize a title; normalize a ticket code; sort with `key=str.casefold`; regex digit extraction; regex `fullmatch`/`search` groups
- `assignments/homework.ipynb` — Homework questions
