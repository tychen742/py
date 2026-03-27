# Chapter 10 Materials (Algorithms)

This checklist is for building and delivering:

- `1000-intro-algorithms.ipynb`
- `1001-algorithms.ipynb`
- `1002-searching.ipynb`
- `1003-sorting.ipynb`

> Note: `1000` is the chapter intro stub; `1001` is the concept framing notebook (no exercises). Exercises live in `1002` and `1003`.

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

- Algorithm input-process-output model (max_value example)
- Algorithm building blocks (sequence, decision, repetition)
- Runtime measurement basics (`timeit` module vs `time.perf_counter`)
- Why asymptotic analysis matters; Big O growth table
- Algorithm design checklist (5-step)
- Algorithm Selection Guide table
- Think Ahead teasing questions for 1001 and 1002

### `1001-searching.ipynb`

- Implement linear search
- Implement binary search (manual; with sorted-index caveat)
- `bisect` module as its own section:
  - `bisect_left`/`bisect_right`: sorted-position lookup (stdlib binary search)
  - `insort_left`/`insort_right`: maintaining a sorted list on insertion
  - Cross-reference to 1002: `insort` as "incremental sorted insert" vs. sorting from scratch
- Hash-based lookup (`set`/`dict`) — compared with linear and binary
- Correctness checks including hash-based edge cases
- Benchmark timing comparison across methods
- Exercises: min_value warm-up, classify_scores warm-up, O(n log n) reasoning, binary_search_first

### `1002-sorting.ipynb`

- Demonstrate Python `sorted()` and `.sort()` with stability demo
- Insertion sort and bubble sort (in-place, O(1) extra space)
- Merge sort and quick sort (divide-and-conquer)
- Order: insertion → bubble → merge → quick (simple to advanced)
- Benchmark across input patterns: random, sorted, reverse, duplicates
- Extension exercise: counting sort (non-comparison sort)
- Note: pass `data[:]` copies when calling in-place sorts in tests/benchmarks

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

- `average_runtime` utility: defined in both `1002` (repeats=30) and `1003` (repeats=8); duplication is intentional for standalone notebook execution
- Common test pattern: `data[:]` copies for in-place sorts (insertion, bubble); merge and quick are non-mutating
- Optional plotting helper for timing vs input size

## Chapter 10 Delivery Order (Recommended)

1. Chapter intro stub (`1000`)
2. Algorithm concepts + Big O + benchmarking (`1001`)
3. Search implementation and reasoning (`1002`)
4. Sorting implementation and benchmarking (`1003`)
5. Combined wrap-up: choose the right algorithm under constraints

## Coordination Note

Chapter 10 planning and delivery are algorithms-only for this course.
