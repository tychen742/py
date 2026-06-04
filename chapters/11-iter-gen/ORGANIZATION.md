# Chapter 11 Organization (Iterators and Generators)

This chapter is split into:

- `1100-intro-iter-gen.ipynb`
- `1101-iterators.ipynb`
- `1102-generators.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1100-intro-iter-gen.ipynb`
   - Chapter intro: learning goals, motivation, chapter flow map. No exercises.
2. `1101-iterators.ipynb`
   - Iterator protocol; `iter()`/`next()` manually; built-in lazy iterators
     (`enumerate`, `zip`, `map`, `filter`, `reversed`); custom iterator classes
     (`__iter__`/`__next__`/`StopIteration`); 1 exercise
3. `1102-generators.ipynb`
   - Generator functions (`yield`); generator expressions; memory efficiency (`sys.getsizeof`);
     `any()`/`all()` with generator expressions (short-circuit evaluation);
     infinite sequences; `itertools.islice`, `itertools.chain`;
     `yield from` (generator delegation); `itertools.count`, `itertools.cycle`,
     `itertools.combinations`, `itertools.permutations`;
     conceptual bridge to asynchronous iteration (`async for`, async generators);
     3 exercises

## One-Week Delivery Scope (Required vs Enrichment)

### Required Core (in-class + required homework)

- `1100-intro-iter-gen.ipynb`
  - Full notebook
- `1101-iterators.ipynb`
  - Iterator protocol, `iter()`/`next()`, and one custom iterator class
  - Built-in lazy iterators (`enumerate`, `zip`, `map`, `filter`, `reversed`)
- `1102-generators.ipynb`
  - Generator functions, generator expressions, memory-efficiency framing
  - `itertools.islice`, `itertools.chain`, and one infinite-sequence pattern
  - `yield from` concept and async-iteration bridge (conceptual)

### Enrichment / Project Track (optional, extra credit, or follow-up week)

- `1101-iterators.ipynb`
  - Additional custom iterator design drills
- `1102-generators.ipynb`
  - Extended `itertools` combinatorics (`count`, `cycle`, `combinations`, `permutations`)
  - Additional streaming-data mini-projects and benchmarking exercises

## File Roles

- `1100-intro-iter-gen.ipynb`: Chapter intro — learning goals and chapter map. No exercises.
- `1101-iterators.ipynb`: Iterator protocol; built-in iterators; custom iterator classes.
  Exercise: Cycling Iterator.
- `1102-generators.ipynb`: Generator functions; generator expressions; `any()`/`all()` with generator
  expressions (short-circuit evaluation); infinite sequences; `itertools.islice`, `itertools.chain`;
  `yield from`; `itertools.count/cycle/combinations/permutations`.
  Exercises: Running Total Generator; `any()`/`all()`; itertools.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/11-iter-gen/*` as the only Chapter 11 track for planning, delivery, and assessment.

## Archived Files

`0701-databases.ipynb` was archived in `materials/_archived/ch11-iter-gen-stray/` because it is not part of the active Chapter 11 sequence.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 11 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview questions
- `assignments/homework.ipynb` — Homework questions
- `assignments/lab.ipynb` — Lab assignment
