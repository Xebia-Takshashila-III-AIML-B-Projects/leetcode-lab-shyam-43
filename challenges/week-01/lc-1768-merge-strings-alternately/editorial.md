# 📖 Editorial - LC-1768: Merge Strings Alternately

## Problem Overview

We are given two strings.

Our task is to merge them by taking one character from each string alternately.

If one string is longer,

append the remaining characters.

---

# Example

```text
word1 = "abc"

word2 = "pqr"
```

Output

```text
apbqcr
```

---

# Key Idea

Both strings are sequences.

Instead of processing one completely before the other,

we process them together.

Maintain two indices,

one for each string.

Move both forward while building the answer.

---

# Why This Works

Every character is processed exactly once.

No character is revisited.

This makes the solution efficient.

---

# Time Complexity

```text
O(n + m)
```

where

- n = length of word1
- m = length of word2

---

# Space Complexity

```text
O(n + m)
```

for the resulting merged string.

---

# Relation to Today's Lecture

Today's lecture focused on **Teaching Machines to Remember**.

When processing sequential data,

a model cannot randomly access future elements.

It moves through the sequence one step at a time.

This challenge demonstrates that same idea.

You keep track of your current position in both strings,

similar to how an RNN keeps track of its position while processing sequences.

---

# Interview Tip

Whenever a problem asks you to process two sequences together,

consider using

- Two pointers
- Two indices

This is a common interview pattern.

---

# Key Takeaways

- Traverse multiple sequences simultaneously.
- Maintain independent positions.
- Handle unequal lengths carefully.
- Process each element only once.

Happy Coding! 🚀
