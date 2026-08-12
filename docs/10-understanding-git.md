# 🧠 10 - Understanding Git

Most beginners memorize Git commands.

Professional software engineers understand **what Git is doing behind the scenes**.

Once you understand Git, it becomes much easier to solve problems, recover mistakes, and collaborate with others.

---

# 🎯 Learning Objectives

After reading this guide, you will understand

- What Git is
- What a Repository is
- What a Commit is
- What a Branch is
- What HEAD means
- What Origin means
- What Staging is
- What happens when you run Git commands

---

# What is Git?

Git is a **Distributed Version Control System (DVCS)**.

It records every change made to your project.

Instead of creating multiple copies like

```text
Project Final.py

Project Final 2.py

Project Latest.py

Project Final Final.py
```

Git stores the complete history of your project.

---

# What is a Repository?

A Repository (Repo) is simply a project managed by Git.

Example

```text
leetcode-lab-lohith-66/
```

Everything inside this folder is tracked by Git.

Repositories contain

- Files
- Folders
- Commit history
- Branches

---

# Local Repository vs Remote Repository

There are two copies of your project.

## Local Repository

Stored on your computer.

Example

```text
C:\Users\Lohith\Documents\leetcode-lab-lohith-66
```

---

## Remote Repository

Stored on GitHub.

Example

```text
github.com/xebia-takshila-aiml/leetcode-lab-lohith-66
```

Git keeps these two repositories synchronized.

---

# Understanding the Git Workflow

```text
Your Computer

↓

Local Repository

↓

GitHub Repository
```

Whenever you code

You modify files on your computer first.

---

# What is a Commit?

A Commit is a snapshot of your project.

Imagine saving checkpoints while playing a game.

```text
Checkpoint 1

↓

Checkpoint 2

↓

Checkpoint 3
```

Git commits work the same way.

Every commit records

- Changed files
- Author
- Date
- Commit message

---

# Commit History

Example

```text
A

↓

B

↓

C

↓

D
```

Each letter represents a commit.

Git allows you to return to any previous commit if needed.

---

# What is a Branch?

A Branch is an independent line of development.

Instead of modifying the main project directly

You create another branch.

Example

```text
main

│

├──────────────► feature/lc-0001-two-sum
```

You can safely experiment without affecting the main project.

---

# Why Do We Use Branches?

Imagine five developers working together.

Without branches

Everyone edits the same files.

Chaos.

With branches

Everyone works independently.

Later

Their work is merged together.

---

# What is HEAD?

HEAD points to the branch you are currently working on.

Example

```text
HEAD

↓

feature/lc-0001-two-sum
```

When you switch branches

HEAD moves.

Example

```bash
git checkout main
```

Now

```text
HEAD

↓

main
```

---

# What is Origin?

Origin is simply the default name for the remote repository.

Example

```bash
git push origin main
```

Means

Push the main branch to GitHub.

---

# What is Staging?

Git does not automatically commit every file.

Instead

Git has a staging area.

```text
Working Directory

↓

Staging Area

↓

Commit
```

---

# What Happens When You Run git add?

Suppose you modify

```text
starter.py
```

Git knows it changed.

But it is not yet ready for a commit.

Running

```bash
git add starter.py
```

moves it into the staging area.

---

# What Happens When You Run git commit?

Running

```bash
git commit -m "feat: solved challenge"
```

creates a permanent snapshot.

That snapshot is stored inside your local repository.

---

# What Happens When You Run git push?

A commit only exists on your computer.

Running

```bash
git push
```

uploads those commits to GitHub.

```text
Local Repository

↓

GitHub Repository
```

---

# What Happens When You Run git pull?

Suppose your instructor updates the repository.

Those changes exist only on GitHub.

Running

```bash
git pull origin main
```

downloads those changes to your computer.

---

# What Happens When You Clone?

```bash
git clone
```

downloads

- Files
- Branches
- Commit history

from GitHub.

You now have a complete copy of the project.

---

# Visualizing Git

```text
GitHub Repository

↓

Clone

↓

Your Local Repository

↓

Edit Files

↓

git add

↓

git commit

↓

git push

↓

GitHub Updated
```

---

# The Three States of Git

Every file exists in one of three states.

```text
Working Directory

↓

Staging Area

↓

Repository
```

Working Directory

You edit files.

↓

Staging Area

Git prepares files.

↓

Repository

Git permanently saves the snapshot.

---

# Common Git Commands Explained

| Command | What It Actually Does |
|----------|----------------------|
| git clone | Downloads an entire repository |
| git status | Shows changed files |
| git add | Moves files into staging |
| git commit | Creates a snapshot |
| git push | Uploads commits to GitHub |
| git pull | Downloads new commits |
| git checkout | Switches branches |
| git branch | Lists branches |
| git merge | Combines branches |

---

# Summary

Git is not just a collection of commands.

It is a system for tracking and managing changes to software projects.

Understanding how Git works will make you a more confident developer and help you collaborate effectively in real-world software teams.

---

# 🎉 Congratulations!

You now understand the core concepts behind Git, including repositories, commits, branches, HEAD, origin, staging, and how your local repository communicates with GitHub.

From this point onward, you'll be using Git not just by memorizing commands, but by understanding what each command does behind the scenes.
