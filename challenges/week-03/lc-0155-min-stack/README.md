# LeetCode 155 – Min Stack

## Problem Difficulty

**Medium**

---

## Problem Statement

Design a stack that supports the following operations in **constant time**.

Implement the `MinStack` class:

- `MinStack()` initializes the stack.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` returns the top element of the stack.
- `int getMin()` retrieves the minimum element currently present in the stack.

All operations must run in **O(1)** time complexity.

---

## Example

### Input

```text
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```

### Output

```text
[null,null,null,null,-3,null,0,-2]
```

---

## Explanation

```text
MinStack minStack = new MinStack();

minStack.push(-2);
minStack.push(0);
minStack.push(-3);

minStack.getMin(); // returns -3

minStack.pop();

minStack.top();    // returns 0

minStack.getMin(); // returns -2
```

---

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top`, and `getMin` will always be called on non-empty stacks.
- At most `3 × 10^4` operations will be performed.

---

## Learning Objectives

After completing this challenge, you should be able to:

- Understand how a stack works.
- Design custom data structures.
- Maintain additional state efficiently.
- Achieve constant-time minimum retrieval.
- Analyze time and space complexity.

---

## Concepts Practiced

- Stack
- Auxiliary Stack
- Data Structure Design
- Constant Time Operations
- Object-Oriented Programming

---

## Expected Time Complexity

| Operation | Complexity |
|-----------|------------|
| push | O(1) |
| pop | O(1) |
| top | O(1) |
| getMin | O(1) |

---

## Expected Space Complexity

```text
O(n)
```

where **n** is the number of elements stored in the stack.

---

## Challenge

Can you implement all operations without traversing the stack while keeping every operation in constant time?
