# Chapter 11 Materials (Exceptions and Testing)

This checklist is for building and delivering:

- `1100-exception-testing.ipynb`
- `1101-exceptions.ipynb`
- `1102-unit-testing.ipynb`

## Must-Have Teaching Materials

- Slide deck or notes covering:
  - Exception handling (try/except/else/finally)
  - Raising and custom exceptions
  - `logging` module: log levels, `basicConfig`, logging vs `print`
  - Unit testing with `unittest`; doctests
  - `pytest`: test discovery, assert style, `pytest.raises`, `pytest.mark.parametrize`
  - Mocking/stubbing dependencies (`unittest.mock`, monkeypatch) and basic coverage interpretation
- Code examples and demos ready to run in class
- Practice dataset or starter code where applicable

## Notebook Content Targets

Use a two-tier model for one chapter per week:

- **Required core**: must be covered in lecture/lab and assessed
- **Enrichment/project track**: optional, extra credit, or follow-up content

### `1100-exception-testing.ipynb`

- Required core:
  - Chapter intro: learning goals, error-type motivation, chapter flow map (no exercises)

### `1101-exceptions.ipynb`

- Required core:
  - Error types; `try/except/else/finally`; multiple exception handling
  - Raising exceptions and custom exception classes
  - Reading tracebacks and one systematic debugging technique
  - `logging` fundamentals (levels, `basicConfig`, logging vs `print`)
  - Exercises: Safe Division with Cleanup; Custom Exception Class
- Enrichment/project track:
  - Additional debugging-technique demonstrations
  - Extended logging exercise and instrumentation patterns

### `1102-unit-testing.ipynb`

- Required core:
  - `unittest.TestCase`: writing/running tests, `setUp`/`tearDown`
  - Doctest module and pytest core workflow (`assert` style, discovery)
  - `pytest.mark.parametrize` and one mocking example
  - Coverage basics (what % means and how to read gaps)
  - Exercises: Fix the Failing Doctest; Write pytest-style tests
- Enrichment/project track:
  - Expanded mocking/stubbing cases (dependency boundaries)
  - Deeper coverage analysis and targeted test-improvement workflow

## Practice and Assessment Pack

- In-class checks:
  - 2–3 conceptual poll/discussion questions
  - 1–2 "predict the output" questions
- Lab tasks:
  - Write try/except for user input; write a test class with at least 3 test methods
- Homework:
  - Add exception handling and tests to a prior chapter function
- Grading anchors:
  - Correctness
  - Code clarity and style
  - Understanding shown in comments or docstrings

## Reusable Assets to Prepare

- Shared starter code snippets
- Any datasets or input files needed by exercises
- Solution cells (tagged `hide-input`) for all exercises

## Chapter 11 Delivery Order (Recommended)

1. `1100-exception-testing.ipynb` — Chapter intro: learning goals and chapter map
2. `1101-exceptions.ipynb` — Exception handling, raising, custom exceptions, debugging
3. `1102-unit-testing.ipynb` — unittest and doctests

## Coordination Note

Chapter 11 planning and delivery are scoped to `chapters/11-testing/` only.
