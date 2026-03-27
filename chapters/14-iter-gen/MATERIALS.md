# Chapter 14 Materials (Iterators and Generators)

This checklist is for building and delivering:

- `1400-intro-iter-gen.ipynb`
- `1401-iterators.ipynb`
- `1402-generators.ipynb`

## Must-Have Teaching Materials

- Slide deck or notes covering:
  - Iteration protocol; `iter()`/`next()`/`StopIteration`
  - Custom iterator classes (`__iter__`/`__next__`)
  - Generator functions (`yield`, lazy evaluation); `yield from` (delegation)
  - Generator expressions; `itertools.islice`, `itertools.chain`
  - `itertools.count`, `itertools.cycle`, `itertools.combinations`, `itertools.permutations`
- Code examples and demos ready to run in class
- Practice dataset or starter code where applicable

## Notebook Content Targets

### `1400-intro-iter-gen.ipynb`

- Chapter intro: learning goals, motivation, chapter flow map (no exercises)

### `1401-iterators.ipynb`

- Iterator protocol; `iter()`/`next()` manually; `StopIteration`; built-in lazy
  iterators (`enumerate`, `zip`, `map`, `filter`, `reversed`); custom iterator
  classes (`__iter__`/`__next__`)
- Exercise: Cycling Iterator (infinite `Cycle` class using `itertools.islice`)

### `1402-generators.ipynb`

- Generator functions (`yield`, lazy evaluation); generator expressions;
  memory efficiency (`sys.getsizeof`); infinite sequences;
  `itertools.islice`, `itertools.chain`;
  `yield from` (generator delegation to sub-generators);
  `itertools.count`, `itertools.cycle`, `itertools.combinations`, `itertools.permutations`
- Exercises: Running Total Generator + even squares generator expression; itertools

## Practice and Assessment Pack

- In-class checks:
  - 2–3 conceptual poll/discussion questions
  - 1–2 "predict the output" questions
- Lab tasks:
  - Build a custom iterator; convert a list-based function to a generator
- Homework:
  - Implement an infinite sequence generator; benchmark memory use vs list
- Grading anchors:
  - Correctness
  - Code clarity and style
  - Understanding shown in comments or docstrings

## Reusable Assets to Prepare

- Shared starter code snippets
- Any datasets or input files needed by exercises
- Solution cells (tagged `hide-input`) for all exercises

## Chapter 14 Delivery Order (Recommended)

1. `1400-intro-iter-gen.ipynb` — Chapter intro: learning goals and chapter flow map
2. `1401-iterators.ipynb` — Iterator protocol; built-in iterators; custom iterator classes
3. `1402-generators.ipynb` — Generator functions; generator expressions; infinite sequences

## Coordination Note

Chapter 14 planning and delivery are scoped to `chapters/14-iter-gen/` only.
