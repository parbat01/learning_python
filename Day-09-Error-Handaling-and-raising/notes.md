# Day 9 — Error Handling & Virtual Environments 🐍

## What I Learned

### Error Handling

* `try` — contains code that may cause an error.
* `except` — handles errors without crashing the program.
* `finally` — runs whether an error occurs or not.
* `raise` — manually raises an exception when a condition is invalid.

### Example

```python
try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

except ValueError as e:
    print(e)

finally:
    print("Program finished.")
```

## Day 9 Project 🎮

Built a **Quiz Game** using:

* `try` / `except`
* `raise`
* `match-case`
* Lists
* Loops
* Conditions
* String methods
* User input
* Score tracking

### Key Takeaway

> Errors are not just problems to avoid — Python gives us tools to handle them properly and make our programs more reliable.
