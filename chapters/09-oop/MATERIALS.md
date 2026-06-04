# Chapter 09 Materials (Object-Oriented Programming)

This checklist is for building and delivering:

- `0900-intro-oop.ipynb`
- `0901-oop-design.ipynb` *(merged from former `1202-oop-methods`)*
- `0902-oop-pillars.ipynb`
- `0903-oop-advanced.ipynb`

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

### `0900-intro-oop.ipynb`

- Required core:
  - What OOP is; classes vs instances; motivation; first class (`Point`); `isinstance()`, `type()`
- Enrichment/project track:
  - Additional analogy-driven examples as time permits

### `0901-oop-design.ipynb`

- Required core:
  - Programmer-defined types; `__init__`, `__str__`, `__repr__`; object mutation and copying
  - Pure functions vs. modifier methods; `@staticmethod`; `@classmethod`; `@property`
  - One operator-overloading example (`__add__` or equivalent)
- Enrichment/project track:
  - Additional operator-overloading variants and extended design drills

### `0902-oop-pillars.ipynb`

- Required core:
  - The Four Pillars: encapsulation, inheritance, polymorphism, abstraction
  - One focused code example per pillar
- Enrichment/project track:
  - Extended examples comparing pillar trade-offs across different class designs

### `0903-oop-advanced.ipynb`

- Required core:
  - Inheritance; method overriding; polymorphism
  - `super()`; `issubclass()`; `@dataclass`; `namedtuple`
  - Composition vs inheritance rubric with one short design checkpoint
- Enrichment/project track:
  - Full applied card game (Deck, Card, Hand as Deck subclass)
  - Extended ABC/Protocol implementations for interchangeable designs
  - Shallow copy vs. deep copy; `copy.copy` vs. `copy.deepcopy`
  - Object identity vs. equality (`is` vs. `==`) extended examples

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

## Chapter 09 Delivery Order (Recommended)

1. `0900-intro-oop.ipynb` — What OOP is; classes vs instances; motivation
2. `0901-oop-design.ipynb` — `__init__`, attributes, methods, self; encapsulation principles
3. `0902-oop-pillars.ipynb` — Encapsulation, inheritance, polymorphism, and abstraction
4. `0903-oop-advanced.ipynb` — Inheritance/polymorphism practice; advanced object-state topics

## Coordination Note

Chapter 09 planning and delivery are scoped to `chapters/09-oop/` only.

## Assignments

- `assignments/preview.ipynb` — Preview questions
- `assignments/homework.ipynb` — Homework questions
- `assignments/lab.ipynb` — Lab assignment
