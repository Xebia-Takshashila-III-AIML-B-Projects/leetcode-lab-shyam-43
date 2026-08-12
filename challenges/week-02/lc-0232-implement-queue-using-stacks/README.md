# LC-0232: Implement Queue using Stacks

**Difficulty:** 🟢 Easy

**Week:** 02

**Day:** 08 (Section B)

**Topic:** Stack, Queue, Design

**Related Course Topic:** Why Long Short-Term Memory (LSTM)?

---

# 🎯 Learning Objective

In this challenge, you will design a queue using only stack operations.

You will learn how two different data structures can work together to produce the behavior of another data structure.

This challenge introduces the concept of abstraction and efficient data structure design.

---

# 📚 Course Connection

Today's lecture introduced **Long Short-Term Memory (LSTM)** networks.

LSTMs carefully control how information enters memory, moves through memory, and leaves memory.

Similarly, this challenge demonstrates how information can be transferred between two stacks to produce queue behavior.

Although the implementation is different, both systems rely on **controlled movement of information** rather than random access.

---

# 📝 Problem Statement

Implement a **First-In First-Out (FIFO)** queue using only two stacks.

Implement the following methods:

- `push(x)` — Push element `x` to the back of the queue.
- `pop()` — Remove the element from the front of the queue and return it.
- `peek()` — Return the front element.
- `empty()` — Return `True` if the queue is empty, otherwise `False`.

You may only use standard stack operations.

---

# Example

Input

```text
MyQueue()

push(1)

push(2)

peek()

pop()

empty()
```

Output

```text
null

null

null

1

1

False
```

---

# Constraints

- 1 ≤ x ≤ 9
- At most 100 operations

---

# 💡 Hint

One stack stores newly inserted elements.

The other stack helps retrieve elements in FIFO order.

---

# 🏆 Challenge

Can you implement every operation efficiently using only stack operations?

---

# 📂 Files

| File | Purpose |
|------|---------|
| README.md | Problem description and instructions |
| solution.py | Write your solution here |
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

git commit -m "feat: solved lc-0232 implement queue using stacks"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine moving books between two piles.

One pile is used for adding books.

The other pile is used when removing books.

By carefully transferring books between the two piles, you can make them behave like a queue even though each pile is a stack.
