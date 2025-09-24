# 🍪 JAR

## 📌 Task
- Implement a `Jar` class to simulate a cookie jar.  
- The class should have the following methods:
  - `__init__(capacity=12)`: initialize the jar with a given capacity. Raise `ValueError` if capacity is not a non-negative integer.  
  - `__str__()`: return a string with one `🍪` per cookie in the jar.  
  - `deposit(n)`: add `n` cookies to the jar. Raise `ValueError` if this exceeds capacity.  
  - `withdraw(n)`: remove `n` cookies from the jar. Raise `ValueError` if insufficient cookies.  
  - `capacity`: property that returns the jar's capacity.  
  - `size`: property that returns the number of cookies currently in the jar (initially 0).  

---

### ⚙️ Requirements
- Implement all methods with the specified parameters.  
- Do **not** change method signatures.  
- Write a separate test file with at least four test functions using `pytest`:
  - Test initialization (`__init__`) and properties (`capacity`, `size`).  
  - Test string representation (`__str__`).  
  - Test depositing cookies (`deposit`).  
  - Test withdrawing cookies (`withdraw`).  
- Tests should raise `ValueError` when attempting invalid operations.  

---

### 💡 Hints
- Maintain an internal variable (e.g., `_size`) to track the current number of cookies.  
- Ensure `__str__` returns the correct number of cookie emojis for current size.  
- Test edge cases such as:
  - Depositing 0 cookies.  
  - Withdrawing all cookies.  
  - Depositing more than capacity.  
  - Withdrawing more than available.  
- Use `assert` statements in tests to verify behavior.  

---

## 💻 Solution
👉 [jar.py](jar.py)
