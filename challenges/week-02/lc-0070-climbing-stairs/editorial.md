# 📖 Editorial - LC-0070: Climbing Stairs

## Problem Overview

We are given a staircase with `n` steps.

At every move, we may climb either

- one step
- two steps

Our goal is to determine the total number of distinct ways to reach the top.

---

# Example

Input

```text
n = 5
```

Possible answer

```text
8
```

---

# Approach

Consider how we reach the final step.

To reach step `n`,

we must have arrived from

- step `n - 1`
- step `n - 2`

Therefore,

the total number of ways to reach step `n`

depends on the total number of ways to reach the previous two steps.

Instead of solving the same problem repeatedly,

we build the answer from smaller subproblems.

---

# Why This Works

Every solution depends only on the previous two computed values.

Once those values are known,

the next answer can be calculated immediately.

This avoids repeated computation.

---

# Time Complexity

```text
O(n)
```

Each step is processed once.

---

# Space Complexity

```text
O(1)
```

Only two previous values need to be stored.

---

# Relation to Today's Lecture

Today's lecture introduced the **Vanishing Gradient Problem**.

In sequence models, each new state depends on previous states.

Similarly,

this algorithm builds every new answer using information computed in earlier steps.

Maintaining previous state is essential for solving the problem efficiently.

---

# Interview Tips

When explaining your solution,

1. Explain the recursive relationship.
2. Describe why recursion repeats work.
3. Introduce Dynamic Programming.
4. Optimize the space requirement.
5. Discuss time and space complexity.

---

# Key Takeaways

- Dynamic Programming avoids repeated work.
- Many optimization problems depend on previous states.
- The Fibonacci pattern appears in numerous interview questions.
- Maintaining state is an important programming technique.

---

# Challenge Extension

After completing this challenge, try:

- LC-198 – House Robber
- LC-746 – Min Cost Climbing Stairs
- LC-509 – Fibonacci Number
- LC-1137 – N-th Tribonacci Number

These problems extend the same Dynamic Programming concepts.

Happy Coding! 🚀
