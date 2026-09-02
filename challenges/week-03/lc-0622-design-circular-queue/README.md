# LC-0622: Design Circular Queue

## 🟡 Difficulty
Medium

## 📅 Roadmap
- **Week:** 02
- **Day:** 09
- **Topic:** Queue, Circular Queue, Design
- **Related Course Topic:** Gates in Long Short-Term Memory (LSTM)

## 🎯 Learning Objective

In this challenge, you will design a circular queue with a fixed capacity.

You will learn how a circular queue reuses available positions instead of shifting elements after every deletion.

## 🔗 Course Connection

Today's lecture introduced the **Gates in Long Short-Term Memory (LSTM)**.

LSTMs carefully control how information enters, remains, and leaves memory.

Similarly, a circular queue carefully manages how elements enter and leave a fixed-size structure.

## 📝 Problem Statement

Design a circular queue with a fixed capacity.

Implement the following operations:

- `enQueue(value)` — Insert an element into the queue.
- `deQueue()` — Delete an element from the queue.
- `Front()` — Get the front item.
- `Rear()` — Get the last item.
- `isEmpty()` — Check whether the queue is empty.
- `isFull()` — Check whether the queue is full.

Return:

- `True` when `enQueue` or `deQueue` succeeds.
- `False` when the operation cannot be performed.
- `-1` for `Front()` or `Rear()` when the queue is empty.

## 💡 Example

### Input

```text
MyCircularQueue(3)
enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
Rear()
isFull()
deQueue()
enQueue(4)
Rear()
```

### Output

```text
True
True
True
False
3
True
True
True
4
```

## Constraints

- `1 <= k <= 1000`
- `0 <= value <= 1000`
- At most `3000` operations
- The queue has a fixed capacity

## 💡 Hint

A circular queue allows the rear position to wrap around to the beginning of the array when space becomes available.

## 🏆 Challenge

Can you implement all queue operations efficiently without shifting elements after every deletion?

## 📂 Files

| File | Purpose |
|------|---------|
| README.md | Problem description and instructions |
| solution.py | Write your solution here |
| test_solution.py | Automated unit tests |
| hints.md | Progressive hints |
| editorial.md | Detailed explanation |

## 🚀 Getting Started

Open `solution.py`.

Complete the implementation.

Save the file.

Run the tests:

```bash
pytest
```

Commit your changes:

```bash
git add .
git commit -m "feat: solved lc-0622 design circular queue"
git push
```

## 🧠 Think Like an Engineer

Imagine a circular conveyor belt.

Items enter the belt and leave from another position.

When the belt reaches its final position, it loops back to the beginning and reuses available space.

A circular queue works in the same way.

The queue must carefully manage:

- Front position
- Rear position
- Current size
- Maximum capacity

## 🔄 Key Idea

Instead of shifting elements after every deletion, use the array as a circle.

When a position reaches the end of the array, move back to the beginning.

This allows queue operations to remain efficient.