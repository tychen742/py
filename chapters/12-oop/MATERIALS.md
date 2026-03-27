# Chapter 12 Materials (Object-Oriented Programming)

This checklist is for building and delivering:

- `1200-intro-oop.ipynb`
- `1201-oop-design.ipynb`
- `1201b-oop-objects.ipynb`
- `1202-oop-practice.ipynb`

## Must-Have Teaching Materials

- Slide deck or notes covering:
  - Classes and instances; `__init__`, `__str__`, `__repr__`
  - Attributes and methods; `@staticmethod`, `@classmethod`, `@property`
  - Encapsulation; operator overloading
  - Inheritance; polymorphism; method overriding; `super()`
  - `issubclass()`; `@dataclass`
  - Composition vs inheritance trade-offs; ABC/Protocol concepts for interface design
- Code examples and demos ready to run in class
- Practice dataset or starter code where applicable

## Notebook Content Targets

Use a two-tier model for one chapter per week:

- **Required core**: must be covered in lecture/lab and assessed
- **Enrichment/project track**: optional, extra credit, or follow-up content

### `1200-intro-oop.ipynb`

- Required core:
  - What OOP is; classes vs instances; motivation; first class (`Point`); `isinstance()`, `type()`
- Enrichment/project track:
  - Additional analogy-driven examples as time permits

### `1201-oop-design.ipynb`

- Required core:
  - Programmer-defined types; `__init__`, `__str__`, `__repr__`; object mutation and copying
  - Pure functions vs. modifier methods; `@staticmethod`; `@classmethod`; `@property`
  - One operator-overloading example (`__add__` or equivalent)
- Enrichment/project track:
  - Additional operator-overloading variants and extended design drills

### `1201b-oop-objects.ipynb`

- Required core:
  - Point and Line construction
  - Equivalence vs identity (`==` vs `is`)
- Enrichment/project track:
  - Rectangle mutation walkthroughs
  - Deep-copy edge cases and extra geometry exercises

### `1202-oop-practice.ipynb`

- Required core:
  - Inheritance; method overriding; polymorphism
  - `super()`; `issubclass()`; `@dataclass`
  - Composition vs inheritance rubric with one short design checkpoint
- Enrichment/project track:
  - Full applied card game (Deck, Card, Hand as Deck subclass)
  - Extended ABC/Protocol implementations for interchangeable designs

## Practice and Assessment Pack

- In-class checks:
  - 2–3 conceptual poll/discussion questions
  - 1–2 "predict the output" questions
- Lab tasks:
  - Design and instantiate a class; extend it with a subclass
- Homework:
  - Model a real-world entity as a class hierarchy with at least two levels
- Grading anchors:
  - Correctness
  - Code clarity and style
  - Understanding shown in comments or docstrings

## Reusable Assets to Prepare

- Shared starter code snippets
- Any datasets or input files needed by exercises
- Solution cells (tagged `hide-input`) for all exercises

## Chapter 12 Delivery Order (Recommended)

1. `1200-intro-oop.ipynb` — What OOP is; classes vs instances; motivation
2. `1201-oop-design.ipynb` — `__init__`, attributes, methods, self; encapsulation principles
3. `1201b-oop-objects.ipynb` — Point/Line object modeling and identity/equivalence checks
4. `1202-oop-practice.ipynb` — Inheritance/polymorphism core first; card-game extension as enrichment

## Coordination Note

Chapter 12 planning and delivery are scoped to `chapters/12-oop/` only.
