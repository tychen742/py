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

# Chapter 4

Functions

*4.0 Intro · 4.1 Functions · 4.2 Function Design · 4.3 Recursion*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 4.1 Functions

Defining, calling, parameters, return values, type annotations

---

## Defining & Calling Functions

<div class="cols">
<div>

```python
def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"

print(greet("Alice"))   # Hello, Alice!
```

- `def` keyword defines a function.
- The body is indented.
- `return` sends a value back to the caller.
- Without `return`, a function returns `None`.

</div>
<div>

### Parameters & Arguments

```python
def power(base, exp=2):     # default value
    return base ** exp

print(power(3))      # 9   (exp=2)
print(power(3, 3))   # 27  (exp=3)
print(power(exp=3, base=2)) # 8 (keyword)
```

| Term | Meaning |
|---|---|
| Parameter | Variable in the function definition |
| Argument | Value passed when calling |

</div>
</div>

---

## `*args` and `**kwargs`

<div class="cols">
<div>

```python
# *args — variable positional arguments (tuple)
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))   # 10

# **kwargs — variable keyword arguments (dict)
def describe(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe(name="Alice", age=25, city="Rolla")
```

</div>
<div>

### Full parameter order

```python
def f(pos, /, normal, *, kw_only,
      **kwargs):
    ...
```

| Type | Example |
|---|---|
| Positional | `f(1)` |
| Default | `f(x=2)` |
| `*args` | Collects extras → tuple |
| `**kwargs` | Collects key=val → dict |

</div>
</div>

---

<!-- _class: section -->

## 4.2 Function Design

Scope, composition, docstrings, lambda

---

## Scope

<div class="cols">
<div>

- **Local scope**: variables inside a function.
- **Global scope**: variables at the module level.
- A function can **read** globals but not **write** to them without `global`.

```python
x = 10   # global

def show():
    print(x)   # reads global — OK

def double():
    global x
    x *= 2     # modifies global — needs 'global'
```

</div>
<div>

<div class="callout warn">

Prefer **returning values** over modifying globals. Functions that depend only on their arguments are easier to test.

</div>

### Function composition

```python
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def format_temp(c):
    f = celsius_to_fahrenheit(c)
    return f"{c}°C = {f:.1f}°F"

print(format_temp(100))   # 100°C = 212.0°F
```

</div>
</div>

---

## Docstrings & Lambda

<div class="cols">
<div>

### Docstrings

```python
def area(radius):
    """Return the area of a circle.

    Args:
        radius: The radius (non-negative float).
    Returns:
        Area as a float.
    """
    import math
    return math.pi * radius ** 2
```

Access with `help(area)` or `area.__doc__`.

</div>
<div>

### Lambda — small anonymous function

```python
# Named function
def square(x): return x ** 2

# Equivalent lambda
square = lambda x: x ** 2

# Common use: sort key
words = ["banana", "kiwi", "apple"]
words.sort(key=lambda w: len(w))
print(words)   # ['kiwi', 'apple', 'banana']
```

<div class="callout warn">

Use `def` when the logic needs a name or more than one expression.

</div>

</div>
</div>

---

<!-- _class: section -->

## 4.3 Recursion

Recursive functions · base cases · tracing calls

---

## Recursion

<div class="cols">
<div>

A function that calls **itself**. Every recursive function needs:

1. A **base case** — stops the recursion.
2. A **recursive case** — moves toward the base case.

<div class="callout warn">

Without a base case, recursion runs forever → `RecursionError`.

</div>

</div>
<div>

```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))   # 120
# 5 * 4 * 3 * 2 * 1 * 1 = 120
```

```python
def fibonacci(n):
    if n <= 1:          # base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 55
```

</div>
</div>

---

## Chapter 4 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Define function | `def name(params): return value` |
| Default param | `def f(x=10):` |
| `*args` | Collect extra positional → tuple |
| `**kwargs` | Collect extra keyword → dict |
| Docstring | Triple-quoted string as first statement |
| Lambda | `lambda args: expression` |
| Scope | Local vars stay local; use `return` |
| Recursion | Must have a base case |

---

<!-- _class: title -->

# End of Chapter 4

*Next: Chapter 5 — Exceptions & Testing*

*try · except · raise · pytest · unittest · doctest*
