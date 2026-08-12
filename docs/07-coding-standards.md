# 📝 07 - Coding Standards

Writing code that works is important.

Writing code that is **clean, readable, maintainable, and understandable** is even more important.

Professional software engineers spend more time reading code than writing it.

Throughout this course, you are expected to follow these coding standards.

---

# 🎯 Why Coding Standards Matter

Good coding standards help developers

- Read code easily
- Find bugs faster
- Maintain projects efficiently
- Work effectively in teams
- Improve code quality

Imagine reading code written by someone else six months later.

Good coding practices make this much easier.

---

# What is Clean Code?

Clean code is code that is

- Easy to read
- Easy to understand
- Easy to modify
- Well organized
- Properly named
- Free from unnecessary complexity

---

# Python Style Guide (PEP 8)

Python has an official coding style guide called **PEP 8**.

This course follows the PEP 8 recommendations whenever possible.

Reference:

https://peps.python.org/pep-0008/

---

# 1. Use Meaningful Variable Names

Good

```python
numbers = [2, 7, 11, 15]

target = 9

index = 0
```

Bad

```python
a = [2,7,11,15]

x = 9

i = 0
```

Variable names should describe their purpose.

---

# 2. Use Meaningful Function Names

Good

```python
def find_two_sum():
```

Good

```python
def calculate_average():
```

Bad

```python
def abc():
```

Bad

```python
def test():
```

A function name should explain what it does.

---

# 3. Use Proper Indentation

Python uses indentation to define code blocks.

Correct

```python
if number > 0:

    print("Positive")
```

Incorrect

```python
if number > 0:
print("Positive")
```

Always use **4 spaces** for indentation.

Do not mix tabs and spaces.

---

# 4. Keep Functions Small

Each function should perform **one task**.

Good

```python
def calculate_total():
```

Bad

```python
def calculate_total_and_print_and_save_and_upload():
```

One function should solve one problem.

---

# 5. Write Readable Code

Good

```python
total_price = quantity * price
```

Bad

```python
t = q * p
```

Code should be understandable without additional explanation.

---

# 6. Avoid Hardcoding Values

Bad

```python
discount = price * 0.18
```

Better

```python
GST_RATE = 0.18

discount = price * GST_RATE
```

Constants make code easier to update.

---

# 7. Follow Proper Naming Conventions

## Variables

Use

```python
student_name

total_marks

average_score
```

Avoid

```python
StudentName

studentName

student-name
```

Use **snake_case**.

---

## Functions

Use

```python
calculate_total()

find_maximum()

is_palindrome()
```

Use lowercase with underscores.

---

## Classes

Use

```python
Student

Solution

BinaryTree
```

Classes use **PascalCase**.

---

## Constants

Use uppercase.

```python
PI = 3.14159

MAX_SIZE = 100

PASS_MARK = 40
```

---

# 8. Add Comments Only When Necessary

Comments should explain **why**, not **what**.

Good

```python
# Store previously seen values for O(1) lookup
lookup = {}
```

Bad

```python
# Create dictionary
lookup = {}
```

Avoid unnecessary comments.

---

# 9. Remove Unused Code

Do not leave

```python
print()

input()

unused variables

commented-out code
```

Example

Bad

```python
#print(answer)
```

Delete code you no longer need.

---

# 10. Avoid Duplicate Code

Bad

```python
total = a + b

print(total)

total = x + y

print(total)
```

Better

```python
def display_total(a, b):

    print(a + b)
```

Reusable code is easier to maintain.

---

# 11. Keep Lines Short

Avoid very long lines.

Good

```python
result = calculate_average(
    marks,
    attendance,
    assignments
)
```

Long lines are difficult to read.

---

# 12. Handle Edge Cases

Always think about unusual inputs.

Examples

- Empty list
- Single element
- Negative numbers
- Duplicate values
- Very large input

Good programmers test edge cases before submission.

---

# 13. Write Efficient Code

Correct code is important.

Efficient code is even better.

Example

Bad

```python
for i in numbers:

    for j in numbers:

        ...
```

Better

```python
lookup = {}

for value in numbers:

    ...
```

Always think about

- Time Complexity
- Space Complexity

---

# 14. Keep Code Consistent

Use the same naming style throughout your project.

Good

```python
student_name

student_age

student_marks
```

Bad

```python
student_name

StudentAge

studentMarks
```

Consistency improves readability.

---

# 15. Follow Challenge Requirements

Do not

- Rename files
- Rename functions
- Change parameters
- Modify test files

The automated tests depend on the provided structure.

---

# Code Example

Poor Code

```python
a=[2,7,11,15]

for i in range(len(a)):

    for j in range(len(a)):

        if a[i]+a[j]==9:

            print(i,j)
```

Improved Code

```python
class Solution:

    def two_sum(self, numbers, target):

        lookup = {}

        for index, value in enumerate(numbers):

            difference = target - value

            if difference in lookup:

                return [lookup[difference], index]

            lookup[value] = index
```

Notice the improvements

- Better variable names
- Cleaner structure
- Efficient algorithm
- Easier to understand

---

# Submission Checklist

Before submitting your solution

- [ ] Variable names are meaningful.
- [ ] Functions have descriptive names.
- [ ] Code follows PEP 8.
- [ ] Proper indentation is used.
- [ ] No unnecessary comments.
- [ ] No debugging statements.
- [ ] No duplicate code.
- [ ] Edge cases considered.
- [ ] Tests pass successfully.

---

# Professional Tips

Professional developers always ask themselves

- Can someone else understand my code?
- Can this code be simplified?
- Is this the most efficient approach?
- Have I handled edge cases?
- Would I be proud to show this code during a code review?

If the answer is **yes**, your code is likely well written.

---

# Summary

Throughout this course, always strive to write code that is

- Correct
- Readable
- Maintainable
- Efficient
- Consistent
- Professional

Remember:

> **"Code is read far more often than it is written."**

Writing clean code is one of the most valuable skills you can develop as a software engineer.

---

# Next Step

Continue to **08-git-cheat-sheet.md** for a quick reference to the Git commands you'll use throughout the semester.

Happy Coding! 🚀
