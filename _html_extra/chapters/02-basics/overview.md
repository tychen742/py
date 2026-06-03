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

# Chapter 2

Variables & Types

*2.0 Intro · 2.1 Variables · 2.2 Operators · 2.3 Types · 2.4–2.6 Built-ins & Collections*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 2.1 Variables

Assignment, naming conventions, and dynamic typing

---

## Variables & Assignment

<div class="cols">
<div>

- A **variable** is a name bound to a value.
- Assignment uses `=` (not equality).
- Python is **dynamically typed** — the type is inferred from the value.
- Multiple assignment and swapping are concise.

</div>
<div>

```python
x = 42           # int
name = "Alice"   # str
pi = 3.14159     # float
active = True    # bool

# Multiple assignment
a, b, c = 1, 2, 3

# Swap without a temp variable
a, b = b, a

# Augmented assignment
x += 10   # same as x = x + 10
```

</div>
</div>

---

<!-- _class: section -->

## 2.2 Operators

Arithmetic, comparison, logical, and assignment operators

---

## Operators

<div class="cols">
<div>

### Arithmetic

| Op | Meaning | Example |
|---|---|---|
| `+` `-` `*` `/` | Basic | `5 / 2` → `2.5` |
| `//` | Floor division | `5 // 2` → `2` |
| `%` | Modulus | `5 % 2` → `1` |
| `**` | Exponent | `2 ** 8` → `256` |

### Comparison

`==`, `!=`, `<`, `>`, `<=`, `>=` → returns `True`/`False`

</div>
<div>

### Logical

```python
x = 5
print(x > 0 and x < 10)  # True
print(x < 0 or x > 3)    # True
print(not x == 5)         # False
```

### Short-circuit evaluation

`and` stops at the first `False`.
`or` stops at the first `True`.

```python
data = None
result = data or []   # [] if data is falsy
```

</div>
</div>

---

<!-- _class: section -->

## 2.3–2.5 Built-in Types

Numbers, strings, booleans, and type conversion

---

## Numeric Types

<div class="cols">
<div>

| Type | Example | Notes |
|---|---|---|
| `int` | `42`, `-7` | Unlimited precision |
| `float` | `3.14`, `1e-6` | IEEE 754 double |
| `complex` | `2+3j` | `j` for imaginary unit |

```python
print(type(42))      # <class 'int'>
print(type(3.14))    # <class 'float'>
print(10 / 3)        # 3.3333...
print(10 // 3)       # 3
```

</div>
<div>

### Type Conversion

```python
int("42")        # 42
float("3.14")    # 3.14
str(100)         # '100'
bool(0)          # False
bool("hello")    # True
```

<div class="callout warn">

`0`, `""`, `[]`, `{}`, `None` are all **falsy**. Everything else is truthy.

</div>

</div>
</div>

---

## Strings

<div class="cols">
<div>

- Immutable sequences of Unicode characters.
- Single, double, or triple quotes.
- Indexing (`s[0]`) and slicing (`s[1:4]`).
- Rich method library: `.upper()`, `.split()`, `.strip()`, `.replace()`, …

</div>
<div>

```python
s = "Hello, World!"
print(s[0])        # H
print(s[-1])       # !
print(s[7:12])     # World
print(s.lower())   # hello, world!
print(s.split(",")) # ['Hello', ' World!']
print(len(s))      # 13
```

</div>
</div>

---

## 2.6 Collection Types — Overview

| Type | Ordered | Mutable | Unique | Access |
|---|---|---|---|---|
| `list` | ✓ | ✓ | — | index |
| `tuple` | ✓ | ✗ | — | index |
| `dict` | ✓ (insertion) | ✓ | keys only | key |
| `set` | ✗ | ✓ | ✓ | membership |

```python
nums   = [1, 2, 3]           # list
point  = (3.0, 4.0)          # tuple
person = {"name": "Alice"}   # dict
unique = {1, 2, 3}           # set
```

---

## Chapter 2 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Variable | `x = value` — dynamic typing |
| Augmented assign | `x += 1`, `x *= 2` |
| Floor division | `//` integer quotient; `%` remainder |
| Exponent | `2 ** 10` → 1024 |
| Type check | `type(x)`, `isinstance(x, int)` |
| Conversion | `int()`, `float()`, `str()`, `bool()` |
| Falsy values | `0`, `""`, `[]`, `{}`, `None` |
| String methods | `.upper()`, `.split()`, `.strip()`, `.replace()` |

---

<!-- _class: title -->

# End of Chapter 2

*Next: Chapter 3 — Control Flow*

*if · elif · else · for · while · break · continue*
