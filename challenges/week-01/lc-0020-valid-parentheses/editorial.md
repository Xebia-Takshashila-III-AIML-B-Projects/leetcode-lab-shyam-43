# 📖 Editorial - LC-0020: Valid Parentheses

## Problem Overview

We are given a string containing different types of brackets.

Our task is to determine whether every opening bracket is matched correctly with its corresponding closing bracket.

---

# Example

Input

```text
"{[]}"
```

Output

```text
True
```

Explanation

```text
{

  [

  ]

}
```

Every bracket closes in the correct order.

---

# Approach

As we traverse the string,

- Store every opening bracket.
- When a closing bracket appears,
  compare it with the most recently stored opening bracket.

If they match,

continue processing.

Otherwise,

the string is invalid.

---

# Why This Works

The most recently opened bracket must always be closed first.

A **Stack** naturally supports this Last-In, First-Out (LIFO) behavior.

This makes it the ideal data structure for solving this problem efficiently.

---

# Time Complexity

```text
O(n)
```

Each character is processed exactly once.

---

# Space Complexity

```text
O(n)
```

In the worst case, every character is an opening bracket.

---

# Relation to Today's Lecture

Today's lecture focused on how sequential models remember previous information.

Similarly,

a stack stores previously encountered opening brackets while processing the sequence.

Each decision depends on the current input and the information remembered from earlier in the sequence.

---

# Interview Tips

When explaining your solution:

1. Explain why nested brackets require memory.
2. Introduce the Stack data structure.
3. Describe how opening and closing brackets are processed.
4. Analyze the time and space complexity.

---

# Key Takeaways

- Stack follows the Last-In, First-Out (LIFO) principle.
- Nested structures are commonly solved using stacks.
- Matching problems frequently appear in coding interviews.
- Sequential processing often requires remembering previous information.

---

# Challenge Extension

After solving this challenge, try:

- LC-155 – Min Stack
- LC-232 – Implement Queue using Stacks
- LC-394 – Decode String
- LC-71 – Simplify Path

These challenges further strengthen your understanding of stack-based algorithms.

Happy Coding! 🚀
