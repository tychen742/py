# Chapter 10 Organization (Object-Oriented Programming)

This chapter is split into:

- `1000-intro-oop.ipynb`
- `1001-oop-design.ipynb` *(merged from former `1202-oop-methods`)*
- `1002-oop-pillars.ipynb`
- `1003-oop-advanced.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1000-intro-oop.ipynb`
   - What OOP is and why it exists; class vs. instance analogy
   - `__init__`, `__str__`, `isinstance()`, `type()`
   - A first class (`Point`); `Temperature` exercise
2. `1001-oop-design.ipynb`
   - Programmer-defined types, attributes, object mutation, copying
   - Pure functions vs. modifier methods; design-first development (`Time` as base-60 example)
   - Classes and methods: `__init__`, `__str__`, `__repr__`, `@staticmethod`, `@classmethod`
   - `@property` for controlled read-only access
   - Operator overloading (`__add__`, etc.)
3. `1002-oop-pillars.ipynb`
   - The Four Pillars of OOP: encapsulation, inheritance, polymorphism, abstraction
   - Each pillar shown with a focused, self-contained code example
4. `1003-oop-advanced.ipynb`
   - Inheritance; polymorphism; method overriding; parent and child classes
   - `super()` for calling parent `__init__`; `issubclass()` for runtime class relationship checks
   - `@dataclass` for boilerplate-free data classes
   - Composition vs inheritance decision guide
   - Interface-oriented design with ABC/Protocol-level concepts
   - Applied class design: card game (representing, comparing, deck operations)
   - Specialization: Hand as a subclass of Deck
   - Object copying: shallow copy vs. deep copy
   - Object identity vs. equality (`is` vs. `==`)
   - Additional advanced object-state topics

## One-Week Delivery Scope (Required vs Enrichment)

To keep Chapter 10 realistic for one week, deliver in two tiers.

### Required Core (in-class + required homework)

- `1000-intro-oop.ipynb`
   - Full notebook
- `1001-oop-design.ipynb`
   - Required sections: classes and methods (`__init__`, `__str__`, `__repr__`), design-first development
   - Keep one operator-overloading example only (minimal demonstration)
- `1002-oop-pillars.ipynb`
   - Full notebook (concise; good conceptual anchoring)
- `1003-oop-advanced.ipynb`
   - Required sections: inheritance basics, method overriding, polymorphism,
      `super()`, `issubclass()`, `@dataclass`, composition vs inheritance rubric

### Enrichment / Project Track (optional, extra credit, or follow-up week)

- `1001-oop-design.ipynb`
   - Remaining deep operator-overloading patterns; `@classmethod`, `@property` deep dives
- `1003-oop-advanced.ipynb`
   - Full card-game build-out and Hand-as-Deck specialization
   - Extended interface-oriented design patterns (ABC/Protocol implementations)

## File Roles

- `1000-intro-oop.ipynb`: Chapter intro — OOP motivation, class/instance concepts, first class, exercise.
- `1001-oop-design.ipynb`: Core OOP mechanics — design-first development, all method types (`__init__`, `__str__`, `__repr__`, `@staticmethod`, `@classmethod`, `@property`), operator overloading. *(Merged from former `1202-oop-methods`.)*
- `1002-oop-pillars.ipynb`: The Four Pillars of OOP — encapsulation, inheritance, polymorphism, abstraction; one example each.
- `1003-oop-advanced.ipynb`: Inheritance, polymorphism, method overriding; `super()`, `issubclass()`, `@dataclass`, `namedtuple`; applied OOP via the card game case study; advanced object-state topics.
- `MATERIALS.md`: teaching/assessment assets and prep checklist.

## Known Structural Issues (to address in a future pass)

- `1003-oop-advanced` still mixes conceptual content (inheritance/polymorphism) with a long applied project (card game). Keep project sections optional in one-week delivery, or split into a concepts notebook and project notebook.
- The card game section is essentially a direct port from ThinkPython and may benefit from a fresher motivating example.

## Source of Truth

Use `chapters/10-oop/*` as the only Chapter 10 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 10 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
