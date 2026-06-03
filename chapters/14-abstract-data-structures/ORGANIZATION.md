# Chapter 14 Organization (Abstract Data Structures)

This chapter is split into:

- `1400-abstract-data-structures.ipynb`
- `1401-adt-basics.ipynb`
- `1402-stacks-queues.ipynb`
- `1403-trees-graphs.ipynb`
- `1404-assignments.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1400-abstract-data-structures.ipynb`
   - Chapter intro: learning goals, motivation, chapter flow map. No exercises.
2. `1401-adt-basics.ipynb`
   - ADT concept; interface vs. implementation; the ADT contract
3. `1402-stacks-queues.ipynb`
   - Stack: LIFO, push/pop, Python list as stack, call stack analogy, use cases
   - Queue: FIFO, enqueue/dequeue, `collections.deque`, use cases
4. `1403-trees-graphs.ipynb`
   - Trees: terminology, binary trees, traversals (pre/in/post-order), BST basics
   - Graphs: vertices and edges, adjacency list/matrix, DFS and BFS
5. `1404-assignments.ipynb`
   - Chapter exercises covering all four data structures

## File Roles

- `1400-abstract-data-structures.ipynb`: Chapter intro — learning goals and chapter map. No exercises.
- `1401-adt-basics.ipynb`: ADT concept; interface vs. implementation.
- `1402-stacks-queues.ipynb`: Stack and Queue — implementation, operations, and use cases.
- `1403-trees-graphs.ipynb`: Trees and Graphs — structure, traversal, and representation.
- `1404-assignments.ipynb`: Applied exercises and problems.
- `MATERIALS.md`: Teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/14-abstract-data-structures/*` as the only Chapter 14 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Ensure chapter outcomes align with any Chapter 14 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.
