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
  section.section p { color: #c8e6c9; font-size: 0.95em; }
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; align-items: start; }
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
  section::after { color: #aaa; font-size: 0.7em; }
---

<!-- _class: title -->

# Chapter 1

Introduction to Python

*1.0 Intro · 1.1 Programming Concepts · 1.2 Basic Syntax*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## What is Python?

A high-level, interpreted programming language designed for readability

---

## Why Python?

<div class="cols">
<div>

- **Readable** — code reads almost like English
- **Versatile** — web, data science, automation, AI
- **Large ecosystem** — 400,000+ packages on PyPI
- **Interactive** — run code line-by-line in Jupyter

</div>
<div>

```python
# Your first Python program
print("Hello, world!")

# Simple data science
scores = [72, 88, 95, 61, 79]
average = sum(scores) / len(scores)
print(f"Average: {average:.1f}")
```

</div>
</div>

---

<!-- _class: section -->

## 1.1 Programming Concepts

Programming languages, abstraction, constructs, number systems, encoding

---

## Natural vs. Formal Languages

<div class="cols">
<div>

**Natural languages** evolved naturally (English, Spanish).
**Formal languages** are designed for a specific purpose.

| Property | Natural | Formal |
|---|---|---|
| Ambiguity | High | None |
| Redundancy | High | Low |
| Literalness | Low | Exact |

<div class="callout">

Programming languages are **formal languages** — every detail matters.

</div>

</div>
<div>

### Interpreted vs. Compiled

| Style | Examples | How it runs |
|---|---|---|
| Interpreted | Python, JS | Line by line at runtime |
| Compiled | C, Rust | Translated to machine code first |
| Hybrid | Java | Compiled to bytecode, then run |

Python is interpreted — fast to try ideas, no compile step.

</div>
</div>

---

## Programming Constructs

Every program is built from three control structures:

| Construct | Meaning | Python example |
|---|---|---|
| **Sequence** | Execute one after another | `x = 1` then `y = 2` |
| **Selection** | Choose a path | `if x > 0:` |
| **Iteration** | Repeat | `for i in range(10):` |

Plus supporting elements: variables, operators, functions, data types, collections.

---

## Number Systems & Character Encoding

<div class="cols">
<div>

| System | Base | Python prefix |
|---|---|---|
| Binary | 2 | `0b1010` |
| Octal | 8 | `0o12` |
| Decimal | 10 | `10` |
| Hex | 16 | `0xa` |

```python
print(bin(100))   # '0b1100100'
print(hex(255))   # '0xff'
```

</div>
<div>

**ASCII** — 128 characters, 1 byte each.
**Unicode / UTF-8** — 1.1M+ code points; backward-compatible with ASCII.

```python
print(ord('A'))      # 65
print(chr(65))       # 'A'
print(ord('😊'))     # 128522
```

<div class="callout">

All text in Python 3 is Unicode by default.

</div>

</div>
</div>

---

<!-- _class: section -->

## 1.2 Basic Syntax

Indentation, print, input, comments, objects, keywords, modules

---

## Indentation & Block Structure

```python
for i in range(5):
    print(i)          # indented → part of the loop

if x > 0:
    print("positive") # indented → part of the if
    y = x * 2         # still in the if block
print("done")         # not indented → after the if
```

<div class="callout warn">

Python uses **indentation** (4 spaces) to define code blocks — not `{}`. Inconsistent indentation raises `IndentationError`.

</div>

---

## `print()` and F-Strings

<div class="cols">
<div>

```python
# Basic print
print("Hello")
print("a", "b", sep="-")  # a-b
print("x", end=" ")       # no newline
```

</div>
<div>

```python
# F-strings (Python 3.6+)
name = "Alice"
age = 25
print(f"Hello, {name}! You are {age}.")

x, y = 3, 4
print(f"Distance: {(x**2 + y**2)**0.5:.2f}")
```

</div>
</div>

---

## Comments, Objects, Keywords & Modules

<div class="cols">
<div>

```python
# Single-line comment

def area(r):
    """Docstring: return area of circle."""
    import math
    return math.pi * r ** 2

# Everything in Python is an object
x = 42
print(type(x))   # <class 'int'>
print(id(x))     # unique identity
```

</div>
<div>

**Keywords** — reserved words Python uses for structure:
`if`, `for`, `while`, `def`, `class`, `import`, `return`, `True`, `False`, `None`, …

**Modules** — import to extend Python:
```python
import math
from collections import Counter
import random
```

</div>
</div>

---

## Chapter 1 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Print | `print(value, sep=' ', end='\n')` |
| F-string | `f"text {expression}"` |
| Input | `name = input("prompt: ")` |
| Comment | `# single line` · `"""docstring"""` |
| Type check | `type(x)` · `isinstance(x, int)` |
| Object identity | `id(x)` |
| Import | `import math` · `from math import pi` |
| Binary / Hex | `0b1010`, `0xff` · `bin()`, `hex()` |

---

<!-- _class: title -->

# End of Chapter 1

*Next: Chapter 2 — Variables & Types*

*variables · operators · types · built-ins · collections*
