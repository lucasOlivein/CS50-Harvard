# 💰 Tip Calculator
## 📌 Task

We’ve written most of a **tip calculator** for you.  
Unfortunately, two functions still need to be implemented:

---

### ⚙️ Requirements

1. **`dollars_to_float`**  
   - Accepts a `str` as input (formatted as `$##.##`, where each `#` is a digit).  
   - Removes the leading `$`.  
   - Returns the amount as a `float`.  
   - Example:  
     - Input: `$50.00`  
     - Output: `50.0`  

2. **`percent_to_float`**  
   - Accepts a `str` as input (formatted as `##%`, where each `#` is a digit).  
   - Removes the trailing `%`.  
   - Returns the percentage as a `float`.  
   - Example:  
     - Input: `15%`  
     - Output: `0.15`  

---

### 💡 Hints

- Recall that `input` returns a string.  
- Recall that float can convert a str to a float.
- Recall that a str comes with quite a few methods.

---
## 💻 Solution

👉 [tip.py](tip.py)

🔗 **Official exercise**: [Tip Calculator — CS50 Python, Pset 0](https://cs50.harvard.edu/python/psets/0/tip)

