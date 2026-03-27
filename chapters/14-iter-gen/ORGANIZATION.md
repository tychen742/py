# Chapter 14 Organization (Iterators and Generators)

This chapter is currently split into:

- `1400-intro-iter-gen.ipynb`
- `1401-iterators.ipynb`
- `1402-generators.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1400-intro-iter-gen.ipynb`
   - Chapter intro: learning goals, motivation, chapter flow map. No exercises.
2. `1401-iterators.ipynb`
   - Iterator protocol; `iter()`/`next()` manually; built-in lazy iterators
     (`enumerate`, `zip`, `map`, `filter`, `reversed`); custom iterator classes
     (`__iter__`/`__next__`/`StopIteration`); 1 exercise
3. `1402-generators.ipynb`
   - Generator functions (`yield`); generator expressions; memory efficiency (`sys.getsizeof`);
     infinite sequences; `itertools.islice`, `itertools.chain`;
     `yield from` (generator delegation); `itertools.count`, `itertools.cycle`,
     `itertools.combinations`, `itertools.permutations`; 2 exercises

## File Roles

- `1400-intro-iter-gen.ipynb`: Chapter intro — learning goals and chapter map. No exercises.
- `1401-iterators.ipynb`: Iterator protocol; built-in iterators; custom iterator classes.
  Exercise: Cycling Iterator.
- `1402-generators.ipynb`: Generator functions; generator expressions; infinite sequences;
  `itertools.islice`, `itertools.chain`; `yield from`; `itertools.count/cycle/combinations/permutations`.
  Exercises: Running Total Generator; itertools.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/14-iter-gen/*` as the only Chapter 14 track for planning, delivery, and assessment.

## Stray Files

`0701-databases.ipynb` is in this folder but belongs to Chapter 7. It should be relocated to `chapters/07-tuples/` or deleted.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 14 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
