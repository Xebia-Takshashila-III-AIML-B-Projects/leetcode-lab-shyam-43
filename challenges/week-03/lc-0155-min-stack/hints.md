# Hints

## Hint 1

A normal stack can perform:

- push
- pop
- top

all in **O(1)** time.

The challenge is maintaining the minimum element in **O(1)**.

---

## Hint 2

Think about storing additional information whenever you push a new element.

Can you know the minimum so far at every step?

---

## Hint 3

Instead of only storing values,

store:

(value, current_min)

inside the stack.

Example:

push(3)

[(3,3)]

push(5)

[(3,3),(5,3)]

push(2)

[(3,3),(5,3),(2,2)]

---

## Hint 4

Then getMin() simply returns the second value of the top element.
