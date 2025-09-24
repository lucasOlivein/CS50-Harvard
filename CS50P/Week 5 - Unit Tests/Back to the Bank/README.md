# 🏦 BACK TO THE BANK

## 📌 Task

### Reimplementation
- Reimplement **Home Federal Savings Bank** from **CS50 Python, Pset 1**.  
- Restructure your code into functions:
  - `main`: prompts the user for input and prints output.  
  - `value`: takes a greeting as input and returns an integer:
    - `0` if the greeting starts with `"hello"` (case-insensitive)  
    - `20` if the greeting starts with `"h"` but not `"hello"`  
    - `100` otherwise  
- You may assume that the string passed to the `value` function will not contain any leading spaces.  
- Only `main` should call `print`.  

### Testing
- In a separate file `test_bank.py`, implement at least three test functions using `pytest`.  
- Each test should call `value()` to verify correctness.  
- Ensure tests cover:
  - Greetings starting with `"hello"`  
  - Greetings starting with `"h"` but not `"hello"`  
  - Other greetings  
- Tests should raise exceptions for invalid inputs if applicable.  

---

### ⚙️ Requirements
- Implement `main()` and `value(greeting)` in your program.  
- Use `pytest` for testing and ensure tests are properly named with the `test_` prefix.  
- Include any necessary import statements in the test file.  

---

### 💡 Hints
- Keep functions small and focused: `main` handles I/O, `value` handles logic.  
- Use `pytest test_bank.py` to run your tests.  
- Test edge cases like `"Hello"`, `"hey"`, `"good morning"`.  

---

## 💻 Solution
👉 [bank.py](bank.py)

🔗 **Official exercise**: [Back to the Bank — CS50 Python, Pset 5](https://cs50.harvard.edu/python/psets/5/bank/)

