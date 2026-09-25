---
orphan: true
---

# Chapter 08 Organization (Strings and Text)

This chapter is split into:

- `0800-strings.ipynb`
- `0801-strings.ipynb`
- `0802-regex.ipynb`
- `0803-text-analysis.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `0800-strings.ipynb`: string and text overview
2. `0801-strings.ipynb`
   - String Creation and Accessing: quotes, escape sequences and raw strings, indexing and slicing, concatenation and repetition
   - String Methods: case methods, searching and testing, cleaning, splitting and joining, string formatting, type-checking methods, methods reference
   - String Comparison
   - Looping and Sorting, including docstrings
   - Application: Word List
3. `0802-regex.ipynb`
   - Backslashes in Regex Patterns: why regex patterns are written as raw strings
   - The `re` Module and the `Match` object
   - Metacharacters: quantifiers, greedy vs. non-greedy, anchors, character classes, groups and capturing, alternation
   - Advanced Topics: flags, compiled patterns, lookahead and lookbehind
   - Applications: cleaning text, string substitution, `re.fullmatch()` for validation
4. `0803-text-analysis.ipynb`
   - Unique words
   - Punctuation: cleaning and normalizing words
   - Word Frequencies: `Counter`, optional parameters, dictionary subtraction
   - Random numbers: weighted random choice, bigrams
   - Markov analysis: successor map, generating text

### Escape sequences in 0801 and 0802

Escape sequences and raw strings appear in both notebooks on purpose, with different jobs:

- `0801` teaches Python string escapes (`\n`, `\t`, `\\`, `\"`) and introduces raw strings. Students need these before the string methods that follow.
- `0802` does not re-teach them. It links back to 0801 and explains the one new idea: Python processes backslashes before the regex engine sees the pattern, so patterns are written as raw strings (`r"\d+"`, not `"\\d+"`).
- Regex escapes such as `\d`, `\w`, `\s`, and `\.` belong in 0802's Metacharacters section, not in the opening section.

## Planned Additions

Topics from the 2026-09-25 coverage review. Status: planned, not yet written. When a topic is written, move it into the sequence above and delete it here.

- **New section `0802-files.ipynb` (Files)**, taught once and then used by the rest of the chapter:
  - reading and writing text files with `open()` and `with`; `pathlib.Path`
  - encodings: `encoding="utf-8"`, `str` vs. `bytes`
  - CSV files with the `csv` module (`csv.reader`, `csv.DictReader`, `csv.writer`)
  - JSON files with the `json` module (`json.load`, `json.dump`)
  - dates in text data with `datetime` (`strptime`, `strftime`, `timedelta`)
  - Source: move the appendix's `packaging/0501-files.ipynb` (file I/O and `pathlib`) here and expand it; retire it from the appendix.
  - When written, renumber `0802-regex` to `0803-regex` and `0803-text-analysis` to `0804-text-analysis`, and update `_toc.yml`, the landing page, the slides, and cross-references.
  *Why:* file I/O is taught only in the appendix, yet the regex and text-analysis sections read and write files; CSV, JSON, and dates are the formats data-science students handle most.

## Exercises

Each exercise is a `thebe-interactive` question cell followed by a `hide-input` solution cell. In delivery order:

- `0801-strings.ipynb` (15): Escape Sequences and Raw Strings; Indexing and Slicing; Concatenation and Repetition; Case Methods; Searching and Testing; Cleaning Strings; Splitting and Joining; String Formatting; Type-Checking Methods; Methods Reference Practice; String Comparison; Looping Through String Lists; Sorting Lists; Writing a Docstring; Word List Application
- `0802-regex.ipynb` (11): The Match Object; Greedy and Non-greedy Quantifiers; Regex Syntax Essentials; Regex Escape Sequences; Capture Groups; Regex Flags; Compiled Patterns; Lookahead & Lookbehind; Download and Clean Text; String Substitution; Full String Validation
- `0803-text-analysis.ipynb` (10): Counting Unique Words; Cleaning Words; Word Frequency Counter; Counter for Word Frequencies; Function with Optional Parameter; Dictionary Subtraction; Weighted Random Selection; Counting Bigrams; Building a Successor Map; Generate Text from Successor Map

## Source of Truth

Use `chapters/08-strings/*` as the only active Chapter 08 track for planning, delivery, and assessment.

Previous split subsection notebooks are preserved in `materials/_archived/ch09-strings-split/`.

## Material Files

The notebooks download their texts into the project-level `data/` folder on first run:

- `data/words.txt`: word list from Think Python, used in 0801 (Application: Word List) and 0803 (Dictionary Subtraction)
- `data/pg345.txt` and `data/pg345_cleaned.txt`: *Dracula* from Project Gutenberg, downloaded and cleaned in 0802 (Applications)
- `data/pg43.txt` and `data/dr_jekyll.txt`: *The Strange Case of Dr. Jekyll and Mr. Hyde* from Project Gutenberg, used throughout 0803

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Add local `{contents}` navigation near the top of each section notebook.
- Ensure chapter outcomes align with any Chapter 08 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview
- `assignments/lab.ipynb` — Lab assignment
- `assignments/homework.ipynb` — Homework questions
