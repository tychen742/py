# Appendix Organization (Modules, Files, and Tooling)

This appendix unit is currently split into:

- `0500-intro-modules.ipynb`
- `0501-files.ipynb`
- `0502-modules.ipynb`
- `0503-packaging.ipynb`
- `0504-coding-tooling.ipynb`

## Purpose

This appendix is a **tooling reference for the whole book**. Students read it once for orientation and return to specific sections as needed.

## Scope and Sequencing

1. `0500-intro-modules.ipynb`
   - Appendix overview; import syntax patterns; module/package/library hierarchy
2. `0501-files.ipynb`
   - Reading/writing text files; `Path()` and pathlib
3. `0502-modules.ipynb`
   - Writing and importing custom modules; `__main__` guard
4. `0503-packaging.ipynb`
   - Package structure; `__init__.py`; `pip`; `requirements.txt`; virtual environments
5. `0504-coding-tooling.ipynb`
   - List comprehensions; lambda; docstrings + `help()`; type hints; `enumerate()`/`zip()`; `try`/`except`; f-string formatting

## Planned Additions

Topics from the 2026-09-25 coverage review. Status: planned, not yet written. When a topic is written, move it into the sequence above and delete it here.

- **`0501-files.ipynb`**: move into the new Files section planned for Chapter 8 (`0802-files.ipynb`); leave a one-line pointer here or remove this page from the TOC.
  *Why:* file I/O is a core topic, and Chapter 8 already depends on it.
- **`0502-modules.ipynb`**: running a module as a script: the `if __name__ == "__main__":` guard, then command-line arguments with `sys.argv` and `argparse`.
  *Why:* students need to run Python outside notebooks. The guard is listed in this doc (Duplication rules, File Roles) but 0502 does not teach it yet, and no other notebook does either.
- **`0503-packaging.ipynb`**: `pyproject.toml` and `uv` for setting up a project, compared with `pip` + `requirements.txt`.
  *Why:* current packaging practice; the appendix teaches only `pip` + `requirements.txt`.
- **`0504-coding-tooling.ipynb`**: it re-teaches comprehensions (6.1), lambda (4.2), type hints (2.3, 4.1), `enumerate`/`zip` (6.2), `try`/`except` (5.1), and f-strings (2.1). Turn it into a one-page quick reference that links to those sections, or remove it.
  *Why:* duplicated teaching drifts out of sync with the main chapters.

## Duplication rules

- `with` statement: **0501 only** (file context)
- `__main__` guard: **0502 only** (module context)
- `0504` covers all other idioms used book-wide; do not add file/module topics there

## File Roles

- `0500-intro-modules.ipynb`: Appendix intro; import syntax; orientation table.
- `0501-files.ipynb`: Reading and writing text files; `Path()`; context managers.
- `0502-modules.ipynb`: Creating and importing custom modules; `__main__` guard.
- `0503-packaging.ipynb`: Package structure; `__init__.py`; `pip`; `requirements.txt`; virtual environments.
- `0504-coding-tooling.ipynb`: Everyday Python idioms — comprehensions, lambda, docstrings, type hints, `enumerate`/`zip`, `try/except`, f-string formatting.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Material Files

Runnable examples, text files, package examples, and configuration demos for this appendix live in `materials/appendices/packaging/`.

## Source of Truth

Use `chapters/appendices/packaging/*` as the only track for this appendix unit's planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure appendix outcomes align with any related assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
