# 📅 Outdated

## 📌 Task
Implement a program that prompts the user for a date, anno Domini, in **month-day-year** order, formatted like `9/8/1636` or `September 8, 1636`,  
wherein the month in the latter might be any of the values in the list below:

    ["January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"]


Then output that same date in `YYYY-MM-DD` format.  

If the user’s input is not a valid date in either format, prompt the user again.  
Assume that every month has no more than 31 days (i.e., no need to validate whether a month has 28, 29, 30, or 31 days).  

---

## ⚙️ Requirements
- Accept input in **two formats**:  
  - Numeric (`M/D/YYYY`, e.g., `9/8/1636`).  
  - Textual (`Month D, YYYY`, e.g., `September 8, 1636`).  
- Convert input to ISO format (`YYYY-MM-DD`).  
- Reprompt the user if the input is invalid.  
- No need to validate exact month lengths (just day ≤ 31).  

---

## 💡 Hint
- Use **`str.split()`** or **`str.replace()`** to handle commas and separators.  
- A **dictionary** mapping month names to numbers will simplify conversion.  
- Wrap parsing logic in a loop so invalid inputs trigger a reprompt.  

---

## 💻 Solution
👉 [outdated.py](outdated.py)

🔗 **Official exercise**: [Outdated — CS50 Python, Pset 3](https://cs50.harvard.edu/python/psets/3/outdated/)
