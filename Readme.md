# Garden Guardian — Data Engineering for Smart Agriculture

*This activity has been created as part of the 42 curriculum by <your_login>.*

---

## What is this?

Garden Guardian is a Python exception handling project built around smart agriculture scenarios. You build resilient data pipelines that don't crash when things go wrong — bad sensor readings, invalid inputs, missing files, or resource leaks.

This is the third project in the garden series, following Growing Code (functions) and Code Cultivation (OOP).

---

## What you will learn

- How to catch errors with `try / except` without crashing the program
- How to raise your own exceptions with `raise`
- How to handle different error types separately (`ValueError`, `TypeError`, `FileNotFoundError`, etc.)
- How to create custom exception classes with inheritance
- How to use `finally` to always clean up resources, even after an error

---

## Project structure

```
ex0/    ft_first_exception.py      → first try/except, catching basic errors
ex1/    ft_raise_exception.py      → raising exceptions with validation logic
ex2/    ft_different_errors.py     → handling multiple exception types
ex3/    ft_custom_errors.py        → custom exceptions (GardenError, PlantError, WaterError)
ex4/    ft_finally_block.py        → try/except/finally and resource cleanup
```

---

## How to run

```bash
# Run a specific exercise
python3 ex0/ft_first_exception.py

# Check code style (required)
flake8 ex0/ft_first_exception.py

# Check type hints (required)
mypy ex0/ft_first_exception.py
```

**Requirements:** Python 3.10+, flake8, mypy

---

## Resources

- [Python Exceptions — Official Docs](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exception Types](https://docs.python.org/3/library/exceptions.html)
- [Real Python — Exception Handling](https://realpython.com/python-exceptions/)
- [flake8](https://flake8.pycqa.org/) / [mypy](https://mypy.readthedocs.io/)
