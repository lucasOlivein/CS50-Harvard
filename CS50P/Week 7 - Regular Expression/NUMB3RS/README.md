# 🔢 NUMB3RS

## 📌 Task
- Implement a function `validate` that checks if a given string is a valid **IPv4 address**.  
- The string must be in `#.#.#.#` format.  
- Each `#` must be a number **0 through 255**, inclusive.  
- The function should return `True` if the input is valid, `False` otherwise.  
- Implement thorough tests for the function using `pytest`.  

---

### ⚙️ Requirements
- Do not import any libraries beyond those allowed (`re` or `sys`).  
- Optionally use helper functions for validation.  
- Validate both format and numeric range of each octet.  
- Write tests in a separate file with functions prefixed by `test_`.  
- Tests should cover:
  - Valid addresses (`127.0.0.1`, `255.255.255.255`)  
  - Invalid addresses (`256.0.0.1`, `1.2.3.4.5`, `cat`)  

---

### 💡 Hints
- Use regular expressions (`re`) to check the general format.  
- Use raw strings (`r"pattern"`) to avoid escape issues.  
- Split the address by `.` and check each octet is an integer between 0 and 255.  
- Test edge cases carefully.  
- `re.search` with capturing groups can help extract octets.  

---

## 💻 Solution
👉 [numb3rs.py](numb3rs.py)
