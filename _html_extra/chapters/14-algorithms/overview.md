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

# Chapter 15

Algorithms

*15.0 Intro · 15.1 Algorithm Concepts · 15.2 Searching · 15.3 Sorting*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 15.1 Algorithm Concepts

Big O · time & space complexity · benchmarking

---

## Big O Notation

How an algorithm's runtime scales with input size *n*:

| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | Dict lookup, list append |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | List scan, linear search |
| O(n log n) | Linearithmic | Merge sort, Timsort |
| O(n²) | Quadratic | Bubble sort, nested loops |

<div class="callout rule">

Always prefer O(1) and O(log n) over O(n) and O(n²) when working with large data.

</div>

---

## Benchmarking

<div class="cols">
<div>

```python
import time

# time.perf_counter — wall clock, high precision
start = time.perf_counter()
result = sum(range(1_000_000))
elapsed = time.perf_counter() - start
print(f"{elapsed:.6f}s")
```

```python
import timeit

# timeit — eliminates startup noise, repeats automatically
t = timeit.timeit(
    "sum(range(1_000_000))",
    number=10
)
print(f"avg: {t/10:.6f}s")
```

</div>
<div>

### Best / worst / average case

| Case | Meaning |
|---|---|
| Best | Most favourable input |
| Worst | Most unfavourable input |
| Average | Expected over all inputs |

Big O usually refers to the **worst case**.

<div class="callout">

Benchmark with realistic data sizes — microbenchmarks on tiny inputs often mislead.

</div>

</div>
</div>

---

<!-- _class: section -->

## 15.2 Searching

Linear · binary · `bisect` · hash-based

---

## Linear & Binary Search

<div class="cols">
<div>

### Linear search — O(n)

```python
def linear_search(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1
```

Works on any list. Scans every element in the worst case.

</div>
<div>

### Binary search — O(log n)

**Requires a sorted list.**

```python
def binary_search(lst, target):
    lo, hi = 0, len(lst) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

</div>
</div>

---

## `bisect` Module & Hash-Based Lookup

<div class="cols">
<div>

### `bisect` — maintain sorted order

```python
import bisect

data = [1, 3, 5, 7, 9]

# Find insertion point
i = bisect.bisect_left(data, 6)   # 3

# Insert maintaining sort order
bisect.insort(data, 6)
print(data)   # [1, 3, 5, 6, 7, 9]

# Lookup: is x in the sorted list?
def sorted_contains(lst, x):
    i = bisect.bisect_left(lst, x)
    return i < len(lst) and lst[i] == x
```

</div>
<div>

### Hash-based — O(1) average

```python
# Preprocess once
lookup = set(data)     # or dict for key→value

# O(1) membership check
print(6 in lookup)     # True

# Summary
```

| Method | Time | Requirement |
|---|---|---|
| Linear | O(n) | None |
| Binary | O(log n) | Sorted |
| bisect | O(log n) | Sorted |
| Hash | O(1) avg | Hashable elements |

</div>
</div>

---

<!-- _class: section -->

## 15.3 Sorting

Built-in · insertion · bubble · merge · quicksort

---

## Built-in Sort & Simple Algorithms

<div class="cols">
<div>

### Python's Timsort — O(n log n)

```python
lst = [3, 1, 4, 1, 5, 9, 2, 6]
lst.sort()                        # in-place
s = sorted(lst)                   # new list
s = sorted(lst, reverse=True)     # descending
s = sorted(lst, key=abs)          # custom key
```

### Insertion sort — O(n²) worst

```python
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
```

</div>
<div>

### Merge sort — O(n log n)

```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left  = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]
```

</div>
</div>

---

## Sorting Algorithm Comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| Timsort (Python) | O(n) | O(n log n) | O(n log n) | O(n) | ✓ |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✓ |
| Quick sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ✗ |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | ✓ |
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | ✓ |

<div class="callout">

Use Python's built-in `sorted()` / `.sort()` in practice — Timsort is exceptionally well-optimized.

</div>

---

## Chapter 15 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| Big O | O(1) < O(log n) < O(n) < O(n log n) < O(n²) |
| Benchmark | `time.perf_counter()`, `timeit.timeit()` |
| Linear search | O(n) — works on any list |
| Binary search | O(log n) — requires sorted list |
| bisect | `bisect_left`, `bisect_right`, `insort` — O(log n) |
| Hash lookup | `x in set_or_dict` — O(1) average |
| Built-in sort | `lst.sort()` / `sorted(lst)` — Timsort O(n log n) |
| Stable sort | Equal elements keep original order |

---

<!-- _class: title -->

# End of Chapter 15

*Congratulations — you've reached the end of ThinkPy!*

*algorithms · data structures · Python programming*
