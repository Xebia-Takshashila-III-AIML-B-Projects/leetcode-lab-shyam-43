# 🌿 04 - Git Workflow

Git is one of the most important tools used by software engineers.

Whether you work at a startup or a large technology company, Git is used to track changes, collaborate with teammates, and manage software projects.

This guide explains the Git workflow followed throughout this course.

---

# 📖 What is Git?

Git is a **Version Control System (VCS)**.

A Version Control System keeps track of every change made to your project.

Instead of saving multiple copies like

```text
project-final.py

project-final-final.py

project-final-latest.py

project-final-final-v2.py
```

Git maintains the complete history of your project.

You can always:

- View previous versions
- Restore old code
- Compare changes
- Collaborate with others

---

# Why Do We Use Git?

Git helps developers

- Track project history
- Work on multiple features
- Collaborate safely
- Recover deleted code
- Review changes
- Resolve conflicts

Without Git, teamwork becomes very difficult.

---

# Git Workflow

Every challenge in this course follows the same workflow.

```text
Pull Latest Changes
        │
        ▼
Create Feature Branch
        │
        ▼
Write Code
        │
        ▼
Test Code
        │
        ▼
Stage Changes
        │
        ▼
Commit
        │
        ▼
Push
        │
        ▼
Create Pull Request
        │
        ▼
Merge
```

---

# Step 1 — Check Current Branch

Before starting any work

```bash
git branch
```

Example

```text
* main
```

The `*` indicates your current branch.

---

# Step 2 — Switch to Main

Always begin from the latest main branch.

```bash
git checkout main
```

or

```bash
git switch main
```

---

# Step 3 — Download Latest Changes

Always update your repository before creating a branch.

```bash
git pull origin main
```

Expected output

```text
Already up to date.
```

or

```text
Updating...
```

---

# Step 4 — Create a Feature Branch

Never work directly on the `main` branch.

Create a new feature branch.

```bash
git checkout -b feature/lc-0001-two-sum
```

Verify it.

```bash
git branch
```

Output

```text
* feature/lc-0001-two-sum

main
```

---

# Branch Naming Convention

Use

```text
feature/<challenge-name>
```

Examples

```text
feature/lc-0001-two-sum

feature/lc-0125-valid-palindrome

feature/lc-0242-valid-anagram
```

Use lowercase letters only.

---

# Step 5 — Write Your Code

Open the challenge folder.

Complete the solution.

Save your work.

---

# Step 6 — Check Repository Status

See what has changed.

```bash
git status
```

Example

```text
modified:

starter.py
```

Always verify your changes before committing.

---

# Step 7 — View Changes

Compare your current code with the last commit.

```bash
git diff
```

Git will display every line that has changed.

This helps you review your work before committing.

---

# Step 8 — Stage Your Changes

Tell Git which files should be included.

Stage everything

```bash
git add .
```

Or stage a specific file

```bash
git add starter.py
```

---

# Step 9 — Commit Changes

A commit is a snapshot of your project.

Commit with a meaningful message.

```bash
git commit -m "feat: solved lc-0001 two sum"
```

---

# Writing Good Commit Messages

Use the following format.

```text
type: short description
```

Examples

```text
feat: solved lc-0001 two sum

fix: handled empty input

docs: updated notes

test: added additional test cases

refactor: improved algorithm
```

Avoid

```text
updated

done

code

changes
```

Good commit messages make the project history easier to understand.

---

# Step 10 — Push Your Branch

Upload your work to GitHub.

```bash
git push -u origin feature/lc-0001-two-sum
```

The `-u` option links your local branch with the remote branch.

Future pushes only require

```bash
git push
```

---

# Step 11 — Open GitHub

Navigate to your repository.

GitHub will display

```text
Compare & Pull Request
```

Click it.

---

# Step 12 — Create a Pull Request

Verify

Base Branch

```text
main
```

Compare Branch

```text
feature/lc-0001-two-sum
```

Add

Title

```text
Solve LC-0001 Two Sum
```

Description

```text
Implemented Hash Map solution.

All tests passed.
```

Click

```text
Create Pull Request
```

---

# Step 13 — Merge

Once your Pull Request is approved,

Merge it into

```text
main
```

---

# Step 14 — Delete Feature Branch

After merging

Delete the feature branch from GitHub.

Then locally

```bash
git branch -d feature/lc-0001-two-sum
```

---

# Step 15 — Update Local Repository

Before starting the next challenge

```bash
git checkout main

git pull origin main
```

Then create the next feature branch.

---

# Useful Git Commands

| Command | Purpose |
|----------|----------|
| `git status` | Show modified files |
| `git branch` | List branches |
| `git checkout main` | Switch to main |
| `git switch main` | Alternative to checkout |
| `git checkout -b feature/...` | Create a branch |
| `git add .` | Stage all changes |
| `git add <file>` | Stage one file |
| `git commit -m "message"` | Create commit |
| `git push` | Upload commits |
| `git pull origin main` | Download latest changes |
| `git diff` | Show changes |
| `git log --oneline` | Show commit history |

---

# Common Errors

## Forgot to Create a Branch

Stop working.

Create a new branch.

Commit your work there.

Never continue working on `main`.

---

## Nothing to Commit

Run

```bash
git status
```

Check whether you saved your files.

---

## Authentication Failed

Check

- GitHub login
- Repository permissions
- Personal Access Token (if required)

---

## Merge Conflict

Do not panic.

Read the conflicting lines carefully.

Choose the correct version.

Save the file.

Commit the resolved changes.

---

# Best Practices

✅ Pull before starting work.

✅ Create one feature branch per challenge.

✅ Commit regularly.

✅ Use meaningful commit messages.

✅ Push after every completed challenge.

✅ Never modify the `main` branch directly.

✅ Keep your branch focused on a single task.

---

# Git Workflow Summary

```text
git checkout main

↓

git pull origin main

↓

git checkout -b feature/lc-xxxx-name

↓

Write Code

↓

pytest

↓

git add .

↓

git commit -m "feat: solved challenge"

↓

git push -u origin feature/lc-xxxx-name

↓

Create Pull Request

↓

Merge

↓

Delete Branch

↓

Repeat
```

---

# 🎉 Congratulations!

You now understand the complete Git workflow used throughout this course.

This same workflow is followed in many professional software development teams and will be used for every challenge in LeetCode Lab.
