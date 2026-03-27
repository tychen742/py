# Chapter 13 Materials (Functional Programming)

This checklist is for building and delivering:

- `1300-intro-func-prog.ipynb`
- `1301-func-prog.ipynb`
- `1302-func-practice.ipynb`

## Must-Have Teaching Materials

- Slide deck or notes covering:
  - Pure functions vs. side effects; immutability; first-class functions
  - Decorators (function-based and class-based, `@wraps`, timer decorator)
  - List, dict, and set comprehensions
  - Lambda with `map()`, `filter()`, `sorted()`
  - When to prefer comprehensions/generator expressions vs `map()`/`filter()`
  - `functools.reduce()`, `functools.partial()`, `functools.lru_cache()`
  - Recursion (factorial, Fibonacci, tree traversal) and recursion vs. iteration
  - Context managers with `@contextmanager`
- Code examples and demos ready to run in class
- Practice dataset or starter code where applicable

## Notebook Content Targets

Use a two-tier model for one chapter per week:

- **Required core**: must be covered in lecture/lab and assessed
- **Enrichment/project track**: optional, extra credit, or follow-up content

### `1300-intro-func-prog.ipynb`

- Required core:
  - Chapter intro: learning goals, motivation, chapter flow map (no exercises)
  - Conceptual framing: pure functions vs. side effects; immutability; first-class functions
- Enrichment/project track:
  - Additional conceptual discussion prompts or short reflection tasks

### `1301-func-prog.ipynb`

- Required core:
  - Decorators (`@wraps`, timer baseline)
  - List/dict/set comprehensions; lambda with `map()`/`filter()`/`sorted()`
  - Decision guide: comprehension/generator expression vs `map()`/`filter()`
  - Functional pipeline readability checks
- Enrichment/project track:
  - Class-based decorators and advanced decorator composition
  - Functional pipeline readability refactor challenge

### `1302-func-practice.ipynb`

- Required core:
  - Recursion fundamentals (factorial/Fibonacci) and recursion-vs-iteration table
  - `functools.reduce()` (fold), `functools.partial()`, `functools.lru_cache()`
  - Context managers with `@contextmanager`
  - Exercises: Sorting and Filtering with Lambda; one recursion exercise
- Enrichment/project track:
  - Tree-recursion variants and deeper recursion tracing
  - Context-manager implementation exercises with `@contextmanager`

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
2. `1301-func-prog.ipynb` — Functional concepts: decorators; comprehensions; lambda/map/filter; decision criteria
3. `1302-func-practice.ipynb` — Functional practice: recursion; context managers; `functools`

## Coordination Note

Chapter 13 planning and delivery are scoped to `chapters/13-functional/` only.
