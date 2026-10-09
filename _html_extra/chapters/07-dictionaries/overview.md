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

Dictionaries

*7.1 Dictionaries · 7.2 Core Operations · 7.3 Dictionary Patterns · 7.4 Sets*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 7.1 Dictionaries

Key-value mappings — the workhorse of Python data

---

## What Is a Dictionary?

<div class="cols">
<div>

A **dictionary** stores data as **key–value pairs**.

- Look up a *key* → get its *value*
- Keys must be **unique** and **hashable**
- Values can be any type

```python
person = {"name": "Alice", "age": 28}
config = {"debug": True, "timeout": 30}
word_count = {}          # empty dict
```

</div>
<div>

### When to use a dict

- You need **labeled** data (vs positional)
- You want **fast lookups by name**
- You need a **mapping** relationship

| Use case | Example |
|---|---|
| Student records | `{"id": 42, "gpa": 3.8}` |
| Config settings | `{"theme": "dark"}` |
| Word counts | `{"the": 12, "cat": 3}` |
| JSON data | any API response |

</div>
</div>

---

## Creating Dictionaries

<div class="cols">
<div>

### Dict literal
```python
scores = {"alice": 92, "bob": 85}
```

### `dict()` constructor
```python
# from keyword arguments
d = dict(name="Alice", age=28)

# from list of (key, value) pairs
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
```

### `dict.fromkeys()`
```python
# all keys share the same default value
keys = ["x", "y", "z"]
d = dict.fromkeys(keys, 0)
# {"x": 0, "y": 0, "z": 0}
```

</div>
<div>

### Dict comprehension
```python
squares = {x: x**2 for x in range(6)}
# {0:0, 1:1, 2:4, 3:9, 4:16, 5:25}
```

<div class="callout">

**Keys must be hashable** — `str`, `int`, `float`, and `tuple` work; `list` and `dict` do not.

</div>

### Nesting
```python
students = {
    "alice": {"gpa": 3.9, "year": 2},
    "bob":   {"gpa": 3.4, "year": 3},
}
print(students["alice"]["gpa"])   # 3.9
```

</div>
</div>

---

<!-- _class: section -->

## 7.2 Core Operations

Accessing, modifying, and querying dictionaries

---

## Accessing Items

<div class="cols">
<div>

### Square-bracket access
```python
person = {"name": "Alice", "age": 28}

print(person["name"])      # Alice
# person["email"]          # KeyError!
```

### Safe access with `.get()`
```python
# returns None if key missing
print(person.get("email"))        # None

# returns default if key missing
print(person.get("email", "N/A")) # N/A
```

</div>
<div>

### Membership testing
```python
"name" in person      # True
"email" in person     # False
"email" not in person # True
```

<div class="callout rule">

Prefer `.get(key, default)` over `dict[key]` when the key might be absent — it avoids a `KeyError` without needing a try/except.

</div>

</div>
</div>

---

## Lists and Dictionaries: Access and Mutation

Lists use positions; dictionaries use keys.

| Operation | List `nums` | Dictionary `d` |
| --- | --- | --- |
| Read | `nums[i]` | `d[key]` |
| Read with fallback | No `get()` equivalent | `d.get(key, default)` |
| Replace | `nums[i] = value` (existing index) | `d[key] = value` (add or replace) |
| Add | `nums.append(value)` or `nums.insert(i, value)` | `d[key] = value` (new key) |
| Delete, no return | `del nums[i]` or `del nums[i:j]` | `del d[key]` |

Invalid indices raise `IndexError`; missing keys raise `KeyError` when no fallback is supplied.

---

## Lists and Dictionaries: Removal and Inspection

| Operation | List `nums` | Dictionary `d` |
| --- | --- | --- |
| Remove by value | `nums.remove(value)` removes first match | No `remove()`; deletion uses keys |
| Remove and return | `nums.pop(i)`; no fallback | `d.pop(key, default)` |
| Remove last | `nums.pop()` returns an element | `d.popitem()` returns `(key, value)` |
| Clear | `nums.clear()` | `d.clear()` |
| Membership | `value in nums` | `key in d`; `value in d.values()` |
| Iterate | `for value in nums` | `for key in d`; `for key, value in d.items()` |
| Count | `len(nums)` | `len(d)` |

---

## Adding, Updating, and Deleting

<div class="cols">
<div>

### Add / update
```python
person["email"] = "alice@example.com"  # add
person["age"] = 29                     # update

# update multiple keys at once
person.update({"age": 30, "city": "Rolla"})
```

### Delete
```python
del person["city"]           # statement, no return
email = person.pop("email")  # remove, return value
phone = person.pop("phone", "N/A")  # default if missing
last = person.popitem()      # remove last inserted pair
```

`del` also removes list elements, slices, and variable bindings. It does not return a value.

Dictionary `pop(key, default)` uses a key and an optional fallback. List `pop(index)` uses an optional index and has no fallback. Without a fallback, a missing dictionary key raises `KeyError`. Like list `pop()`, `d.popitem()` removes the last item, but returns a `(key, value)` tuple.

</div>
<div>

### Useful inspection methods
```python
person.keys()    # dict_keys([...])
person.values()  # dict_values([...])
person.items()   # dict_items([(k,v), ...])
len(person)      # number of key-value pairs
```

<div class="callout warn">

`dict.keys()`, `.values()`, and `.items()` return **view objects** — they reflect changes to the dict in real time.

</div>

</div>
</div>

---

<!-- _class: section -->

## 7.3 Dictionary Patterns

Comprehensions, counting, defaults, iteration, and memory

---

## Dictionary Comprehension

Same idea as list comprehension — builds a dict in one expression.

<div class="cols">
<div>

```python
# basic: square each number
squares = {x: x**2 for x in range(6)}
# {0:0, 1:1, 2:4, 3:9, 4:16, 5:25}

# with filter: only even squares
even_sq = {x: x**2 for x in range(6)
           if x % 2 == 0}
# {0:0, 2:4, 4:16}

# transform an existing dict
prices = {"apple": 1.2, "banana": 0.5}
discounted = {k: v * 0.9
              for k, v in prices.items()}
```

</div>
<div>

### Invert a dictionary
```python
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1:"a", 2:"b", 3:"c"}
```

<div class="callout">

Inversion only works cleanly when values are unique. Duplicate values will overwrite each other.

</div>

</div>
</div>

---

## Counting Patterns

<div class="cols">
<div>

### Manual counter
```python
words = "the cat sat on the mat".split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
# {"the":2, "cat":1, "sat":1, ...}
```

### `Counter` — one line
```python
from collections import Counter

counts = Counter(words)
counts.most_common(3)
# [("the", 2), ("cat", 1), ("sat", 1)]

# combine two counters
c2 = Counter(["the", "dog"])
print(counts + c2)
```

</div>
<div>

### `defaultdict` — skip the guard
```python
from collections import defaultdict

# int factory: missing keys default to 0
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1   # no KeyError

# list factory: group values by key
groups = defaultdict(list)
for name, score in records:
    groups[name].append(score)
```

<div class="callout">

`Counter` is best for tallying. `defaultdict` is best for grouping or accumulating into containers.

</div>

</div>
</div>

---

## Iterating Through Dictionaries

```python
d = {"name": "Alice", "age": 28, "city": "Rolla"}
```

<div class="cols">
<div>

### Keys (default)
```python
for key in d:
    print(key)
# name  age  city
```

### Values
```python
for val in d.values():
    print(val)
# Alice  28  Rolla
```

</div>
<div>

### Key-value pairs
```python
for key, val in d.items():
    print(f"{key}: {val}")
# name: Alice
# age: 28
# city: Rolla
```

### Sorted iteration
```python
for key in sorted(d):
    print(key, d[key])
```

</div>
</div>

<div class="callout warn">

Do not add or remove keys while iterating — it raises `RuntimeError`. Iterate over `list(d.items())` if you need to modify during the loop.

</div>

---

## Why Dict Lookup Is Fast — O(1)

<div class="cols">
<div>

- Dicts and sets use **hash tables**.
- Python computes `hash(key)` → jumps directly to the bucket.
- Lookup is **O(1) average** regardless of dict size.
- List `in` operator scans every element — **O(n)**.

```python
import time, random

n = 1_000_000
big_list = list(range(n))
big_dict = {i: True for i in range(n)}
target = n - 1   # worst case for list

t = time.perf_counter()
_ = target in big_list
print(f"list: {time.perf_counter()-t:.5f}s")

t = time.perf_counter()
_ = target in big_dict
print(f"dict: {time.perf_counter()-t:.5f}s")
```

</div>
<div>

| Operation | `list` | `dict` / `set` |
|---|---|---|
| `x in c` | O(n) | O(1) avg |
| `c[key]` | O(1) by index | O(1) by key |
| Insert | O(1) append | O(1) avg |
| Delete | O(n) | O(1) avg |

<div class="callout rule">

**Hashable keys**: `int`, `str`, `float`, `tuple` (of hashables) are hashable. `list` and `dict` are not — they cannot be dict keys.

</div>

</div>
</div>

---

<!-- _class: section -->

## 7.4 Sets

Unordered collections of **unique, hashable** elements

---

## Creating Sets and Membership

<div class="cols">
<div>

### Create
```python
a = {1, 2, 3}
b = set([3, 4, 5])    # from list
empty = set()          # NOT {} (that's a dict)

# duplicates removed automatically
s = {1, 2, 2, 3, 3}   # {1, 2, 3}
```

### No indexing — iterate or test membership
```python
3 in a      # True   O(1)
6 not in a  # True

for item in a:
    print(item)    # order not guaranteed
```

</div>
<div>

### When to use a set

| Need | Use |
|---|---|
| Ordered, duplicates OK | `list` |
| Fixed structure, hashable | `tuple` |
| Unique elements, fast lookup | `set` |
| Key-value mapping | `dict` |

<div class="callout">

Sets are great for **deduplication** and **membership testing**. `x in set` is O(1); `x in list` is O(n).

</div>

</div>
</div>

---

## Set Algebra and Mutation

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

<div class="cols">
<div>

| Operation | Operator | Method |
|---|---|---|
| Union | `a \| b` | `a.union(b)` |
| Intersection | `a & b` | `a.intersection(b)` |
| Difference | `a - b` | `a.difference(b)` |
| Sym. difference | `a ^ b` | `a.symmetric_difference(b)` |

```python
a | b   # {1, 2, 3, 4, 5, 6}
a & b   # {3, 4}
a - b   # {1, 2}
a ^ b   # {1, 2, 5, 6}
```

</div>
<div>

### Modify in place
```python
a.add(5)          # add one element
a.update({6, 7})  # add multiple

a.remove(1)       # KeyError if missing
a.discard(99)     # safe — no error
a.pop()           # remove arbitrary element
```

### Subset / superset
```python
{1, 2} <= {1, 2, 3}   # True  (subset)
{1, 2, 3} >= {1, 2}   # True  (superset)
```

</div>
</div>

---

## Frozensets, Hashability, and Performance

<div class="cols">
<div>

### `frozenset` — immutable set
```python
fs = frozenset({1, 2, 3})
# fs.add(4)   ← AttributeError

# Can be a dict key or set element
graph = {frozenset({1, 2}): "edge A"}
```

| | `set` | `frozenset` |
|---|---|---|
| Mutable | ✓ | ✗ |
| Hashable | ✗ | ✓ |
| Dict key | ✗ | ✓ |

</div>
<div>

### Set comprehension
```python
# unique squares of even numbers
s = {x**2 for x in range(10) if x % 2 == 0}
# {0, 4, 16, 36, 64}

# deduplicate a list
words = ["the", "cat", "the", "mat"]
unique = {w.lower() for w in words}
```

### O(1) membership — why it matters
```python
# set membership is O(1) vs O(n) for list
big = set(range(1_000_000))
999_999 in big   # instant
```

</div>
</div>

---

## Chapter 7 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Create | `{"k": v}` · `dict(k=v)` · `dict.fromkeys(keys, 0)` |
| Access | `d[key]` (KeyError if missing) · `d.get(key, default)` (safe) |
| Add / update | `d[key] = val` · `d.update({...})` |
| Delete | `del d[key]` · `d.pop(key)` · `d.popitem()` |
| Membership | `key in d` — O(1) |
| Iterate | `d.keys()` · `d.values()` · `d.items()` |
| Comprehension | `{k: v for k, v in iterable}` |
| Count | `Counter(seq)` → `.most_common(n)` |
| Group | `defaultdict(list)` — no KeyError on first access |
| Invert | `{v: k for k, v in d.items()}` |
| Memoize | Store previous results in a dict to avoid repeated work |
| Sets | `{1, 2}` · `set()` for an empty set · `s.add(x)` · `s.discard(x)` |
| Set algebra | `a \| b` · `a & b` · `a - b` · `a ^ b` |
| Deduplicate | `list(set(lst))` |

---

<!-- _class: title -->

# End of Chapter 7

*Next: Chapter 8 — Strings*

*string methods · regex · text analysis · word frequencies*
