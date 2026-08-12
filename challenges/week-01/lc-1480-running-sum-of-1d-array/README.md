# LC-1480: Running Sum of 1D Array

**Difficulty:** 🟢 Easy

**Week:** 01

**Day:** 03 (Section A) / Day 04 (Section B)

**Topic:** Arrays, Prefix Sum

**Related Course Topic:** Mathematics Behind a Recurrent Neural Network (RNN)

---

# 🎯 Learning Objective

In this challenge, you will learn how to efficiently maintain cumulative information while traversing a sequence.

Instead of repeatedly calculating previous values, you will continuously update a running total as you process each element.

This introduces the concept of **state accumulation**, which is fundamental in sequence-processing algorithms.

---

# 📚 Course Connection

Today's lecture introduced the mathematical foundation of Recurrent Neural Networks (RNNs).

An RNN processes data one element at a time while carrying information from previous time steps through its hidden state.

Similarly, in this challenge, the running sum stores previously accumulated values, allowing future computations to build upon past information.

This demonstrates how maintaining context leads to more efficient computation.

---

# 📝 Problem Statement

Given an array `nums`, return a new array where each element at index `i` is equal to the sum of all elements from index `0` to `i`.

The running sum of an array is defined as

```text
runningSum[i] = nums[0] + nums[1] + ... + nums[i]
```

---

# Example 1

Input

```text
nums = [1,2,3,4]
```

Output

```text
[1,3,6,10]
```

---

# Example 2

Input

```text
nums = [1,1,1,1,1]
```

Output

```text
[1,2,3,4,5]
```

---

# Example 3

Input

```text
nums = [3,1,2,10,1]
```

Output

```text
[3,4,6,16,17]
```

---

# Constraints

- 1 ≤ nums.length ≤ 1000
- -10⁶ ≤ nums[i] ≤ 10⁶

---

# 💡 Hint

Do you really need to calculate the sum from the beginning for every element?

Can you reuse the previous running total?

---

# 🏆 Challenge

Can you solve this problem in **O(n)** time?

---

# 📂 Files

| File | Purpose |
|------|---------|
| solution.py | Write your solution here |
| test_solution.py | Automated test cases |
| hints.md | Progressive hints |
| editorial.md | Detailed explanation |

---

# 🚀 Getting Started

1. Open `solution.py`.

2. Implement your solution.

3. Save the file.

4. Run the tests.

```bash
pytest
```

5. If all tests pass, commit your changes.

```bash
git add .

git commit -m "feat: solved lc-1480 running sum of 1d array"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine keeping track of the total distance you've walked during a journey.

Instead of adding every previous step each time someone asks how far you've traveled, you simply remember your current total and update it whenever you take another step.

This is exactly how a running sum works.