# Chapter 10 Materials (Algorithms)

This checklist is for building and delivering:

- `1000-intro-algorithms.ipynb`
- `1001-searching.ipynb`
- `1002-sorting.ipynb`

## Must-Have Teaching Materials

- Slide deck or markdown notes for complexity classes:
  - `O(1), O(log n), O(n), O(n log n), O(n^2)`
- Visual aid for algorithm growth rates (small table or plot)
- Search demo dataset:
  - small sorted list
  - unsorted list
  - edge cases: empty, one-element, duplicates
- Sorting demo dataset:
  - random integers
  - already sorted
  - reverse sorted
  - many duplicates
- One short "algorithm selection" decision guide handout

## Notebook Content Targets

### `1000-intro-algorithms.ipynb`

- Definitions and motivation
- Runtime measurement basics (`time.perf_counter` or `timeit`)
- Why asymptotic analysis matters
- Preview of search and sort as chapter core

### `1001-searching.ipynb`

- Implement linear search
- Implement binary search
- Compare correctness and complexity
- Practice prompts:
  - first occurrence in sorted data
  - membership test with duplicates
  - choose search strategy from scenario constraints

### `1002-sorting.ipynb`

- Demonstrate Python `sorted()` and `.sort()`
- Implement at least two educational sorts (e.g., insertion + merge)
- Compare runtime trends with input patterns
- Discuss stability and memory trade-offs

## Practice and Assessment Pack

- In-class checks:
  - 3 conceptual clicker/poll questions
  - 2 "predict output" questions
- Lab tasks:
  - search implementation + tests
  - sort implementation + simple benchmark
- Homework:
  - select algorithm for 3 scenarios and justify with Big O + constraints
- Grading anchors:
  - correctness
  - complexity reasoning
  - code clarity
  - test coverage on edge cases

## Reusable Assets to Prepare

- Utility timing cell/snippet shared by `1001` and `1002`
- Common test helper for randomized correctness checks
- Optional plotting helper for timing vs input size

## Chapter 10 Delivery Order (Recommended)

1. Intro + complexity framing (`1000`)
2. Search implementation and reasoning (`1001`)
3. Sorting implementation and benchmarking (`1002`)
4. Combined wrap-up: choose the right algorithm under constraints

## Coordination Note

Chapter 10 planning and delivery are algorithms-only for this course.
