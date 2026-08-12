# LC-1768: Merge Strings Alternately

**Difficulty:** 🟢 Easy

**Week:** 01

**Day:** 02

**Topic:** Strings, Two Pointers

**Related Course Topic:** Teaching Machines to Remember

---

# 🎯 Learning Objective

In this challenge, you will learn how to traverse two sequences simultaneously while maintaining the correct order of elements.

This mirrors how sequence models process multiple streams of information one step at a time.

---

# 📚 Course Connection

Today's lecture introduced the concept of machines remembering previous information while processing sequences.

In this challenge, you will process two strings together.

Instead of finishing one string before the other, you must alternate between them while remembering your current position in both.

This reinforces the importance of sequential processing.

---

# 📝 Problem Statement

You are given two strings `word1` and `word2`.

Merge the strings by alternating their characters, starting with `word1`.

If one string becomes shorter, append the remaining characters from the longer string.

Return the merged string.

---

# Example 1

Input

```text
word1 = "abc"

word2 = "pqr"
```

Output

```text
"apbqcr"
```

---

# Example 2

Input

```text
word1 = "ab"

word2 = "pqrs"
```

Output

```text
"apbqrs"
```

---

# Example 3

Input

```text
word1 = "abcd"

word2 = "pq"
```

Output

```text
"apbqcd"
```

---

# Constraints

- 1 ≤ word1.length, word2.length ≤ 100
- word1 and word2 consist of lowercase English letters.

---

# 💡 Hint

Can you use two indices?

One index for each string.

---

# 🏆 Challenge

Can you solve this in one traversal?

---

# 📂 Files

| File | Purpose |
|------|---------|
| solution.py | Write your solution |
| test_solution.py | Automated tests |
| hints.md | Progressive hints |
| editorial.md | Explanation |

---

# 🚀 Getting Started

1. Open `solution.py`
2. Implement your solution.
3. Run

```bash
pytest
```

4. Commit your changes

```bash
git add .

git commit -m "feat: solved lc-1768 merge strings alternately"

git push
```

5. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine two queues of people entering a room.

Instead of allowing one queue to finish completely, you allow one person from each queue alternately until everyone has entered.
