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

Dictionaries & Sets

*8.0 Intro · 8.1 Dictionaries · 8.2 Sets · 8.3 Advanced*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 8.1 Dictionaries

Key-value mappings with O(1) average lookup

---

## Creating & Accessing Dicts

<div class="cols">
<div>

```python
person = {"name": "Alice", "age": 28}

# Access
print(person["name"])           # Alice
print(person.get("email", "N/A"))  # N/A

# Add / update
person["email"] = "alice@example.com"
person.update({"age": 29, "city": "Rolla"})

# Delete
del person["city"]
popped = person.pop("email")
```

</div>
<div>

### Iterating

```python
for key in person:
    print(key)

for val in person.values():
    print(val)

for key, val in person.items():
    print(key, val)
```

### Dict comprehension

```python
squares = {x: x**2 for x in range(5)}
filtered = {k: v for k, v in d.items() if v > 0}
```

</div>
</div>

---

## Counter & defaultdict

<div class="cols">
<div>

### `Counter`

```python
from collections import Counter

words = "the cat sat on the mat".split()
c = Counter(words)
print(c.most_common(3))
# [('the', 2), ('cat', 1), ('sat', 1)]

# Combine counters
c2 = Counter(["the", "dog"])
print(c + c2)
```

</div>
<div>

### `defaultdict`

```python
from collections import defaultdict

# int factory — missing keys default to 0
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1

# list factory — group by key
courses = defaultdict(list)
for name, course in records:
    courses[name].append(course)
```

</div>
</div>

---

## Why Dict Lookup Is Fast — O(1)

<div class="cols">
<div>

- Dicts and sets use **hash tables**.
- Python computes `hash(key)` → jumps directly to the slot.
- Lookup time is **O(1) average** regardless of size.
- List `in` operator is **O(n)** — scans every element.

</div>
<div>

```python
import time, random

n = 1_000_000
big_list = list(range(n))
big_dict = {i: True for i in range(n)}
target = n - 1   # worst case

# O(n) list scan
t = time.perf_counter()
target in big_list
print(f"list: {time.perf_counter()-t:.5f}s")

# O(1) dict lookup
t = time.perf_counter()
target in big_dict
print(f"dict: {time.perf_counter()-t:.5f}s")
```

</div>
</div>

---

<!-- _class: section -->

## 8.2 Sets

Unordered collections of unique, hashable elements

---

## Sets — Creation & Operations

<div class="cols">
<div>

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # {1,2,3,4,5}  union
print(a & b)   # {3}           intersection
print(a - b)   # {1,2}         difference
print(a ^ b)   # {1,2,4,5}    symmetric difference

# Membership (O(1))
print(3 in a)   # True

# Deduplicate a list
unique = list(set([1, 2, 2, 3, 3, 3]))
```

</div>
<div>

### frozenset — immutable set

```python
fs = frozenset({1, 2, 3})
# fs.add(4)   ← AttributeError

# Can be used as dict key or set element
graph = {frozenset({1,2}): "edge"}
```

| Feature | `set` | `frozenset` |
|---|---|---|
| Mutable | ✓ | ✗ |
| Hashable | ✗ | ✓ |
| Dict key | ✗ | ✓ |

</div>
</div>

---

## Chapter 7 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Create dict | `{"key": value}` or `dict(key=value)` |
| Safe get | `.get(key, default)` |
| Iterate | `.keys()`, `.values()`, `.items()` |
| Dict comprehension | `{k: v for k, v in ...}` |
| Counter | `Counter(seq)` → `.most_common(n)` |
| defaultdict | `defaultdict(int)` or `defaultdict(list)` |
| Set ops | `\|` `&` `-` `^` — union/intersection/diff/sym-diff |
| Membership | `x in s` — O(1) for dict/set, O(n) for list |
| Hashable keys | `int`, `str`, `tuple` (immutable types) |

---

<!-- _class: title -->

# End of Chapter 7

*Next: Chapter 8 — Strings*

*string methods · regex · text analysis · word frequencies*
