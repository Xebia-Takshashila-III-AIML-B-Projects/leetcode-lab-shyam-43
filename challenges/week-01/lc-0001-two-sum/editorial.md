# 📖 Editorial - LC-0001: Two Sum

## Problem Overview

We are given an array of integers and a target value.

Our goal is to return the indices of two numbers whose sum equals the target.

Exactly one valid answer exists.

---

# Example

Input

```text
nums = [2,7,11,15]

target = 9
```

Output

```text
[0,1]
```

Because

```text
2 + 7 = 9
```

---

# Approach 1 — Brute Force

The simplest solution is

Compare every number with every other number.

Example

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

### Time Complexity

```text
O(n²)
```

### Space Complexity

```text
O(1)
```

Although correct,

this becomes slow for large arrays.

---

# Approach 2 — Hash Map (Optimal)

Instead of repeatedly searching the array,

remember the numbers you have already seen.

A dictionary allows lookups in nearly constant time.

---

# Key Idea

For every element,

calculate

```text
difference = target - current_number
```

Then ask

> Have I already seen this difference?

If yes,

the answer has been found.

Otherwise,

store the current number and continue.

---

# Dry Run

Input

```text
nums = [2,7,11,15]

target = 9
```

Initially

```text
dictionary = {}
```

---

### Step 1

Current Number

```text
2
```

Required

```text
7
```

Dictionary

```text
{}
```

Not found.

Store

```text
{
    2 : 0
}
```

---

### Step 2

Current Number

```text
7
```

Required

```text
2
```

Dictionary

```text
{
    2 : 0
}
```

Found!

Return

```text
[0,1]
```

The algorithm stops immediately.

---

# Why This Works

Every time we visit a number,

we remember where we found it.

Instead of searching the array again,

we simply ask the dictionary.

Dictionary lookups are extremely fast.

---

# Time Complexity

Each element is processed exactly once.

```text
O(n)
```

---

# Space Complexity

The dictionary may store every element.

```text
O(n)
```

---

# Relation to Today's Lecture

Today's topic was

> **Why Machines Need Memory**

A machine processing sequential information often needs to remember what it has already seen.

This problem demonstrates exactly that.

The dictionary acts as memory.

Without memory,

the algorithm repeatedly searches the array.

With memory,

the answer is found much more efficiently.

This same principle appears throughout Machine Learning,

especially in sequence models such as **Recurrent Neural Networks (RNNs)**, where previous information influences future decisions.

---

# Interview Tips

During interviews,

explain your thinking clearly.

1. Describe the brute-force approach.
2. Discuss its limitations.
3. Introduce the Hash Map optimization.
4. Explain why it reduces the time complexity.
5. Analyze time and space complexity.

Interviewers value your reasoning as much as your final solution.

---

# Key Takeaways

- Brute-force is simple but inefficient.
- Hash Maps provide fast lookups.
- Storing previous information avoids repeated work.
- Memory can significantly improve algorithm performance.
- Understanding the problem-solving process is more important than memorizing the code.

---

# Challenge Extension

Try solving the following without looking at the solution:

- Two Sum II (Sorted Array)
- Three Sum
- Four Sum

Notice how each problem builds upon the same idea of efficient searching and remembering previously processed values.

Happy Coding! 🚀
