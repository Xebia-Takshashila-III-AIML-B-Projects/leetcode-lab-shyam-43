# LC-0070: Climbing Stairs

**Difficulty:** 🟢 Easy

**Week:** 02

**Day:** 07 (Section A)

**Topic:** Dynamic Programming

**Related Course Topic:** The Vanishing Gradient Problem

---

# 🎯 Learning Objective

In this challenge, you will learn how to solve problems where the current solution depends on previously computed results.

Instead of solving the same subproblem repeatedly, you will reuse earlier computations to efficiently determine the final answer.

This introduces one of the most fundamental concepts in Dynamic Programming.

---

# 📚 Course Connection

Today's lecture focused on the **Vanishing Gradient Problem**.

When processing long sequences, Recurrent Neural Networks rely on information from previous time steps. As sequences become longer, preserving useful information becomes increasingly difficult.

Similarly, in this challenge, every step depends directly on the results of previous steps. Maintaining these previous results allows us to compute the final answer efficiently without repeating work.

---

# 📝 Problem Statement

You are climbing a staircase.

It takes `n` steps to reach the top.

Each time you may climb either

- 1 step
- 2 steps

Return the total number of distinct ways to reach the top.

---

# Example 1

Input

```text
n = 2
```

Output

```text
2
```

Explanation

```text
1 + 1

2
```

---

# Example 2

Input

```text
n = 3
```

Output

```text
3
```

Explanation

```text
1 + 1 + 1

1 + 2

2 + 1
```

---

# Constraints

- 1 ≤ n ≤ 45

---

# 💡 Hint

How many ways can you reach step `n`?

Does it depend on the number of ways to reach previous steps?

---

# 🏆 Challenge

Can you solve this problem in **O(n)** time using only constant extra space?

---

# 📂 Files

| File | Purpose |
|------|---------|
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

git commit -m "feat: solved lc-0070 climbing stairs"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine climbing a staircase.

To reach the current step, you must have come from either the previous step or the step before that.

Instead of recalculating every possible path repeatedly, you can build the answer using previously computed results.
