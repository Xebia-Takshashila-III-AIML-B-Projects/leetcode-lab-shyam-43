# 🧪 06 - Running Tests

Testing is an essential part of software development.

Professional software engineers do not simply write code and assume it works—they verify it using automated tests.

Throughout this course, every coding challenge includes test cases that help you verify the correctness of your solution before submission.

---

# 🎯 Why Do We Test?

Testing helps us

- Verify that the solution works correctly.
- Catch bugs early.
- Prevent accidental mistakes.
- Ensure future changes do not break existing functionality.
- Build confidence before submitting code.

---

# What is PyTest?

PyTest is one of the most popular testing frameworks in Python.

It allows developers to automatically verify whether their code produces the expected output.

Instead of manually checking every input and output, PyTest performs these checks automatically.

---

# Challenge Structure

A typical challenge contains the following files.

```text
lc-0001-two-sum/

├── README.md
├── starter.py
├── test_solution.py
├── hints.md
├── editorial.md
└── assets/
```

The important files for testing are

- `starter.py`
- `test_solution.py`

---

# Understanding the Files

## starter.py

This is where you write your solution.

Example

```python
class Solution:

    def twoSum(self, nums, target):
        pass
```

---

## test_solution.py

This file contains automated test cases.

Example

```python
from starter import Solution

def test_case_1():
    assert Solution().twoSum([2,7,11,15],9) == [0,1]
```

Do **not** modify this file.

---

# Installing PyTest

If PyTest is not already installed, install it using

```bash
pip install pytest
```

You can also install all required packages using

```bash
pip install -r requirements.txt
```

Verify the installation.

```bash
pytest --version
```

Example output

```text
pytest 8.x.x
```

---

# Running All Tests

Navigate to the repository.

Example

```bash
cd leetcode-lab-lohith-66
```

Run

```bash
pytest
```

or

```bash
python -m pytest
```

PyTest automatically discovers every test file.

---

# Running Tests for a Single Challenge

Navigate to the challenge folder.

Example

```bash
cd challenges/week-01/lc-0001-two-sum
```

Run

```bash
pytest
```

Only the tests inside that folder will be executed.

---

# Expected Output

If every test passes

```text
==========================

3 passed

==========================
```

Congratulations!

Your solution is correct.

---

# When Tests Fail

Example

```text
==========================

1 failed

2 passed

==========================
```

This means one or more test cases failed.

Read the error carefully.

---

# Understanding Test Failures

Example

```text
AssertionError

Expected

[0,1]

Received

None
```

This usually means

- Missing return statement
- Incorrect logic
- Wrong output format

Fix the problem and run the tests again.

---

# Common Errors

## Syntax Error

Example

```text
SyntaxError
```

Cause

A typing mistake.

Example

```python
if x = 10:
```

Correct

```python
if x == 10:
```

---

## NameError

Example

```text
NameError
```

Cause

Using a variable before defining it.

---

## IndentationError

Python uses indentation.

Incorrect

```python
def test():

print("Hello")
```

Correct

```python
def test():

    print("Hello")
```

---

## ModuleNotFoundError

Example

```text
ModuleNotFoundError
```

Possible reasons

- File renamed
- Wrong import
- Missing package

---

# Running a Specific Test

Run one file.

```bash
pytest test_solution.py
```

Run one specific test.

```bash
pytest test_solution.py::test_case_1
```

This is useful when debugging.

---

# Verbose Mode

Run

```bash
pytest -v
```

Example

```text
test_case_1 PASSED

test_case_2 PASSED

test_case_3 FAILED
```

Verbose mode provides more detailed information.

---

# Stopping After the First Failure

Run

```bash
pytest -x
```

PyTest stops immediately after the first failed test.

This helps focus on one problem at a time.

---

# Running Tests with Detailed Output

Run

```bash
pytest -vv
```

Useful for debugging.

---

# Good Testing Workflow

Every time you solve a challenge

```text
Write Code

↓

Save File

↓

Run Tests

↓

Fix Errors

↓

Run Tests Again

↓

Commit

↓

Push

↓

Create Pull Request
```

Never skip testing.

---

# Common Beginner Mistakes

❌ Not saving the file before running tests.

---

❌ Editing the test file instead of fixing the solution.

---

❌ Ignoring failed tests.

---

❌ Renaming

```text
starter.py
```

---

❌ Renaming functions.

---

❌ Deleting provided code.

---

# Best Practices

Always

- Read the error message carefully.
- Fix one problem at a time.
- Run tests frequently.
- Test before committing.
- Ensure every test passes before pushing.

---

# Troubleshooting

## PyTest command not found

Install PyTest.

```bash
pip install pytest
```

---

## No Tests Ran

Possible reasons

- Wrong directory
- Test file renamed
- File does not begin with

```text
test_
```

---

## Import Error

Ensure

- The file names are unchanged.
- The imports match the starter code.
- Required packages are installed.

---

# Testing Checklist

Before submitting

- [ ] Code compiles successfully.
- [ ] No syntax errors.
- [ ] All tests pass.
- [ ] No files renamed.
- [ ] No test files modified.
- [ ] Solution produces expected output.

---

# Professional Tip

Professional software engineers don't test only once.

They write code in small steps and test frequently.

A good habit is

```text
Write a small piece of code

↓

Run tests

↓

Fix problems

↓

Repeat
```

This makes debugging much easier than writing hundreds of lines of code before testing.

---

# 🎉 Congratulations!

You now know how to run automated tests using PyTest, understand test failures, debug common errors, and verify your solutions before submission.

In the next guide, you'll learn how to write clean, readable, and maintainable Python code by following professional coding standards.
