# 📖 Editorial - LC-0724: Find Pivot Index

## Problem Overview

We are given an array of integers.

Our objective is to find the index where

```text
Sum of elements on the left
=
Sum of elements on the right
```

If no such index exists,

return **-1**.

---

# Example

Input

```text
nums = [1,7,3,6,5,6]
```

Output

```text
3
```

Explanation

```text
Left Sum  = 1 + 7 + 3 = 11

Right Sum = 5 + 6 = 11
```

---

# Approach

A brute-force solution would calculate the left and right sums separately for every index.

However, this performs many repeated calculations.

A better approach is to:

- Calculate the total sum once.
- Maintain a running left sum while traversing the array.
- Derive the right sum using the total sum.

This avoids unnecessary work and processes every element only once.

---

# Why This Works

At every position, you already know:

- The total sum of the array.
- The sum of all elements you've already visited.

Using these two values, you can immediately determine the remaining sum on the right without traversing the array again.

---

# Time Complexity

```text
O(n)
```

Each element is visited exactly once.

---

# Space Complexity

```text
O(1)
```

Only a few variables are required.

---

# Relation to Today's Lecture

Today's lecture focused on the mathematical foundation of Recurrent Neural Networks and Forward Propagation.

As an RNN processes sequential data, it carries forward a hidden state containing previously learned information.

Similarly, this algorithm carries a running left sum while processing the array.

Rather than recomputing previous values, it continuously updates the stored information, demonstrating how maintaining context leads to efficient computation.

---

# Interview Tips

When explaining your solution:

1. Describe the brute-force approach.
2. Explain why repeated calculations are inefficient.
3. Introduce the running left sum.
4. Show how the right sum can be derived.
5. Discuss the time and space complexity.

Interviewers often evaluate your thought process more than your final code.

---

# Key Takeaways

- Running sums eliminate repeated calculations.
- Maintaining context improves efficiency.
- Prefix Sum is a common interview pattern.
- Sequential processing often relies on accumulated information.
- Similar concepts appear in Dynamic Programming and Recurrent Neural Networks.

---

# Challenge Extension

After solving this problem, try exploring:

- LC-1480 – Running Sum of 1D Array
- LC-303 – Range Sum Query
- LC-560 – Subarray Sum Equals K
- LC-238 – Product of Array Except Self

These problems build upon the same idea of cumulative information and efficient sequence processing.

Happy Coding! 🚀