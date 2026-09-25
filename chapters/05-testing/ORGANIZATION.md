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
   - Types of errors (syntax/runtime/semantic); reading tracebacks; handling exceptions
     (`try`/`except`, accessing the exception object, multiple exception types);
     `else`/`finally`; raising exceptions (with type hints vs. static vs. runtime
     checking, and custom exception classes nested under it); debugging philosophy and
     three techniques (print-statement, assertions, bisection); logging; 8 exercises
3. `0502-unit-testing.ipynb`
   - `pytest` (assert-based test functions; discovery via `test_*.py`; running tests from the
     terminal, as a subprocess, and in the notebook with `ipytest`; `pytest.raises`);
     `unittest.TestCase` (writing and running tests, `setUp`/`tearDown`, comparison with `pytest`);
     doctests and the `doctest` module; mocking external dependencies (`unittest.mock.patch` /
     `pytest` monkeypatch); test parametrization (`pytest.mark.parametrize`); basic coverage
     workflow and interpretation; 5 exercises

## One-Week Delivery Scope (Required vs Enrichment)

### Required Core (in-class + required homework)

- `0500-exception-testing.ipynb`
   - Full notebook
- `0501-exceptions.ipynb`
   - Error types, `try/except/else/finally`, multiple exception handling, raising
     exceptions, custom exception classes
   - Traceback reading, all three debugging-technique demos, and logging fundamentals
- `0502-unit-testing.ipynb`
   - `pytest` core workflow (including `pytest.raises`), `unittest` basics with `setUp`/`tearDown`, doctest
   - Parametrized tests and one mocking example
   - Coverage basics at interpretation level

### Enrichment / Project Track (optional, extra credit, or follow-up week)

- `0501-exceptions.ipynb`
   - Type hints, static checking (`mypy`), and runtime checking (optional aside after
     custom exceptions)
- `0502-unit-testing.ipynb`
   - Advanced mocking/stubbing scenarios and richer coverage workflows
   - Additional pytest-vs-unittest architecture exercises

## File Roles

- `0500-exception-testing.ipynb`: Chapter intro — learning goals and chapter flow map. No exercises.
- `0501-exceptions.ipynb`: Types of errors and reading tracebacks; exception handling (`try`/`except`, multiple exception types, `else`/`finally`); raising exceptions, with a type-hints/static-checking aside and custom exception classes; debugging (print-statement, assertions, bisection); and `logging` (levels, `basicConfig`, logging vs `print`). Exercises, in delivery order: Reading a Traceback; Catching Exceptions; Multiple Exception Types; Safe Division with Cleanup (`finally`); Raising Exceptions; Custom Exception Class; Using Assertions; Add Logging.
- `0502-unit-testing.ipynb`: `pytest` (test functions, discovery, assert style, `pytest.raises`, `ipytest`); `unittest` (`setUp`/`tearDown`, comparison with `pytest`); doctests; more testing techniques: mocking (`unittest.mock.patch`, `monkeypatch`), parametrized tests, coverage basics. Exercises, in delivery order: Write pytest-style tests; Write a TestCase for to_celsius; Fix the Failing Doctest; Mock a database lookup; Parametrize tests for is_leap_year.
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
- Add local `{contents}` navigation near the top of each section notebook.
- Ensure chapter outcomes align with any Chapter 05 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview
- `assignments/lab.ipynb` — Lab assignment
- `assignments/homework.ipynb` — Homework questions
