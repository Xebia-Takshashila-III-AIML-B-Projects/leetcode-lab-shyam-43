# 📖 Editorial - LC-0053: Maximum Subarray

## Problem Overview

We are given an array of integers.

Our goal is to find the contiguous subarray that has the largest possible sum.

---

# Example

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

Best Subarray

```text
[4,-1,2,1]
```

Maximum Sum

```text
6
```

---

# Approach

A brute-force solution would examine every possible subarray.

However,

this results in many repeated calculations.

Instead,

we can determine the best subarray ending at each position using information from the previous position.

At every element,

we ask:

```text
Should I extend the current subarray?

OR

Should I start a new one?
```

The better choice becomes the current best.

---

# Why This Works

Every optimal subarray ending at position `i`

depends only on

- the current value
- the best subarray ending at position `i - 1`

This allows us to process the array only once.

This algorithm is commonly known as **Kadane's Algorithm**.

---

# Time Complexity

```text
O(n)
```

Each element is processed once.

---

# Space Complexity

```text
O(1)
```

Only a few variables are maintained.

---

# Relation to Today's Lecture

Today's lecture focused on **Backpropagation Through Time (BPTT)**.

During training,

the model continuously updates itself based on previous computations.

Similarly,

Kadane's Algorithm continuously updates its current best solution using previously accumulated information.

Rather than exploring every possibility again,

it carries forward only the most useful information.

---

# Interview Tips

When explaining your solution:

1. Describe the brute-force solution.
2. Explain why it is inefficient.
3. Introduce the idea of maintaining the best subarray ending at each position.
4. Discuss Kadane's Algorithm.
5. Analyze time and space complexity.

---

# Key Takeaways

- Dynamic Programming can optimize repeated calculations.
- Maintaining state often leads to linear-time algorithms.
- Kadane's Algorithm is one of the most important interview algorithms.
- Sequential optimization appears frequently in Machine Learning and Neural Networks.

---

# Challenge Extension

After solving this challenge, try:

- LC-121 – Best Time to Buy and Sell Stock
- LC-198 – House Robber
- LC-152 – Maximum Product Subarray
- LC-918 – Maximum Sum Circular Subarray

These problems build upon the same optimization principles.

Happy Coding! 🚀
