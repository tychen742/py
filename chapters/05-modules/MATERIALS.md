# Chapter 05 Materials (Modules and Files)

This checklist is for building and delivering:

- `0500-intro-modules.ipynb`
- `0501-files.ipynb`
- `0502-modules.ipynb`
- `0503-packaging.ipynb`
- `0504-coding-tooling.ipynb`

## Must-Have Teaching Materials

- Slide deck or notes covering:
  - Importing modules
  - File I/O and context managers
  - Custom modules and packaging
  - Coding tooling patterns
- Code examples and demos ready to run in class
- Practice dataset or starter code where applicable

## Notebook Content Targets

### `0500-intro-modules.ipynb`

- What modules are; import syntax; standard library overview

### `0501-files.ipynb`

- Reading and writing text files; context managers (with statement)

### `0502-modules.ipynb`

- Creating and importing custom modules; __main__ guard

### `0503-packaging.ipynb`

- Package structure; __init__.py; pip install basics

### `0504-coding-tooling.ipynb`

- Comprehensions with lambdas; coding tooling patterns; try-exception

## Practice and Assessment Pack

- In-class checks:
  - 2–3 conceptual poll/discussion questions
  - 1–2 "predict the output" questions
- Lab tasks:
  - Build a tax module; write/read a text file; add __main__ guard to a script
- Homework:
  - Create a small module with two functions and import it from a separate script
- Grading anchors:
  - Correctness
  - Code clarity and style
  - Understanding shown in comments or docstrings

## Reusable Assets to Prepare

- Shared starter code snippets
- Any datasets or input files needed by exercises
- Solution cells (tagged `hide-input`) for all exercises

## Chapter 05 Delivery Order (Recommended)

1. `0500-intro-modules.ipynb` — What modules are; import syntax; standard library overview\n2. `0501-files.ipynb` — Reading and writing text files; context managers (with statement)\n3. `0502-modules.ipynb` — Creating and importing custom modules; __main__ guard\n4. `0503-packaging.ipynb` — Package structure; __init__.py; pip install basics\n5. `0504-coding-tooling.ipynb` — Comprehensions with lambdas; coding tooling patterns\n
## Coordination Note

Chapter 05 planning and delivery are scoped to `chapters/05-modules/` only.

type hint:
class Solution:
    def romanToInt(self, s: str) -> int: