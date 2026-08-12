# LC-0053: Maximum Subarray

**Difficulty:** 🟡 Medium

**Week:** 01

**Day:** 05 (Section A)

**Topic:** Arrays, Dynamic Programming

**Related Course Topic:** Backpropagation Through Time (BPTT)

---

# 🎯 Learning Objective

In this challenge, you will learn how to make optimal decisions while traversing a sequence.

Instead of considering every possible subarray, you will continuously evaluate whether extending the current solution is beneficial or whether starting a new one produces a better result.

This introduces the concept of dynamic decision-making, a key principle in optimization algorithms.

---

# 📚 Course Connection

Today's lecture introduced **Backpropagation Through Time (BPTT)**.

During training, a Recurrent Neural Network continuously updates its parameters by learning from previous computations.

Similarly, this problem requires making the best decision at every step based on information accumulated so far.

Each new element either improves the current solution or starts a completely new one.

---

# 📝 Problem Statement

Given an integer array `nums`, find the contiguous subarray with the largest sum and return its sum.

A subarray must contain at least one element.

---

# Example 1

Input

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

Output

```text
6
```

Explanation

```text
[4,-1,2,1]
```

has the largest sum.

---

# Example 2

Input

```text
nums = [1]
```

Output

```text
1
```

---

# Example 3

Input

```text
nums = [5,4,-1,7,8]
```

Output

```text
23
```

---

# Constraints

- 1 ≤ nums.length ≤ 10⁵
- -10⁴ ≤ nums[i] ≤ 10⁴

---

# 💡 Hint

At every element ask yourself:

Should I continue the current subarray?

OR

Should I start a new subarray from here?

---

# 🏆 Challenge

Can you solve this problem in **O(n)** time?

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

git commit -m "feat: solved lc-0053 maximum subarray"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine hiking across hills and valleys.

As you move forward, you continuously decide whether it's worth continuing your current route or beginning a completely new path.

Your goal is to find the route that gives the highest overall elevation gain.
