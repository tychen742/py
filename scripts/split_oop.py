import json, copy, uuid

def load(path):
    with open(path) as f:
        return json.load(f)

def save(nb, path):
    with open(path, 'w') as f:
        json.dump(nb, f, indent=1)
    print(f"  ✓ Wrote {path.split('/')[-1]}  ({len(nb['cells'])} cells)")

def make_nb(cells, metadata=None):
    return {
        "cells": cells,
        "metadata": metadata or {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.13.0"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

def md_cell(src):
    return {"cell_type": "markdown", "id": f"new-{uuid.uuid4().hex[:8]}", "metadata": {}, "source": src}

def code_cell(src, tags=None):
    m = {"tags": tags} if tags else {}
    return {"cell_type": "code", "execution_count": None, "id": f"new-{uuid.uuid4().hex[:8]}",
            "metadata": m, "outputs": [], "source": src}

BASE = '/Users/tychen/workspace/py/chapters/12-oop'
nb1201 = load(f'{BASE}/1201-oop-design.ipynb')
nb1202 = load(f'{BASE}/1202-oop-practice.ipynb')

cells1201 = nb1201['cells']
cells1202 = nb1202['cells']
meta = nb1201.get('metadata', {})
setup_cell = copy.deepcopy(cells1201[1])  # hide-input setup

# ── NEW 1201: OOP Basics (cells idx 0-51) ────────────────────────────────────
new1201 = make_nb(copy.deepcopy(cells1201[:52]), meta)
save(new1201, f'{BASE}/1201-oop-design.ipynb')

# ── NEW 1202: Methods & Design (new title+setup + cells idx 91-181) ──────────
title_1202 = md_cell("# Methods and Design")
setup_1202  = copy.deepcopy(setup_cell)
new1202 = make_nb([title_1202, setup_1202] + copy.deepcopy(cells1201[91:]), meta)
save(new1202, f'{BASE}/1202-oop-methods.ipynb')

# Advanced pool from 1201: Copying, Pure Functions, Prototype & Patch (idx 52-90)
adv_from_1201 = copy.deepcopy(cells1201[52:91])

# Advanced pool from 1202: card game (idx 12-111), Debugging (136-139), @dataclass (147-150)
adv_from_1202 = (
    copy.deepcopy(cells1202[12:112]) +
    copy.deepcopy(cells1202[136:140]) +
    copy.deepcopy(cells1202[147:151])
)

# ── NEW 1204: Advanced OOP ────────────────────────────────────────────────────
title_1204 = md_cell("# Advanced OOP Topics")
setup_1204  = copy.deepcopy(setup_cell)
summary_1204 = md_cell(
    "## Summary\n\n"
    "Optional but powerful OOP tools:\n\n"
    "- **Copying**: shallow vs deep copy, `copy` module\n"
    "- **Pure functions** vs in-place mutation with objects\n"
    "- **Prototype-and-patch** development workflow\n"
    "- **Card game**: a full worked OOP example (`Card`, `Deck`)\n"
    "- **Debugging** OOP code\n"
    "- **Dataclasses**: `@dataclass` for concise data containers\n"
)
new1204 = make_nb([title_1204, setup_1204] + adv_from_1201 + adv_from_1202 + [summary_1204], meta)
save(new1204, f'{BASE}/1204-oop-advanced.ipynb')

# ── NEW 1203: The Four Pillars ────────────────────────────────────────────────
# From current 1202: Polymorphism+Inheritance (idx 3-11), Parents+Spec (112-135),
# Circle exercise (140-142), super/issubclass (143-146)
pillar_cells = (
    copy.deepcopy(cells1202[3:12]) +
    copy.deepcopy(cells1202[112:136]) +
    copy.deepcopy(cells1202[140:147])
)

title_1203   = md_cell("# The Four Pillars of OOP")
setup_1203   = copy.deepcopy(setup_cell)
intro_1203   = md_cell(
    "Object-oriented programming is built on four core principles.\n\n"
    "| Pillar | Core idea |\n"
    "|--------|-----------|\n"
    "| **Encapsulation** | Bundle data + behavior; hide internal state |\n"
    "| **Inheritance** | Build new classes on top of existing ones |\n"
    "| **Polymorphism** | Same interface, different implementations |\n"
    "| **Abstraction** | Expose only what callers need, hide the rest |\n"
)

encap_md = md_cell(
    "## Encapsulation\n\n"
    "**Encapsulation** bundles data (attributes) and behavior (methods) together in one unit,\n"
    "and restricts direct access to internal state. In Python the convention is to prefix\n"
    "private attributes with `_`. Use `@property` to expose controlled access.\n\n"
    "The goal: callers interact only through the *public interface*, not implementation details."
)
encap_code = code_cell(
    "class BankAccount:\n"
    "    def __init__(self, owner, balance=0):\n"
    "        self.owner = owner\n"
    "        self._balance = balance       # private by convention\n\n"
    "    @property\n"
    "    def balance(self):\n"
    "        \"\"\"Read-only access to balance.\"\"\"\n"
    "        return self._balance\n\n"
    "    def deposit(self, amount):\n"
    "        if amount <= 0:\n"
    "            raise ValueError('Deposit must be positive')\n"
    "        self._balance += amount\n\n"
    "    def withdraw(self, amount):\n"
    "        if amount > self._balance:\n"
    "            raise ValueError('Insufficient funds')\n"
    "        self._balance -= amount\n\n"
    "    def __repr__(self):\n"
    "        return f'BankAccount({self.owner!r}, balance={self._balance})'\n\n\n"
    "acct = BankAccount('Alice', 100)\n"
    "acct.deposit(50)\n"
    "acct.withdraw(30)\n"
    "print(acct)          # BankAccount('Alice', balance=120)\n"
    "print(acct.balance)  # 120 — read-only via property\n"
)

abstraction_md = md_cell(
    "## Abstraction\n\n"
    "**Abstraction** means defining a clean interface and hiding implementation details.\n"
    "Python's `abc` module lets you create **Abstract Base Classes** that guarantee every\n"
    "subclass implements a required set of methods — without specifying *how*."
)
abstraction_code = code_cell(
    "from abc import ABC, abstractmethod\n"
    "import math\n\n"
    "class Shape(ABC):\n"
    "    \"\"\"Abstract base: every Shape must implement area() and perimeter().\"\"\"\n\n"
    "    @abstractmethod\n"
    "    def area(self): ...\n\n"
    "    @abstractmethod\n"
    "    def perimeter(self): ...\n\n"
    "    def describe(self):\n"
    "        return f'{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}'\n\n\n"
    "class Circle(Shape):\n"
    "    def __init__(self, radius): self.radius = radius\n"
    "    def area(self): return math.pi * self.radius ** 2\n"
    "    def perimeter(self): return 2 * math.pi * self.radius\n\n\n"
    "class Rectangle(Shape):\n"
    "    def __init__(self, w, h): self.w, self.h = w, h\n"
    "    def area(self): return self.w * self.h\n"
    "    def perimeter(self): return 2 * (self.w + self.h)\n\n\n"
    "for s in [Circle(5), Rectangle(4, 6)]:\n"
    "    print(s.describe())\n"
    "# Shape()  →  TypeError: Can't instantiate abstract class\n"
)

summary_1203 = md_cell(
    "## Summary\n\n"
    "The four pillars work together:\n\n"
    "- **Encapsulation** — protect state; expose behavior through a clean interface\n"
    "- **Inheritance** — reuse and extend existing classes with `class Child(Parent):`\n"
    "- **Polymorphism** — write code that works on any object with the right interface\n"
    "- **Abstraction** — define contracts with ABCs; callers depend on interfaces, not details\n"
)

new1203 = make_nb(
    [title_1203, setup_1203, intro_1203,
     encap_md, encap_code] +
    pillar_cells +
    [abstraction_md, abstraction_code, summary_1203],
    meta
)
save(new1203, f'{BASE}/1203-oop-pillars.ipynb')

print("\nAll done! Summary:")
print(f"  1201: {len(new1201['cells'])} cells  (OOP Basics)")
print(f"  1202: {len(new1202['cells'])} cells  (Methods & Design)")
print(f"  1203: {len(new1203['cells'])} cells  (Four Pillars)")
print(f"  1204: {len(new1204['cells'])} cells  (Advanced, optional)")
