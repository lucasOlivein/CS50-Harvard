# 🕘 WORKING 9 TO 5

## 📌 Task
- Implement a function `convert` that converts times from **12-hour format** to **24-hour format**.  
- Input can be in any of these formats:
  - `9:00 AM to 5:00 PM`
  - `9 AM to 5 PM`
  - `9:00 AM to 5 PM`
  - `9 AM to 5:00 PM`
- Return the corresponding string in 24-hour format (e.g., `"09:00 to 17:00"`).  
- Raise a `ValueError` for invalid formats or invalid times (e.g., `12:60 AM`, `13:00 PM`).  

---

### ⚙️ Requirements
- Handle both hours and optional minutes.  
- Times may start AM or PM and end AM or PM (e.g., `"5:00 PM to 9:00 AM"`).  
- Do not import any libraries other than `re` or `sys`.  
- Implement optional helper functions as needed.  
- Include a `main` function to prompt for input and print the result.  
- Create tests in a separate file to verify various valid and invalid inputs.  

---

### 💡 Hints
- Use regular expressions (`re`) to parse hours, minutes, and AM/PM.  
- Remember that `12 AM` → `00:00` and `12 PM` → `12:00`.  
- Validate minutes (`00–59`) and hours (`1–12`).  
- Consider edge cases where work spans overnight (PM → AM).  
- Use raw strings (`r"pattern"`) to avoid escaping issues in regex.  

---

## 💻 Solution
👉 [working.py](working.py)

🔗 **Official exercise**: [Working 9 to 5 — CS50 Python, Pset 7](https://cs50.harvard.edu/python/psets/7/working/)

