# LC-0724: Find Pivot Index

**Difficulty:** 🟢 Easy

**Week:** 01

**Day:** 03 (Section B) / Day 04 (Section A)

**Topic:** Arrays, Prefix Sum

**Related Course Topic:** Mathematics Behind a Recurrent Neural Network (RNN) & Forward Propagation

---

# 🎯 Learning Objective

In this challenge, you will learn how to efficiently maintain cumulative information while traversing an array.

Instead of repeatedly calculating the left and right sums for every index, you will use previously computed information to make efficient decisions.

This introduces the concept of **context accumulation**, an important idea in sequence processing algorithms.

---

# 📚 Course Connection

During today's lecture, you learned that Recurrent Neural Networks (RNNs) process information sequentially by carrying forward a hidden state.

Similarly, this problem requires you to maintain information about previously processed elements while determining whether the current index satisfies the required condition.

Rather than recalculating everything from scratch, you continuously update your knowledge as you move through the array.

---

# 📝 Problem Statement

Given an integer array `nums`, find the **pivot index**.

The pivot index is the index where the sum of all elements strictly to the left is equal to the sum of all elements strictly to the right.

If multiple pivot indices exist, return the leftmost one.

If no pivot index exists, return **-1**.

---

# Example 1

Input

```text
nums = [1,7,3,6,5,6]
```

Output

```text
3
```

---

# Example 2

Input

```text
nums = [1,2,3]
```

Output

```text
-1
```

---

# Example 3

Input

```text
nums = [2,1,-1]
```

Output

```text
0
```

---

# Constraints

- 1 ≤ nums.length ≤ 10⁴
- -1000 ≤ nums[i] ≤ 1000

---

# 💡 Hint

Can you calculate the total sum only once?

Then, while traversing the array, maintain a running left sum and derive the right sum from it.

---

# 🏆 Challenge

Can you solve this problem in **O(n)** time while using only **O(1)** extra space?

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
4. Run the tests.

```bash
pytest
```

5. If all tests pass, commit your changes.

```bash
git add .

git commit -m "feat: solved lc-0724 find pivot index"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine balancing a weighing scale.

As you move the balance point across the scale, you already know the total weight.

Instead of recounting every object on both sides each time, you simply keep track of the weight you've already passed.

This allows you to determine whether the scale is balanced much more efficiently.