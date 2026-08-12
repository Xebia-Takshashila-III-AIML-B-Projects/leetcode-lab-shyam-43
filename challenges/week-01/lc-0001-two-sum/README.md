# LC-0001: Two Sum

**Difficulty:** 🟢 Easy

**Week:** 01

**Day:** 01

**Topic:** Arrays, Hash Maps

**Related Course Topic:** Why Machines Need Memory (Recurrent Neural Networks)

---

# 🎯 Learning Objective

In this challenge, you will learn how to efficiently search through an array while remembering values that have already been seen.

Although this is a simple programming problem, it introduces an important concept used throughout Artificial Intelligence and Machine Learning—**memory**.

A machine often needs to remember previous information before making its next decision.

---

# 📚 Course Connection

During today's lecture, you learned that machines processing sequential data cannot rely only on the current input.

Instead, they must remember previous information.

This challenge demonstrates the same idea.

Instead of repeatedly searching the entire array, you remember previously visited elements using a **Hash Map**.

This is the foundation of many sequence-processing algorithms.

---

# 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers whose sum equals the target.

You may assume that:

- Exactly one solution exists.
- The same element cannot be used twice.
- The answer can be returned in any order.

---

# Example 1

Input

```text
nums = [2,7,11,15]

target = 9
```

Output

```text
[0,1]
```

Explanation

```text
nums[0] + nums[1] = 2 + 7 = 9
```

---

# Example 2

Input

```text
nums = [3,2,4]

target = 6
```

Output

```text
[1,2]
```

---

# Example 3

Input

```text
nums = [3,3]

target = 6
```

Output

```text
[0,1]
```

---

# Constraints

- 2 ≤ nums.length ≤ 10⁴
- -10⁹ ≤ nums[i] ≤ 10⁹
- -10⁹ ≤ target ≤ 10⁹
- Only one valid answer exists.

---

# 💡 Hint

Can you remember the numbers you have already visited instead of searching the array again?

Think about using a **dictionary (Hash Map)**.

---

# 🏆 Challenge

Can you solve this problem in **O(n)** time complexity?

---

# 📂 Files

| File | Purpose |
|------|---------|
| starter.py | Write your solution here |
| solution.py | Instructor reference solution |
| test_solution.py | Automated test cases |
| hints.md | Progressive hints |
| editorial.md | Detailed explanation |

---

# 🚀 Getting Started

1. Open `starter.py`.
2. Complete the function.
3. Save the file.
4. Run the tests.

```bash
pytest
```

5. If all tests pass, commit your work.

```bash
git add .

git commit -m "feat: solved lc-0001 two sum"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine you're checking attendance in a classroom.

Instead of repeatedly asking whether you've already seen a student, you keep a notebook of everyone you've checked.

That notebook acts as **memory**, allowing you to find answers much faster.

This is exactly what a Hash Map does in this problem.
