# ⛽ Fuel Gauge

## 📌 Task
Implement a program that prompts the user for a fraction, formatted as **X/Y**, wherein each of X and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.  

If 1% or less remains, output **E** instead to indicate that the tank is essentially empty.  
If 99% or more remains, output **F** instead to indicate that the tank is essentially full.  

---

## ⚙️ Requirements
- Input must be formatted as **X/Y**.  
- Both **X** and **Y** must be positive integers.  
- **X ≤ Y**, otherwise prompt again.  
- **Y ≠ 0**, otherwise prompt again.  
- Handle invalid input by reprompting.  
- Output should be a **percentage rounded to the nearest integer**, or `E`/`F` if at the extremes.  

---

## 💡 Hint
- Use `try`/`except` blocks to handle `ValueError` and `ZeroDivisionError`.  
- The `round()` function will help when formatting the percentage.  

---

## 💻 Solution
👉 [fuel.py](fuel.py)

🔗 **Official exercise**: [Fuel Gauge — CS50 Python, Pset 3](https://cs50.harvard.edu/python/psets/3/fuel/)
