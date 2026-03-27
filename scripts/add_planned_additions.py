#!/usr/bin/env python3
"""Add Planned Additions topics to ch11-15 notebooks."""
import json, uuid, sys, os

def cell_id():
    return str(uuid.uuid4())[:8]

def md(src_lines):
    return {"cell_type": "markdown", "id": cell_id(), "metadata": {}, "source": src_lines}

def code(src_lines):
    return {"cell_type": "code", "execution_count": None, "id": cell_id(),
            "metadata": {}, "outputs": [], "source": src_lines}

def find_idx(cells, substring):
    for i, c in enumerate(cells):
        if substring in ''.join(c['source']):
            return i
    return None

def load(path):
    with open(path) as f:
        return json.load(f)

def save(nb, path):
    with open(path, 'w') as f:
        json.dump(nb, f, indent=1)
    print(f"Saved {path} ({len(nb['cells'])} cells)")

# ──────────────────────────────────────────────────────────────────
# 1. CH11 / 1101: Add ## Logging before ## Summary
# ──────────────────────────────────────────────────────────────────
def update_1101():
    path = 'chapters/11-testing/1101-exceptions.ipynb'
    nb = load(path)
    cells = nb['cells']
    idx = find_idx(cells, '## Summary')
    assert idx is not None, "Summary not found in 1101"

    new = [
        md([
            "## Logging\n",
            "\n",
            "The `logging` module provides a flexible framework for recording diagnostic\n",
            "messages during program execution. Unlike `print()`, logging lets you control\n",
            "*which* messages appear, *where* they go, and *how much detail* to include —\n",
            "without changing your code.\n",
            "\n",
            "### Log Levels\n",
            "\n",
            "| Level | Value | When to use |\n",
            "|---|---|---|\n",
            "| `DEBUG` | 10 | Detailed diagnostic info (development only) |\n",
            "| `INFO` | 20 | Confirmation that things are working as expected |\n",
            "| `WARNING` | 30 | Something unexpected; program still running |\n",
            "| `ERROR` | 40 | A more serious problem; something failed |\n",
            "| `CRITICAL` | 50 | A severe error; program may not continue |\n",
            "\n",
            "The default level is `WARNING` — only `WARNING`, `ERROR`, and `CRITICAL`\n",
            "messages appear unless you configure a lower threshold.\n",
        ]),
        code([
            "import logging\n",
            "\n",
            "# Show ALL levels (DEBUG and above)\n",
            "logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')\n",
            "\n",
            "logging.debug('Reading config file')        # detailed diagnostics\n",
            "logging.info('Server started on port 8080') # normal operations\n",
            "logging.warning('Disk space is low')        # something unexpected\n",
            "logging.error('Failed to connect to database')  # something failed\n",
            "logging.critical('System is shutting down') # severe error\n",
        ]),
        md([
            "### Logging vs `print()`\n",
            "\n",
            "| | `print()` | `logging` |\n",
            "|---|---|---|\n",
            "| Severity levels | No | Yes |\n",
            "| Easy to silence | No (must delete/comment) | Yes (set level higher) |\n",
            "| Timestamps | No | Yes (with format string) |\n",
            "| Write to file | No | Yes |\n",
            "| Production-ready | No | Yes |\n",
            "\n",
            "Best practice: use `print()` for user-facing output and `logging` for\n",
            "diagnostic messages during development and production monitoring.\n",
        ]),
        code([
            "import logging\n",
            "\n",
            "logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')\n",
            "\n",
            "def divide(a, b):\n",
            "    logging.debug(f'divide called with a={a}, b={b}')\n",
            "    if b == 0:\n",
            "        logging.error('Division by zero attempted')\n",
            "        raise ValueError('Cannot divide by zero')\n",
            "    result = a / b\n",
            "    logging.info(f'Result: {result}')\n",
            "    return result\n",
            "\n",
            "print(divide(10, 2))   # 5.0\n",
        ]),
        code([
            "### Exercise: Add Logging\n",
            "#   Rewrite `safe_sqrt(x)` to use `logging` instead of `print`:\n",
            "#     - DEBUG: log the input value before computing\n",
            "#     - WARNING: log a warning if x is negative\n",
            "#     - ERROR: raise ValueError if x is negative\n",
            "#     - INFO: log the result before returning\n",
            "#   Test: safe_sqrt(25) → 5.0; safe_sqrt(0) → 0.0; safe_sqrt(-4) → ValueError.\n",
            "import math\n",
            "### Your code starts here.\n",
            "\n",
            "\n",
            "\n",
            "### Your code ends here.\n",
        ]),
        code([
            "### Solution\n",
            "import math, logging\n",
            "\n",
            "logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')\n",
            "\n",
            "def safe_sqrt(x):\n",
            "    logging.debug(f'safe_sqrt({x})')\n",
            "    if x < 0:\n",
            "        logging.warning(f'Negative input: {x}')\n",
            "        raise ValueError(f'Cannot take sqrt of {x}')\n",
            "    result = math.sqrt(x)\n",
            "    logging.info(f'Result: {result}')\n",
            "    return result\n",
            "\n",
            "print(safe_sqrt(25))   # 5.0\n",
            "print(safe_sqrt(0))    # 0.0\n",
            "try:\n",
            "    safe_sqrt(-4)\n",
            "except ValueError as e:\n",
            "    print(f'Caught: {e}')\n",
        ]),
    ]

    nb['cells'] = cells[:idx] + new + cells[idx:]
    save(nb, path)

# ──────────────────────────────────────────────────────────────────
# 2. CH11 / 1102: Add ## pytest after last cell (appended at end)
# ──────────────────────────────────────────────────────────────────
def update_1102():
    path = 'chapters/11-testing/1102-unit-testing.ipynb'
    nb = load(path)
    cells = nb['cells']

    # Find the last doctest exercise solution cell and insert pytest after it
    new = [
        md([
            "## pytest\n",
            "\n",
            "`pytest` is the most widely used testing framework in Python. Unlike `unittest`,\n",
            "it requires no boilerplate classes — you write plain functions that start with\n",
            "`test_`, use plain `assert` statements, and run everything with `pytest` on the\n",
            "command line.\n",
            "\n",
            "### Install\n",
            "\n",
            "```bash\n",
            "pip install pytest\n",
            "```\n",
            "\n",
            "### Test file convention\n",
            "\n",
            "Save test functions in files named `test_*.py` or `*_test.py`.\n",
            "`pytest` discovers them automatically.\n",
            "\n",
            "```python\n",
            "# test_math.py\n",
            "def test_add():\n",
            "    assert 1 + 1 == 2\n",
            "\n",
            "def test_divide():\n",
            "    assert 10 / 2 == 5.0\n",
            "\n",
            "def test_divide_by_zero():\n",
            "    import pytest\n",
            "    with pytest.raises(ZeroDivisionError):\n",
            "        1 / 0\n",
            "```\n",
            "\n",
            "Run from the terminal:\n",
            "```bash\n",
            "pytest test_math.py -v\n",
            "```\n",
        ]),
        md([
            "### pytest vs unittest\n",
            "\n",
            "| Feature | `unittest` | `pytest` |\n",
            "|---|---|---|\n",
            "| Requires class? | Yes (`TestCase`) | No |\n",
            "| Assertion style | `self.assertEqual(a, b)` | `assert a == b` |\n",
            "| Discovery | Manual `unittest.main()` | Automatic with `pytest` command |\n",
            "| Output | Minimal | Detailed, colored diff |\n",
            "| Fixtures | `setUp/tearDown` | `@pytest.fixture` |\n",
            "| Ecosystem | Standard library | Third-party, widely adopted |\n",
            "\n",
            "Both are valid. `unittest` is built-in; `pytest` is preferred in industry\n",
            "because its plain-`assert` style produces clearer failure messages.\n",
        ]),
        code([
            "# pytest can be run inside a Jupyter notebook using the ipython-pytest plugin\n",
            "# or by writing the test file to disk and invoking subprocess.\n",
            "# Here we demonstrate the test structure using inline assertion checks:\n",
            "\n",
            "def add(a, b):\n",
            "    return a + b\n",
            "\n",
            "def subtract(a, b):\n",
            "    return a - b\n",
            "\n",
            "# pytest-style test functions (would go in test_calc.py)\n",
            "def test_add_positive():\n",
            "    assert add(2, 3) == 5\n",
            "\n",
            "def test_add_negative():\n",
            "    assert add(-1, -1) == -2\n",
            "\n",
            "def test_subtract():\n",
            "    assert subtract(10, 4) == 6\n",
            "\n",
            "# Run them manually (simulating pytest discovery)\n",
            "for test_fn in [test_add_positive, test_add_negative, test_subtract]:\n",
            "    test_fn()\n",
            "    print(f'{test_fn.__name__} PASSED')\n",
        ]),
        code([
            "### Exercise: Write pytest-style tests\n",
            "#   Write three test functions for `is_palindrome(s)` defined below:\n",
            "#     1. test_palindrome_true: a word that IS a palindrome\n",
            "#     2. test_palindrome_false: a word that is NOT a palindrome\n",
            "#     3. test_palindrome_empty: the empty string should be considered a palindrome\n",
            "#   Each function should use plain `assert` (no `self`, no class).\n",
            "\n",
            "def is_palindrome(s):\n",
            "    return s == s[::-1]\n",
            "\n",
            "### Your code starts here.\n",
            "\n",
            "\n",
            "\n",
            "### Your code ends here.\n",
        ]),
        code([
            "### Solution\n",
            "\n",
            "def is_palindrome(s):\n",
            "    return s == s[::-1]\n",
            "\n",
            "def test_palindrome_true():\n",
            "    assert is_palindrome('racecar') == True\n",
            "    assert is_palindrome('madam') == True\n",
            "\n",
            "def test_palindrome_false():\n",
            "    assert is_palindrome('hello') == False\n",
            "\n",
            "def test_palindrome_empty():\n",
            "    assert is_palindrome('') == True\n",
            "\n",
            "for fn in [test_palindrome_true, test_palindrome_false, test_palindrome_empty]:\n",
            "    fn()\n",
            "    print(f'{fn.__name__} PASSED')\n",
        ]),
    ]

    nb['cells'] = cells + new
    save(nb, path)

# ──────────────────────────────────────────────────────────────────
# 3. CH12 / 1201: Add @classmethod after Static Methods section
#                  Add __repr__ and @property after __str__ section
# ──────────────────────────────────────────────────────────────────
def update_1201():
    path = 'chapters/12-oop/1201-oop-design.ipynb'
    nb = load(path)
    cells = nb['cells']

    # Insertion 1: @classmethod after cell id=008f2327 (cell 132)
    cm_idx = next(i for i, c in enumerate(cells) if c.get('id','') == '008f2327') + 1

    classmethod_cells = [
        md([
            "### Class Methods\n",
            "\n",
            "A **class method** is a method that receives the *class itself* as its first\n",
            "argument (conventionally named `cls`) instead of an instance. Class methods\n",
            "are decorated with `@classmethod` and are commonly used as **alternative\n",
            "constructors** — ways to create an instance from different kinds of input.\n",
        ]),
        code([
            "%%add_method_to Time\n",
            "\n",
            "    @classmethod\n",
            "    def from_string(cls, s):\n",
            "        \"\"\"Create a Time from a 'HH:MM:SS' string.\"\"\"\n",
            "        parts = s.split(':')\n",
            "        hour, minute, second = int(parts[0]), int(parts[1]), int(parts[2])\n",
            "        return cls(hour, minute, second)\n",
        ]),
        code([
            "# Use the class method as an alternative constructor\n",
            "t = Time.from_string('09:45:30')\n",
            "print(t)   # 09:45:30\n",
            "\n",
            "# Contrast: static method uses the class name; class method receives it\n",
            "# as `cls`, so subclasses inherit the right constructor automatically.\n",
        ]),
    ]

    # Insertion 2: __repr__ and @property after cell id=ad482b8a (cell 148, end of __str__ section)
    repr_idx = next(i for i, c in enumerate(cells) if c.get('id','') == 'ad482b8a') + 1

    repr_property_cells = [
        md([
            "### The `__repr__` Method\n",
            "\n",
            "`__repr__` returns a string that ideally looks like a valid Python expression\n",
            "that could recreate the object. It is used in the interactive interpreter and\n",
            "by `repr()`. When `__str__` is not defined, Python falls back to `__repr__`.\n",
            "\n",
            "| Method | Called by | Purpose |\n",
            "|---|---|---|\n",
            "| `__str__` | `str()`, `print()`, f-strings | Human-readable output |\n",
            "| `__repr__` | `repr()`, interactive shell | Unambiguous, ideally reconstructable |\n",
        ]),
        code([
            "%%add_method_to Time\n",
            "\n",
            "    def __repr__(self):\n",
            "        return f'Time({self.hour}, {self.minute}, {self.second})'\n",
        ]),
        code([
            "t = Time(9, 45, 30)\n",
            "print(str(t))    # 09:45:30       ← from __str__\n",
            "print(repr(t))   # Time(9, 45, 30) ← from __repr__\n",
        ]),
        md([
            "### Properties\n",
            "\n",
            "The `@property` decorator lets you define a method that behaves like an attribute.\n",
            "This is useful when you want controlled read-only (or validated) access to a\n",
            "value computed from object state, *without* changing how callers access it.\n",
        ]),
        code([
            "%%add_method_to Time\n",
            "\n",
            "    @property\n",
            "    def total_seconds(self):\n",
            "        \"\"\"Total seconds since midnight (read-only).\"\"\"\n",
            "        return self.hour * 3600 + self.minute * 60 + self.second\n",
        ]),
        code([
            "t = Time(1, 30, 0)\n",
            "# Access like an attribute — no parentheses needed\n",
            "print(t.total_seconds)   # 5400\n",
            "\n",
            "# Attempting to set it raises AttributeError (read-only)\n",
            "try:\n",
            "    t.total_seconds = 9999\n",
            "except AttributeError as e:\n",
            "    print(f'Error: {e}')\n",
        ]),
    ]

    # Apply insertions from BACK to FRONT so indices stay valid
    nb['cells'] = (cells[:repr_idx] + repr_property_cells +
                   cells[repr_idx:])
    # Now re-load and apply @classmethod insertion
    cells2 = nb['cells']
    cm_idx2 = next(i for i, c in enumerate(cells2) if c.get('id','') == '008f2327') + 1
    nb['cells'] = cells2[:cm_idx2] + classmethod_cells + cells2[cm_idx2:]

    save(nb, path)

# ──────────────────────────────────────────────────────────────────
# 4. CH12 / 1202: Add super(), issubclass(), @dataclass before Summary
# ──────────────────────────────────────────────────────────────────
def update_1202():
    path = 'chapters/12-oop/1202-oop-practice.ipynb'
    nb = load(path)
    cells = nb['cells']
    idx = find_idx(cells, '## Summary')
    assert idx is not None

    new = [
        md([
            "## `super()` and `issubclass()`\n",
            "\n",
            "### `super()`\n",
            "\n",
            "`super()` returns a proxy object that lets you call a method from a parent\n",
            "class without naming it explicitly. This is especially useful in `__init__`\n",
            "to ensure the parent class is properly initialized before you add child-specific\n",
            "attributes.\n",
        ]),
        code([
            "class Animal:\n",
            "    def __init__(self, name, sound):\n",
            "        self.name = name\n",
            "        self.sound = sound\n",
            "\n",
            "    def speak(self):\n",
            "        return f'{self.name} says {self.sound}!'\n",
            "\n",
            "class Dog(Animal):\n",
            "    def __init__(self, name, breed):\n",
            "        super().__init__(name, sound='Woof')  # call parent __init__\n",
            "        self.breed = breed\n",
            "\n",
            "    def info(self):\n",
            "        return f'{self.name} is a {self.breed}'\n",
            "\n",
            "d = Dog('Rex', 'Labrador')\n",
            "print(d.speak())   # Rex says Woof!\n",
            "print(d.info())    # Rex is a Labrador\n",
        ]),
        md([
            "### `issubclass()`\n",
            "\n",
            "`issubclass(Child, Parent)` returns `True` if `Child` is a subclass of `Parent`\n",
            "(or is `Parent` itself). Use it when you want to check class relationships at\n",
            "runtime — analogous to `isinstance()`, but for classes rather than instances.\n",
            "\n",
            "| Function | Checks |\n",
            "|---|---|\n",
            "| `isinstance(obj, cls)` | Is `obj` an instance of `cls` (or subclass)? |\n",
            "| `issubclass(A, B)` | Is class `A` a subclass of `B`? |\n",
        ]),
        code([
            "print(issubclass(Dog, Animal))   # True\n",
            "print(issubclass(Animal, Dog))   # False\n",
            "print(issubclass(Dog, Dog))      # True (a class is a subclass of itself)\n",
            "\n",
            "# Common use: guarding against wrong arguments\n",
            "def make_animal(cls, *args, **kwargs):\n",
            "    if not issubclass(cls, Animal):\n",
            "        raise TypeError(f'{cls} is not an Animal subclass')\n",
            "    return cls(*args, **kwargs)\n",
            "\n",
            "rex = make_animal(Dog, 'Rex', 'Labrador')\n",
            "print(rex.speak())   # Rex says Woof!\n",
        ]),
        md([
            "## `@dataclass`\n",
            "\n",
            "The `@dataclass` decorator (from `dataclasses`) automatically generates\n",
            "`__init__`, `__repr__`, and `__eq__` for you based on class-level type\n",
            "annotations. It drastically reduces boilerplate for simple data-holding classes.\n",
            "\n",
            "```python\n",
            "from dataclasses import dataclass\n",
            "\n",
            "@dataclass\n",
            "class Point:\n",
            "    x: float\n",
            "    y: float\n",
            "```\n",
            "\n",
            "This is equivalent to defining `__init__(self, x, y)`, `__repr__`, and\n",
            "`__eq__` manually.\n",
        ]),
        code([
            "from dataclasses import dataclass, field\n",
            "\n",
            "@dataclass\n",
            "class Student:\n",
            "    name: str\n",
            "    gpa: float\n",
            "    courses: list = field(default_factory=list)  # mutable default\n",
            "\n",
            "s1 = Student('Alice', 3.8)\n",
            "s2 = Student('Alice', 3.8)\n",
            "\n",
            "print(s1)            # Student(name='Alice', gpa=3.8, courses=[])\n",
            "print(s1 == s2)      # True  — __eq__ compares field values\n",
            "print(repr(s1))      # Student(name='Alice', gpa=3.8, courses=[])\n",
            "\n",
            "s1.courses.append('CS101')\n",
            "print(s1.courses)    # ['CS101']\n",
            "print(s2.courses)    # [] — separate list (field(default_factory=list))\n",
        ]),
        code([
            "### Exercise: Dataclass Design\n",
            "#   Define a @dataclass named `Book` with fields:\n",
            "#     title: str, author: str, year: int, pages: int = 0\n",
            "#   Then:\n",
            "#   1. Create two Book instances — one without specifying pages.\n",
            "#   2. Print both — confirm __repr__ is auto-generated.\n",
            "#   3. Check equality: two books with the same title/author/year/pages should be equal.\n",
            "### Your code starts here.\n",
            "\n",
            "\n",
            "\n",
            "### Your code ends here.\n",
        ]),
        code([
            "### Solution\n",
            "from dataclasses import dataclass\n",
            "\n",
            "@dataclass\n",
            "class Book:\n",
            "    title: str\n",
            "    author: str\n",
            "    year: int\n",
            "    pages: int = 0\n",
            "\n",
            "b1 = Book('Think Python', 'Allen Downey', 2024)\n",
            "b2 = Book('Think Python', 'Allen Downey', 2024, 350)\n",
            "b3 = Book('Think Python', 'Allen Downey', 2024)\n",
            "\n",
            "print(b1)           # Book(title='Think Python', author='Allen Downey', year=2024, pages=0)\n",
            "print(b2)           # Book(title='Think Python', author='Allen Downey', year=2024, pages=350)\n",
            "print(b1 == b3)     # True\n",
            "print(b1 == b2)     # False  (pages differ)\n",
        ]),
    ]

    nb['cells'] = cells[:idx] + new + cells[idx:]
    save(nb, path)

# ──────────────────────────────────────────────────────────────────
# 5. CH13 / 1301: Add functools section before ## Summary
# ──────────────────────────────────────────────────────────────────
def update_1301():
    path = 'chapters/13-functional/1301-func-prog.ipynb'
    nb = load(path)
    cells = nb['cells']
    idx = find_idx(cells, '## Summary')
    assert idx is not None

    new = [
        md([
            "## The `functools` Module\n",
            "\n",
            "The `functools` module provides higher-order functions that operate on or\n",
            "return other functions. Three particularly useful tools are `reduce`,\n",
            "`partial`, and `lru_cache`.\n",
        ]),
        md([
            "### `functools.reduce()`\n",
            "\n",
            "`reduce(function, iterable)` applies a two-argument function cumulatively\n",
            "to the items of an iterable, reducing it to a single value.\n",
            "Think of it as a fold: it combines elements left to right.\n",
        ]),
        code([
            "from functools import reduce\n",
            "\n",
            "# Sum all numbers (same as built-in sum, shown for illustration)\n",
            "total = reduce(lambda acc, x: acc + x, [1, 2, 3, 4, 5])\n",
            "print(total)    # 15\n",
            "\n",
            "# Product of all numbers\n",
            "product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4, 5])\n",
            "print(product)  # 120\n",
            "\n",
            "# Flatten a list of lists\n",
            "nested = [[1, 2], [3, 4], [5, 6]]\n",
            "flat = reduce(lambda acc, x: acc + x, nested)\n",
            "print(flat)     # [1, 2, 3, 4, 5, 6]\n",
        ]),
        md([
            "### `functools.partial()`\n",
            "\n",
            "`partial(function, *args, **kwargs)` returns a new function with some\n",
            "arguments pre-filled. This is called **partial application** — useful for\n",
            "creating specialized versions of general-purpose functions.\n",
        ]),
        code([
            "from functools import partial\n",
            "\n",
            "def power(base, exponent):\n",
            "    return base ** exponent\n",
            "\n",
            "square = partial(power, exponent=2)\n",
            "cube   = partial(power, exponent=3)\n",
            "\n",
            "print(square(4))   # 16\n",
            "print(cube(3))     # 27\n",
            "\n",
            "# Practical: pre-configure print with a separator\n",
            "import functools\n",
            "header = functools.partial(print, sep=' | ')\n",
            "header('Name', 'Score', 'Grade')  # Name | Score | Grade\n",
        ]),
        md([
            "### `functools.lru_cache()`\n",
            "\n",
            "`@lru_cache` memoizes a function's results: the first time a function is\n",
            "called with given arguments, the result is stored. On subsequent calls with\n",
            "the same arguments, the cached result is returned immediately — no\n",
            "recomputation needed.\n",
            "\n",
            "LRU stands for **Least Recently Used**: when the cache is full, the least\n",
            "recently accessed entry is evicted.\n",
        ]),
        code([
            "from functools import lru_cache\n",
            "import time\n",
            "\n",
            "@lru_cache(maxsize=None)  # unlimited cache\n",
            "def fib(n):\n",
            "    if n <= 1:\n",
            "        return n\n",
            "    return fib(n - 1) + fib(n - 2)\n",
            "\n",
            "# Without cache, fib(40) would take seconds (2^40 calls)\n",
            "start = time.perf_counter()\n",
            "print(fib(50))   # 12586269025\n",
            "elapsed = time.perf_counter() - start\n",
            "print(f'Computed in {elapsed:.6f}s')  # microseconds with cache\n",
            "\n",
            "# Inspect cache statistics\n",
            "print(fib.cache_info())  # CacheInfo(hits=..., misses=51, maxsize=None, currsize=51)\n",
        ]),
        code([
            "### Exercise: functools\n",
            "#   1. Use reduce() to find the maximum value in [3, 1, 4, 1, 5, 9, 2, 6].\n",
            "#      (Hint: lambda acc, x: acc if acc > x else x)\n",
            "#   2. Use partial() to create `add10` — a function that adds 10 to any number.\n",
            "#      Test: add10(5) → 15, add10(-3) → 7.\n",
            "#   3. Decorate `count_ways(n)` below with @lru_cache to speed it up.\n",
            "#      count_ways(n) returns how many ways to climb n stairs (1 or 2 at a time).\n",
            "from functools import reduce, partial, lru_cache\n",
            "\n",
            "def count_ways(n):\n",
            "    if n <= 1: return 1\n",
            "    return count_ways(n - 1) + count_ways(n - 2)\n",
            "\n",
            "### Your code starts here.\n",
            "\n",
            "\n",
            "\n",
            "### Your code ends here.\n",
        ]),
        code([
            "### Solution\n",
            "from functools import reduce, partial, lru_cache\n",
            "\n",
            "# 1. reduce to find max\n",
            "nums = [3, 1, 4, 1, 5, 9, 2, 6]\n",
            "maximum = reduce(lambda acc, x: acc if acc > x else x, nums)\n",
            "print(maximum)    # 9\n",
            "\n",
            "# 2. partial to create add10\n",
            "add = lambda a, b: a + b\n",
            "add10 = partial(add, 10)\n",
            "print(add10(5))   # 15\n",
            "print(add10(-3))  # 7\n",
            "\n",
            "# 3. lru_cache to speed up count_ways\n",
            "@lru_cache(maxsize=None)\n",
            "def count_ways(n):\n",
            "    if n <= 1: return 1\n",
            "    return count_ways(n - 1) + count_ways(n - 2)\n",
            "\n",
            "print(count_ways(30))  # 1346269 (fast with cache)\n",
        ]),
    ]

    nb['cells'] = cells[:idx] + new + cells[idx:]
    save(nb, path)

# ──────────────────────────────────────────────────────────────────
# 6. CH14 / 1402: Add yield from + itertools before ## Summary
# ──────────────────────────────────────────────────────────────────
def update_1402():
    path = 'chapters/14-iter-gen/1402-generators.ipynb'
    nb = load(path)
    cells = nb['cells']
    idx = find_idx(cells, '## Summary')
    assert idx is not None

    new = [
        md([
            "## `yield from`\n",
            "\n",
            "`yield from` delegates yielding to another iterable (including another generator).\n",
            "It is essentially a shorthand for `for item in sub: yield item`, but also\n",
            "properly forwards `send()` and `throw()` calls to the sub-generator.\n",
        ]),
        code([
            "def flatten(nested):\n",
            "    \"\"\"Recursively flatten a nested list structure.\"\"\"\n",
            "    for item in nested:\n",
            "        if isinstance(item, list):\n",
            "            yield from flatten(item)  # delegate to recursive call\n",
            "        else:\n",
            "            yield item\n",
            "\n",
            "data = [1, [2, 3], [4, [5, 6]], 7]\n",
            "print(list(flatten(data)))   # [1, 2, 3, 4, 5, 6, 7]\n",
        ]),
        code([
            "# yield from with multiple sub-generators\n",
            "def combined(*iterables):\n",
            "    for it in iterables:\n",
            "        yield from it\n",
            "\n",
            "result = list(combined([1, 2], 'ab', range(3)))\n",
            "print(result)   # [1, 2, 'a', 'b', 0, 1, 2]\n",
        ]),
        md([
            "## More `itertools`\n",
            "\n",
            "The `itertools` module provides iterator building-blocks. Beyond `islice` and\n",
            "`chain` (already covered), three more are especially useful in data processing.\n",
            "\n",
            "| Function | Description | Example |\n",
            "|---|---|---|\n",
            "| `count(start, step)` | Infinite counter | `count(1, 2)` → 1, 3, 5, … |\n",
            "| `cycle(iterable)` | Repeats iterable endlessly | `cycle('AB')` → A, B, A, B, … |\n",
            "| `combinations(it, r)` | All r-length combos (no repeat) | `combinations('ABC', 2)` → AB AC BC |\n",
            "| `permutations(it, r)` | All ordered r-length arrangements | `permutations('AB', 2)` → AB BA |\n",
        ]),
        code([
            "import itertools\n",
            "\n",
            "# count: infinite arithmetic sequence\n",
            "evens = itertools.islice(itertools.count(0, 2), 5)\n",
            "print('First 5 even numbers:', list(evens))  # [0, 2, 4, 6, 8]\n",
            "\n",
            "# cycle: round-robin scheduling\n",
            "servers = ['A', 'B', 'C']\n",
            "requests = list(itertools.islice(itertools.cycle(servers), 7))\n",
            "print('Request routing:', requests)   # ['A', 'B', 'C', 'A', 'B', 'C', 'A']\n",
        ]),
        code([
            "import itertools\n",
            "\n",
            "# combinations: choose without caring about order\n",
            "teams = list(itertools.combinations(['Alice', 'Bob', 'Carol'], 2))\n",
            "print('Possible pairs:', teams)\n",
            "# [('Alice', 'Bob'), ('Alice', 'Carol'), ('Bob', 'Carol')]\n",
            "\n",
            "# permutations: order matters (e.g. race positions)\n",
            "podium = list(itertools.permutations(['Gold', 'Silver', 'Bronze'], 2))\n",
            "print(f'Top-2 orderings: {len(podium)} total')\n",
            "print(podium[:3])   # first 3 arrangements\n",
        ]),
        code([
            "### Exercise: itertools\n",
            "#   1. Use itertools.count() and islice() to generate the first 8\n",
            "#      multiples of 7 (7, 14, 21, ..., 56).\n",
            "#   2. Use itertools.cycle() and islice() to simulate dealing cards\n",
            "#      to 4 players, 3 cards each (total 12 cards from an infinite deck).\n",
            "#      Players are 'North', 'East', 'South', 'West'.\n",
            "#   3. Use itertools.combinations() to find all 3-letter combinations\n",
            "#      from 'ABCDE' and count them.\n",
            "import itertools\n",
            "\n",
            "### Your code starts here.\n",
            "\n",
            "\n",
            "\n",
            "### Your code ends here.\n",
        ]),
        code([
            "### Solution\n",
            "import itertools\n",
            "\n",
            "# 1. First 8 multiples of 7\n",
            "multiples = list(itertools.islice(itertools.count(7, 7), 8))\n",
            "print(multiples)   # [7, 14, 21, 28, 35, 42, 49, 56]\n",
            "\n",
            "# 2. Deal 3 cards each to 4 players\n",
            "players = itertools.cycle(['North', 'East', 'South', 'West'])\n",
            "cards   = range(1, 13)  # card values 1-12\n",
            "deal    = list(zip(itertools.islice(players, 12), cards))\n",
            "print(deal)\n",
            "# [('North', 1), ('East', 2), ('South', 3), ('West', 4),\n",
            "#  ('North', 5), ('East', 6), ...]\n",
            "\n",
            "# 3. Count 3-letter combinations from 'ABCDE'\n",
            "combos = list(itertools.combinations('ABCDE', 3))\n",
            "print(f'{len(combos)} combinations')   # 10\n",
            "print(combos)\n",
        ]),
    ]

    nb['cells'] = cells[:idx] + new + cells[idx:]
    save(nb, path)

# ──────────────────────────────────────────────────────────────────
# 7. CH15 / 1501: Add POST, headers, nested JSON before ## Summary
# ──────────────────────────────────────────────────────────────────
def update_1501():
    path = 'chapters/15-apis/1501-apis.ipynb'
    nb = load(path)
    cells = nb['cells']
    idx = find_idx(cells, '## Summary')
    assert idx is not None

    new = [
        md([
            "## POST Requests\n",
            "\n",
            "A **GET** request retrieves data from a server. A **POST** request *sends*\n",
            "data to a server — typically to create a resource or submit a form. POST\n",
            "requests carry a **body** (payload), usually formatted as JSON.\n",
        ]),
        code([
            "import requests\n",
            "\n",
            "# httpbin.org/post echoes back whatever you send — great for testing\n",
            "url = 'https://httpbin.org/post'\n",
            "\n",
            "payload = {\n",
            "    'username': 'ada',\n",
            "    'score': 98,\n",
            "    'passed': True\n",
            "}\n",
            "\n",
            "response = requests.post(url, json=payload, timeout=10)\n",
            "response.raise_for_status()\n",
            "\n",
            "data = response.json()\n",
            "print('Status:', response.status_code)   # 200\n",
            "print('JSON sent:', data['json'])         # echoes our payload\n",
        ]),
        md([
            "## Headers and API Keys\n",
            "\n",
            "Many APIs require authentication. Common patterns:\n",
            "\n",
            "| Pattern | Example |\n",
            "|---|---|\n",
            "| Query parameter | `?api_key=abc123` |\n",
            "| Bearer token header | `Authorization: Bearer <token>` |\n",
            "| Custom header | `X-API-Key: abc123` |\n",
            "\n",
            "Pass headers as a dictionary to the `headers=` argument.\n",
            "**Never hard-code real API keys in code**; use environment variables instead.\n",
        ]),
        code([
            "import requests, os\n",
            "\n",
            "# Pattern 1: Bearer token (e.g., GitHub, OpenAI)\n",
            "# token = os.environ['GITHUB_TOKEN']  # load from environment in real code\n",
            "token = 'demo_token_placeholder'\n",
            "\n",
            "headers = {\n",
            "    'Authorization': f'Bearer {token}',\n",
            "    'Accept': 'application/json',\n",
            "}\n",
            "\n",
            "# httpbin.org/headers echoes received headers\n",
            "r = requests.get('https://httpbin.org/headers', headers=headers, timeout=10)\n",
            "print('Headers echoed back:')\n",
            "for k, v in r.json()['headers'].items():\n",
            "    print(f'  {k}: {v}')\n",
        ]),
        md([
            "## Navigating Nested JSON\n",
            "\n",
            "Real-world API responses are often deeply nested. You can chain `[]`\n",
            "subscripts and use `.get()` to safely navigate the structure.\n",
        ]),
        code([
            "import requests\n",
            "\n",
            "# Open-Meteo: free weather API (no key required)\n",
            "url = 'https://api.open-meteo.com/v1/forecast'\n",
            "params = {\n",
            "    'latitude': 37.77,\n",
            "    'longitude': -122.42,\n",
            "    'current_weather': True,\n",
            "}\n",
            "\n",
            "r = requests.get(url, params=params, timeout=10)\n",
            "r.raise_for_status()\n",
            "data = r.json()\n",
            "\n",
            "# Navigate nested dict\n",
            "weather = data['current_weather']\n",
            "print(f\"Temperature: {weather['temperature']} °C\")\n",
            "print(f\"Wind speed:  {weather['windspeed']} km/h\")\n",
            "print(f\"Weather code: {weather['weathercode']}\")\n",
        ]),
        code([
            "# Safe navigation with .get() for optional keys\n",
            "sample = {\n",
            "    'user': {\n",
            "        'profile': {\n",
            "            'name': 'Alice',\n",
            "            'email': 'alice@example.com'\n",
            "        }\n",
            "    }\n",
            "}\n",
            "\n",
            "# Chained .get() returns None instead of raising KeyError\n",
            "name  = sample.get('user', {}).get('profile', {}).get('name', 'Unknown')\n",
            "phone = sample.get('user', {}).get('profile', {}).get('phone', 'Not provided')\n",
            "\n",
            "print(name)   # Alice\n",
            "print(phone)  # Not provided\n",
        ]),
        code([
            "### Exercise: Working with APIs\n",
            "#   Use the Open-Meteo API (no key needed) to answer:\n",
            "#   1. Make a GET request with latitude=40.71 (New York) and longitude=-74.01.\n",
            "#      Include current_weather=True in params.\n",
            "#   2. Extract and print the temperature and wind speed.\n",
            "#   3. Make a POST request to https://httpbin.org/post with a JSON body\n",
            "#      containing {'city': 'New York', 'temp': <the temperature you got>}.\n",
            "#      Print the 'json' field from the response to confirm what was sent.\n",
            "import requests\n",
            "\n",
            "### Your code starts here.\n",
            "\n",
            "\n",
            "\n",
            "### Your code ends here.\n",
        ]),
        code([
            "### Solution\n",
            "import requests\n",
            "\n",
            "# 1 & 2: GET weather for New York\n",
            "r = requests.get(\n",
            "    'https://api.open-meteo.com/v1/forecast',\n",
            "    params={'latitude': 40.71, 'longitude': -74.01, 'current_weather': True},\n",
            "    timeout=10\n",
            ")\n",
            "r.raise_for_status()\n",
            "weather = r.json()['current_weather']\n",
            "temp = weather['temperature']\n",
            "wind = weather['windspeed']\n",
            "print(f'New York — Temp: {temp} °C, Wind: {wind} km/h')\n",
            "\n",
            "# 3: POST with the temperature\n",
            "resp = requests.post(\n",
            "    'https://httpbin.org/post',\n",
            "    json={'city': 'New York', 'temp': temp},\n",
            "    timeout=10\n",
            ")\n",
            "resp.raise_for_status()\n",
            "print('Sent:', resp.json()['json'])\n",
        ]),
    ]

    nb['cells'] = cells[:idx] + new + cells[idx:]
    save(nb, path)


if __name__ == '__main__':
    os.chdir('/Users/tychen/workspace/py')
    update_1101()
    update_1102()
    update_1201()
    update_1202()
    update_1301()
    update_1402()
    update_1501()
    print('All notebooks updated successfully.')
