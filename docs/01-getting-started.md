# 🚀 01 - Getting Started

Welcome to **LeetCode Lab**!

This guide will help you set up your development environment so you're ready to solve coding challenges throughout the semester.

If this is your first time using Git or GitHub, don't worry. Follow each step carefully, and you'll be ready to start coding.

---

# 📋 Prerequisites

Before you begin, make sure you have the following:

- A computer running Windows, macOS, or Linux
- An internet connection
- A GitHub account
- Permission to join the course GitHub Organization

---

# 🛠 Required Software

Install the following software before continuing.

| Software | Purpose |
|----------|---------|
| Python 3.11 or above | Programming Language |
| Git | Version Control System |
| Git Bash | Command Line Interface |
| Visual Studio Code | Code Editor |
| GitHub Account | Repository Hosting |

---

# Step 1 — Create a GitHub Account

If you already have a GitHub account, you can skip this step.

1. Visit https://github.com
2. Click **Sign Up**
3. Create your account
4. Verify your email address

Choose a professional username because it will be visible throughout the semester.

Example:

```
john-doe

arunkumar

lohith66
```

Avoid usernames like

```
coolboy123

killer007

dragonking
```

---

# Step 2 — Join the GitHub Organization

Your instructor will invite you to the GitHub Organization.

After receiving the invitation:

1. Log in to GitHub.
2. Open the invitation.
3. Click **Accept Invitation**.

Once accepted, you should be able to see the organization on your GitHub profile.

---

# Step 3 — Install Python

Download Python from

https://www.python.org/downloads/

During installation, make sure you enable

✅ Add Python to PATH

After installation, verify it.

Open **Git Bash**

Run

```bash
python --version
```

Expected output

```text
Python 3.11.x
```

If Python is not recognized, restart your computer and try again.

---

# Step 4 — Install Git

Download Git from

https://git-scm.com/downloads

Install using the default settings.

After installation, open Git Bash.

Run

```bash
git --version
```

Expected output

```text
git version 2.xx.x
```

---

# Step 5 — Install Visual Studio Code

Download Visual Studio Code from

https://code.visualstudio.com/

Install it using the default settings.

After installation, open Visual Studio Code once to complete the initial setup.

---

# Step 6 — Configure Git (First Time Only)

Git needs to know who you are before you start making commits.

Run

```bash
git config --global user.name "Your Name"
```

Example

```bash
git config --global user.name "Lohith"
```

Now configure your email.

```bash
git config --global user.email "your-email@example.com"
```

Use the same email address that is linked to your GitHub account.

Verify the configuration.

```bash
git config --list
```

You should see

```text
user.name=Your Name
user.email=your-email@example.com
```

---

# Step 7 — Create Your Personal Repository

Each student maintains one personal repository.

Repository naming format

```text
leetcode-lab-<studentname>-<rollnumber>
```

Examples

```text
leetcode-lab-lohith-66

leetcode-lab-arun-01

leetcode-lab-priya-12
```

Repository names must

- Use lowercase letters
- Use hyphens (`-`)
- Not contain spaces
- Not contain special characters

---

# Step 8 — Clone Your Repository

Open **Git Bash**.

Navigate to the folder where you want to save your repository.

Example

```bash
cd Documents
```

Clone your repository.

```bash
git clone https://github.com/<organization-name>/leetcode-lab-lohith-66.git
```

Move into the repository.

```bash
cd leetcode-lab-lohith-66
```

---

# Step 9 — Open the Repository in Visual Studio Code

Inside Git Bash, run

```bash
code .
```

If the command doesn't work

Open Visual Studio Code manually.

Select

```
File → Open Folder
```

Choose your repository folder.

---

# Step 10 — Install Project Dependencies

Some challenges may require additional Python packages.

Install them using

```bash
pip install -r requirements.txt
```

This command installs every package required by the project.

---

# Step 11 — Verify Everything

Run

```bash
python --version
```

```bash
git --version
```

```bash
git status
```

Expected output

```text
On branch main

Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

If you see the above message, your setup is complete.

---

# Common Issues

## Python is not recognized

Make sure Python was added to PATH during installation.

Restart your computer if necessary.

---

## Git is not recognized

Reinstall Git and use the default installation options.

Restart your terminal.

---

## code command not found

Open Visual Studio Code.

Press

```
Ctrl + Shift + P
```

Search for

```
Shell Command: Install 'code' command in PATH
```

Restart Git Bash.

---

## Authentication Failed While Cloning

Ensure

- You are logged in to GitHub.
- You have accepted the organization invitation.
- You are cloning the correct repository.
- You have permission to access the repository.

---

# Checklist

Before moving to the next guide, ensure you have completed all of the following.

- [ ] GitHub account created
- [ ] Joined the GitHub Organization
- [ ] Installed Python
- [ ] Installed Git
- [ ] Installed Visual Studio Code
- [ ] Configured Git username
- [ ] Configured Git email
- [ ] Cloned your personal repository
- [ ] Opened the repository in Visual Studio Code
- [ ] Installed project dependencies
- [ ] Verified your setup

---

# Next Step

Continue to

**02-repository-structure.md**

In the next guide, you'll learn:

- What every folder does
- Which files you should edit
- Which files you should never modify
- How the repository is organized
- How new challenges are released

Happy Coding! 🚀
