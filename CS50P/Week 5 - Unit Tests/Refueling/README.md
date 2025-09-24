# ⛽ REFUELING

## 📌 Task

### Reimplementation
- Reimplement **Fuel Gauge** from **CS50 Python, Pset 3**.  
- Restructure your code into functions:
  - `main`: prompts the user for input and prints output.  
  - `convert`: takes a string in `"X/Y"` format and returns that fraction as an integer percentage rounded to the nearest whole number:
    - Raises `ValueError` if `X` or `Y` is not an integer, or if `X > Y`.  
    - Raises `ZeroDivisionError` if `Y` is `0`.  
  - `gauge`: takes an integer percentage and returns a string:
    - `"E"` if percentage ≤ 1  
    - `"F"` if percentage ≥ 99  
    - `"Z%"` otherwise, where `Z` is the integer percentage.  
- Only `main` should call `print`.  

### Testing
- In a separate file `test_fuel.py`, implement at least two test functions using `pytest`.  
- Tests should thoroughly check `convert` and `gauge` for correctness.  
- Each test function’s name should start with `test_` to be executable by `pytest`.  

---

### ⚙️ Requirements
- Include appropriate import statements (`import fuel` or `from fuel import convert, gauge`) in your test file.  
- Ensure `convert` returns an `int` and `gauge` returns a `str`.  
- Raise exceptions appropriately for invalid inputs in `convert`.  

---

### 💡 Hints
- Only `main` should call `print`.  
- Use `pytest test_fuel.py` to run your tests.  
- You can check exception handling with `pytest.raises`.  
- Test edge cases such as `"1/2"`, `"0/1"`, `"1/0"`, `"5/2"`, and percentages near `1%` and `99%`.  

---

## 💻 Solution
👉 [fuel.py](fuel.py)

🔗 **Official exercise**: [Refueling — CS50 Python, Pset 5](https://cs50.harvard.edu/python/psets/5/fuel/)

