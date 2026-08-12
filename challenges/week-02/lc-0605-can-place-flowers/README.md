# LC-0605: Can Place Flowers

**Difficulty:** 🟢 Easy

**Week:** 02

**Day:** 06 (Section B)

**Topic:** Arrays, Greedy Algorithm

**Related Course Topic:** Activation Functions and Tanh

---

# 🎯 Learning Objective

In this challenge, you will learn how to make decisions based on the surrounding context.

Rather than examining a single position independently, you must inspect its neighboring positions before deciding whether a flower can be planted.

This introduces context-aware decision making, where the current action depends on nearby information.

---

# 📚 Course Connection

Today's lecture introduced **Activation Functions**, which determine whether information should pass through a neural network based on the current input.

Similarly, before planting a flower, the algorithm must examine the surrounding plots.

A flower can only be planted when both neighboring plots satisfy the required condition.

Although the implementation is different, both involve making decisions based on local context.

---

# 📝 Problem Statement

You have a flowerbed represented by an array.

- `0` represents an empty plot.
- `1` represents a planted flower.

Flowers cannot be planted in adjacent plots.

Given the flowerbed and an integer `n`, determine whether it is possible to plant `n` new flowers without violating the rule.

Return `True` if possible, otherwise return `False`.

---

# Example 1

Input

```text
flowerbed = [1,0,0,0,1]

n = 1
```

Output

```text
True
```

---

# Example 2

Input

```text
flowerbed = [1,0,0,0,1]

n = 2
```

Output

```text
False
```

---

# Constraints

- 1 ≤ flowerbed.length ≤ 2 × 10⁴
- flowerbed[i] is either 0 or 1
- 0 ≤ n ≤ flowerbed.length

---

# 💡 Hint

Before planting at a position, check:

- Left neighbor
- Current plot
- Right neighbor

---

# 🏆 Challenge

Can you solve this problem in **O(n)** time using only **O(1)** extra space?

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

git commit -m "feat: solved lc-0605 can place flowers"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine parking cars in a parking lot where every parked car needs one empty space on both sides.

Before parking a new car, you always inspect the neighboring spaces.

This is exactly how this algorithm works.
