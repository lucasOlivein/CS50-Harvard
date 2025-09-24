# 🍽️ Meal Time  

## 📌 Task

Implement a program in **Python** that prompts the user for a **time** and outputs  
whether it’s **breakfast time**, **lunch time**, or **dinner time**.  

If it’s not time for a meal, the program should output **nothing**.  

Input format:  
- 24-hour time as `#:##` or `##:##` (e.g., `7:30`, `12:00`, `18:45`).  

---

### 🕒 Meal Times
- 🍳 **Breakfast** → `07:00` to `08:00`  
- 🥪 **Lunch** → `12:00` to `13:00`  
- 🍽️ **Dinner** → `18:00` to `19:00`  

*(All ranges are inclusive — e.g., `7:00`, `7:30`, `8:00` are all breakfast time.)*  

---

### ⚙️ Requirements
- Input must be normalized into **hours and minutes** before comparison.  
- Output only one meal time if within range, otherwise output **nothing**.  
- Comparison should handle **edge cases** like `7:00` and `8:00`.  

---

### 💡 Hints

- Recall that `split(":")` can separate hours and minutes.  
- Recall that `int` can convert strings to integers.  
- Recall that you can convert minutes into fractions of an hour (e.g., `30` → `0.5`).  

---

## 💻 Solution

👉 [meal.py](meal.py)

🔗 **Official exercise**: [Meal Time — CS50 Python, Pset 1](https://cs50.harvard.edu/python/psets/1/mealtime/)

