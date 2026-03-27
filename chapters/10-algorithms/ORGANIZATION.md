# Chapter 10 Organization (Algorithms)

This chapter is split into:

- `1000-intro-algorithms.ipynb` (chapter intro stub — title and chapter map only)
- `1001-algorithms.ipynb` (algorithm concepts: design, Big O, benchmarking, selection guide)
- `1002-searching.ipynb` (searching: linear, binary, bisect module, hash-based, benchmarking)
- `1003-sorting.ipynb` (sorting: built-in, insertion, bubble, merge, quick, benchmarking)

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1000-intro-algorithms.ipynb`
   - Chapter intro stub: title and chapter flow map. No exercises.
2. `1001-algorithms.ipynb`
   - What algorithms are; design process; control patterns (sequence/decision/repetition)
   - Time complexity and space complexity; Big O intuition (O(1) through O(n²))
   - Best/average/worst-case reasoning and trade-offs by input pattern
   - Benchmarking basics (`time.perf_counter`, `timeit.timeit`, `timeit.repeat`)
   - Algorithm design checklist (input → process → output)
   - Algorithm Selection Guide table
3. `1002-searching.ipynb`
   - Linear search
   - Binary search (manual iterative implementation with sorted-input caveat)
   - `bisect` module (own `##` section): `bisect_left`/`bisect_right` for lookup;
     `insort` for maintaining sorted order; compare with manual implementation
   - Hash-based lookup (`set`/`dict`) — compared with linear and binary
   - Search trade-offs by data condition (sorted vs unsorted, static vs dynamic)
4. `1003-sorting.ipynb`
   - Built-in sort with `key=` and stability
   - Insertion sort (educational baseline, in-place)
   - Bubble sort (teaching baseline, in-place, for contrast)
   - Merge sort and quick sort (divide-and-conquer framing)
   - Stability and in-place vs out-of-place decision criteria
   - Benchmarking across input patterns (random, sorted, reverse, duplicates)

## One-Week Delivery Scope (Required vs Enrichment)

### Required Core (in-class + required homework)

- `1000-intro-algorithms.ipynb`
   - Full notebook
- `1001-algorithms.ipynb`
   - Big O intuition, best/average/worst-case framing, selection guide
- `1002-searching.ipynb`
   - Linear and binary search, plus one `bisect` and one hash-lookup comparison
- `1003-sorting.ipynb`
   - Built-in sort, insertion and merge (required implementations)
   - Space complexity and stability trade-off discussion

### Enrichment / Project Track (optional, extra credit, or follow-up week)

- `1002-searching.ipynb`
   - Full `bisect`/`insort` comparison extensions and extra benchmarking variants
- `1003-sorting.ipynb`
   - Bubble and quick sort deeper comparison labs
   - Counting-sort extension and expanded benchmark matrix

## File Roles

- `1000-intro-algorithms.ipynb`: Chapter intro stub. No exercises.
- `1001-algorithms.ipynb`: Algorithm concepts, Big O, benchmarking, selection guide. No exercises (intro-level framing notebook).
- `1002-searching.ipynb`: coding lab + bisect module + hash-based lookup + exercises.
- `1003-sorting.ipynb`: coding lab + benchmarking + exercises.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/10-algorithms/*` as the only Chapter 10 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Prefer small benchmark inputs in notebooks to keep runtime fast.
- `1000` and `1001` have no exercises (`1001` is concept framing).
- `1002` and `1003` each have exercises per section.
- Pass fresh copies to in-place sorts (insertion, bubble) in tests and benchmarks.
- Ensure chapter outcomes align with any Chapter 10 assignment/quiz prompt.
