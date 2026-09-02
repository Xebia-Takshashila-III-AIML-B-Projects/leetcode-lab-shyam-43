# LC-0622: Design Circular Queue — Editorial

## 🧩 Problem Overview

You need to implement a queue with a **fixed capacity**.

A normal queue can waste array positions after elements are removed.

For example:

```text
Capacity = 5

[10, 20, 30, 40, 50]
 ↑              ↑
Front          Rear

After removing 10 and 20:

[_, _, 30, 40, 50]
       ↑       ↑
     Front    Rear
```

The empty positions at the beginning should be reusable.

A **circular queue** solves this by allowing the rear position to wrap back to the beginning.

---

## 💡 Example

For a queue of capacity `3`:

```text
Insert 1

[1, _, _]
 ↑
Front
```

Insert `2`:

```text
[1, 2, _]
 ↑     ↑
Front Rear
```

Insert `3`:

```text
[1, 2, 3]
 ↑       ↑
Front   Rear
```

Now the queue is full.

After removing `1`:

```text
[_, 2, 3]
    ↑
  Front
```

There is now an available position at index `0`.

Insert `4`:

```text
[4, 2, 3]
 ↑
Rear wraps around
```

The logical queue is:

```text
2 → 3 → 4
```

---

## 🧠 Approach

Use an array and maintain four important pieces of information:

```text
queue
front
rear
size
capacity
```

### `front`

Stores the position of the first element.

### `rear`

Stores the position where the next element should be inserted.

### `size`

Stores the number of elements currently in the queue.

### `capacity`

Stores the maximum number of elements.

---

## 🔄 Circular Movement

Use modulo to wrap around the array:

```python
next_position = (current_position + 1) % capacity
```

For capacity `3`:

```text
0 → 1 → 2 → 0 → 1 → 2
```

This is the key idea behind the circular queue.

---

## ➕ EnQueue

To insert an element:

1. Check whether the queue is full.
2. Store the value at `rear`.
3. Move `rear` to the next circular position.
4. Increase `size`.

Conceptually:

```python
queue[rear] = value
rear = (rear + 1) % capacity
size += 1
```

If the queue is already full, return `False`.

Otherwise, return `True`.

---

## ➖ DeQueue

To remove an element:

1. Check whether the queue is empty.
2. Move `front` to the next circular position.
3. Decrease `size`.

Conceptually:

```python
front = (front + 1) % capacity
size -= 1
```

If the queue is empty, return `False`.

Otherwise, return `True`.

---

## 👀 Front

If the queue is empty:

```python
return -1
```

Otherwise:

```python
return queue[front]
```

Importantly, `Front()` only reads the element.

It does **not** remove it.

---

## 👀 Rear

Because `rear` represents the **next insertion position**, the actual last element is one position before it.

Use circular movement:

```python
last_position = (rear - 1) % capacity
```

Then:

```python
return queue[last_position]
```

If the queue is empty, return `-1`.

---

## 🚫 Checking Empty and Full

The `size` variable makes these checks simple.

### Empty

```python
size == 0
```

### Full

```python
size == capacity
```

This is one reason tracking `size` is useful.

---

## ⚙️ Why This Works

The queue never shifts elements.

Instead, `front` and `rear` move around the fixed array.

For example:

```text
Capacity = 5

0 → 1 → 2 → 3 → 4
↑               ↓
└───────────────┘
```

When `rear` reaches index `4`, the next position becomes index `0`.

Therefore, previously freed positions can be reused.

---

## ⏱️ Time Complexity

Each operation requires a constant number of steps.

| Operation | Time |
|-----------|------|
| `enQueue` | `O(1)` |
| `deQueue` | `O(1)` |
| `Front` | `O(1)` |
| `Rear` | `O(1)` |
| `isEmpty` | `O(1)` |
| `isFull` | `O(1)` |

There is **no shifting of elements**.

---

## 💾 Space Complexity

The queue stores at most `k` elements.

Therefore:

```text
Space = O(k)
```

where `k` is the queue capacity.

---

## 🔗 Relation to Today's Lecture

Today's lecture discussed **Gates in Long Short-Term Memory (LSTM)**.

An LSTM controls information flow through its gates:

```text
Forget Gate
     ↓
Input Gate
     ↓
Cell State
     ↓
Output Gate
```

A circular queue also controls how information enters and leaves a fixed-size structure.

The connection is not that both use the same algorithm.

The important engineering idea is:

> A limited resource needs controlled movement and reuse.

The circular queue reuses array positions.

The LSTM controls and reuses its memory state.

---

## 🎯 Interview Tips

When solving circular queue problems, remember:

1. Identify the fixed capacity.
2. Track the front position.
3. Track the next insertion position.
4. Track the current size.
5. Use modulo for circular movement.
6. Never shift all elements after deletion.
7. Handle empty and full states explicitly.

---

## 🔑 Key Takeaways

- A circular queue is a fixed-size FIFO data structure.
- Array positions can be reused after deletion.
- Modulo enables circular movement.
- `front` identifies the first element.
- `rear` identifies the next insertion position.
- `size` distinguishes empty and full states.
- Queue operations can be performed in `O(1)` time.

---

## 🚀 Challenge Extension

After completing this implementation, try answering:

**Can you implement a circular queue without storing `size`?**

Think about how the relationship between `front` and `rear` could be used to distinguish between empty and full states.

---

## 🏁 Happy Coding!

Understand the movement of `front` and `rear` first.

Once the circular movement becomes clear, the implementation becomes much easier.