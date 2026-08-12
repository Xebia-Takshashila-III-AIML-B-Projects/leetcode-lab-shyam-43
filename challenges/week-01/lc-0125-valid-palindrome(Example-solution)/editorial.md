# Editorial

## Intuition

Only alphanumeric characters contribute to determining whether the string is a palindrome.

Instead of creating a new filtered string, two pointers can skip invalid characters while comparing the remaining characters.

---

## Algorithm

1. Initialize two pointers:
   - `left` at the beginning.
   - `right` at the end.

2. Skip non-alphanumeric characters.

3. Compare characters after converting them to lowercase.

4. If the characters differ, return `False`.

5. Move both pointers inward.

6. Continue until the pointers meet.

---

## Correctness

The algorithm compares every valid character from both ends exactly once while ignoring irrelevant characters.

If every comparison matches, the cleaned string reads the same forwards and backwards.

---

## Complexity Analysis

| Metric | Complexity |
|---------|------------|
| Time | O(n) |
| Space | O(1) |

---

## Key Concepts

- Two Pointers
- String Traversal
- Character Filtering
- Constant Extra Space
