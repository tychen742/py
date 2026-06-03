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

# Chapter 3

Control Flow

*3.0 Intro · 3.1 Conditionals · 3.2 Iteration*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 3.1 Conditionals

if / elif / else · nested conditionals · conditional expressions

---

## `if` / `elif` / `else`

<div class="cols">
<div>

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")   # Grade: B
```

</div>
<div>

- Conditions are evaluated top-to-bottom.
- Only the **first matching** branch runs.
- `else` is optional; catches everything remaining.
- Any expression that is truthy/falsy works as a condition.

<div class="callout">

`0`, `""`, `[]`, `None` are **falsy**. Everything else is truthy — no need for `== True`.

</div>

</div>
</div>

---

## Nested Conditionals & Logical Operators

<div class="cols">
<div>

### Nested (avoid when possible)

```python
if x > 0:
    if x < 10:
        print("single digit")
```

### Better: logical operators

```python
if 0 < x < 10:       # chained comparison
    print("single digit")

if x > 0 and x < 10: # equivalent
    print("single digit")
```

</div>
<div>

### Common patterns

```python
# Guard clause — exit early
def process(data):
    if not data:
        return []
    # ... rest of function

# Membership test
if color in {"red", "green", "blue"}:
    print("primary")
```

</div>
</div>

---

## Conditional Expressions (Ternary)

A concise one-liner for choosing between two values.

```python
# if/else block
if x > 0:
    label = "positive"
else:
    label = "non-positive"

# Equivalent conditional expression
label = "positive" if x > 0 else "non-positive"
```

<div class="callout rule">

Read as: "give me A **if** condition is true, **else** B." Use when both branches are simple expressions.

</div>

---

<!-- _class: section -->

## 3.2 Iteration

for loops · while loops · break / continue · accumulator pattern

---

## `for` Loops

<div class="cols">
<div>

```python
# Iterate over a sequence
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# Iterate with index
for i, fruit in enumerate(["apple", "banana"]):
    print(i, fruit)

# Range
for n in range(1, 6):
    print(n)   # 1 2 3 4 5
```

</div>
<div>

```python
# Iterate over dict
scores = {"alice": 92, "bob": 85}
for name, score in scores.items():
    print(f"{name}: {score}")

# List comprehension (Pythonic)
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
```

</div>
</div>

---

## `while` Loops & Loop Control

<div class="cols">
<div>

```python
# while loop
n = 1
while n < 100:
    n *= 2
print(n)   # 128

# break — exit the loop early
for i in range(10):
    if i == 5:
        break
    print(i)   # 0 1 2 3 4

# continue — skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)   # 1 3 5 7 9
```

</div>
<div>

### Accumulator pattern

```python
# Sum (accumulate a number)
total = 0
for score in scores:
    total += score

# Collect (accumulate a list)
passing = []
for score in scores:
    if score >= 60:
        passing.append(score)

# Count (accumulate a tally)
count = 0
for score in scores:
    if score >= 90:
        count += 1
```

</div>
</div>

---

## Chapter 3 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| if / elif / else | First matching branch wins |
| Chained comparison | `0 < x < 10` |
| Conditional expression | `A if condition else B` |
| for loop | `for item in iterable:` |
| range | `range(start, stop, step)` |
| enumerate | `for i, v in enumerate(seq):` |
| while loop | Runs while condition is truthy |
| break / continue | Exit loop / skip to next iteration |
| Accumulator | Initialize before loop; update inside |

---

<!-- _class: title -->

# End of Chapter 3

*Next: Chapter 4 — Functions*

*defining functions · parameters · return values · recursion*
