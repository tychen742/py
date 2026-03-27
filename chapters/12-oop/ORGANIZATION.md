# Chapter 12 Organization (Object-Oriented Programming)

This chapter is currently split into:

- `1200-intro-oop.ipynb`
- `1201-oop-design.ipynb`
- `1202-oop-practice.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1200-intro-oop.ipynb`
   - What OOP is and why it exists; class vs. instance analogy
   - `__init__`, `__str__`, `isinstance()`, `type()`
   - A first class (`Point`); `Temperature` exercise
2. `1201-oop-design.ipynb`
   - Programmer-defined types, attributes, object mutation, copying
   - Pure functions vs. modifier methods; prototype-and-patch design
   - Classes and methods: `__init__`, `__str__`, `__repr__`, `@staticmethod`, `@classmethod`
   - `@property` for controlled read-only access
   - Operator overloading (`__add__`, etc.)
   - Point, Line, Rectangle class examples; equivalence vs. identity; deep copy
3. `1202-oop-practice.ipynb`
   - Inheritance; polymorphism; method overriding; parent and child classes
   - `super()` for calling parent `__init__`; `issubclass()` for runtime class relationship checks
   - `@dataclass` for boilerplate-free data classes
   - Applied class design: card game (representing, comparing, deck operations)
   - Specialization: Hand as a subclass of Deck

## File Roles

- `1200-intro-oop.ipynb`: Chapter intro — OOP motivation, class/instance concepts, first class, exercise.
- `1201-oop-design.ipynb`: Core OOP mechanics. Classes, methods, `__init__`, `__str__`, `__repr__`, `@staticmethod`, `@classmethod`, `@property`, operator overloading, Point/Line/Rectangle examples.
- `1202-oop-practice.ipynb`: Inheritance, polymorphism, method overriding; `super()`, `issubclass()`, `@dataclass`; applied OOP via the card game case study.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Known Structural Issues (to address in a future pass)

- `1201` is oversized — two ThinkPython chapters merged into one notebook. Candidate split: keep `## Classes and Functions` + `## Design-First Development` in `1201`; move `## Classes and Objects` (Point/Line/Rectangle) to a new `1201b` or restructured `1202`.
- `1202` mixes conceptual content (inheritance/polymorphism) with a long applied project (card game). Consider splitting into a concepts notebook and a project notebook.
- The card game section is essentially a direct port from ThinkPython and may benefit from a fresher motivating example.

## Source of Truth

Use `chapters/12-oop/*` as the only Chapter 12 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 12 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
