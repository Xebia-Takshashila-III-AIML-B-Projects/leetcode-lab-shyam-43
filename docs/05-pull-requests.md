# 🔀 05 - Pull Requests

A Pull Request (PR) is one of the most important parts of modern software development.

Companies like Google, Microsoft, Amazon, Meta, and countless open-source projects use Pull Requests to review code before it becomes part of the main project.

Throughout this course, **every coding challenge must be submitted using a Pull Request**.

---

# 📖 What is a Pull Request?

A Pull Request is a request to merge your code from one branch into another.

Instead of directly changing the `main` branch, you:

1. Create a feature branch.
2. Write your code.
3. Push the branch to GitHub.
4. Create a Pull Request.
5. Wait for review.
6. Merge the Pull Request.

---

# Why Use Pull Requests?

Pull Requests help teams

- Review code before merging
- Find bugs early
- Discuss improvements
- Maintain code quality
- Keep project history clean

Without Pull Requests, mistakes can easily reach the main project.

---

# Pull Request Workflow

```text
Create Feature Branch
        │
        ▼
Write Code
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
        │
        ▼
Code Review
        │
        ▼
Merge
```

---

# Before Creating a Pull Request

Make sure that

- You are **not** on the `main` branch.
- All tests pass.
- Your code is complete.
- Your code follows coding standards.
- Your commit messages are meaningful.

Run

```bash
git status
```

Expected output

```text
On branch feature/lc-0001-two-sum

nothing to commit, working tree clean
```

---

# Step 1 — Push Your Branch

If you haven't already pushed your branch

```bash
git push -u origin feature/lc-0001-two-sum
```

After the first push

```bash
git push
```

is enough.

---

# Step 2 — Open GitHub

Open your repository.

Example

```text
https://github.com/<organization-name>/leetcode-lab-yourname-rollnumber
```

GitHub usually displays a banner saying

```text
feature/lc-0001-two-sum had recent pushes

Compare & pull request
```

Click

```text
Compare & pull request
```

---

# Step 3 — Verify the Branches

Before creating the Pull Request, check the branches carefully.

Base Branch

```text
main
```

Compare Branch

```text
feature/lc-0001-two-sum
```

Never reverse these branches.

Correct

```text
feature

↓

main
```

Incorrect

```text
main

↓

feature
```

---

# Step 4 — Write a Good Title

Choose a short and meaningful title.

Good examples

```text
Solve LC-0001 Two Sum

Implement Valid Palindrome Solution

Complete Week 01 Challenge 02
```

Avoid

```text
Done

Update

Fixed

Assignment
```

---

# Step 5 — Write a Description

A good Pull Request explains what you changed.

Example

```text
## Summary

Implemented the Hash Map approach for LC-0001 Two Sum.

## Changes

- Added solution
- Passed all test cases

## Notes

Time Complexity: O(n)

Space Complexity: O(n)
```

A clear description helps reviewers understand your work quickly.

---

# Step 6 — Create the Pull Request

Click

```text
Create Pull Request
```

Your Pull Request is now ready for review.

---

# Code Review

After creating a Pull Request

Your instructor may

- Approve it
- Request changes
- Leave comments
- Suggest improvements

Code review is a normal part of software development.

Receiving feedback is an opportunity to improve your code.

---

# Making Changes After Review

If your instructor requests changes

Simply edit your code.

Then

```bash
git add .

git commit -m "fix: addressed review comments"

git push
```

You do **not** create another Pull Request.

GitHub automatically updates the existing Pull Request.

---

# Merging the Pull Request

After approval

Click

```text
Merge Pull Request
```

Then

```text
Confirm Merge
```

Your feature branch is now merged into the `main` branch.

---

# Delete the Branch

After merging

Delete the remote branch.

GitHub provides a button

```text
Delete Branch
```

Delete the local branch.

```bash
git checkout main

git branch -d feature/lc-0001-two-sum
```

---

# Update Your Repository

Before starting another challenge

```bash
git pull origin main
```

This downloads the latest version of the project.

---

# Example Pull Request Lifecycle

```text
Create Branch

↓

Write Code

↓

Run Tests

↓

Commit

↓

Push

↓

Open Pull Request

↓

Instructor Reviews

↓

Changes Requested (if needed)

↓

Update Code

↓

Push Again

↓

Approved

↓

Merged

↓

Delete Branch

↓

Repeat
```

---

# Pull Request Best Practices

Always

- Create one Pull Request per challenge.
- Keep Pull Requests small and focused.
- Write meaningful titles.
- Add a clear description.
- Respond politely to review comments.
- Run tests before submitting.

Never

- Open one Pull Request for multiple challenges.
- Commit directly to `main`.
- Ignore review comments.
- Merge without approval (unless instructed).

---

# Common Mistakes

## Pull Request Shows Too Many Files

You may have accidentally worked on the wrong branch.

Check

```bash
git branch
```

---

## Wrong Base Branch

Ensure

```text
Base → main

Compare → feature/...
```

---

## Merge Conflicts

This happens when two branches modify the same lines.

If a conflict occurs

1. Pull the latest changes.
2. Resolve the conflicting code.
3. Save the file.
4. Commit the resolution.
5. Push again.

---

## Accidentally Committed to Main

Do not continue working.

Inform your instructor.

Future work should always be done in a feature branch.

---

# Pull Request Checklist

Before submitting

- [ ] Working on a feature branch
- [ ] Latest changes pulled
- [ ] Solution completed
- [ ] Tests passed
- [ ] Meaningful commit messages
- [ ] Branch pushed to GitHub
- [ ] Pull Request title is clear
- [ ] Description added
- [ ] Ready for review

---

# Professional Tips

A Pull Request should answer three questions:

1. **What problem does this solve?**

2. **How was it solved?**

3. **Has it been tested?**

If a reviewer can answer these three questions quickly, your Pull Request is well written.

---

# 🎉 Congratulations!

You now know how to create, update, review, and merge Pull Requests using a professional GitHub workflow.

This same process is used in many software companies and open-source projects around the world.
