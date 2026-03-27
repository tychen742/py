# Chapter 11 Organization (Exceptions and Testing)

This chapter is currently split into:

- `1100-exception-testing.ipynb`
- `1101-exceptions.ipynb`
- `1102-unit-testing.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1100-exception-testing.ipynb`
   - Chapter introduction: learning goals, motivation, chapter flow map
2. `1101-exceptions.ipynb`
   - Error types (syntax/runtime/semantic); `try/except/else/finally`; multiple exception
     handling; raising exceptions; custom exception classes; debugging philosophy,
     traceback reading, and debugging techniques; 2 exercises
3. `1102-unit-testing.ipynb`
   - `unittest.TestCase` (writing, running, setUp/tearDown); doctests and `doctest` module;
     1 exercise (fix a failing doctest)

## File Roles

- `1100-exception-testing.ipynb`: Chapter intro — learning goals and chapter flow map. No exercises.
- `1101-exceptions.ipynb`: Full exception handling and debugging content. Exercises: Safe Division with Cleanup (`finally`); Custom Exception Class.
- `1102-unit-testing.ipynb`: Unit testing with `unittest`; doctest introduction. Exercise: Fix the Failing Doctest.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/11-testing/*` as the only Chapter 11 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 11 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
