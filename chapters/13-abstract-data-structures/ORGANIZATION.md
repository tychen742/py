# Chapter 13 Organization (Abstract Data Structures)

This chapter is split into:

- `1300-abstract-data-structures.ipynb`
- `1301-adt-basics.ipynb`
- `1302-stacks-queues.ipynb`
- `1303-trees-graphs.ipynb`

## Scope and Sequencing

Use this sequence to avoid overlap and keep pacing clear:

1. `1300-abstract-data-structures.ipynb`
   - Chapter intro: learning goals, motivation, chapter flow map. No exercises.
2. `1301-adt-basics.ipynb`
   - ADT concept; interface vs. implementation; the ADT contract
3. `1302-stacks-queues.ipynb`
   - Stack: LIFO, push/pop, Python list as stack, call stack analogy, use cases
   - Queue: FIFO, enqueue/dequeue, `collections.deque`, use cases
4. `1303-trees-graphs.ipynb`
   - Trees: terminology, binary trees, traversals (pre/in/post-order), BST basics
   - Graphs: vertices and edges, adjacency list/matrix, DFS and BFS

## Planned Additions

Topics from the 2026-09-25 coverage review. Status: planned, not yet written. When a topic is written, move it into the sequence above and delete it here.

- **`1301-adt-basics.ipynb`**: hash tables as the implementation behind the map ADT (`dict` and `set`): hashing, buckets, collisions, load factor, and why lookups are O(1) on average.
  *Why:* interview staple; Chapters 6, 7, and 14 mention hashing but never explain it.
- **`1302-stacks-queues.ipynb`**: linked lists: a singly linked `Node` class, traversal, insertion and deletion at the head, and their costs compared with Python lists; then a stack and a queue built on a linked list.
  *Why:* interview staple; mentioned in several chapters but never implemented.
- **`1303-trees-graphs.ipynb`**: heaps and priority queues: the binary heap as a complete binary tree, `heapq` (`heappush`, `heappop`, `nlargest`), and the top-k pattern.
  *Why:* interview staple; not covered anywhere.
- **`1303-trees-graphs.ipynb` (enrichment)**: shortest paths with Dijkstra's algorithm, using `heapq` on a weighted graph.
  *Why:* combines heaps and graphs; currently only mentioned in 14.1.

## File Roles

- `1300-abstract-data-structures.ipynb`: Chapter intro — learning goals and chapter map. No exercises.
- `1301-adt-basics.ipynb`: ADT concept; interface vs. implementation.
- `1302-stacks-queues.ipynb`: Stack and Queue — implementation, operations, and use cases.
- `1303-trees-graphs.ipynb`: Trees and Graphs — structure, traversal, and representation.
- `MATERIALS.md`: Teaching/assessment assets and prep checklist.

## Source of Truth

Use `chapters/13-abstract-data-structures/*` as the only Chapter 13 track for planning, delivery, and assessment.

## Build/Quality Checklist

- Keep each notebook executable top-to-bottom.
- Keep function definitions in chapter notebooks self-contained.
- Add at least one checkpoint exercise per major section.
- Add local `{contents}` navigation near the top of each section notebook.
- Ensure chapter outcomes align with any Chapter 13 assignment/quiz prompt.
- Tag question cells `thebe-interactive` and solution cells `hide-input`.

## Assignments

- `assignments/index.ipynb` — Assignment section landing page
- `assignments/preview.ipynb` — Preview
- `assignments/lab.ipynb` — Lab assignment
- `assignments/homework.ipynb` — Homework questions
