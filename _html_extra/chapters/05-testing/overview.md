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

# Chapter 5

Exceptions & Testing

*5.0 Intro · 5.1 Exceptions · 5.2 Unit Testing*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## Why Exceptions and Testing?

Handle failures gracefully and verify that code does what it claims

---

## Two Kinds of Problems

<div class="cols">
<div>

### Runtime failures

The program stops because Python raises an exception.

```python
age = int("twenty")
# ValueError
```

Exception handling lets the program recover or report a useful message.

</div>
<div>

### Semantic bugs

The program runs, but the answer is wrong.

```python
def average(nums):
    return sum(nums) / (len(nums) - 1)
# wrong formula
```

Tests catch wrong behavior before users do.

</div>
</div>

---

## Chapter 5 Toolkit

<div class="grid3">
<div><strong>Tracebacks</strong> Follow the error path to the failing line.</div>
<div><strong>try / except</strong> Recover from expected runtime failures.</div>
<div><strong>raise</strong> Signal invalid input or state clearly.</div>
<div><strong>logging</strong> Record what happened without cluttering output.</div>
<div><strong>assert</strong> Check assumptions while developing.</div>
<div><strong>tests</strong> Make behavior repeatable and verifiable.</div>
</div>

---

<!-- _class: section -->

## 5.1 Exceptions

Tracebacks, try/except, else/finally, custom exceptions, and logging

---

## Reading Tracebacks

<div class="cols">
<div>

- Start at the **bottom** for the exception type and message.
- Look upward to find the line in your code that failed.
- Tracebacks show the call stack: who called whom.

<div class="callout rule">

A traceback is a map, not just an error message.

</div>

</div>
<div>

```python
def parse_age(text):
    return int(text)

def register(raw_age):
    age = parse_age(raw_age)
    return {"age": age}

register("twenty")
# ValueError: invalid literal for int()
```

</div>
</div>

---

## `try` / `except`

<div class="cols">
<div>

- Put risky code in the `try` block.
- Catch specific exception types.
- Return, retry, or explain the failure.

<div class="callout warn">

Avoid bare `except:`. It can hide real bugs.

</div>

</div>
<div>

```python
def parse_int(text):
    try:
        return int(text)
    except ValueError:
        print(f"{text!r} is not an integer")
        return None

print(parse_int("42"))     # 42
print(parse_int("hello"))  # None
```

</div>
</div>

---

## Multiple Exceptions

<div class="cols">
<div>

Different failures deserve different responses.

| Exception | Common cause |
|---|---|
| `ValueError` | Invalid value, like `int("x")` |
| `FileNotFoundError` | Missing file path |
| `KeyError` | Missing dictionary key |
| `ZeroDivisionError` | Division by zero |

</div>
<div>

```python
def get_score(scores, name):
    try:
        return scores[name]
    except KeyError:
        return "missing student"
    except TypeError:
        return "scores must be a dict"
```

</div>
</div>

---

## `else` and `finally`

<div class="cols">
<div>

- `else` runs only if **no exception** occurred.
- `finally` always runs — exception or not.
- Use `finally` for cleanup.

</div>
<div>

```python
try:
    value = int("42")
except ValueError:
    print("bad input")
else:
    print("converted:", value)
finally:
    print("done")
```

</div>
</div>

---

## Raising Exceptions

<div class="cols">
<div>

- Use `raise` when a function cannot honor its contract.
- Choose a specific built-in exception when possible.
- Create custom exceptions for domain-specific failures.

</div>
<div>

```python
class OverdraftError(Exception):
    pass

def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise OverdraftError("insufficient funds")
    return balance - amount
```

</div>
</div>

---

## Logging

<div class="cols">
<div>

Logging records diagnostic information without scattered `print()` calls.

| Level | Use |
|---|---|
| `DEBUG` | Detailed developer info |
| `INFO` | Normal progress |
| `WARNING` | Unexpected but recoverable |
| `ERROR` | Operation failed |

</div>
<div>

```python
import logging

logging.basicConfig(level=logging.INFO)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("division by zero")
        return None
```

</div>
</div>

---

<!-- _class: section -->

## 5.2 Unit Testing

pytest, unittest, doctest, fixtures, mocking, parametrization, and coverage

---

## What is a Unit Test?

<div class="cols">
<div>

- A small automated check for one behavior.
- Tests one function, method, or class behavior.
- Should be repeatable and independent.

<div class="callout">

Tests turn examples into executable evidence.

</div>

</div>
<div>

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

</div>
</div>

---

## `pytest`

<div class="cols">
<div>

- Test files start with `test_`.
- Test functions start with `test_`.
- Use plain `assert` statements.

<div class="callout rule">

Run from the terminal with `python -m pytest`.

</div>

</div>
<div>

```python
# test_calc.py
from calc import add, divide

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5
```

</div>
</div>

---

## Testing Exceptions

<div class="cols">
<div>

Good tests check both normal behavior and expected failure behavior.

- Use `pytest.raises` for expected exceptions.
- Test the contract, not implementation details.

</div>
<div>

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b cannot be 0")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

</div>
</div>

---

## `unittest`

<div class="cols">
<div>

- Python's built-in testing framework.
- Organizes tests inside classes.
- Uses assertion methods like `assertEqual`.

<div class="callout">

You will see `unittest` in many older or standard-library-oriented projects.

</div>

</div>
<div>

```python
import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

</div>
</div>

---

## Doctests

<div class="cols">
<div>

- Examples embedded in docstrings.
- Useful for simple functions and documentation.
- Best when outputs are short and stable.

</div>
<div>

```python
def square(x):
    """Return x squared.

    >>> square(4)
    16
    >>> square(-3)
    9
    """
    return x * x
```

</div>
</div>

---

## Advanced pytest Tools

<div class="cols">
<div>

| Tool | Use |
|---|---|
| Parametrize | Run one test with many inputs |
| Fixture | Reusable setup data or objects |
| Mock | Replace slow or external dependencies |
| Coverage | Find code paths tests did not run |

</div>
<div>

```python
import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [(2, 3, 5), (0, 0, 0), (-1, 1, 0)]
)
def test_add_cases(a, b, expected):
    assert add(a, b) == expected
```

</div>
</div>

---

## Testing Strategy

<div class="cols">
<div>

### Test these first

- Normal cases
- Boundary cases
- Error cases
- Previously fixed bugs

</div>
<div>

### Keep tests useful

- Small and focused
- Readable names
- Independent of test order
- Fast enough to run often

</div>
</div>

<div class="callout">

Testing is design feedback: if code is hard to test, it is often doing too much.

</div>

---

## Chapter 5 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Catch exception | `try:` / `except ValueError:` |
| Exception object | `except Exception as e:` |
| Cleanup | `finally` always runs |
| Raise exception | `raise ValueError("message")` |
| Logging | `logging.info()`, `logging.error()` |
| pytest test | `def test_name(): assert result == expected` |
| Expected exception | `with pytest.raises(Error):` |
| unittest | `class TestX(unittest.TestCase):` |
| doctest | Examples in docstrings with `>>>` |

---

<!-- _class: title -->

# End of Chapter 5

*Next: Chapter 6 — Lists*

*tracebacks · exceptions · logging · pytest · unittest · doctest*
