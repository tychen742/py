# Chapter 12 Organization (Object-Oriented Programming)

This chapter is split into:

- `1200-intro-oop.ipynb`
- `1201-oop-design.ipynb`
- `1201b-oop-objects.ipynb`
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
3. `1201b-oop-objects.ipynb`
   - Point, Line, Rectangle class examples (applied geometry library)
   - Creating and printing objects; equivalence vs. identity (`==` vs. `is`)
   - Mutating objects; deep vs. shallow copy
4. `1202-oop-practice.ipynb`
   - Inheritance; polymorphism; method overriding; parent and child classes
   - `super()` for calling parent `__init__`; `issubclass()` for runtime class relationship checks
   - `@dataclass` for boilerplate-free data classes
   - Composition vs inheritance decision guide
   - Interface-oriented design with ABC/Protocol-level concepts
   - Applied class design: card game (representing, comparing, deck operations)
   - Specialization: Hand as a subclass of Deck

## One-Week Delivery Scope (Required vs Enrichment)

To keep Chapter 12 realistic for one week, deliver in two tiers.

### Required Core (in-class + required homework)

- `1200-intro-oop.ipynb`
   - Full notebook
- `1201-oop-design.ipynb`
   - Required sections: `## Classes and Functions`, `## Design-First Development`
   - Keep one operator-overloading example only (minimal demonstration)
- `1201b-oop-objects.ipynb`
   - Required sections: Point creation, Line creation, equivalence vs identity (`==` vs `is`)
- `1202-oop-practice.ipynb`
   - Required sections: inheritance basics, method overriding, polymorphism,
      `super()`, `issubclass()`, `@dataclass`, composition vs inheritance rubric

### Enrichment / Project Track (optional, extra credit, or follow-up week)

- `1201-oop-design.ipynb`
   - Remaining deep operator-overloading patterns
- `1201b-oop-objects.ipynb`
   - Extended rectangle mutation/copying drills beyond first pass
- `1202-oop-practice.ipynb`
   - Full card-game build-out and Hand-as-Deck specialization
   - Extended interface-oriented design patterns (ABC/Protocol implementations)

## File Roles

- `1200-intro-oop.ipynb`: Chapter intro — OOP motivation, class/instance concepts, first class, exercise.
- `1201-oop-design.ipynb`: Core OOP mechanics — classes and functions, design-first development, operator overloading.
- `1201b-oop-objects.ipynb`: Applied geometry library — Point, Line, Rectangle; equivalence, mutation, deep copy.
- `1202-oop-practice.ipynb`: Inheritance, polymorphism, method overriding; `super()`, `issubclass()`, `@dataclass`; applied OOP via the card game case study.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Known Structural Issues (to address in a future pass)

- `1202` still mixes conceptual content (inheritance/polymorphism) with a long applied project (card game). Keep project sections optional in one-week delivery, or split into a concepts notebook and project notebook.
- The card game section is essentially a direct port from ThinkPython and may benefit from a fresher motivating example.

## Source of Truth

Use `chapters/12-oop/*` as the only Chapter 12 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 12 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
