# Chapter 13 Organization (Functional Programming)

This chapter is currently split into:

- `1300-intro-func-prog.ipynb`
- `1301-func-prog.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1300-intro-func-prog.ipynb`
   - Chapter intro: learning goals, motivation, chapter flow map. No exercises.
   - Conceptual framing: pure functions vs. side effects; immutability; first-class functions
2. `1301-func-prog.ipynb`
   - Decorators (function-based and class-based, `@wraps`, timer);
     list/dict/set comprehensions; lambda with `map()`/`filter()`/`sorted()`;
     recursion (factorial, Fibonacci, tree traversal); context managers
     with `@contextmanager`;
     `functools`: `reduce()` (fold/accumulate), `partial()` (partial application),
     `lru_cache()` (memoization); 3 exercises

## File Roles

- `1300-intro-func-prog.ipynb`: Chapter intro — learning goals and chapter map; pure functions/immutability framing. No exercises.
- `1301-func-prog.ipynb`: Decorators; comprehensions; lambda/map/filter; recursion; context managers; `functools.reduce`, `functools.partial`, `functools.lru_cache`.
  Exercises: Sorting and Filtering with Lambda; Recursive Functions; functools.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/13-functional/*` as the only Chapter 13 track for planning, delivery, and assessment.

## Stray Files

The following files in `chapters/13-functional/` are not part of the Chapter 13 content track and should be relocated or removed:

- `generics.ipynb`
- `module-package.ipynb`
- `test-debug.ipynb`

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 13 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
