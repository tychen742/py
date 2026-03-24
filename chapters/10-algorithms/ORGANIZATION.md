# Chapter 10 Organization (Algorithms)

This chapter is split into:

- `1000-intro-algorithms.ipynb` (intro: concept framing, Big O, algorithm design, selection guide)
- `1001-searching.ipynb` (searching: linear, binary, hash-based, benchmarking)
- `1002-sorting.ipynb` (sorting: built-in, insertion, bubble, merge, quick, benchmarking)

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1000-intro-algorithms.ipynb`
   - What algorithms are
   - Time/space complexity and Big O intuition
   - Algorithm design checklist (input → process → output)
   - Algorithm selection guide (table: condition → recommended approach)
   - Think Ahead preview questions
2. `1001-searching.ipynb`
   - Linear search
   - Binary search
   - Search trade-offs by data condition (sorted vs unsorted, static vs dynamic)
3. `1002-sorting.ipynb`
   - Built-in sort with `key=` and stability
   - Insertion sort (educational baseline, in-place)
   - Bubble sort (teaching baseline, in-place, for contrast)
   - Merge sort and quick sort (divide-and-conquer framing)
   - Benchmarking across input patterns (random, sorted, reverse, duplicates)

## File Roles

- `1000-intro-algorithms.ipynb`: concept framing only; no exercises (intro notebook rule).
- `1001-searching.ipynb`: coding lab + complexity comparison + exercises.
- `1002-sorting.ipynb`: coding lab + benchmarking + exercises.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/10-algorithms/*` as the only Chapter 10 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Prefer small benchmark inputs in notebooks to keep runtime fast.
- `1000` must have no exercises (intro notebook rule per AI_guidelines).
- `1001` and `1002` each have exercises per section.
- Pass fresh copies to in-place sorts (insertion, bubble) in tests and benchmarks.
- Ensure chapter outcomes align with any Chapter 10 assignment/quiz prompt.
