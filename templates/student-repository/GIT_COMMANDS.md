# Git Bash Quick Reference

This document contains the Git commands used throughout the LeetCode Lab.

---

# Clone Repository

```bash
git clone <repository-url>
```

---

# Move into Repository

```bash
cd leetcode-lab-<register-number>
```

---

# Check Status

```bash
git status
```

---

# Check Current Branch

```bash
git branch
```

---

# Create a Feature Branch

```bash
git checkout -b feature/lc-0001-two-sum
```

---

# Stage Changes

```bash
git add .
```

---

# Commit Changes

```bash
git commit -m "feat: solved lc-0001 two sum"
```

---

# Push Branch

```bash
git push origin feature/lc-0001-two-sum
```

---

# Create Pull Request

Open your repository on GitHub and create a Pull Request from your feature branch into `main`.

---

# Switch to Main Branch

```bash
git checkout main
```

---

# Pull Latest Changes

```bash
git pull origin main
```

---

# Delete Local Branch

```bash
git branch -d feature/lc-0001-two-sum
```

---

# Delete Remote Branch

```bash
git push origin --delete feature/lc-0001-two-sum
```

---

# Daily Workflow

```text
Receive Challenge
        │
        ▼
Create Feature Branch
        │
        ▼
Write Solution
        │
        ▼
Test Solution
        │
        ▼
git add .
        │
        ▼
git commit
        │
        ▼
git push
        │
        ▼
Create Pull Request
        │
        ▼
Merge
        │
        ▼
git checkout main
        │
        ▼
git pull
```

---

# Best Practices

- Create a new branch for every challenge.
- Write meaningful commit messages.
- Pull the latest changes before starting a new challenge.
- Keep commits small and focused.
- Never push unfinished code to `main`.
- Test your solution before creating a Pull Request.
