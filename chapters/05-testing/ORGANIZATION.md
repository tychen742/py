# Chapter 05 Organization (Exceptions and Testing)

This chapter is split into:

- `0500-exception-testing.ipynb`
- `0501-exceptions.ipynb`
- `0502-unit-testing.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `0500-exception-testing.ipynb`
   - Chapter introduction: learning goals, motivation, chapter flow map
2. `0501-exceptions.ipynb`
   - Error types (syntax/runtime/semantic); `try/except/else/finally`; multiple exception
     handling; raising exceptions; custom exception classes;
     debugging philosophy, traceback reading, and debugging techniques; 2 exercises
3. `0502-unit-testing.ipynb`
   - `unittest.TestCase` (writing, running, setUp/tearDown); doctests and `doctest` module;
     `pytest` (test discovery via `test_*.py`; assert-based syntax; comparison with `unittest`);
     mocking external dependencies (`unittest.mock` / `pytest` monkeypatch);
     test parametrization (`pytest.mark.parametrize`);
     basic coverage workflow and interpretation;
     2 exercises

## One-Week Delivery Scope (Required vs Enrichment)

### Required Core (in-class + required homework)

- `0500-exception-testing.ipynb`
   - Full notebook
- `0501-exceptions.ipynb`
   - Error types, `try/except/else/finally`, traceback reading, custom exceptions
   - One debugging-technique demo and logging fundamentals
- `0502-unit-testing.ipynb`
   - `unittest` basics, doctest, pytest core workflow
   - Parametrized tests and one mocking example
   - Coverage basics at interpretation level

### Enrichment / Project Track (optional, extra credit, or follow-up week)

- `0501-exceptions.ipynb`
   - Extended debugging-method comparison labs
- `0502-unit-testing.ipynb`
   - Advanced mocking/stubbing scenarios and richer coverage workflows
   - Additional pytest-vs-unittest architecture exercises

## File Roles

- `0500-exception-testing.ipynb`: Chapter intro — learning goals and chapter flow map. No exercises.
- `0501-exceptions.ipynb`: Full exception handling and debugging content; `logging` module (levels, `basicConfig`, logging vs `print`). Exercises: Safe Division with Cleanup (`finally`); Custom Exception Class; Add Logging.
- `0502-unit-testing.ipynb`: Unit testing with `unittest`; doctest introduction; `pytest` (test functions, discovery, assert style); mocking external calls; parametrized tests; coverage basics. Exercises: Fix the Failing Doctest; Write pytest-style tests.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Material Files

- `materials/05-testing/calc.py`: calculator module used in testing examples.
- `materials/05-testing/app.log`: sample log output from logging examples.

## Source of Truth

Use `chapters/05-testing/*` as the only Chapter 05 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 05 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview questions
- `assignments/homework.ipynb` — Homework questions
- `assignments/lab.ipynb` — Lab assignment
