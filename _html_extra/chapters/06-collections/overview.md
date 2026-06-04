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
  section.title p { color: #c8e6c9; }
  section.section { background: #2a6b37; color: white; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; }
  section.section h2 { color: white; border: none; font-size: 1.9em; }
  section.section p { color: #c8e6c9; }
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

# Chapter 6

Lists

*6.0 Intro · 6.1 Creating · 6.2 Accessing · 6.3 Operations · 6.4 Aliasing · 6.5 Advanced*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 6.1 Creating Lists

Literals, constructors, comprehensions

---

## Creating Lists

<div class="cols">
<div>

```python
# Literal
fruits = ["apple", "banana", "cherry"]

# Constructor
nums = list(range(5))       # [0, 1, 2, 3, 4]
chars = list("hello")       # ['h','e','l','l','o']

# List comprehension
squares = [x**2 for x in range(6)]
# [0, 1, 4, 9, 16, 25]

# With filter
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

</div>
<div>

### Nested lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[1][2])   # 6

# Flatten with comprehension
flat = [x for row in matrix for x in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

</div>
</div>

---

<!-- _class: section -->

## 6.2–6.3 Accessing & Operating on Lists

Indexing, slicing, methods, iteration

---

## Indexing & Slicing

<div class="cols">
<div>

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])     # apple   (first)
print(fruits[-1])    # date    (last)
print(fruits[1:3])   # ['banana', 'cherry']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[::2])   # ['apple', 'cherry'] (step 2)
print(fruits[::-1])  # reversed
```

</div>
<div>

### Common list methods

| Method | Effect |
|---|---|
| `.append(x)` | Add to end |
| `.insert(i, x)` | Insert at index |
| `.extend(seq)` | Add all from seq |
| `.remove(x)` | Remove first match |
| `.pop(i)` | Remove & return |
| `.sort()` | Sort in place |
| `.reverse()` | Reverse in place |
| `sorted(lst)` | Return new sorted list |

</div>
</div>

---

<!-- _class: section -->

## 6.4 Aliasing & Copying

Identity vs. value · shallow copies

---

## Aliasing vs. Copying

<div class="cols">
<div>

**Aliasing** — two names for the same object.

```python
a = [1, 2, 3]
b = a           # alias — same object
b[0] = 99
print(a)        # [99, 2, 3] — a changed!
print(a is b)   # True
```

**Copying** — a separate object with same values.

```python
c = a[:]        # slice copy
c = a.copy()    # explicit copy
c = list(a)     # constructor copy
c[0] = 0
print(a)        # [99, 2, 3] — a unchanged
```

</div>
<div>

<div class="callout warn">

When you pass a list to a function, the function gets a **reference**. Mutations inside the function affect the original.

</div>

```python
def clear_first(lst):
    lst[0] = None   # mutates the original!

data = [1, 2, 3]
clear_first(data)
print(data)   # [None, 2, 3]
```

Pass a copy if you don't want the original changed:
```python
clear_first(data[:])
```

</div>
</div>

---

<!-- _class: section -->

## 6.5 Advanced Lists

`any()`, `all()`, and list patterns

---

## `any()` and `all()`

```python
scores = [72, 88, 95, 61, 79]

# all() — True only if every element satisfies the condition
print(all([s >= 60 for s in scores]))   # True  — everyone passed
print(all([s >= 90 for s in scores]))   # False

# any() — True if at least one element satisfies the condition
print(any([s >= 90 for s in scores]))   # True  — at least one A
print(any([s < 0   for s in scores]))   # False
```

<div class="callout rule">

Pass a **list comprehension** here. In Chapter 11 you will see that dropping the brackets `[...]` makes these even more efficient.

</div>

---

## Chapter 6 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| List literal | `[1, 2, 3]` |
| Comprehension | `[expr for x in seq if cond]` |
| Index | `lst[0]`, `lst[-1]` |
| Slice | `lst[start:stop:step]` |
| Append / extend | `.append(x)`, `.extend(seq)` |
| Sort | `.sort()` in-place; `sorted(lst)` new list |
| Copy | `lst[:]`, `lst.copy()`, `list(lst)` |
| Alias check | `a is b` |
| any / all | `any([...])`, `all([...])` |

---

<!-- _class: title -->

# End of Chapter 6

*Next: Chapter 7 — Tuples*

*immutable sequences · unpacking · zip · enumerate*
