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

Functional Programming in Python

*11.0 Intro · 11.1 Functional Concepts · 11.2 Functional Practice*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## What is Functional Programming?

Writing programs as transformations from inputs to outputs

---

## Why Functional Programming?

<div class="cols">
<div>

### Imperative approach

Describe each step and update state along the way.

```python
prices = [10, 20, 30]
discounted = []

for price in prices:
    new_price = price * 0.9
    discounted.append(new_price)
```

</div>
<div>

### Functional approach

Describe the transformation and produce a new value.

```python
prices = [10, 20, 30]

discounted = [
    price * 0.9
    for price in prices
]
```

</div>
</div>

<div class="callout">

FP benefits: smaller functions, fewer side effects, easier testing, and clearer data pipelines.

</div>

---

## Functional Vocabulary

<div class="grid3">
<div><strong>Pure function</strong> Same input gives same output; no external changes.</div>
<div><strong>Immutability</strong> Return new values instead of changing old ones.</div>
<div><strong>First-class function</strong> Pass functions around like any other value.</div>
<div><strong>Higher-order function</strong> Takes a function or returns a function.</div>
<div><strong>Lambda</strong> Small anonymous function written inline.</div>
<div><strong>Decorator</strong> Wraps a function with reusable behavior.</div>
</div>

---

<!-- _class: section -->

## 11.1 Functional Concepts

Purity, immutability, functions as values, lambdas, decorators, comprehensions

---

## Pure Functions

<div class="cols">
<div>

- Depend only on their arguments.
- Return a value instead of modifying external state.
- Easier to test because they are predictable.

<div class="callout rule">

Same input → same output. No hidden reads or writes.

</div>

</div>
<div>

```python
# Pure
def add_tax(price, rate):
    return price * (1 + rate)

# Not pure: depends on global state
tax_rate = 0.07

def add_tax_global(price):
    return price * (1 + tax_rate)
```

</div>
</div>

---

## Immutability

<div class="cols">
<div>

Functional code often returns a new value instead of changing an existing one.

- Original data stays available.
- Unexpected side effects are less likely.
- Pipelines become easier to reason about.

</div>
<div>

```python
def add_item(items, new_item):
    return items + [new_item]

cart = ["book", "pen"]
new_cart = add_item(cart, "notebook")

print(cart)      # ['book', 'pen']
print(new_cart)  # ['book', 'pen', 'notebook']
```

</div>
</div>

---

## Functions as Values

<div class="cols">
<div>

- Assign a function to a variable.
- Pass a function as an argument.
- Return a function from another function.

<div class="callout">

This is the foundation for `map`, `filter`, decorators, callbacks, and custom sorting.

</div>

</div>
<div>

```python
def square(x):
    return x * x

def apply(func, values):
    return [func(v) for v in values]

nums = [1, 2, 3, 4]
print(apply(square, nums))
# [1, 4, 9, 16]
```

</div>
</div>

---

## Lambda Functions

<div class="cols">
<div>

A `lambda` is a small anonymous function for simple expressions.

| Use case | Example |
|---|---|
| Sort key | `key=lambda s: len(s)` |
| Quick transform | `lambda x: x * 2` |
| Pair key | `lambda item: item[1]` |

<div class="callout warn">

If the logic needs multiple steps, use `def`.

</div>

</div>
<div>

```python
names = ["Ada", "Grace", "Linus"]

by_length = sorted(
    names,
    key=lambda name: len(name)
)

print(by_length)
# ['Ada', 'Grace', 'Linus']
```

</div>
</div>

---

## Map, Filter, and Comprehensions

<div class="cols">
<div>

### Functional tools

```python
nums = [1, 2, 3, 4, 5]

squares = list(map(lambda n: n*n, nums))
evens   = list(filter(lambda n: n % 2 == 0, nums))
```

</div>
<div>

### Pythonic alternative

```python
nums = [1, 2, 3, 4, 5]

squares = [n*n for n in nums]
evens   = [n for n in nums if n % 2 == 0]
```

</div>
</div>

<div class="callout">

In Python, comprehensions are often clearer than `map` and `filter` with lambdas.

</div>

---

## Higher-Order Functions

<div class="cols">
<div>

A higher-order function works with other functions.

- Takes a function as input.
- Returns a function as output.
- Builds reusable behavior without duplicating control flow.

</div>
<div>

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30
```

</div>
</div>

---

## Decorators

<div class="cols">
<div>

- A decorator takes a function and returns a wrapped function.
- Use for logging, timing, validation, caching, and access checks.
- `@decorator` syntax replaces manual wrapping.

</div>
<div>

```python
def announce(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@announce
def greet(name):
    return f"Hello, {name}"

print(greet("Ada"))
```

</div>
</div>

---

<!-- _class: section -->

## 11.2 Functional Practice

Recursion, context managers, and practical tools from `functools`

---

## Recursion

<div class="cols">
<div>

- A recursive function calls itself.
- Every recursive function needs a **base case**.
- Good fit for problems with repeated self-similar structure.

<div class="callout warn">

Recursion is elegant for some problems, but iteration is often simpler in Python.

</div>

</div>
<div>

```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))     # 120
```

</div>
</div>

---

## Context Managers

<div class="cols">
<div>

A context manager handles setup and cleanup around a block of code.

- Open and close files safely.
- Acquire and release resources.
- Keep cleanup reliable even when errors happen.

</div>
<div>

```python
from contextlib import contextmanager

@contextmanager
def section(name):
    print(f"Start {name}")
    try:
        yield
    finally:
        print(f"End {name}")

with section("demo"):
    print("working")
```

</div>
</div>

---

## The `functools` Module

<div class="cols">
<div>

| Tool | Use |
|---|---|
| `reduce` | Combine many values into one |
| `partial` | Pre-fill some function arguments |
| `lru_cache` | Memoize expensive function calls |

<div class="callout rule">

Use these when they simplify the code. Do not force them into every problem.

</div>

</div>
<div>

```python
from functools import reduce, partial, lru_cache

total = reduce(lambda a, b: a + b, [1, 2, 3])

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

</div>
</div>

---

## Choosing a Style

<div class="cols">
<div>

### Use functional style when…

- You are transforming collections.
- A pure helper function makes logic easier to test.
- A comprehension or small pipeline is clearer than a loop.

</div>
<div>

### Prefer another style when…

- The lambda becomes hard to read.
- The code needs several statements or error handling.
- Mutating state is the simplest honest model.

</div>
</div>

<div class="callout">

Python supports multiple styles. The goal is readable, testable code — not functional purity.

</div>

---

## Chapter 10 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Pure function | No side effects; depends only on arguments |
| Immutable update | Return a new value instead of mutating the original |
| Lambda | `lambda args: expression` |
| Map / filter | `map(func, xs)`, `filter(pred, xs)` |
| Comprehension | `[expr for item in xs if condition]` |
| Decorator | `@decorator` wraps a function |
| Recursion | Base case plus recursive case |
| Context manager | `with manager:` handles setup and cleanup |
| functools | `reduce`, `partial`, `lru_cache` |

---

<!-- _class: title -->

# End of Chapter 10

*Next: Chapter 11 — Iterators & Generators*

*iterators · generators · yield · itertools*
