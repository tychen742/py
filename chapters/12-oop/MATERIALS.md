# Chapter 12 Materials (Object-Oriented Programming)

This checklist is for building and delivering:

- `1200-intro-oop.ipynb`
- `1201-oop-design.ipynb`
- `1202-oop-practice.ipynb`

## Must-Have Teaching Materials

- Slide deck or notes covering:
  - Classes and instances; `__init__`, `__str__`, `__repr__`
  - Attributes and methods; `@staticmethod`, `@classmethod`, `@property`
  - Encapsulation; operator overloading
  - Inheritance; polymorphism; method overriding; `super()`
  - `issubclass()`; `@dataclass`
- Code examples and demos ready to run in class
- Practice dataset or starter code where applicable

## Notebook Content Targets

### `1200-intro-oop.ipynb`

- What OOP is; classes vs instances; motivation; first class (`Point`); `isinstance()`, `type()`

### `1201-oop-design.ipynb`

- Programmer-defined types; `__init__`, `__str__`, `__repr__`; object mutation and copying;
  pure functions vs. modifier methods; `@staticmethod`; `@classmethod` (alternative constructors);
  `@property` (controlled read-only access); operator overloading (`__add__`, etc.);
  Point, Line, Rectangle examples; equivalence vs. identity; deep copy

### `1202-oop-practice.ipynb`

- Inheritance; method overriding; polymorphism; `super()` (calling parent `__init__`);
  `issubclass()` (runtime class relationship checks); `@dataclass` (boilerplate-free data classes);
  applied design: card game (Deck, Card, Hand as Deck subclass)

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
3. `1202-oop-practice.ipynb` — Inheritance, overriding, polymorphism; hands-on class design

## Coordination Note

Chapter 12 planning and delivery are scoped to `chapters/12-oop/` only.
