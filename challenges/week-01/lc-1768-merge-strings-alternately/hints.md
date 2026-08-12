# 💡 Hints - LC-1768: Merge Strings Alternately

Try solving the problem before revealing each hint.

---

# Hint 1

You need to read two strings at the same time.

Can you maintain one position for each string?

---

# Hint 2

Think about using two pointers (indices).

One pointer moves through `word1`.

The other moves through `word2`.

---

# Hint 3

At every step,

append one character from `word1`

followed by

one character from `word2`.

---

# Hint 4

What happens if one string finishes before the other?

The remaining characters should still be added.

---

# Hint 5

Instead of comparing every character,

continue until both strings have been completely processed.

---

# Final Hint

Maintain

- index for word1
- index for word2

Append characters whenever the index is still within the string length.

Good luck! 🚀
