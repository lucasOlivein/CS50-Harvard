## 📌 Task
Reimplement the **Fuel Gauge** problem from Problem Set 3, but this time organize the logic into functions:

- In `fuel.py`:
  - `convert(fraction: str) -> int`  
    - Takes a string in the form `"X/Y"`.  
    - Returns the fraction as an integer **percentage (0–100)**, rounded to the nearest integer.  
    - Raise `ValueError` if X or Y are not integers or if X > Y.  
    - Raise `ZeroDivisionError` if Y is 0.  

  - `gauge(percentage: int) -> str`  
    - Return `"E"` if percentage ≤ 1.  
    - Return `"F"` if percentage ≥ 99.  
    - Otherwise, return `"N%"`.  

- In `test_fuel.py`:
  - Implement at least **two test functions** (`test_...`) that test `convert` and `gauge`.  
  - Use `pytest` to validate correct behavior and exceptions.  

---

## ⚙️ Requirements
- **fuel\.py**
  - Must define `convert` and `gauge`.  
  - Functions should **return values**, not print.  
- **Error handling**
  - Raise `ValueError` for invalid input (e.g., `"5/3"`, `"cat/dog"`).  
  - Raise `ZeroDivisionError` if denominator is zero.  
- **Tests**
  - Validate both valid inputs (`"1/2"`, `"99/100"`, etc.) and errors.  
  - Use `with pytest.raises(...)` for exceptions.  
  - Ensure `gauge` correctly outputs `"E"`, `"F"`, or `"N%"`.  

---

## 💡 Hint
- Use `split("/")` to separate numerator and denominator.  
- Convert to integers and handle exceptions with `try/except`.  
- Use `round()` for percentage rounding.  
- With `pytest`, cover both **normal cases** and **edge/error cases**.  

---

## 💻 Solution
👉 Expected files:  
- [fuel.py](fuel.py)  
- [test_fuel.py](test_fuel.py)  



🔗 **Official exercise**: [Refueling — CS50 Python, Pset 5](https://cs50.harvard.edu/python/psets/5/test_fuel/)  
