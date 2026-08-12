# Challenge Template

This directory contains the standard template used for every LeetCode Lab challenge.

All challenges should follow this structure to ensure consistency, automated validation, and maintainability.

---

## Directory Structure

```
challenge/
├── README_TEMPLATE.md
├── editorial.md
├── hints.md
├── notes.md
├── solution.py
└── test_solution.py
```

---

## Files

### README_TEMPLATE.md

Provides an overview of the challenge template and folder structure.

This file should remain unchanged unless the template itself is updated.

---

### editorial.md

Contains the official editorial for the challenge.

Typical contents include:

- Problem intuition
- Approach
- Algorithm
- Complexity Analysis
- Reference explanation

This document is intended for instructors or students after attempting the challenge.

---

### hints.md

Contains progressive hints.

Recommended format:

- Hint 1 (very small clue)
- Hint 2 (approach)
- Hint 3 (algorithm)
- Hint 4 (edge cases)

Avoid revealing the complete solution immediately.

---

### notes.md

Contains additional learning material such as:

- Common mistakes
- Edge cases
- Interview tips
- Alternative approaches
- Related LeetCode problems
- Important observations

---

### solution.py

Reference implementation.

It should include:

- Problem ID
- Function signature
- Time Complexity
- Space Complexity
- Clean, well-documented code

Students replace the template implementation with their solution.

---

### test_solution.py

PyTest-based automated validation.

Responsibilities:

- Validate correctness
- Test edge cases
- Verify return types
- Ensure expected behavior

Every challenge should contain comprehensive and deterministic test cases.

---

## Challenge Creation Checklist

When creating a new challenge:

- Copy this template.
- Rename the folder using the challenge naming convention.
- Update the problem statement.
- Write the editorial.
- Add progressive hints.
- Include additional notes if necessary.
- Implement the reference solution.
- Write comprehensive PyTest test cases.
- Verify that all tests pass locally before committing.

---

## Naming Convention

Use the following format for challenge directories:

```
lc-<problem-number>-<problem-name>
```

Examples:

```
lc-0001-two-sum
lc-0053-maximum-subarray
lc-0070-climbing-stairs
lc-0146-lru-cache
```

---

## Validation

GitHub Actions automatically validates challenges.

The workflow:

1. Detects modified challenge folders.
2. Executes only the corresponding `test_solution.py`.
3. Reports pass/fail status.
4. Prevents invalid solutions from being merged.

---

## Best Practices

- Follow PEP 8.
- Keep solutions readable.
- Write deterministic tests.
- Cover edge cases.
- Document time and space complexity.
- Keep the template structure unchanged.

---

Maintaining a consistent template ensures every challenge behaves predictably and integrates seamlessly with the automated validation pipeline.
