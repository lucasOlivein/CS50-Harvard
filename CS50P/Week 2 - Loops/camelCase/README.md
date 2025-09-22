## 📌 Task

Implement a program in **Python** that prompts the user for the name of a variable in **camelCase**  
and outputs the corresponding name in **snake_case**.  

Example conversions:  
- `myVariableName` → `my_variable_name`  
- `thisIsCS50` → `this_is_cs50`  

---

### ⚙️ Requirements
- Input will always be in **camelCase**.  
- Each uppercase letter should be replaced with an **underscore + lowercase letter**.  
- Output must be entirely **lowercase** and use underscores `_` as separators.  

---

### 💡 Hints

- Recall that `isupper()` can check if a character is uppercase.  
- Build a new string by inserting `_` before uppercase letters.  
- Don’t forget to convert those uppercase letters to lowercase.  

---

## 💻 Solution
👉 [camel.py](camel.py)
