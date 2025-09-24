# 🍂 SEASONS

## 📌 Task
- Implement a program that prompts the user for their date of birth in `YYYY-MM-DD` format.  
- Calculate how old the user is in **minutes**, assuming:
  - Birth time is midnight of the input date.  
  - Current time is midnight of today’s date.  
- Print the age in **English words**, rounded to the nearest integer, without using numerals or the word `and`.  
- Structure the program with a `main` function and additional helper functions as needed.  

---

### ⚙️ Requirements
- Use the `datetime` module to handle dates and calculate differences.  
- Use the `inflect` module to convert numbers to words (`pip install inflect`).  
- Exit gracefully with `sys.exit` if the user input is not in `YYYY-MM-DD` format.  
- Ensure the program does **not** raise any exceptions on valid or invalid input.  
- Write thorough tests in `test_seasons.py` for all functions except `main`, using `pytest`.  

---

### 💡 Hints
- Subtract two `date` objects to get a `timedelta` object; its `days` attribute gives the number of days between dates.  
- Multiply days by 24 × 60 to convert to minutes.  
- Use `inflect.engine().number_to_words` to convert integers to English words.  
- Round the final number of minutes before converting to words.  
- Validate user input carefully using string splitting or `datetime.strptime`.  

---

## 💻 Solution
👉 [seasons.py](seasons.py)
