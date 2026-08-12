# 📖 Editorial - LC-0232: Implement Queue using Stacks

## Problem Overview

We need to implement a queue using only stack operations.

A queue follows **First-In First-Out (FIFO)**.

A stack follows **Last-In First-Out (LIFO)**.

The challenge is to combine two stacks so they behave like a queue.

---

# Example

```text
push(1)

push(2)

peek() → 1

pop() → 1

empty() → False
```

---

# Approach

Maintain two stacks.

- Input Stack
- Output Stack

When inserting,

push directly into the input stack.

When removing or peeking,

if the output stack is empty,

move every element from the input stack to the output stack.

This reverses the order and places the oldest element on top.

---

# Why This Works

The first reversal occurs while pushing into the input stack.

The second reversal occurs when transferring elements to the output stack.

Two reversals restore the original insertion order, producing FIFO behavior.

---

# Time Complexity

```text
push()

O(1)

pop()

Amortized O(1)

peek()

Amortized O(1)

empty()

O(1)
```

---

# Space Complexity

```text
O(n)
```

Both stacks together store all elements.

---

# Relation to Today's Lecture

Today's lecture introduced **Long Short-Term Memory (LSTM)**.

An LSTM carefully controls how information moves between different memory states.

Similarly,

this implementation controls how data moves between two stacks to achieve queue behavior.

Both systems rely on structured information flow instead of unrestricted access.

---

# Interview Tips

When explaining your solution:

1. Explain FIFO vs LIFO.
2. Describe why one stack is insufficient.
3. Introduce two stacks.
4. Explain when elements are transferred.
5. Discuss amortized time complexity.

---

# Key Takeaways

- Multiple data structures can work together.
- Two stacks can simulate a queue.
- Amortized analysis is important in interviews.
- Design problems test understanding beyond coding syntax.

---

# Challenge Extension

After solving this challenge, try:

- LC-225 – Implement Stack using Queues
- LC-155 – Min Stack
- LC-622 – Design Circular Queue
- LC-641 – Design Circular Deque

These problems further strengthen your understanding of data structure design.

Happy Coding! 🚀
