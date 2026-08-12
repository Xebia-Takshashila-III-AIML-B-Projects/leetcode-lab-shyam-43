# ❓ 09 - Frequently Asked Questions (FAQ)

Welcome to the Frequently Asked Questions (FAQ) section.

This guide contains answers to the most common questions students ask while working on LeetCode Lab.

Before contacting your instructor, check whether your question has already been answered here.

---

# 📚 Repository Questions

## 1. Why does every student have their own repository?

Each student works in their own repository so that

- Your work is independent.
- Your progress can be tracked.
- Your commits belong to you.
- The automation system can evaluate your submissions.
- Other students cannot accidentally modify your work.

---

## 2. Why can't I work directly on the main branch?

The **main** branch represents the stable version of your repository.

Professional software teams never develop new features directly on the main branch.

Instead, they create a feature branch.

Example

```text
main

↓

feature/lc-0001-two-sum
```

After review, the feature branch is merged into the main branch.

---

## 3. Why do I need a Pull Request?

Pull Requests allow

- Code review
- Discussion
- Feedback
- Better code quality

Even if you're working alone, using Pull Requests helps build good software engineering habits.

---

## Git Questions

## 4. I forgot to create a feature branch. What should I do?

Stop making further changes.

Create a feature branch immediately.

```bash
git checkout -b feature/lc-0001-two-sum
```

Continue working from the new branch.

---

## 5. I accidentally committed to the main branch.

Don't panic.

If you haven't pushed your changes yet, contact your instructor before continuing.

Avoid making more commits on the main branch.

---

## 6. Why does Git say "nothing to commit"?

Possible reasons

- You forgot to save your file.
- No changes were made.
- The file was not modified.

Check

```bash
git status
```

---

## 7. Why does Git ask me to pull first?

Someone has pushed new changes to GitHub.

Download them first.

```bash
git pull origin main
```

Then continue working.

---

## 8. What is a merge conflict?

A merge conflict occurs when Git cannot automatically combine two versions of the same file.

Read the conflicting code carefully.

Choose the correct version.

Save the file.

Commit the resolved changes.

---

## 9. What does "origin" mean?

`origin` is the default name of the remote repository on GitHub.

Example

```bash
git push origin main
```

means

Push the `main` branch to GitHub.

---

## 10. What does HEAD mean?

HEAD points to the branch or commit you are currently working on.

Example

```text
HEAD -> feature/lc-0001-two-sum
```

means you are currently on that feature branch.

---

# Challenge Questions

## 11. Which files should I edit?

Normally

```text
starter.py
```

or any file specifically mentioned in the challenge instructions.

---

## 12. Which files should I never edit?

Never modify

```text
README.md

test_solution.py

editorial.md

templates/

.github/
```

unless your instructor specifically tells you to do so.

---

## 13. Can I rename files?

No.

The automation system expects the original file names.

Renaming files may cause your submission to fail.

---

## 14. Can I rename functions?

No.

The automated tests depend on the provided function names.

---

## 15. Can I delete starter code?

Only replace

```python
pass
```

with your implementation.

Do not remove the provided class or function unless instructed.

---

# Testing Questions

## 16. PyTest is not recognized.

Install PyTest.

```bash
pip install pytest
```

Verify installation.

```bash
pytest --version
```

---

## 17. Why do my tests fail?

Common reasons

- Incorrect logic
- Missing return statement
- Syntax error
- Wrong output format
- Edge cases not handled

Read the error message carefully.

---

## 18. Can I edit the test file?

No.

Fix your solution instead.

The test files are maintained by the instructor.

---

## GitHub Questions

## 19. I cannot push my code.

Check

- Internet connection
- Repository permissions
- GitHub login
- Personal Access Token (if required)

---

## 20. I accidentally deleted my branch.

If it was merged, you can simply create a new feature branch for the next challenge.

If it was not merged, contact your instructor.

---

## 21. I cannot see my repository.

Possible reasons

- You haven't accepted the organization invitation.
- You are logged into the wrong GitHub account.
- You don't have permission.

---

## 22. My Pull Request shows many unrelated files.

You probably worked on the wrong branch.

Check

```bash
git branch
```

---

## 23. I pushed the wrong code.

Fix the code.

Commit again.

```bash
git add .

git commit -m "fix: corrected solution"

git push
```

The Pull Request will update automatically.

---

# Python Questions

## 24. Should I use AI to solve the problems?

AI can help you understand concepts, but you should first attempt the challenge yourself.

The goal is to develop your own problem-solving skills.

---

## 25. Can I copy solutions from the internet?

No.

The purpose of LeetCode Lab is learning, not just completing challenges.

Submitting copied solutions defeats the purpose of the course.

---

## 26. My solution works but looks different from others.

That's perfectly fine.

There can be multiple correct solutions to the same problem.

---

## Best Practices

Before asking for help

1. Read the challenge README.
2. Read the error message.
3. Run the tests again.
4. Check this FAQ.
5. Search the documentation.
6. Ask your instructor if you're still stuck.

---

# Useful Commands

Check status

```bash
git status
```

Current branch

```bash
git branch
```

Pull latest changes

```bash
git pull origin main
```

Push changes

```bash
git push
```

Run tests

```bash
pytest
```

---

# Need More Help?

If your issue is still not resolved,

Please include the following information when asking your instructor for help:

- Challenge name
- Error message
- Screenshot (if applicable)
- Steps you have already tried
- Git command you executed
- Terminal output

Providing complete information helps others diagnose the issue more quickly.

---

# 🎉 Final Note

Learning Git, GitHub, and software development takes practice.

Making mistakes is a normal part of the learning process.

Read the documentation, experiment with the tools, ask questions, and keep practicing.

Every challenge you complete will make you a more confident software developer.

Happy Coding! 🚀
