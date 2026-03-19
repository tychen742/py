# Chapter 14 Organization (Iterators and Generators)

This chapter is currently split into:

- `1400-intro-iter-gen.ipynb`
- `1401-iterators.ipynb`
- `1402-generators.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1400-intro-iter-gen.ipynb`
   - Iteration protocol; iter() and next(); lazy evaluation motivation
2. `1401-iterators.ipynb`
   - Custom iterator classes; __iter__ and __next__
3. `1402-generators.ipynb`
   - Generator functions (yield); generator expressions; memory efficiency

## File Roles

- `1400-intro-iter-gen.ipynb`: Iteration protocol; iter() and next(); lazy evaluation motivation.
- `1401-iterators.ipynb`: Custom iterator classes; __iter__ and __next__.
- `1402-generators.ipynb`: Generator functions (yield); generator expressions; memory efficiency.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/14-iter-gen/*` as the only Chapter 14 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 14 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
