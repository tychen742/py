# Chapter 13 Materials (Functional Programming)

This checklist is for building and delivering:

- `1300-intro-func-prog.ipynb`
- `1301-func-prog.ipynb`

## Must-Have Teaching Materials

- Slide deck or notes covering:
  - Pure functions vs. side effects; immutability; first-class functions
  - Decorators (function-based and class-based, `@wraps`, timer decorator)
  - List, dict, and set comprehensions
  - Lambda with `map()`, `filter()`, `sorted()`
  - `functools.reduce()`, `functools.partial()`, `functools.lru_cache()`
  - Recursion (factorial, Fibonacci, tree traversal) and recursion vs. iteration
  - Context managers with `@contextmanager`
- Code examples and demos ready to run in class
- Practice dataset or starter code where applicable

## Notebook Content Targets

### `1300-intro-func-prog.ipynb`

- Chapter intro: learning goals, motivation, chapter flow map (no exercises)
- Conceptual framing: pure functions vs. side effects; immutability; first-class functions

### `1301-func-prog.ipynb`

- Decorators (`@wraps`, timer); list/dict/set comprehensions; lambda with
  `map()`/`filter()`/`sorted()`; `functools.reduce()` (fold/accumulate);
  `functools.partial()` (partial application); `functools.lru_cache()` (memoization);
  recursion (factorial, Fibonacci, tree traversal);
  recursion vs. iteration table; context managers with `@contextmanager`
- Exercises: Sorting and Filtering with Lambda; Recursive Functions; functools

## Practice and Assessment Pack

- In-class checks:
  - 2–3 conceptual poll/discussion questions
  - 1–2 "predict the output" questions
- Lab tasks:
  - Write a decorator; rewrite a loop as a comprehension; filter/sort with lambda
- Homework:
  - Implement a recursive solution and compare it to an iterative equivalent
- Grading anchors:
  - Correctness
  - Code clarity and style
  - Understanding shown in comments or docstrings

## Reusable Assets to Prepare

- Shared starter code snippets
- Any datasets or input files needed by exercises
- Solution cells (tagged `hide-input`) for all exercises

## Chapter 13 Delivery Order (Recommended)

1. `1300-intro-func-prog.ipynb` — Chapter intro: learning goals and chapter flow map
2. `1301-func-prog.ipynb` — Decorators; comprehensions; lambda/map/filter; recursion; context managers

## Coordination Note

Chapter 13 planning and delivery are scoped to `chapters/13-functional/` only.
