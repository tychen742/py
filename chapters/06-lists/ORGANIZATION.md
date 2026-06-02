# Chapter 06 Organization (Lists)

This chapter is currently split into:

- `0600-intro-lists.ipynb`
- `0601-creating-lists.ipynb`
- `0602-accessing-lists.ipynb`
- `0603-list-operations.ipynb`
- `0604-aliasing-copying.ipynb`
- `0605-advanced-lists.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `0600-intro-lists.ipynb` — chapter overview and learning objectives
2. `0601-creating-lists.ipynb` — list creation, constructors, comprehensions, lists and strings
3. `0602-accessing-lists.ipynb` — indexing, slicing, and element access
4. `0603-list-operations.ipynb` — list operators, methods, iteration, and common operations
5. `0604-aliasing-copying.ipynb` — aliasing, shallow copies, and mutation behavior
6. `0605-advanced-lists.ipynb` — nested lists and advanced list concepts

## Source of Truth

Use `chapters/06-lists/*` as the only Chapter 06 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 06 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.

## Topic Coverage Reference

### Introduction

- What lists are (ordered, mutable collections)
- Difference between lists vs. tuples vs. sets
- Creating a list (literals `[]`, `list()` constructor, list assignment)

### Basic Operators

- Indexing (`mylist[0]`, `mylist[-1]`)
- Slicing (`mylist[1:4]`, `mylist[::-1]`)
- Length with `len()`
- Iterating through lists (`for` loops, `while` loops)

### Adding & Removing Elements

- `append()`, `insert()`, `extend()`
- `remove()`, `pop()`, `del`
- Clearing a list (`clear()`)

### Searching & Checking

- Membership (`in`, `not in`)
- `index()`, `count()`

### Updating Elements

- Assigning by index (`mylist[2] = "newvalue"`)
- Assigning slices (`mylist[1:3] = [7, 8]`)

### Useful List Methods

- Sorting: `sort()` vs. `sorted()`
- Reversing: `reverse()`
- Copying: `copy()`, slicing (`[:]`), `list()`

### Advanced Usage

- Nested lists (2D lists, accessing inner lists)
- List comprehensions (with conditions)
- Combining lists (`+`, `*` operators)
- `zip()` with lists
- Built-in functions: `min()`, `max()`, `sum()`

### Common Pitfalls

- Mutable vs immutable behavior
- Copy vs reference (aliasing)
- Lists of lists (shallow vs deep copies)

### Practice Ideas

- Create a shopping list program
- Reverse a list manually (without `reverse()`)
- Find the largest number in a list
- Flatten a nested list
- Build a list comprehension that squares only even numbers
