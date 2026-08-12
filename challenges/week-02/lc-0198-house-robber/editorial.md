# 📖 Editorial - LC-0198: House Robber

## Problem Overview

We are given a row of houses.

Each house contains some money.

The only rule is that two adjacent houses cannot both be robbed.

Our objective is to maximize the total amount stolen.

---

# Example

```text
nums = [2,7,9,3,1]
```

Best choice

```text
2 + 9 + 1 = 12
```

---

# Approach

For every house,

consider two possibilities.

- Rob the current house.
- Skip the current house.

The optimal answer is whichever produces the larger amount.

Instead of recalculating previous results,

reuse the answers already computed.

---

# Why This Works

The best answer for the current house depends only on the best answers from earlier houses.

This makes the problem ideal for Dynamic Programming.

---

# Time Complexity

```text
O(n)
```

Each house is processed once.

---

# Space Complexity

```text
O(1)
```

Only a few variables are required.

---

# Relation to Today's Lecture

Today's lecture focused on the **Vanishing Gradient Problem**.

Long sequences require preserving useful information from previous states.

Similarly,

this algorithm carries forward the best decisions made earlier instead of recomputing them.

Maintaining state efficiently is the key to solving this problem.

---

# Interview Tips

When explaining your solution:

1. Explain the robbery constraint.
2. Describe the two choices at every house.
3. Introduce Dynamic Programming.
4. Optimize the solution to constant space.
5. Discuss time and space complexity.

---

# Key Takeaways

- Dynamic Programming builds solutions incrementally.
- Every decision depends on previous decisions.
- Maintaining state avoids repeated computation.
- Many interview problems follow this pattern.

---

# Challenge Extension

After solving this challenge, try:

- LC-70 – Climbing Stairs
- LC-213 – House Robber II
- LC-337 – House Robber III
- LC-740 – Delete and Earn

These challenges further strengthen your understanding of Dynamic Programming.

Happy Coding! 🚀
