# LC-0020: Valid Parentheses

**Difficulty:** 🟢 Easy

**Week:** 01

**Day:** 02 (Section B)

**Topic:** Stack

**Related Course Topic:** Teaching Machines to Remember

---

# 🎯 Learning Objective

In this challenge, you will learn how to use a **Stack** to keep track of previously encountered information.

A stack allows you to temporarily store data and retrieve it in the reverse order in which it was added. This makes it ideal for problems involving matching symbols, nested structures, and sequential validation.

---

# 📚 Course Connection

Today's lecture introduced the importance of memory in sequential processing.

Just as a Recurrent Neural Network (RNN) remembers information from previous time steps, a stack remembers previously encountered opening brackets while processing a sequence.

Every closing bracket depends on information stored earlier in the sequence.

---

# 📝 Problem Statement

Given a string `s` containing only the characters

- `(`
- `)`
- `{`
- `}`
- `[`
- `]`

Determine whether the input string is valid.

A string is valid if:

- Every opening bracket has a matching closing bracket.
- Brackets close in the correct order.
- Every closing bracket matches the most recent unmatched opening bracket.

Return `True` if the string is valid; otherwise return `False`.

---

# Example 1

Input

```text
s = "()"
```

Output

```text
True
```

---

# Example 2

Input

```text
s = "()[]{}"
```

Output

```text
True
```

---

# Example 3

Input

```text
s = "(]"
```

Output

```text
False
```

---

# Example 4

Input

```text
s = "([)]"
```

Output

```text
False
```

---

# Example 5

Input

```text
s = "{[]}"
```

Output

```text
True
```

---

# Constraints

- 1 ≤ s.length ≤ 10⁴
- `s` contains only brackets.

---

# 💡 Hint

When you encounter an opening bracket,

where should you store it until you find its matching closing bracket?

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

git commit -m "feat: solved lc-0020 valid parentheses"

git push
```

6. Create a Pull Request.

---

# 🧠 Think Like an Engineer

Imagine checking whether every opening door has been closed correctly before leaving a building.

Whenever you open a new door, you remember it.

When closing a door, it must always be the most recently opened one.

This is exactly how a stack works.
