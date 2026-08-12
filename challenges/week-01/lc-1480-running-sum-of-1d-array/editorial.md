# 📖 Editorial - LC-1480: Running Sum of 1D Array

## Problem Overview

We are given an array of integers.

Our task is to create a new array where each element represents the cumulative sum from the beginning of the array up to the current position.

---

# Example

Input

```text
nums = [1,2,3,4]
```

Output

```text
[1,3,6,10]
```

Explanation

```text
1

1 + 2 = 3

1 + 2 + 3 = 6

1 + 2 + 3 + 4 = 10
```

---

# Approach

Instead of recalculating the sum for every index,

maintain a running total.

For each element

1. Add the current value to the running total.
2. Store the updated total in the result.

This avoids repeated calculations and processes each element only once.

---

# Why This Works

The running total always contains the sum of all previously processed elements.

As each new value is added,

the accumulated information grows naturally.

This allows us to build the answer efficiently.

---

# Time Complexity

```text
O(n)
```

Each element is processed exactly once.

---

# Space Complexity

```text
O(n)
```

if a separate result array is created.

Some implementations may modify the input array directly, reducing the additional space requirement.

---

# Relation to Today's Lecture

Today's lecture focused on the mathematical foundation of Recurrent Neural Networks.

One of the key ideas behind an RNN is that information from previous time steps is carried forward through a hidden state.

Similarly,

the running sum stores previously accumulated values and updates them as the sequence progresses.

This demonstrates how maintaining state enables efficient sequential computation.

---

# Interview Tips

When discussing your solution,

- Explain why recalculating sums repeatedly is inefficient.
- Describe how maintaining a running total eliminates redundant work.
- Analyze both the time and space complexity.

Interviewers value clear reasoning as much as the final implementation.

---

# Key Takeaways

- Running sums eliminate repeated calculations.
- State accumulation improves efficiency.
- Prefix Sum concepts appear frequently in coding interviews.
- Maintaining context is a powerful programming technique.
- Similar ideas are used in many sequence-processing algorithms.

---

# Challenge Extension

After completing this challenge, try exploring

- LC-724 – Find Pivot Index
- LC-303 – Range Sum Query
- LC-560 – Subarray Sum Equals K
- LC-238 – Product of Array Except Self

These challenges build upon the same idea of cumulative information and efficient sequence processing.

Happy Coding! 🚀