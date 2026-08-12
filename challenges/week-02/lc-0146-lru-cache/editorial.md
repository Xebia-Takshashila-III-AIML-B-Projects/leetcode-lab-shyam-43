# 📖 Editorial - LC-0146: LRU Cache

## Problem Overview

We need to design a cache with limited capacity.

Whenever an item is accessed,

it becomes the most recently used.

If the cache becomes full,

the least recently used item must be removed.

Both `get()` and `put()` operations must execute in **O(1)** average time.

---

# Approach

A single data structure cannot efficiently support every required operation.

Instead,

combine two data structures.

- Hash Map
- Doubly Linked List

The hash map provides constant-time lookup.

The doubly linked list maintains the order of recently used items.

---

# Why This Works

Whenever an item is accessed,

move it to the front of the linked list.

Whenever the cache is full,

remove the node at the end of the linked list.

The hash map always knows where every node is located.

This allows every operation to complete efficiently.

---

# Time Complexity

```text
get()

O(1)

put()

O(1)
```

---

# Space Complexity

```text
O(capacity)
```

---

# Relation to Today's Lecture

Today's lecture introduced **Long Short-Term Memory (LSTM)**.

An LSTM continuously decides

- what information to remember,
- what information to forget,
- what information should influence future predictions.

Similarly,

an LRU Cache keeps frequently used information while discarding information that has not been used recently.

Both systems demonstrate that **efficient memory management requires intelligent forgetting**.

---

# Interview Tips

When discussing your solution:

1. Explain why a list alone is too slow.
2. Explain why a hash map alone cannot maintain usage order.
3. Introduce the combination of a hash map and a doubly linked list.
4. Discuss why both operations become O(1).

---

# Key Takeaways

- Hash Maps provide fast lookup.
- Doubly Linked Lists provide fast insertion and deletion.
- Combining multiple data structures often produces optimal solutions.
- Efficient memory management is an important engineering skill.
- Design questions frequently appear in software engineering interviews.

---

# Challenge Extension

After solving this challenge, try:

- LC-460 – LFU Cache
- LC-1466 – Reorder Routes
- LC-706 – Design HashMap
- LC-707 – Design Linked List

These problems further develop your understanding of data structure design.

Happy Coding! 🚀
