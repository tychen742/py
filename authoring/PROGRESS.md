# Progress Tracker

`_toc.yml` is the authoritative notebook order. This tracker records chapter status, assignment scaffolding, and known cleanup work.

Status values: `Draft` · `In Progress` · `Needs Review` · `Complete`

Last build check: `.venv/bin/jupyter-book build .` passed after the assignment nesting and artifact cleanup.

## Part I - Fundamentals

| Chapter | Title | Sections | Assignments | Planning | Status | Notes |
|---------|-------|----------|-------------|----------|--------|-------|
| 01 | Intro to Python | 0101, 0102 | Nested | Yes | In Progress | `text_file.txt` moved to `materials/01-intro-text_file.txt`. |
| 02 | Basics | 0201-0206 | Nested | Yes | In Progress | |
| 03 | Control Flow | 0301, 0302 | Nested | Yes | In Progress | |
| 04 | Functions | 0401-0403 | Nested | Yes | In Progress | Consider restructuring to 3 sections. |
| 05 | Exceptions & Testing | 0501, 0502 | Nested | Yes | In Progress | Runnable examples moved to `materials/05-testing/`. |

## Part II - Data Structures

| Chapter | Title | Sections | Assignments | Planning | Status | Notes |
|---------|-------|----------|-------------|----------|--------|-------|
| 06 | Collections | 0601-0603 | Nested | Yes | In Progress | Lists, tuples, and sets consolidated. |
| 07 | Dictionaries | 0701-0703 | Nested | Yes | In Progress | Mapping chapter split from sets. |
| 08 | Strings and Text | 0801-0803 | Nested | Yes | In Progress | Split subsection pages folded into three section notebooks; text data moved to `materials/08-strings/datasss/`. |

## Part III - Program Design

| Chapter | Title | Sections | Assignments | Planning | Status | Notes |
|---------|-------|----------|-------------|----------|--------|-------|
| 09 | OOP | 0901-0903 | Nested | Yes | In Progress | |
| 10 | Functional Programming | 1001, 1002 | Nested | Yes | In Progress | Extra notebooks not in TOC: `generics.ipynb`, `module-package.ipynb`, `test-debug.ipynb`; review or archive. |
| 11 | Iterators & Generators | 1101, 1102 | Nested | Yes | In Progress | SQLite examples moved to `materials/11-iter-gen/`; stray database notebook archived in `materials/_archived/ch11-iter-gen-stray/`. |
| 12 | APIs | 1201, 1202 | Nested | Yes | In Progress | |

## Part IV - DSA

| Chapter | Title | Sections | Assignments | Planning | Status | Notes |
|---------|-------|----------|-------------|----------|--------|-------|
| 13 | Abstract Data Structures | 1301-1303 | Nested | Yes | In Progress | |
| 14 | Algorithms | 1401-1403 | Nested | Yes | In Progress | |

## Appendices

| Item | Title | Files | Planning | Status | Notes |
|------|-------|-------|----------|--------|-------|
| A1 | Tooling | `chapters/appendices/0101-tooling` | No chapter planning files | In Progress | Single appendix page in TOC. |
| A2 | Modules, Files, and Packaging | 0500-0504 | Yes | In Progress | Runnable examples and support files moved to `materials/appendices/05-tooling/`. |
| A3 | Jupyter Setup | 0200-0204 | No chapter planning files | In Progress | |
| A4 | Bibliography | `chapters/bibliography` | No chapter planning files | In Progress | |
| A5 | Index | External generated index | No chapter planning files | In Progress | Final entry under Appendices. |

## Open Cleanup Items

- Decide whether Chapter 10's extra notebooks should be archived under `materials/_archived/` or folded into the active functional programming sequence.
- Continue auditing chapter planning files when material paths change; `MATERIALS.md` and `ORGANIZATION.md` should move together.
