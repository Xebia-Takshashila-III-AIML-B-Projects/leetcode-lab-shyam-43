# 💡 Hints - LC-0146: LRU Cache

Reveal one hint at a time.

---

# Hint 1

The cache must support

- Fast lookup
- Fast insertion
- Fast deletion

Which data structure provides fast lookup?

---

# Hint 2

A dictionary (hash map) gives O(1) lookup.

Can it also keep track of usage order?

---

# Hint 3

Whenever an item is accessed,

it becomes the **most recently used** item.

How can you move it efficiently?

---

# Hint 4

Whenever the cache becomes full,

which item should be removed?

---

# Hint 5

Think about combining

- Hash Map
- Doubly Linked List

Each solves a different part of the problem.

---

# Final Hint

Use

- Hash Map for O(1) lookup.
- Doubly Linked List for O(1) insertion and removal.

Together they satisfy the required time complexity.

Good luck! 🚀
