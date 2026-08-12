# LC-0146: LRU Cache

**Difficulty:** 🟟 Medium

**Week:** 02

**Day:** 08 (Section A)

**Topic:** Hash Map, Doubly Linked List, Design

**Related Course Topic:** Why Long Short-Term Memory (LSTM)?

---

# 🎯 Learning Objective

In this challenge, you will design a data structure that stores recently used information while automatically removing information that has not been used for the longest time.

This problem introduces efficient memory management and demonstrates how combining multiple data structures can produce an optimal solution.

---

# 📚 Course Connection

Today's lecture introduced **Long Short-Term Memory (LSTM)** networks.

Unlike a standard Recurrent Neural Network (RNN), an LSTM selectively decides:

- What information should be remembered.
- What information should be forgotten.
- What information should influence future predictions.

The LRU (Least Recently Used) Cache follows a similar philosophy.

Since memory is limited, the cache cannot keep everything forever.

Whenever the cache becomes full, it removes the least recently used item so that newer or frequently used data can remain available.

Although the implementation is different from an LSTM, both systems solve the same fundamental problem:

> **Limited memory requires intelligent decisions about what to keep and what to discard.**

---

# 📝 Problem Statement

Design a data structure that follows the constraints of a **Least Recently Used (LRU) Cache**.

Implement the `LRUCache` class with the following operations:

- `LRUCache(capacity)` initializes the cache with a positive capacity.
- `get(key)` returns the value of the key if it exists; otherwise returns `-1`.
- `put(key, value)` updates or inserts the value. If the cache exceeds its capacity, remove the least recently used item.

Both operations must run in **O(1)** average time.

---

# Example

```text
Input

LRUCache(2)

put(1,1)

put(2,2)

get(1)

put(3,3)

get(2)

put(4,4)

get(1)

get(3)

get(4)
```

Output

```text
null

null

null

1

null

-1

null

-1

3

4
```

---

# Constraints

- 1 ≤ capacity ≤ 3000
- 0 ≤ key ≤ 10000
- 0 ≤ value ≤ 100000
- Up to 2 × 10⁵ operations

---

# 💡 Hint

Can one data structure provide

- Fast lookup?
- Fast insertion?
- Fast removal?
- Fast update of recently used items?

---

# 🏆 Challenge

Design the cache so that every operation runs in **O(1)** average time.

---

# 📂 Files

| File | Purpose |
|------|---------|
| solution.py | Write your solution |
| test_solution.py | Automated unit tests |
| hints.md | Progressive hints |
| editorial.md | Detailed explanation |

---

# 🚀 Getting Started

1. Open `solution.py`.

2. Complete the implementation.

3. Save the file.

4. Run

```bash
pytest
```

5. Commit your changes.

```bash
git add .

git commit -m "feat: solved lc-0146 lru cache"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine your desk has space for only a few books.

The books you use frequently stay on your desk.

When a new book arrives and there is no space left, you remove the book that hasn't been used for the longest time.

That is exactly how an LRU Cache works.
