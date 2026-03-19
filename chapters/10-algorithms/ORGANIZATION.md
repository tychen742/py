# Chapter 10 Organization (Algorithms)

This chapter is currently split into:

- `1000-intro-algorithms.ipynb` (overview and survey)
- `1001-searching.ipynb` (placeholder)
- `1002-sorting.ipynb` (placeholder)

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1000-intro-algorithms.ipynb`
   - What algorithms are
   - Time/space complexity and Big O intuition
   - High-level preview of search/sort/graph/dp/greedy
2. `1001-searching.ipynb`
   - Linear search
   - Binary search
   - Search trade-offs by data condition (sorted vs unsorted, static vs dynamic)
3. `1002-sorting.ipynb`
   - Built-in sort with `key=`
   - Selection/bubble/insertion (conceptual baseline)
   - Merge/quick (divide-and-conquer framing)
   - Stability and in-place vs out-of-place trade-offs

## File Roles

- `1000-intro-algorithms.ipynb`: concept framing only; avoid deep code labs.
- `1001-searching.ipynb`: coding lab + complexity comparison.
- `1002-sorting.ipynb`: coding lab + benchmarking.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/10-algorithms/*` as the only Chapter 10 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Prefer small benchmark inputs in notebooks to keep runtime fast.
- Add at least one checkpoint exercise in each of `1001` and `1002`.
- Ensure chapter outcomes align with any Chapter 10 assignment/quiz prompt.
