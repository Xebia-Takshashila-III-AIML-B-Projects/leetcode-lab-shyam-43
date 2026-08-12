# 📌 08 - Git Cheat Sheet

This document is a quick reference for the Git commands used throughout the LeetCode Lab.

Keep this page open whenever you're working on a challenge.

---

# Repository Setup

## Clone Your Repository

Downloads the repository from GitHub to your computer.

```bash
git clone https://github.com/<organization-name>/leetcode-lab-yourname-rollnumber.git
```

Example

```bash
git clone https://github.com/xebia-takshila-aiml/leetcode-lab-lohith-66.git
```

---

## Move Into the Repository

```bash
cd leetcode-lab-lohith-66
```

---

# Check Repository Status

See the current status of your repository.

```bash
git status
```

Example Output

```text
On branch main

nothing to commit, working tree clean
```

---

# Branch Commands

## View All Branches

```bash
git branch
```

Example

```text
* main
```

---

## Switch to Main Branch

```bash
git checkout main
```

or

```bash
git switch main
```

---

## Create a New Feature Branch

```bash
git checkout -b feature/lc-0001-two-sum
```

or

```bash
git switch -c feature/lc-0001-two-sum
```

---

## Switch Between Branches

```bash
git checkout feature/lc-0001-two-sum
```

or

```bash
git switch feature/lc-0001-two-sum
```

---

## Delete a Local Branch

```bash
git branch -d feature/lc-0001-two-sum
```

---

# Update Your Repository

Before starting every challenge, update your local repository.

```bash
git checkout main

git pull origin main
```

---

# View Changes

See what has changed since the last commit.

```bash
git diff
```

---

# Stage Changes

## Stage Everything

```bash
git add .
```

---

## Stage One File

```bash
git add starter.py
```

---

# Commit Changes

Save your work as a Git commit.

```bash
git commit -m "feat: solved lc-0001 two sum"
```

---

# Push Changes

First Push

```bash
git push -u origin feature/lc-0001-two-sum
```

Future Pushes

```bash
git push
```

---

# Pull Latest Changes

Download the newest changes from GitHub.

```bash
git pull origin main
```

---

# View Commit History

Compact History

```bash
git log --oneline
```

Detailed History

```bash
git log
```

---

# Show Remote Repository

```bash
git remote -v
```

Example

```text
origin https://github.com/xebia-takshila-aiml/leetcode-lab-lohith-66.git
```

---

# Rename Current Branch

```bash
git branch -m new-branch-name
```

---

# Undo Changes

## Discard Changes in One File

```bash
git restore starter.py
```

---

## Discard All Uncommitted Changes

```bash
git restore .
```

> ⚠️ This permanently removes all uncommitted changes.

---

# Remove a File from Staging

```bash
git restore --staged starter.py
```

---

# Delete a Remote Branch

```bash
git push origin --delete feature/lc-0001-two-sum
```

---

# Fetch Latest Branches

```bash
git fetch
```

---

# Merge a Branch

```bash
git checkout main

git merge feature/lc-0001-two-sum
```

Normally, this will be done through GitHub Pull Requests.

---

# GitHub Workflow

For every challenge, follow this workflow.

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

Open GitHub

↓

Create Pull Request

↓

Merge

↓

Delete Branch
```

---

# Common Git Commands

| Task | Command |
|------|---------|
| Clone Repository | `git clone <url>` |
| Check Status | `git status` |
| List Branches | `git branch` |
| Switch Branch | `git checkout branch-name` |
| Create Branch | `git checkout -b branch-name` |
| Stage All Files | `git add .` |
| Stage One File | `git add filename` |
| Commit | `git commit -m "message"` |
| Push | `git push` |
| Pull | `git pull origin main` |
| Show History | `git log --oneline` |
| Show Changes | `git diff` |
| Restore File | `git restore filename` |
| Delete Branch | `git branch -d branch-name` |
| Show Remote | `git remote -v` |

---

# Commit Message Examples

Good Examples

```text
feat: solved lc-0001 two sum

feat: completed valid palindrome

fix: handled empty input

fix: corrected index error

docs: updated challenge notes

refactor: optimized solution

test: added additional test cases
```

Avoid

```text
done

updated

changes

code

assignment
```

---

# Branch Naming Examples

Correct

```text
feature/lc-0001-two-sum

feature/lc-0125-valid-palindrome

feature/lc-0242-valid-anagram
```

Incorrect

```text
Branch1

MyCode

Test

Solution

Feature
```

---

# Before Every Challenge

```bash
git checkout main

git pull origin main

git checkout -b feature/lc-xxxx-name
```

---

# Before Every Submission

```bash
pytest

git status

git add .

git commit -m "feat: solved challenge"

git push
```

---

# Emergency Commands

See Current Branch

```bash
git branch
```

See Current Status

```bash
git status
```

See Commit History

```bash
git log --oneline
```

Download Latest Changes

```bash
git pull
```

Upload Latest Changes

```bash
git push
```

---

# Student Checklist

Before starting a challenge

- [ ] Pulled the latest changes
- [ ] Created a feature branch
- [ ] Read the challenge

Before submitting

- [ ] All tests passed
- [ ] Code reviewed
- [ ] Changes committed
- [ ] Branch pushed
- [ ] Pull Request created

---

# Quick Workflow Reference

```bash
git checkout main
git pull origin main
git checkout -b feature/lc-0001-two-sum

# Solve the challenge

pytest

git add .
git commit -m "feat: solved lc-0001 two sum"
git push -u origin feature/lc-0001-two-sum
```

---

# 🎉 Congratulations!

You now have a quick reference guide for the Git commands used throughout this course.

Whenever you're unsure about a Git command, return to this document for a quick reminder.
