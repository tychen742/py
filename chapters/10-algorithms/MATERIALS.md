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

Use a two-tier model for one chapter per week:

- **Required core**: must be covered in lecture/lab and assessed
- **Enrichment/project track**: optional, extra credit, or follow-up content

### `1000-intro-algorithms.ipynb`

- Required core:
  - Chapter intro stub only: title and chapter flow map

### `1001-algorithms.ipynb`

- Required core:
  - Algorithm input-process-output model (max_value example)
  - Runtime measurement basics (`timeit` module vs `time.perf_counter`)
  - Big O growth table and best/average/worst-case framing
  - Algorithm Selection Guide table
- Enrichment/project track:
  - Extended design checklist drills and additional Think Ahead prompts

### `1002-searching.ipynb`

- Required core:
  - Implement linear search and binary search (manual)
  - One `bisect` usage example and one hash-based lookup comparison
  - Basic timing comparison across methods
  - Exercises: core binary-search and correctness checks
- Enrichment/project track:
  - Full `bisect_left/right` + `insort_left/right` comparison lab
  - Expanded edge-case and benchmarking matrix

### `1003-sorting.ipynb`

- Required core:
  - Demonstrate Python `sorted()` and `.sort()` with stability demo
  - Insertion sort and merge sort (required implementations)
  - Space complexity comparison and in-place vs out-of-place trade-offs
  - Baseline benchmark across key input patterns
- Enrichment/project track:
  - Bubble and quick sort comparative analysis
  - Counting sort extension
  - Expanded benchmark experiments and reflection

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
