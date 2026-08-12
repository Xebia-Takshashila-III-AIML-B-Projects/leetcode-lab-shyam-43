# LC-0198: House Robber

**Difficulty:** 🟡 Medium

**Week:** 02

**Day:** 07 (Section B)

**Topic:** Dynamic Programming

**Related Course Topic:** The Vanishing Gradient Problem

---

# 🎯 Learning Objective

In this challenge, you will learn how to make optimal decisions when each choice affects future possibilities.

Rather than considering every possible combination of houses, you will build the solution using previously computed results.

This introduces one of the most common Dynamic Programming patterns.

---

# 📚 Course Connection

Today's lecture introduced the **Vanishing Gradient Problem**.

As sequences become longer, each decision depends on information from previous time steps.

Similarly, in this problem, every decision depends on previous houses.

If you rob the current house, you cannot rob the previous one.

The algorithm therefore maintains information from earlier decisions to determine the best possible outcome.

---

# 📝 Problem Statement

You are a professional robber planning to rob houses along a street.

Each house contains a certain amount of money.

The only constraint is that adjacent houses cannot both be robbed because doing so will trigger the alarm system.

Return the maximum amount of money you can rob without alerting the police.

---

# Example 1

Input

```text
nums = [1,2,3,1]
```

Output

```text
4
```

Explanation

```text
Rob House 1

Skip House 2

Rob House 3

Total = 4
```

---

# Example 2

Input

```text
nums = [2,7,9,3,1]
```

Output

```text
12
```

Explanation

```text
Rob House 1

Skip House 2

Rob House 3

Skip House 4

Rob House 5

Total = 12
```

---

# Constraints

- 1 ≤ nums.length ≤ 100
- 0 ≤ nums[i] ≤ 400

---

# 💡 Hint

At every house, you have two choices:

- Rob this house.
- Skip this house.

Which option gives a larger total?

---

# 🏆 Challenge

Can you solve this problem in **O(n)** time while using **O(1)** extra space?

---

# 📂 Files

| File | Purpose |
|------|---------|
| README.md | Problem description and instructions |
| solution.py | Write your solution here |
| test_solution.py | Automated unit tests |
| hints.md | Progressive hints |
| editorial.md | Detailed explanation |

---

# 🚀 Getting Started

1. Open `solution.py`.
2. Implement your solution.
3. Save the file.
4. Run

```bash
pytest
```

5. Commit your changes.

```bash
git add .

git commit -m "feat: solved lc-0198 house robber"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine walking down a street collecting rewards.

If you collect from one house, you must skip the next one.

At every step, you must decide whether taking the current reward produces a better overall outcome than skipping it.
