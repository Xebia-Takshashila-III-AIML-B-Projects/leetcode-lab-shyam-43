# 📖 Editorial - LC-0121: Best Time to Buy and Sell Stock

## Problem Overview

We are given stock prices for several days.

Our goal is to maximize profit by buying once and selling once.

The buying day must always occur before the selling day.

---

# Example

```text
prices = [7,1,5,3,6,4]
```

Best choice

```text
Buy at 1

Sell at 6

Profit = 5
```

---

# Approach

Instead of checking every pair of days,

process the prices from left to right.

Maintain:

- Lowest price seen so far
- Maximum profit found so far

For each day,

calculate the profit if the stock were sold today.

Update the maximum profit whenever a better profit is found.

---

# Why This Works

At every point,

the best buying day is simply the minimum price encountered earlier.

Using this information,

the best selling decision can be evaluated immediately.

---

# Time Complexity

```text
O(n)
```

Each price is processed once.

---

# Space Complexity

```text
O(1)
```

Only two variables are maintained.

---

# Relation to Today's Lecture

Today's lecture focused on **Backpropagation Through Time (BPTT)**.

As an RNN updates its weights using information accumulated from previous time steps,

this algorithm updates its decisions using the lowest price observed earlier in the sequence.

Efficient algorithms often rely on carrying forward useful information rather than recomputing everything.

---

# Interview Tips

When explaining your solution:

1. Explain the brute-force approach.
2. Discuss why it is inefficient.
3. Introduce the running minimum price.
4. Explain how the maximum profit is updated.
5. Analyze time and space complexity.

---

# Key Takeaways

- Maintain previous state efficiently.
- Greedy algorithms often require only local information.
- Sequential processing avoids unnecessary computations.
- Many optimization problems can be solved in linear time.

---

# Challenge Extension

After solving this challenge, try:

- LC-53 – Maximum Subarray
- LC-122 – Best Time to Buy and Sell Stock II
- LC-309 – Best Time to Buy and Sell Stock with Cooldown
- LC-714 – Best Time to Buy and Sell Stock with Transaction Fee

Happy Coding! 🚀
