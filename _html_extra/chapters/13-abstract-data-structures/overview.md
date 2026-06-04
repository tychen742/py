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

# Chapter 14

Abstract Data Structures

*14.0 Intro · 14.1 ADT Basics · 14.2 Stacks & Queues · 14.3 Trees & Graphs*

*← → or Space to navigate · F for fullscreen*

---

<!-- _class: section -->

## 14.1 ADT Basics

Interface vs. implementation · the ADT contract

---

## What is an Abstract Data Type?

<div class="cols">
<div>

An **ADT** defines **what** operations a data structure supports — not **how** it is implemented.

| Layer | Concern |
|---|---|
| **Interface** | Operations and their behavior |
| **Implementation** | How operations are carried out |

The interface is the **contract**. Users of an ADT only need to know the interface.

</div>
<div>

```python
# Interface — what a Stack does:
# push(item)     add to top
# pop()          remove from top
# peek()         view top without removing
# is_empty()     True if no items

# Implementation A — using a Python list
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0
```

</div>
</div>

---

<!-- _class: section -->

## 14.2 Stacks & Queues

LIFO · FIFO · `collections.deque`

---

## Stack — LIFO

<div class="cols">
<div>

**Last In, First Out** — like a stack of plates.

**Use cases:**
- Function call stack
- Undo/redo history
- Balanced parentheses checking
- Depth-first search

```python
stack = []
stack.append("a")   # push
stack.append("b")
stack.append("c")
print(stack.pop())  # c  (last in, first out)
print(stack.pop())  # b
```

</div>
<div>

### Balanced parentheses

```python
def is_balanced(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0

print(is_balanced("({[]})"))   # True
print(is_balanced("({[})"))    # False
```

</div>
</div>

---

## Queue — FIFO

<div class="cols">
<div>

**First In, First Out** — like a line at a checkout.

**Use cases:**
- Task scheduling
- BFS graph traversal
- Print queues
- Message queues

</div>
<div>

```python
from collections import deque

queue = deque()
queue.append("task1")     # enqueue
queue.append("task2")
queue.append("task3")

print(queue.popleft())    # task1  (FIFO)
print(queue.popleft())    # task2

# deque is O(1) at both ends
# list.pop(0) is O(n) — avoid for queues
```

</div>
</div>

---

<!-- _class: section -->

## 14.3 Trees & Graphs

Terminology · traversals · DFS & BFS

---

## Trees

<div class="cols">
<div>

**Key terms:**
- **Root** — top node (no parent)
- **Leaf** — node with no children
- **Height** — longest root-to-leaf path
- **BST** — Binary Search Tree: left < node < right

**Traversals:**
- **Pre-order**: root → left → right
- **In-order**: left → root → right (sorted for BST)
- **Post-order**: left → right → root

</div>
<div>

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)

# Build a small BST:  4
#                    / \
#                   2   6
root = Node(4)
root.left = Node(2)
root.right = Node(6)
inorder(root)   # 2 4 6
```

</div>
</div>

---

## Graphs & Search

<div class="cols">
<div>

**Vertices** (nodes) connected by **edges**.
- **Directed** — edges have direction
- **Undirected** — edges go both ways

**Representation:**
```python
# Adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}
```

</div>
<div>

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs(graph, "A")   # A B C D
```

<div class="callout rule">

**BFS** → shortest path (unweighted). **DFS** → reachability, cycle detection.

</div>

</div>
</div>

---

## Chapter 14 — Quick Reference

| Concept | Key syntax / notes |
|---|---|
| ADT | Interface (what) vs. implementation (how) |
| Stack | LIFO; `list.append()` / `.pop()` |
| Queue | FIFO; `deque.append()` / `.popleft()` |
| deque | O(1) at both ends; `from collections import deque` |
| Tree traversal | Pre/in/post-order — recursive with base case `None` |
| BST property | Left subtree < node < right subtree |
| BFS | Queue-based; shortest path |
| DFS | Stack or recursion-based; reachability |

---

<!-- _class: title -->

# End of Chapter 14

*Next: Chapter 15 — Algorithms*

*Big O · searching · sorting · benchmarking*
