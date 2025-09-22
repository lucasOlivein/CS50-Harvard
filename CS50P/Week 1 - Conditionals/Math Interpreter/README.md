## 📌 Task

Implement a program in **Python** that prompts the user for an **arithmetic expression**  
and outputs the result as a **floating-point value formatted to one decimal place**.  

The user’s input will be formatted as:
x y z


Where:  
- 🔢 `x` → an integer  
- ➕➖✖️➗ `y` → an operator (`+`, `-`, `*`, `/`)  
- 🔢 `z` → an integer  

---

### ⚙️ Requirements
- Input will always be in the format **`x y z`** (with single spaces).  
- The program must handle the four basic operations.  
- Output must be formatted to **1 decimal place**.  

---
### 💡 Hints

- Recall that a string has methods like `split()`.  
- For example:  
  ```python
  x, y, z = "1 + 1".split(" ")
  # x = "1", y = "+", z = "1"
  ```
- Don’t forget to convert x and z into integers before calculating.
- Use float division when dividing.
- Format the result with **one decimal place**.
---

## 💻 Solution
👉 [interpreter.py](interpreter.py)
