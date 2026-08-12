# 💻 LeetCode Lab

> Enterprise-grade coding challenge platform for Artificial Intelligence & Machine Learning students.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![GitHub](https://img.shields.io/badge/GitHub-Organization-black)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 👋 Welcome

Welcome to **LeetCode Lab**.

This repository is designed to help students become better problem solvers while learning professional software development practices.

Throughout the semester, you will solve coding challenges, improve your programming skills, and gain hands-on experience with Git and GitHub workflows used in the software industry.

Unlike solving problems directly on LeetCode, every challenge in this repository follows a structured engineering workflow.

---

# 🎯 Learning Objectives

By the end of this course, you should be able to:

- Solve algorithmic problems confidently.
- Write clean and maintainable Python code.
- Understand Time Complexity and Space Complexity.
- Use Git professionally.
- Work with GitHub repositories.
- Create feature branches.
- Commit changes using meaningful commit messages.
- Create Pull Requests.
- Read and understand technical documentation.
- Develop an engineering mindset.

---

# 📚 Repository Structure

```text
leetcode-lab/
│
├── .github/
├── challenges/
├── docs/
├── resources/
├── templates/
│
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# 🚀 Quick Start

## 1. Clone Your Repository

```bash
git clone https://github.com/<organization-name>/leetcode-lab-yourname-rollnumber.git
```

Example

```bash
git clone https://github.com/xebia-aiml/leetcode-lab-lohith-66.git
```

Move into the project.

```bash
cd leetcode-lab-lohith-66
```

---

## 2. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 3. Open in Visual Studio Code

```bash
code .
```

---

## 4. Update Your Repository

Before starting every challenge, download the latest changes.

```bash
git checkout main
git pull origin main
```

---

## 5. Create a Feature Branch

Never work directly on the `main` branch.

```bash
git checkout -b feature/lc-0001-two-sum
```

---

## 6. Solve the Challenge

Navigate to the appropriate week's challenge folder.

Example

```text
challenges/
└── week-01/
    └── lc-0001-two-sum/
```

Complete your solution in the provided starter file.

---

## 7. Run Tests

```bash
pytest
```

or

```bash
python -m pytest
```

---

## 8. Commit Your Changes

```bash
git add .

git commit -m "feat: solved lc-0001 two sum"
```

---

## 9. Push Your Branch

```bash
git push -u origin feature/lc-0001-two-sum
```

---

## 10. Create a Pull Request

Open GitHub.

Click

**Compare & Pull Request**

Submit your Pull Request for review.

---

# 📖 Documentation

If you are new to Git or GitHub, read the documentation in the following order.

| Guide | Description |
|--------|-------------|
| `docs/01-getting-started.md` | Install Python, Git, VS Code and clone your repository |
| `docs/02-repository-structure.md` | Understand every folder and file |
| `docs/03-solving-your-first-challenge.md` | Learn how to solve your first coding challenge |
| `docs/04-git-workflow.md` | Complete Git workflow explained step by step |
| `docs/05-pull-requests.md` | Creating and managing Pull Requests |
| `docs/06-running-tests.md` | Running unit tests |
| `docs/07-coding-standards.md` | Clean code and best practices |
| `docs/08-faq.md` | Frequently Asked Questions |
| `docs/09-git-cheat-sheet.md` | Quick Git reference |

---

# 📁 Student Repository Naming Convention

Every student maintains one personal repository.

Format

```text
leetcode-lab-<studentname>-<rollnumber>
```

Example

```text
leetcode-lab-lohith-66

leetcode-lab-arun-01

leetcode-lab-priya-12
```

Repository names must:

- Use lowercase letters only.
- Use hyphens (`-`) as separators.
- Not contain spaces.
- Not contain special characters.

---

# 🌿 Branch Naming Convention

Create one feature branch for every coding challenge.

Format

```text
feature/lc-0001-two-sum
```

Examples

```text
feature/lc-0001-two-sum

feature/lc-0125-valid-palindrome

feature/lc-0242-valid-anagram
```

---

# 📝 Commit Message Convention

Use meaningful commit messages.

Examples

```text
feat: solved lc-0001 two sum

fix: handled empty input

refactor: improved solution

docs: updated notes

test: added edge case tests
```

---

# 📜 Repository Rules

- Never commit directly to the `main` branch.
- Create a feature branch for every challenge.
- Pull the latest changes before starting work.
- Run all tests before pushing.
- Keep commits small and meaningful.
- Use descriptive commit messages.
- Create a Pull Request for every completed challenge.
- Follow the coding standards provided in the documentation.

---

# 🤝 Need Help?

If you encounter any issues:

1. Read the relevant guide in the `docs/` folder.
2. Review the challenge README carefully.
3. Check the Frequently Asked Questions.
4. Contact your instructor if the issue persists.

---

# 🚀 Happy Coding!

Remember the workflow:

```text
Read Problem
      │
      ▼
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
Merge
      │
      ▼
Repeat
```

> **"Great software engineers don't just write code—they write clean code, collaborate effectively, and continuously improve."**
