# 📖 Editorial - LC-0605: Can Place Flowers

## Problem Overview

We are given a flowerbed where:

- `0` represents an empty plot.
- `1` represents a planted flower.

Flowers cannot be planted in adjacent plots.

Our task is to determine whether `n` new flowers can be planted.

---

# Example

```text
flowerbed = [1,0,0,0,1]

n = 1
```

Output

```text
True
```

---

# Approach

Traverse the flowerbed from left to right.

For every empty plot:

- Check the left neighbor.
- Check the right neighbor.

If both are empty (or outside the array),

plant a flower and continue.

---

# Why This Works

Every planting decision depends only on the current plot and its immediate neighbors.

Since each position is processed once,

the algorithm runs efficiently.

---

# Time Complexity

```text
O(n)
```

Each plot is visited once.

---

# Space Complexity

```text
O(1)
```

No additional data structures are required.

---

# Relation to Today's Lecture

Today's lecture introduced **Activation Functions**.

An activation function determines whether information should pass forward based on the current input.

Similarly,

this algorithm determines whether a flower can be planted by evaluating the local neighborhood.

Both involve making decisions using contextual information.

---

# Interview Tips

When explaining your solution:

1. Explain the planting rule.
2. Discuss boundary conditions.
3. Show how neighboring plots are checked.
4. Explain why updating the flowerbed is necessary.
5. Analyze time and space complexity.

---

# Key Takeaways

- Greedy algorithms often make local decisions.
- Boundary conditions are important in array problems.
- Context-aware decisions appear frequently in programming.
- Efficient traversal avoids unnecessary computation.

---

# Challenge Extension

After solving this challenge, try:

- LC-455 – Assign Cookies
- LC-121 – Best Time to Buy and Sell Stock
- LC-55 – Jump Game
- LC-134 – Gas Station

These problems further strengthen your understanding of greedy algorithms.

Happy Coding! 🚀
