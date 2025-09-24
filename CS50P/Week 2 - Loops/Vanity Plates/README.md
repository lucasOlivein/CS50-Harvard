# 🚗 Vanity Plates

## 📌 Task

Implement a program that prompts the user for a **vanity plate** and then outputs **Valid** if it meets all of the requirements, or **Invalid** otherwise.  
Assume that any letters in the user’s input will be uppercase.  

The program must be structured such that:  
- A function `is_valid(s: str) -> bool` is defined.  
- `is_valid` returns `True` if the plate meets all requirements, and `False` otherwise.  
- You may implement additional helper functions for `is_valid` to call (e.g., one per requirement).  

---

### ⚙️ Requirements
- Plates must start with **at least two letters**.  
- Plates may contain a **maximum of 6 characters** (letters or numbers) and a **minimum of 2 characters**.  
- Numbers cannot be used in the middle of a plate; they must come at the **end** (if present).  
- The **first number** used cannot be a **‘0’**.  
- No periods, spaces, or punctuation marks are allowed — only **letters and digits**.  

---

### 💡 Hints

- Plates must start with at least two letters.  
- The first number cannot be 0, and once numbers begin, no more letters are allowed.  
- Valid plates must be 2 to 6 characters long.  


---


## 💻 Solution
👉 [plates.py](plates.py)

🔗 **Official exercise**: [Vanity Plates — CS50 Python, Pset 2](https://cs50.harvard.edu/python/psets/2/plates/)

