# 💡 Hints - LC-0053: Maximum Subarray

Reveal one hint at a time.

---

# Hint 1

The answer is always a **contiguous** subarray.

You cannot skip elements.

---

# Hint 2

Suppose you already know the best subarray ending at the previous element.

Can this help you decide the best subarray ending at the current element?

---

# Hint 3

At every position, compare two choices.

- Continue the current subarray.
- Start a new subarray.

---

# Hint 4

Maintain two values while traversing.

- Current Subarray Sum
- Best Sum Found So Far

---

# Hint 5

Whenever the current sum becomes worse than starting fresh,

begin a new subarray.

---

# Final Hint

Each element is processed exactly once.

The algorithm continuously updates the best answer while moving through the array.

Good luck! 🚀
