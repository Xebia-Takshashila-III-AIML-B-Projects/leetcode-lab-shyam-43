# LC-0121: Best Time to Buy and Sell Stock

**Difficulty:** 🟢 Easy

**Week:** 02

**Day:** 05 (Section B)

**Topic:** Arrays, Greedy Algorithm

**Related Course Topic:** Backpropagation Through Time (BPTT)

---

# 🎯 Learning Objective

In this challenge, you will learn how to make optimal decisions while processing data sequentially.

Instead of comparing every possible buying and selling day, you will continuously keep track of the best buying opportunity seen so far and calculate the maximum possible profit.

This introduces the idea of maintaining the best previous state while processing a sequence.

---

# 📚 Course Connection

Today's lecture introduced **Backpropagation Through Time (BPTT)**.

During training, a Recurrent Neural Network continuously updates its parameters by learning from previous computations.

Similarly, this problem requires continuously updating the lowest buying price encountered and using it to compute the best profit at each step.

Each new day's decision depends on information collected from previous days.

---

# 📝 Problem Statement

You are given an array `prices` where `prices[i]` represents the price of a stock on the `iᵗʰ` day.

You want to maximize your profit by choosing:

- one day to buy
- one future day to sell

Return the maximum profit you can achieve.

If no profit is possible, return **0**.

---

# Example 1

Input

```text
prices = [7,1,5,3,6,4]
```

Output

```text
5
```

Explanation

```text
Buy at price 1

Sell at price 6

Profit = 5
```

---

# Example 2

Input

```text
prices = [7,6,4,3,1]
```

Output

```text
0
```

Explanation

No profitable transaction exists.

---

# Constraints

- 1 ≤ prices.length ≤ 10⁵
- 0 ≤ prices[i] ≤ 10⁴

---

# 💡 Hint

As you traverse the array,

continuously remember the **lowest price** seen so far.

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

git commit -m "feat: solved lc-0121 best time to buy and sell stock"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine you are watching stock prices every day.

You continuously remember the cheapest price you've seen.

Whenever today's price is higher, you calculate the profit you would earn if you sold today.

Keep updating your best profit until the end.
