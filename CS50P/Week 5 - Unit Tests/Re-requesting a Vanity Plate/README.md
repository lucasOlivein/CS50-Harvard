# 🚗 RE-REQUESTING A VANITY PLATE

## 📌 Task

### Reimplementation
- Reimplement **Vanity Plates** from **CS50 Python, Pset 2**.  
- Restructure your code into functions:
  - `main`: prompts the user for input and prints output.  
  - `is_valid`: takes a string as input and returns `True` if the string meets all license plate requirements and `False` otherwise.  
- Only `main` should call `print`.  

### Testing
- In a separate file `test_plates.py`, implement four or more test functions to thoroughly test `is_valid`.  
- Each test function’s name should start with `test_` to be executed by `pytest`.  
- Include at the top of `test_plates.py`:

    import plates

or

    from plates import is_valid

- Ensure `is_valid` **returns** a boolean and does not `print`.  

---

### ⚙️ Requirements
- Implement `main()` and `is_valid(s)` in your program.  
- Use `pytest` for testing and ensure test function names start with `test_`.  
- Include proper imports in the test file.  

---

### 💡 Hints
- Only `main` should call `print`.  
- Test a variety of valid and invalid license plate strings.  
- Use `pytest test_plates.py` to run your tests.  

---

## 💻 Solution
👉 [plates.py](plates.py)


🔗 **Official exercise**: [Re-requesting a Vanity Plate — CS50 Python, Pset 5](https://cs50.harvard.edu/python/psets/5/test_plates/)  


