# 💡 Hints - LC-0001: Two Sum

Try solving the problem yourself before reading the hints.

Only reveal one hint at a time.

---

# Hint 1

What happens if you use **two nested loops**?

Can you compare every pair of numbers?

What would be the time complexity?

---

# Hint 2

While scanning the array, ask yourself:

> "What number do I need to reach the target?"

For every number, compute

```python
target - current_number
```

---

# Hint 3

Suppose the current number is

```text
7
```

and

```text
target = 9
```

What number are you looking for?

```
9 - 7 = 2
```

Have you already seen **2**?

---

# Hint 4

Instead of searching the entire array every time,

store every number you've already visited.

Python provides a perfect data structure for this.

Which one?

✅ Dictionary (Hash Map)

---

# Hint 5

As you move through the array,

store

```python
number -> index
```

Example

```python
{
    2: 0,
    7: 1,
    11: 2
}
```

---

# Hint 6

For every element

1. Compute the required value.

```python
difference = target - current_number
```

2. Check whether that value already exists in your dictionary.

If yes,

you have found the answer.

---

# Hint 7

Only after checking should you store the current number.

Otherwise,

you might accidentally use the same element twice.

---

# Hint 8

Your algorithm should scan the array only once.

Can you solve it in

```text
O(n)
```

instead of

```text
O(n²)
```

---

# Final Hint

The dictionary should store

```python
value → index
```

For every element

```python
difference = target - value
```

If

```python
difference
```

already exists in the dictionary,

return both indices immediately.

Good luck! 🚀
