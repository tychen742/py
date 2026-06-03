---
marp: true
theme: default
paginate: true
style: |
  section { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 20px; color: #1a1a1a; padding: 30px 50px 60px 50px; background: white; }
  h1 { color: #2a6b37; font-size: 1.8em; border-bottom: 3px solid #b8860b; padding-bottom: 8px; margin-bottom: 16px; }
  h2 { color: #2a6b37; font-size: 1.35em; margin-bottom: 10px; }
  h3 { color: #b8860b; font-size: 1.05em; margin-bottom: 6px; }
  ul { margin-left: 1.2em; } li { margin-bottom: 4px; line-height: 1.4; }
  section.title { background: #2a6b37; color: white; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; }
  section.title h1 { color: white; border: none; font-size: 2.2em; }
  section.title p { color: #c8e6c9; font-size: 0.95em; }
  section.section { background: #2a6b37; color: white; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; }
  section.section h2 { color: white; border: none; font-size: 1.9em; }
  section.section p  { color: #c8e6c9; font-size: 0.95em; }
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; align-items: start; }
  .cols.r46 { grid-template-columns: 4fr 6fr; }
  .callout { background: #e8f5eb; border-left: 4px solid #2a6b37; border-radius: 4px; padding: 7px 11px; margin: 8px 0; font-size: 0.72em; line-height: 1.35; }
  .callout.warn { background: #fff8e1; border-color: #b8860b; }
  .callout.rule { background: #f0f4ff; border-color: #5577cc; }
  pre { background: #f6f8fa !important; border: 1px solid #d0e8d4; border-radius: 6px; margin: 8px 0; font-size: 0.68em; line-height: 1.35; }
  code { color: #c7254e; background: #f6f8fa; border: 1px solid #e0e0e0; border-radius: 3px; padding: 1px 4px; }
  pre code { color: inherit; background: none; border: none; padding: 12px 14px; }
  table { font-size: 0.68em; border-collapse: collapse; width: 100%; }
  th { background: #2a6b37; color: white; padding: 5px 8px; text-align: left; }
  td { padding: 5px 8px; border-bottom: 1px solid #e0e0e0; }
  tr:nth-child(even) td { background: #f7faf7; }
  .grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 8px; }
  .grid3 > div { background: #f6f8fa; border: 1px solid #d0e8d4; border-radius: 5px; padding: 8px 10px; font-size: 0.72em; }
  .grid3 > div strong { color: #2a6b37; display: block; margin-bottom: 2px; }
  section::after { color: #aaa; font-size: 0.7em; }
---

<!-- _class: title -->

# Chapter 10

Object-Oriented Programming

*10.0 Intro · 10.1 Design & Methods · 10.2 Four Pillars · 10.3 Advanced Topics*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## What is OOP?

Organizing code around *objects* that combine data and behavior

---

## Why Object-Oriented Programming?

<div class="cols">
<div>

### Procedural approach

Data and functions are separate — you pass data to functions and hope nothing breaks.

```python
name = "Lia"
balance = 100.0

def deposit(balance, amount):
    return balance + amount

balance = deposit(balance, 50)
```

</div>
<div>

### OOP approach

Data and behavior are bundled together — the object knows what it can do.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

acc = BankAccount("Lia", 100.0)
acc.deposit(50)
```

</div>
</div>

<div class="callout">

OOP benefits: **encapsulation** (data is protected), **reuse** (inherit & extend), **modeling** (code mirrors the real world).

</div>

---

<!-- _class: section -->

## 10.1 Design & Methods

Classes, instances, `__init__`, methods, properties

---

## Classes and Instances

<div class="cols">
<div>

- A **class** is a blueprint.
- An **instance** is one concrete object created from that blueprint.
- `self` refers to *this* instance inside the class.
- Each instance has its own copy of instance attributes.

<div class="callout">

`type(obj)` → the class · `isinstance(obj, Cls)` → membership check

</div>

</div>
<div>

```python
class Point:
    def __init__(self, x, y):
        self.x = x   # instance attribute
        self.y = y

    def distance_to(self, other):
        return ((self.x - other.x)**2 +
                (self.y - other.y)**2) ** 0.5

p1 = Point(0, 0)   # instance
p2 = Point(3, 4)

print(p1.distance_to(p2))   # 5.0
print(isinstance(p1, Point)) # True
```

</div>
</div>

---

## The `__init__` Method

<div class="cols">
<div>

- Called automatically when an instance is created.
- Sets up **instance attributes** on `self`.
- Can have default parameter values.
- Does not `return` anything (implicitly `None`).

</div>
<div>

```python
class BankAccount:
    def __init__(self, owner="Unknown",
                 balance=0.0):
        self.owner = owner
        self._balance = balance  # _ = convention

acc = BankAccount("Lia", 500.0)
print(acc.owner)    # Lia
print(acc._balance) # 500.0
```

</div>
</div>

---

## Key Dunder Methods

<div class="grid3">
<div><strong>__init__</strong> Called on creation; sets up attributes.</div>
<div><strong>__str__</strong> Human-readable string; called by <code>print()</code>.</div>
<div><strong>__repr__</strong> Developer string; called in the REPL.</div>
<div><strong>__eq__</strong> Defines <code>==</code> between objects.</div>
<div><strong>__lt__</strong> Defines <code>&lt;</code>; enables sorting.</div>
<div><strong>__hash__</strong> Needed for use as dict key or in a set.</div>
<div><strong>__add__</strong> Defines <code>+</code> operator.</div>
<div><strong>__len__</strong> Defines <code>len(obj)</code>.</div>
<div><strong>__contains__</strong> Defines <code>in</code> operator.</div>
</div>

<div class="callout rule" style="margin-top:12px;">

Dunder = "double underscore". Python calls them automatically behind the scenes.

</div>

---

## Properties — `@property`

<div class="cols r46">
<div>

- Use a method like an attribute.
- Add **computed** or **validated** access.
- Use `@attr.setter` to validate writes.

<div class="callout warn">

`_balance` signals internal use. It is a *convention*, not enforcement.

</div>

</div>
<div>

```python
class BankAccount:
    def __init__(self, balance=0.0):
        self._balance = balance

    @property
    def balance(self):          # getter
        return self._balance

    @balance.setter
    def balance(self, value):   # setter
        if value < 0:
            raise ValueError("Negative balance")
        self._balance = value

acc = BankAccount(100)
print(acc.balance)   # 100  (no parentheses!)
acc.balance = 200    # calls setter
acc.balance = -5     # raises ValueError
```

</div>
</div>

---

<!-- _class: section -->

## 10.2 The Four Pillars of OOP

Encapsulation · Polymorphism · Inheritance · Abstraction

---

## Encapsulation

<div class="cols">
<div>

Bundle data + behavior together, and **restrict** direct access to internals.

| Convention | Meaning |
|---|---|
| `name` | Public — use freely |
| `_name` | Internal — avoid outside class |
| `__name` | Name-mangled — strongest hint |

<div class="callout">

Python relies on *convention*, not hard enforcement. Respect the single underscore.

</div>

</div>
<div>

```python
class Thermostat:
    def __init__(self, temp):
        self._temp = temp   # internal state

    @property
    def temperature(self):
        return self._temp

    def set_temperature(self, value):
        if value < 0 or value > 40:
            raise ValueError("Out of range")
        self._temp = value

t = Thermostat(22)
t.set_temperature(25)   # OK
t.set_temperature(100)  # ValueError
```

</div>
</div>

---

## Inheritance

<div class="cols">
<div>

- A **child class** inherits all attributes and methods of its **parent**.
- Use `super()` to call the parent's method.
- `issubclass(Child, Parent)` → `True`
- Child can **override** any parent method.

</div>
<div>

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):          # override
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):          # override
        return f"{self.name} meows"

pets = [Dog("Rex"), Cat("Luna")]
for p in pets:
    print(p.speak())
# Rex barks
# Luna meows
```

</div>
</div>

---

## Polymorphism

<div class="cols">
<div>

- Same method name, different behavior depending on the object's type.
- Lets you write code that works on *any* object with the right interface.
- Achieved through **method overriding** and **duck typing**.

<div class="callout rule">

**Duck typing:** If it walks like a duck and quacks like a duck, it's a duck. Python checks behavior, not type.

</div>

</div>
<div>

```python
class Shape:
    def area(self): ...

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r**2

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

shapes = [Circle(5), Rectangle(3, 4)]
for s in shapes:
    print(s.area())   # each behaves correctly
```

</div>
</div>

---

## Abstraction & Abstract Base Classes

<div class="cols">
<div>

- Hide implementation details; expose only what the caller needs.
- **Abstract Base Class (ABC)** defines a required interface.
- Any subclass *must* implement the abstract methods or Python raises `TypeError`.

<div class="callout warn">

You cannot instantiate an abstract class directly.

</div>

</div>
<div>

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def charge(self, amount): ...

class CreditCard(PaymentMethod):
    def charge(self, amount):
        print(f"Charging ${amount} to card")

class PayPal(PaymentMethod):
    def charge(self, amount):
        print(f"Sending ${amount} via PayPal")

# PaymentMethod()  ← TypeError!
cc = CreditCard()
cc.charge(50)   # Charging $50 to card
```

</div>
</div>

---

## Class Variables & `super()`

<div class="cols">
<div>

### Class Variables

Shared across *all* instances. Set on the class, not on `self`.

```python
class Counter:
    count = 0           # class variable

    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
print(Counter.count)  # 2
```

</div>
<div>

### `super()`

Call the parent class's method without hardcoding the parent's name.

```python
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance,
                 interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance *= (1 + self.interest_rate)
```

</div>
</div>

---

<!-- _class: section -->

## 10.3 Advanced OOP Topics

Comparison dunders · Operator overloading · `@dataclass` · Static & class methods

---

## Comparison Dunder Methods

<div class="cols">
<div>

| Method | Operator |
|---|---|
| `__eq__` | `==` |
| `__lt__` | `<` |
| `__le__` | `<=` |
| `__gt__` | `>` |
| `__ge__` | `>=` |

<div class="callout rule">

**Shortcut:** Define `__eq__` + one ordering method, then use `@functools.total_ordering` to derive the rest.

</div>

</div>
<div>

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __eq__(self, other):
        return self.gpa == other.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

s1 = Student("Alice", 3.8)
s2 = Student("Bob",   3.5)
print(s1 > s2)   # True  ← derived by decorator
```

</div>
</div>

---

## Hashability & `__hash__`

<div class="cols">
<div>

- Objects used as **dict keys** or in **sets** must be hashable.
- Defining `__eq__` sets `__hash__ = None` by default (unhashable).
- Define `__hash__` explicitly to restore hashability.

<div class="callout warn">

**Rule:** Objects that compare equal must have the same hash.

</div>

</div>
<div>

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

p = Point(1, 2)
seen = {p}             # works — hashable
memo = {p: "origin"}   # works as dict key
```

</div>
</div>

---

## Operator Overloading

<div class="cols">
<div>

| Method | Operator |
|---|---|
| `__add__` | `+` |
| `__sub__` | `-` |
| `__mul__` | `*` |
| `__len__` | `len()` |
| `__getitem__` | `obj[i]` |
| `__contains__` | `in` |

</div>
<div>

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar,
                      self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)    # Vector(4, 6)
print(v1 * 3)     # Vector(3, 6)
```

</div>
</div>

---

## `@dataclass`

<div class="cols">
<div>

Auto-generates `__init__`, `__repr__`, and `__eq__` from annotated fields.

| Option | Effect |
|---|---|
| `eq=True` (default) | Auto-generates `__eq__` |
| `order=True` | Also generates `<`, `<=`, `>`, `>=` |
| `frozen=True` | Immutable; enables `__hash__` |
| `field(default_factory=…)` | Safe mutable default |

</div>
<div>

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class Student:
    name: str
    gpa: float
    courses: list = field(default_factory=list)

s1 = Student("Alice", 3.8)
s2 = Student("Bob",   3.5)
print(s1 > s2)     # True  (order=True)

@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(1, 2)
# p.x = 9   ← FrozenInstanceError
d = {p: "origin"}  # hashable!
```

</div>
</div>

---

## Class vs. Instance Variables

<div class="cols">
<div>

- **Instance variable:** set on `self`; unique per object.
- **Class variable:** set on the class; shared across all instances.

<div class="callout warn">

**Mutation trap:** a *mutable* class variable (like a list) is shared — appending from one instance affects all instances.

</div>

```python
# WRONG — all instances share one list!
class Broken:
    items = []

# CORRECT — each instance gets its own list
class Fixed:
    def __init__(self):
        self.items = []
```

</div>
<div>

```python
class Player:
    count = 0         # class variable

    def __init__(self, name):
        self.name = name      # instance var
        Player.count += 1

p1 = Player("Lia")
p2 = Player("Kai")

print(Player.count)   # 2  (shared)
print(p1.name)        # Lia (unique)
print(p2.name)        # Kai (unique)
```

</div>
</div>

---

## Static & Class Methods

| Decorator | First param | Typical use |
|---|---|---|
| *(none)* | `self` | Regular instance method |
| `@classmethod` | `cls` | Alternative constructors; access class state |
| `@staticmethod` | — | Utility; logically related but needs no instance or class |

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):   # alt constructor
        return cls((f - 32) * 5/9)

    @staticmethod
    def is_valid(celsius):         # utility
        return -273.15 <= celsius

t = Temperature.from_fahrenheit(212)
print(t.celsius)              # 100.0
print(Temperature.is_valid(-300))  # False
```

---

## Chapter 10 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Class definition | `class Name:` + `__init__(self, …)` |
| Property | `@property` getter; `@attr.setter` for validation |
| Inheritance | `class Child(Parent):` + `super().__init__()` |
| Abstract methods | `from abc import ABC, abstractmethod` |
| Ordering | `__eq__` + `__lt__` + `@total_ordering` |
| Operator overload | `__add__`, `__mul__`, `__len__`, … |
| @dataclass | `order=True`, `frozen=True`, `field(default_factory=…)` |
| Class method | `@classmethod` + `cls` param — for alt constructors |
| Static method | `@staticmethod` — no `self` or `cls` |

---

<!-- _class: title -->

# End of Chapter 10

*Next: Chapter 11 — Functional Programming*

*map · filter · lambda · decorators · recursion · functools*
