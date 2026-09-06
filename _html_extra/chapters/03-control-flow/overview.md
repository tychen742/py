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
  pre code { color: inherit; background: none; border: none; display: block; box-sizing: border-box; padding: 12px 14px; white-space: pre; }
  table { font-size: 0.68em; border-collapse: collapse; width: 100%; }
  th { background: #2a6b37; color: white; padding: 5px 8px; text-align: left; }
  td { padding: 5px 8px; border-bottom: 1px solid #e0e0e0; }
  tr:nth-child(even) td { background: #f7faf7; }
  section::after { color: #aaa; font-size: 0.7em; }
---

<!-- _class: title -->

# Chapter 3

Control Flow

*3.0 Intro · 3.1 Conditionals · 3.2 Iteration*

*← → or Space to navigate · F for fullscreen*

---

## Chapter Route

| Notebook | What it covers |
|---|---|
| `0300-control-flow` | Why programs need choices and repetition |
| `0301-conditionals` | `if`, `else`, `elif`, nesting, and expressions |
| `0302-iteration` | Iterables, `for`, `while`, loop control, accumulation |

<div class="callout">

Control flow changes the order in which statements run. Chapter 3 adds two core tools: choose a path with conditionals, then repeat work with loops.

</div>

---

<!-- _class: section -->

## 3.1 Conditionals

integer division and modulus · if / elif / else · nested conditionals · conditional expressions

---

## Integer Division and Modulus

Use `//` for whole-number division and `%` for the remainder.

<div class="cols">
<div>

```python
minutes = 105

hours = minutes // 60
remainder = minutes % 60

print(hours)      # 1
print(remainder)  # 45
```

</div>
<div>

```python
seconds = 12345

hours = seconds // 3600
seconds = seconds % 3600

minutes = seconds // 60
seconds = seconds % 60

print(hours, minutes, seconds)
```

</div>
</div>

<div class="callout">

This pattern is useful whenever a large unit must be split into smaller units: seconds to minutes, cents to dollars, rows to pages.

</div>

---

## Conditional Execution

An `if` statement runs a block only when its condition is truthy.

<div class="cols">
<div>

```python
x = 5

if x > 0:
    print("x is positive")
```

```python
score = 85

if score >= 60:
    print("passing")
```

</div>
<div>

- The condition comes after `if`.
- The colon starts an indented block.
- Indentation defines which statements belong to the branch.
- If the condition is false, Python skips the block.

<div class="callout warn">

Python uses indentation as syntax. Keep each block aligned consistently.

</div>

</div>
</div>

---

## `if` / `elif` / `else`

<div class="cols">
<div>

```python
score = 85

if score > 100 or score < 0:
    grade = "invalid score"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")  # Grade: B
```

</div>
<div>

- Conditions are evaluated top-to-bottom.
- Only the **first matching** branch runs.
- `else` is optional; catches everything remaining.
- Put special cases before broader cases.

<div class="callout">

`0`, `""`, `[]`, `None` are **falsy**. Everything else is truthy. Usually you do not need `== True`.

</div>

</div>
</div>

---

## Nested Conditionals

<div class="cols">
<div>

```python
username = "ada"
password = "python"

if username == "ada":
    if password == "python":
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")
```

</div>
<div>

```python
if username == "ada" and password == "python":
    print("Access granted")
```

```python
x = 5

if 0 < x < 10:
    print("single digit")
```

<div class="callout">

Nested conditionals are useful when one decision depends on another. Combined conditions are often clearer for simple tests.

</div>

</div>
</div>

---

## Placeholder Branches with `pass`

Use `pass` when Python requires a block but you have not written the logic yet.

<div class="cols">
<div>

```python
score = 85

if score >= 90:
    pass
elif score >= 80:
    print("B")
else:
    pass
```

</div>
<div>

- `pass` does nothing at runtime.
- It is useful for draft code and intentional empty branches.
- Replace it with real logic before the program is complete.

<div class="callout warn">

Do not confuse `pass` with `continue`. `pass` does nothing; `continue` jumps to the next loop iteration.

</div>

</div>
</div>

---

## Conditional Expressions

A concise one-liner for choosing between two values.

```python
age = 19
status = "adult" if age >= 18 else "minor"

x = -3
y = math.log(x) if x > 0 else float("nan")
```

<div class="callout rule">

Read as: "give me A **if** condition is true, **else** B." Use when both branches are simple expressions.

</div>

---

<!-- _class: section -->

## 3.2 Iteration

iterables · for loops · range · while loops · loop control · accumulator pattern

---

## Iterators and Iterables

An **iterable** can produce values one at a time. An **iterator** is the object doing that work.

<div class="cols">
<div>

```python
fruit = ("apple", "banana", "cherry")

itr = iter(fruit)

print(next(itr))  # apple
print(next(itr))  # banana
print(next(itr))  # cherry
```

</div>
<div>

- Lists, tuples, strings, ranges, and dictionaries are iterable.
- `iter()` asks for an iterator.
- `next()` gets the next value.
- A `for` loop handles this protocol for you.

<div class="callout">

Most Python loops are loops over iterables, not loops over raw numeric positions.

</div>

</div>
</div>

---

## Looping Through Iterables

<div class="cols">
<div>

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

```python
nums = [2, 4, 6]

for n in nums:
    print(n ** 2)
```

</div>
<div>

```python
word = "Python"

for letter in word:
    print(letter)
```

<div class="callout">

Use a direct `for item in collection:` loop when the item is what you need.

</div>

</div>
</div>

---

## `range()` and Index-Based Loops

<div class="cols">
<div>

```python
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(10, 0, -2):
    print(i)
```

</div>
<div>

```python
numbers = [10, 20, 30]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)  # [20, 40, 60]
```

<div class="callout rule">

Prefer direct iteration unless you need the index to update or compare positions.

</div>

</div>
</div>

---

## Nested Loops

A nested loop runs the inner loop completely for each step of the outer loop.

<div class="cols">
<div>

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end=" ")
    print()
```

</div>
<div>

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

for row in matrix:
    for value in row:
        print(value)
```

<div class="callout">

Nested loops are common with tables, matrices, grids, and paired comparisons.

</div>

</div>
</div>

---

## Advanced `for` Loop Patterns

<div class="cols">
<div>

```python
fruits = ["apple", "banana"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
```

```python
names = ["Ada", "Linus"]
ages = [36, 54]

for name, age in zip(names, ages):
    print(name, age)
```

</div>
<div>

```python
scores = {"Ada": 92, "Linus": 85}

for name, score in scores.items():
    print(name, score)

for name in scores.keys():
    print(name)

for score in scores.values():
    print(score)
```

</div>
</div>

---

## `while` Loops

Use `while` when repetition depends on a condition rather than a known collection.

<div class="cols">
<div>

```python
times = 0

while times < 3:
    print("Hello!")
    times += 1
```

```python
n = 1

while n < 100:
    n *= 2

print(n)  # 128
```

</div>
<div>

```python
total = 0
value = int(input("Number? "))

while value != -1:
    total += value
    value = int(input("Number? "))

print(total)
```

<div class="callout warn">

Make sure something inside the loop can eventually make the condition false.

</div>

</div>
</div>

---

## `while True` and `break`

An infinite loop can be useful when the stopping point is easiest to test inside the loop.

```python
total = 0

while True:
    value = int(input("Number? "))

    if value == -1:
        break

    total += value

print(total)
```

<div class="callout">

`break` exits the nearest loop immediately. Put the stopping test where the decision is clearest.

</div>

---

## Loop Control Statements

<div class="cols">
<div>

```python
for n in range(10):
    if n == 5:
        break
    print(n)
```

```python
for n in range(10):
    if n % 2 == 0:
        continue
    print(n)
```

</div>
<div>

```python
for n in range(3):
    pass
```

```python
for n in [2, 4, 6]:
    if n % 2 == 1:
        print("odd found")
        break
else:
    print("no odd numbers")
```

</div>
</div>

---

## Accumulator Pattern

Initialize a result before the loop, update it inside the loop, then use it after the loop.

<div class="cols">
<div>

```python
rainfall = [0.2, 0.0, 1.3, 0.4]

total = 0
for amount in rainfall:
    total += amount

print(total)
```

</div>
<div>

```python
wet_days = 0

for amount in rainfall:
    if amount > 0:
        wet_days += 1

print(wet_days)
```

<div class="callout rule">

Common accumulators include totals, counts, minimums, maximums, and collected lists.

</div>

</div>
</div>

---

## Chapter 3 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Integer division | `a // b` gives the whole-number quotient |
| Modulus | `a % b` gives the remainder |
| if / elif / else | First matching branch wins |
| Chained comparison | `0 < x < 10` |
| Conditional expression | `A if condition else B` |
| Iterable | Object that can produce values one at a time |
| for loop | `for item in iterable:` |
| range | `range(start, stop, step)` |
| enumerate | `for i, v in enumerate(seq):` |
| zip | Loop over multiple iterables together |
| while loop | Runs while condition is truthy |
| break / continue | Exit loop / skip to the next iteration |
| pass | Placeholder statement that does nothing |
| loop else | Runs only if the loop did not `break` |
| Accumulator | Initialize before loop; update inside |

---

<!-- _class: title -->

# End of Chapter 3

*Next: Chapter 4 — Functions*

*defining functions · parameters · return values · recursion*
