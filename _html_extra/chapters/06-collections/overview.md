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

Collections

*6.1 Lists · 6.2 Tuples · 6.3 Sets*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 6.1 Lists

Ordered, mutable sequences — Python's most versatile collection

---

## Creating Lists

<div class="cols">
<div>

### Literal
```python
fruits = ["apple", "banana", "cherry"]
mixed  = [1, "hello", 3.14, True]
empty  = []
```

### `list()` constructor
```python
list("abc")        # ['a', 'b', 'c']
list(range(5))     # [0, 1, 2, 3, 4]
list((1, 2, 3))    # from tuple
```

### List comprehension
```python
squares = [x**2 for x in range(6)]
# [0, 1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
```

</div>
<div>

### Nested lists
```python
matrix = [[1, 2], [3, 4], [5, 6]]
matrix[1][0]   # 3
```

### Strings ↔ Lists
```python
words = "hello world".split()
# ['hello', 'world']

" ".join(words)   # 'hello world'
```

<div class="callout">

Lists are **mutable** — elements can be added, removed, or changed after creation. Order is preserved and duplicates are allowed.

</div>

</div>
</div>

---

## Accessing & Slicing

<div class="cols">
<div>

### Indexing (zero-based)
```python
fruits = ["apple", "banana", "cherry"]

fruits[0]    # 'apple'
fruits[-1]   # 'cherry'   (last element)
fruits[10]   # IndexError
```

### Slicing `[start:stop:step]`
```python
fruits[1:]    # ['banana', 'cherry']
fruits[:2]    # ['apple', 'banana']
fruits[::2]   # every other element
fruits[::-1]  # reversed
```

</div>
<div>

### Query methods
```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

len(nums)         # 8
nums.count(1)     # 2
nums.index(5)     # 4  (first occurrence)
5 in nums         # True
```

### Unpacking
```python
a, b, c = [10, 20, 30]
first, *rest = [1, 2, 3, 4]
# first=1, rest=[2, 3, 4]
```

</div>
</div>

---

## Modifying Lists

<div class="cols">
<div>

### Add elements
```python
fruits.append("date")          # end
fruits.insert(1, "avocado")    # at index
fruits.extend(["elderberry"])  # merge list
```

### Remove elements
```python
fruits.remove("banana")   # by value
fruits.pop()              # last (returns it)
fruits.pop(0)             # by index
del fruits[1]             # by index, no return
fruits.clear()            # empty the list
```

</div>
<div>

### Sort & reverse
```python
nums = [3, 1, 4, 1, 5]
nums.sort()              # in-place
nums.sort(reverse=True)
nums.reverse()           # in-place

sorted(nums)             # returns new list
```

### Useful helpers
```python
min(nums), max(nums), sum(nums)
enumerate(nums)   # (index, value) pairs
zip(a, b)         # pair two lists
```

</div>
</div>

---

## Aliasing vs. Copying

<div class="cols">
<div>

### Aliasing — shared reference
```python
a = [1, 2, 3]
b = a          # b points to same list
b.append(4)
print(a)       # [1, 2, 3, 4]  ← changed!
```

### Shallow copy — independent top level
```python
b = a[:]       # slice copy
b = a.copy()   # .copy() method
b = list(a)    # list() constructor

b.append(4)
print(a)       # [1, 2, 3]  ← safe
```

</div>
<div>

### Deep copy — independent at every level
```python
import copy

nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)

deep[0].append(99)
print(nested)  # [[1, 2], [3, 4]]  ← safe
```

<div class="callout warn">

Shallow copy is safe for flat lists. Use `deepcopy` when the list contains other mutable objects (nested lists, dicts).

</div>

</div>
</div>

---

<!-- _class: section -->

## 6.2 Tuples

Ordered, **immutable** sequences — safe, hashable, fast

---

## Creating & Using Tuples

<div class="cols">
<div>

### Literal (comma makes the tuple)
```python
point   = (3, 4)
single  = (42,)     # trailing comma required
empty   = ()
no_paren = 1, 2, 3  # parens optional
```

### `tuple()` constructor
```python
tuple([1, 2, 3])    # from list
tuple("abc")        # ('a', 'b', 'c')
tuple(range(4))     # (0, 1, 2, 3)
```

### Accessing (same as lists)
```python
point[0]     # 3
point[-1]    # 4
point[0:1]   # (3,)
```

</div>
<div>

### Immutability
```python
point[0] = 99   # TypeError — can't modify
```

<div class="callout rule">

**Use a tuple when data should not change** — coordinates, RGB colors, database rows, function return values. Tuples are hashable (can be dict keys or set elements); lists are not.

</div>

### Choosing list vs. tuple

| | `list` | `tuple` |
|---|---|---|
| Mutable | ✓ | ✗ |
| Hashable | ✗ | ✓ |
| Performance | good | slightly faster |

</div>
</div>

---

## Tuple Unpacking & Functions

<div class="cols">
<div>

### Basic unpacking
```python
x, y = (3, 4)
a, b, c = "abc"       # works on any iterable

# starred unpacking
first, *rest = (1, 2, 3, 4)
# first=1, rest=[2, 3, 4]
```

### `zip()` and `enumerate()`
```python
names  = ["alice", "bob"]
scores = [92, 85]

for name, score in zip(names, scores):
    print(name, score)

for i, name in enumerate(names):
    print(i, name)
```

</div>
<div>

### Multiple return values
```python
def min_max(nums):
    return min(nums), max(nums)  # returns tuple

lo, hi = min_max([3, 1, 4, 1, 5])
```

### Argument packing with `*args`
```python
def total(*args):    # args is a tuple
    return sum(args)

total(1, 2, 3, 4)   # 10
```

### Sorting by tuple key
```python
pairs = [("bob", 85), ("alice", 92)]
pairs.sort(key=lambda p: p[1])
# sort by score (second element)
```

</div>
</div>

---

<!-- _class: section -->

## 6.3 Sets

Unordered collections of **unique, hashable** elements

---

## Creating & Accessing Sets

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

## Set Operations

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

## Frozensets & Set Comprehensions

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

## Chapter 6 — Quick Reference

| Type | Ordered | Mutable | Duplicates | Hashable | Literal |
|---|---|---|---|---|---|
| `list` | ✓ | ✓ | ✓ | ✗ | `[1, 2]` |
| `tuple` | ✓ | ✗ | ✓ | ✓ | `(1, 2)` |
| `set` | ✗ | ✓ | ✗ | ✗ | `{1, 2}` |
| `frozenset` | ✗ | ✗ | ✗ | ✓ | `frozenset({1,2})` |

| Task | Idiom |
|---|---|
| Deduplicate | `list(set(lst))` |
| Unpack | `a, b, *rest = lst` |
| Copy flat list | `lst[:]` or `lst.copy()` |
| Multiple return | `return a, b` → unpack with `x, y = f()` |
| Set ops | `\|` `&` `-` `^` |
| Membership | `x in s` — O(1) for set/dict, O(n) for list |

---

<!-- _class: title -->

# End of Chapter 6

*Next: Chapter 7 — Dictionaries*

*key-value mappings · core operations · dictionary patterns*
