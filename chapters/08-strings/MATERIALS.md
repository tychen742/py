---
orphan: true
---

# Chapter 08 Materials (Strings and Text)

This checklist is for building and delivering the string, regex, and text-analysis notebooks listed in `ORGANIZATION.md`.

## Chapter 08 Delivery Order (Recommended)

1. `0800-strings.ipynb` — String and text overview, learning objectives, glossary, and chapter flow
2. `0801-strings.ipynb` — String creation and access (including escape sequences and raw strings), methods, comparison, looping/sorting, word lists, and checkpoint exercises
3. `0802-regex.ipynb` — Backslashes in regex patterns (builds on 0801's raw strings), the `re` module, regex syntax, advanced regex, applications, and checkpoint exercises
4. `0803-text-analysis.ipynb` — Unique words, cleaning punctuation, word frequencies (manual dict + `Counter`), random text and bigrams, Markov generation, and checkpoint exercises

See `ORGANIZATION.md` for the section-by-section sequence and the full exercise list.

Previous split subsection notebooks are preserved in `materials/_archived/ch09-strings-split/`.

Chapter 08 planning and delivery are scoped to `chapters/08-strings/` only.

## Material Files

The notebooks download their texts into the project-level `data/` folder on first run:

- `data/words.txt` — Think Python word list (0801, 0803)
- `data/pg345.txt`, `data/pg345_cleaned.txt` — *Dracula*, downloaded and cleaned in 0802
- `data/pg43.txt`, `data/dr_jekyll.txt` — *Dr. Jekyll and Mr. Hyde*, used in 0803

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview
- `assignments/lab.ipynb` — Lab assignment (built, graded, wired to the lab submission API): clean/normalize a title; normalize a ticket code; sort with `key=str.casefold`; regex digit extraction; regex `fullmatch`/`search` groups
- `assignments/homework.ipynb` — Homework questions

## Planned Additions: Materials to Prepare

See `ORGANIZATION.md`, Planned Additions.

- Small data files for the Files section in `data/`: a CSV with a date column (for example, fruit sales by day) and a JSON file with nested records
- Exercises for reading CSV rows into dicts, writing JSON, and parsing dates
