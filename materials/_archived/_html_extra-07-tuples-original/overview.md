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

# Chapter 7

Tuples

*7.0 Intro · 7.1 Creating & Accessing · 7.2 Unpacking · 7.3 Operations · 7.4 Tuples & Functions*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 7.1 Creating & Accessing Tuples

Immutable ordered sequences

---

## Tuples vs. Lists

<div class="cols">
<div>

```python
# Tuple — parentheses (or just commas)
point = (3, 4)
color = "red", "green", "blue"   # no parens needed
single = (42,)   # trailing comma required for 1-tuple

# Indexing and slicing — same as lists
print(point[0])     # 3
print(color[-1])    # 'blue'
print(color[1:])    # ('green', 'blue')
```

</div>
<div>

| Feature | `list` | `tuple` |
|---|---|---|
| Mutable | ✓ | ✗ |
| Hashable | ✗ | ✓ (if elements hashable) |
| Dict key | ✗ | ✓ |
| Set element | ✗ | ✓ |
| Use case | Ordered, changeable | Fixed records |

<div class="callout">

Use tuples for data that **should not change**: coordinates, RGB values, (key, value) pairs.

</div>

</div>
</div>

---

<!-- _class: section -->

## 7.2 Tuple Unpacking

Assign multiple variables from a tuple in one line

---

## Unpacking

<div class="cols">
<div>

```python
# Basic unpacking
x, y = (3, 4)
a, b, c = "abc"

# Swap without temp variable
a, b = b, a

# Starred unpacking
first, *rest = [1, 2, 3, 4, 5]
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

*start, last = [1, 2, 3, 4, 5]
print(last)    # 5
```

</div>
<div>

### Unpacking in loops

```python
pairs = [(1, "one"), (2, "two"), (3, "three")]

for num, word in pairs:
    print(f"{num} → {word}")

# Equivalent with items()
scores = {"alice": 92, "bob": 85}
for name, score in scores.items():
    print(f"{name}: {score}")
```

</div>
</div>

---

<!-- _class: section -->

## 7.3–7.4 Operations & Functions

zip · enumerate · sorting · return values

---

## `zip` and `enumerate`

<div class="cols">
<div>

### `zip` — pair up sequences

```python
names  = ["Alice", "Bob", "Carol"]
scores = [92, 85, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Build a dict from two lists
mapping = dict(zip(names, scores))
# {'Alice': 92, 'Bob': 85, 'Carol': 78}
```

</div>
<div>

### `enumerate` — index + value

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

# Start from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

</div>
</div>

---

## Sorting & Tuples as Return Values

<div class="cols">
<div>

### Sorting with a key

```python
students = [("Alice", 3.8), ("Bob", 3.5), ("Carol", 3.9)]

# Sort by GPA (second element)
students.sort(key=lambda s: s[1], reverse=True)

# Using itemgetter (clearer)
from operator import itemgetter
students.sort(key=itemgetter(1))
```

</div>
<div>

### Multiple return values

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(lo, hi)   # 1 9

def divmod_custom(a, b):
    return a // b, a % b

quotient, remainder = divmod_custom(17, 5)
```

</div>
</div>

---

## Chapter 7 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Tuple literal | `(a, b, c)` or `a, b, c` |
| Single element | `(x,)` — trailing comma required |
| Unpack | `x, y = point` |
| Starred unpack | `first, *rest = seq` |
| Swap | `a, b = b, a` |
| zip | `zip(seq1, seq2)` — pair-wise |
| enumerate | `enumerate(seq, start=0)` — index + value |
| Sort by element | `key=lambda t: t[1]` or `itemgetter(1)` |
| Return multiple | `return a, b` → unpacked by caller |

---

<!-- _class: title -->

# End of Chapter 7

*Next: Chapter 8 — Dictionaries & Sets*

*key-value pairs · hash tables · Counter · defaultdict · sets*
