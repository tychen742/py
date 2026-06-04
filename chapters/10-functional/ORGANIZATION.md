# Chapter 10 Organization (Functional Programming)

This chapter is split into:

- `1000-intro-func-prog.ipynb`
- `1001-func-prog.ipynb`
- `1002-func-practice.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1000-intro-func-prog.ipynb`
   - Chapter intro: learning goals, motivation, chapter flow map. No exercises.
   - Conceptual framing: pure functions vs. side effects; immutability; first-class functions
2. `1001-func-prog.ipynb`
  - Decorators (function-based and class-based, `@wraps`, timer)
  - list/dict/set comprehensions; lambda with `map()`/`filter()`/`sorted()`
  - decision criteria for comprehensions vs `map`/`filter` pipelines
  - readability and maintainability checks for functional pipelines
3. `1002-func-practice.ipynb`
  - Recursion (factorial, Fibonacci, tree traversal)
  - Context managers with `@contextmanager`
  - `functools`: `reduce()` (fold/accumulate), `partial()` (partial application),
    `lru_cache()` (memoization)
  - Practice-focused exercises

## One-Week Delivery Scope (Required vs Enrichment)

### Required Core (in-class + required homework)

- `1000-intro-func-prog.ipynb`
  - Full notebook
- `1001-func-prog.ipynb`
  - Decorators (core pattern + one example)
  - Comprehensions and lambda/map/filter with decision rubric
  - Functional style readability checks
- `1002-func-practice.ipynb`
  - Recursion fundamentals (factorial/Fibonacci-level depth)
  - `functools` essentials: `reduce`, `partial`, `lru_cache`
  - Context-manager essentials

### Enrichment / Project Track (optional, extra credit, or follow-up week)

- `1001-func-prog.ipynb`
  - Class-based decorators in depth
  - Multi-step functional pipeline refactoring challenge
- `1002-func-practice.ipynb`
  - Tree-recursion variants and extended recursion exercises
  - Extended context-manager design with `@contextmanager`

## File Roles

- `1000-intro-func-prog.ipynb`: Chapter intro — learning goals and chapter map; pure functions/immutability framing. No exercises.
- `1001-func-prog.ipynb`: Conceptual foundations — decorators; comprehensions; lambda/map/filter; decision guide for choosing comprehension vs map/filter; functional pipeline readability checks.
- `1002-func-practice.ipynb`: Practice notebook — recursion; context managers; `functools.reduce`, `functools.partial`, `functools.lru_cache`.
  Exercises: Sorting and Filtering with Lambda; Recursive Functions; functools.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/10-functional/*` as the only Chapter 10 track for planning, delivery, and assessment.

## Stray Files

The following files in `chapters/10-functional/` are not part of the Chapter 10 content track and should be relocated or removed:

- `generics.ipynb`
- `module-package.ipynb`
- `test-debug.ipynb`

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 10 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
