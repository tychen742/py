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

# Chapter 11

Iterators & Generators

*12.0 Intro · 12.1 Iterators · 12.2 Generators*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 11.1 Iterators

The iteration protocol · iter() / next() · built-in lazy iterators · custom classes

---

## The Iterator Protocol

<div class="cols">
<div>

An **iterable** can be looped over. An **iterator** remembers where it is.

```python
# What a for loop does internally
nums = [1, 2, 3]
it = iter(nums)          # get iterator

print(next(it))          # 1
print(next(it))          # 2
print(next(it))          # 3
# next(it) → StopIteration
```

</div>
<div>

### Built-in lazy iterators

| Function | What it produces |
|---|---|
| `enumerate(seq)` | `(index, value)` pairs |
| `zip(a, b)` | `(a_i, b_i)` pairs |
| `map(f, seq)` | `f(x)` for each x |
| `filter(pred, seq)` | elements where `pred(x)` is True |
| `reversed(seq)` | elements in reverse |

All are **lazy** — values produced on demand.

</div>
</div>

---

## Custom Iterator Classes

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self           # the iterator IS the iterable here

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in Countdown(5):
    print(n, end=" ")   # 5 4 3 2 1
```

---

<!-- _class: section -->

## 11.2 Generators

`yield` · generator expressions · any/all · itertools

---

## Generator Functions

<div class="cols">
<div>

A generator function uses `yield` instead of `return`. It produces values **lazily** — one at a time.

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

gen = count_up_to(3)
print(next(gen))   # 1
print(next(gen))   # 2
for val in gen:
    print(val)     # 3
```

</div>
<div>

### Memory efficiency

```python
import sys

# List: builds everything in memory
lst = [x**2 for x in range(1_000_000)]
print(sys.getsizeof(lst))   # ~8 MB

# Generator: produces one value at a time
gen = (x**2 for x in range(1_000_000))
print(sys.getsizeof(gen))   # ~200 bytes
```

<div class="callout">

Use a generator when you iterate **once** and don't need to store all values.

</div>

</div>
</div>

---

## `any()` and `all()` with Generator Expressions

Dropping the brackets avoids building an intermediate list and enables **short-circuit evaluation**:

```python
data = [4, -1, 7, 0, 3, -2]

# any() stops as soon as it finds True
print(any(x < 0 for x in data))      # True  (stops at -1)

# all() stops as soon as it finds False
print(all(x > 0 for x in data))      # False (stops at -1)

# Common validation patterns
scores = [82, 91, 74, 88, 65]
print(all(s >= 60 for s in scores))  # True — all passed
print(any(s >= 90 for s in scores))  # True — at least one A
```

---

## `itertools` Highlights

<div class="cols">
<div>

| Function | Description |
|---|---|
| `islice(it, n)` | Take first n items |
| `chain(a, b)` | Concatenate iterables |
| `count(start, step)` | Infinite counter |
| `cycle(seq)` | Repeat sequence infinitely |
| `combinations(seq, r)` | r-length combos |
| `permutations(seq, r)` | r-length ordered arrangements |

</div>
<div>

```python
import itertools

# Infinite Fibonacci
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

first_10 = list(itertools.islice(fib(), 10))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Combinations
pairs = list(itertools.combinations("ABCD", 2))
# [('A','B'), ('A','C'), ...]
```

</div>
</div>

---

## Chapter 11 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Iterator protocol | `__iter__` returns self; `__next__` returns next value |
| Manual iteration | `it = iter(seq)` → `next(it)` → `StopIteration` |
| Built-in lazy | `enumerate`, `zip`, `map`, `filter`, `reversed` |
| Generator function | `def f(): yield value` |
| Generator expression | `(expr for x in seq)` — lazy, O(1) memory |
| any / all | Drop brackets for short-circuit: `any(x > 0 for x in seq)` |
| yield from | Delegate to sub-generator |
| itertools | `islice`, `chain`, `count`, `cycle`, `combinations` |

---

<!-- _class: title -->

# End of Chapter 11

*Next: Chapter 12 — APIs*

*HTTP · requests · JSON · authentication · pagination*
