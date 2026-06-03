# Chapter 14 Materials (Abstract Data Structures)

This checklist is for building and delivering:

- `1400-abstract-data-structures.ipynb`
- `1401-adt-basics.ipynb`
- `1402-stacks-queues.ipynb`
- `1403-trees-graphs.ipynb`
- `1404-assignments.ipynb`

## Must-Have Teaching Materials

- Slide deck or notes covering:
  - What an ADT is vs. a concrete data structure
  - Stack (LIFO) and Queue (FIFO): interface, use cases, Python implementations
  - Trees: terminology (root, node, leaf, height, depth), binary trees, traversals
  - Graphs: vertices, edges, directed vs. undirected, adjacency representation
- Code examples and demos ready to run in class
- Practice dataset or starter code where applicable

## Notebook Content Targets

### `1400-abstract-data-structures.ipynb`

- Chapter intro: learning goals, motivation, chapter flow map. No exercises.

### `1401-adt-basics.ipynb`

- What is an ADT; interface vs. implementation; Python's `collections.deque` as a motivating example
- The ADT contract: operations, preconditions, postconditions

### `1402-stacks-queues.ipynb`

- Stack: LIFO discipline; push/pop; call stack analogy; Python list as stack; use cases (undo, expression evaluation)
- Queue: FIFO discipline; enqueue/dequeue; `collections.deque`; use cases (BFS, task scheduling)

### `1403-trees-graphs.ipynb`

- Trees: terminology; binary trees; traversals (pre-order, in-order, post-order); BST basics
- Graphs: vertices and edges; adjacency list/matrix; DFS and BFS traversal

### `1404-assignments.ipynb`

- Chapter exercises and applied problems covering stacks, queues, trees, and graphs

## Practice and Assessment Pack

- In-class checks:
  - 2–3 conceptual poll/discussion questions (e.g. "is a call stack LIFO or FIFO?")
  - 1–2 trace-the-execution questions
- Lab tasks:
  - Implement a stack-based expression evaluator; BFS on a simple graph
- Homework:
  - Model a real-world process (e.g. browser history, print queue) as an ADT
- Grading anchors:
  - Correctness of ADT operations
  - Appropriate choice of data structure for the problem

## Reusable Assets to Prepare

- Shared starter code snippets
- Solution cells (tagged `hide-input`) for all exercises

## Chapter 14 Delivery Order (Recommended)

1. `1400-abstract-data-structures.ipynb` — Chapter intro
2. `1401-adt-basics.ipynb` — ADT concept and interface vs. implementation
3. `1402-stacks-queues.ipynb` — Stack and Queue
4. `1403-trees-graphs.ipynb` — Trees and Graphs
5. `1404-assignments.ipynb` — Exercises and applied problems

## Coordination Note

Chapter 14 planning and delivery are scoped to `chapters/14-abstract-data-structures/` only.
