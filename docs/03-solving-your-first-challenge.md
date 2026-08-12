# 🧩 03 - Solving Your First Challenge

Welcome to your first coding challenge!

This guide explains the complete workflow for solving a challenge—from reading the problem to submitting your solution.

By the end of this guide, you will know how to:

- Understand a coding problem
- Navigate the challenge folder
- Use the provided starter code
- Write your solution
- Test your solution
- Submit your work using Git

---

# 🎯 Challenge Workflow

Every challenge follows the same workflow.

```text
Read Challenge
      │
      ▼
Understand the Problem
      │
      ▼
Create Feature Branch
      │
      ▼
Write Solution
      │
      ▼
Run Tests
      │
      ▼
Commit Changes
      │
      ▼
Push Branch
      │
      ▼
Create Pull Request
```

Always follow this workflow.

---

# 📂 Challenge Structure

Navigate to the challenge folder.

Example

```text
challenges/

└── week-01/

    └── lc-0001-two-sum/
```

Inside every challenge you will find

```text
lc-0001-two-sum/

├── README.md
├── starter.py
├── test_solution.py
├── hints.md
├── editorial.md
└── assets/
```

---

# Step 1 — Read the Problem Statement

Open

```text
README.md
```

Read everything carefully.

Do not start coding immediately.

Understand

- Problem statement
- Input
- Output
- Constraints
- Examples

Example

```text
Input

nums = [2,7,11,15]

target = 9

Output

[0,1]
```

---

# Step 2 — Understand the Problem

Ask yourself the following questions.

- What is the input?
- What is the expected output?
- Are there any constraints?
- Can duplicate values exist?
- Are negative numbers allowed?
- What edge cases should I consider?

Understanding the problem is more important than writing code quickly.

---

# Step 3 — Create a Feature Branch

Never solve a challenge directly on the **main** branch.

Create a new feature branch.

Example

```bash
git checkout main

git pull origin main

git checkout -b feature/lc-0001-two-sum
```

Verify your branch.

```bash
git branch
```

Expected output

```text
* feature/lc-0001-two-sum

main
```

---

# Step 4 — Open the Starter Code

Open

```text
starter.py
```

Example

```python
class Solution:

    def twoSum(self, nums, target):

        pass
```

Do not rename

- Class names
- Function names
- Parameters

Replace only

```python
pass
```

with your solution.

---

# Step 5 — Write Your Solution

Think before you code.

Avoid writing random code until something works.

Instead,

1. Understand the logic.
2. Write pseudocode.
3. Convert it into Python.

Example

```python
class Solution:

    def twoSum(self, nums, target):

        lookup = {}

        for index, value in enumerate(nums):

            difference = target - value

            if difference in lookup:

                return [lookup[difference], index]

            lookup[value] = index
```

---

# Step 6 — Save Your Work

Save the file.

Shortcut

```text
Ctrl + S
```

Always save before running tests.

---

# Step 7 — Run the Tests

Open the terminal.

Run

```bash
pytest
```

or

```bash
python -m pytest
```

Expected output

```text
===================

3 passed

===================
```

Congratulations!

Your solution is correct.

---

# Step 8 — If Tests Fail

Do not panic.

Read the error message carefully.

Example

```text
AssertionError
```

or

```text
Expected [0,1]

Received None
```

Common reasons

- Forgot to return a value
- Incorrect logic
- Wrong variable name
- Syntax error
- Missing edge case

Fix the issue and run the tests again.

---

# Step 9 — Check Your Changes

Before committing, verify which files have changed.

```bash
git status
```

Example

```text
modified:

starter.py
```

Only your solution file should normally appear.

---

# Step 10 — Stage Your Changes

Add your modified files.

```bash
git add .
```

or

```bash
git add starter.py
```

---

# Step 11 — Commit Your Changes

Write a meaningful commit message.

Example

```bash
git commit -m "feat: solved lc-0001 two sum"
```

Good commit messages explain **what** was changed.

---

# Step 12 — Push Your Branch

Upload your changes to GitHub.

```bash
git push -u origin feature/lc-0001-two-sum
```

Once the branch has been pushed, GitHub will display your branch online.

---

# Step 13 — Create a Pull Request

Open your repository on GitHub.

You should see a notification similar to

```text
Compare & pull request
```

Click it.

Verify

Base Branch

```text
main
```

Compare Branch

```text
feature/lc-0001-two-sum
```

Add a clear title.

Example

```text
Solve LC-0001 Two Sum
```

Optionally add a short description of your approach.

Submit the Pull Request.

---

# 💡 Tips for Better Solutions

Before submitting your work, ask yourself:

- Is my solution correct?
- Can it be simplified?
- Are variable names meaningful?
- Have I considered edge cases?
- Does the code follow Python conventions?

Clean code is easier to read, debug, and maintain.

---

# 🚫 Common Mistakes

Avoid these common errors.

❌ Working directly on `main`

Always create a feature branch.

---

❌ Editing `test_solution.py`

Tests should never be modified.

---

❌ Renaming files

Keep the original file names.

---

❌ Renaming functions

The automated tests depend on the original function names.

---

❌ Ignoring failing tests

Always fix the problem before submitting.

---

# 🧠 Engineering Mindset

Professional developers do not measure success by how fast they write code.

Instead, they focus on

- Understanding the problem
- Writing clean code
- Testing thoroughly
- Following the development workflow

This is the mindset you should develop throughout the semester.

---

# ✅ Submission Checklist

Before submitting your challenge, ensure that:

- [ ] You created a feature branch.
- [ ] You read the problem completely.
- [ ] You modified only the required files.
- [ ] Your solution passes all tests.
- [ ] Your code is clean and readable.
- [ ] You committed with a meaningful message.
- [ ] You pushed your branch to GitHub.
- [ ] You created a Pull Request.

---

# 🎉 Congratulations!

You have successfully completed your first challenge using a professional software development workflow.

In the next guide, **04-git-workflow.md**, you will learn Git in greater detail, including branching, merging, pulling updates, resolving conflicts, and best practices used in software development teams.
