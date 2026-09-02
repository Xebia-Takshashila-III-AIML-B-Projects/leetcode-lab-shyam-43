# LC-0622: Design Circular Queue — Hints

## 💡 Hint 1 — Think About FIFO

A queue follows **First In, First Out (FIFO)**.

You need to know:

- Which element is at the front?
- Where should the next element be inserted?
- Is the queue empty?
- Is the queue full?

---

## 💡 Hint 2 — Use an Array

A fixed-size array can store the elements.

You will need to track:

- `front`
- `rear`
- `size`
- `capacity`

The `rear` position should represent where the next element can be inserted.

---

## 💡 Hint 3 — Make the Array Circular

The important idea is that the array should behave like a circle.

When you reach the last index, go back to index `0`.

For example, with capacity `3`:

```text
0 → 1 → 2 → 0 → 1 → 2 → ...
```

---

## 💡 Hint 4 — Use Modulo

You can move to the next circular position using:

```python
next_position = (current_position + 1) % capacity
```

For capacity `3`:

```text
0 → 1
1 → 2
2 → 0
```

---

## 💡 Hint 5 — Track the Size

The current size makes it easy to determine whether the queue is empty or full.

```text
size == 0          → Empty
size == capacity   → Full
```

This also avoids confusing the empty and full states.

---

## 🏆 Final Hint

Maintain these pieces of information:

```text
Queue storage
Front position
Rear position
Current size
Maximum capacity
```

For insertion:

1. Check whether the queue is full.
2. Store the value at the rear position.
3. Move rear circularly.
4. Increase size.

For deletion:

1. Check whether the queue is empty.
2. Move front circularly.
3. Decrease size.

Try implementing the solution yourself before looking at the editorial.