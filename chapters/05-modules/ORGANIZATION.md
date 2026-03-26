# Chapter 05 Organization (Modules and Files)

This chapter is currently split into:

- `0500-intro-modules.ipynb`
- `0501-files.ipynb`
- `0502-modules.ipynb`
- `0503-packaging.ipynb`
- `0504-coding-tooling.ipynb`

## Purpose

Chapter 5 is a **tooling reference for the whole book**. Students read it once for orientation and return to specific sections as needed. It will move to an appendix in a future edition; it lives here (between ch. 4 Functions and ch. 6 Lists) for this semester.

## Scope and Sequencing

1. `0500-intro-modules.ipynb`
   - Chapter overview; import syntax patterns; module/package/library hierarchy
2. `0501-files.ipynb`
   - Reading/writing text files; `Path()` and pathlib
3. `0502-modules.ipynb`
   - Writing and importing custom modules; `__main__` guard
4. `0503-packaging.ipynb`
   - Package structure; `__init__.py`; `pip`; `requirements.txt`; virtual environments
5. `0504-coding-tooling.ipynb`
   - List comprehensions; lambda; docstrings + `help()`; type hints; `enumerate()`/`zip()`; `try`/`except`; f-string formatting

## Duplication rules

- `with` statement: **0501 only** (file context)
- `__main__` guard: **0502 only** (module context)
- `0504` covers all other idioms used book-wide; do not add file/module topics there

## File Roles

- `0500-intro-modules.ipynb`: Chapter intro; import syntax; orientation table.
- `0501-files.ipynb`: Reading and writing text files; `Path()`; context managers.
- `0502-modules.ipynb`: Creating and importing custom modules; `__main__` guard.
- `0503-packaging.ipynb`: Package structure; `__init__.py`; `pip`; `requirements.txt`; virtual environments.
- `0504-coding-tooling.ipynb`: Everyday Python idioms — comprehensions, lambda, docstrings, type hints, `enumerate`/`zip`, `try/except`, f-string formatting.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/05-modules/*` as the only Chapter 05 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 05 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
