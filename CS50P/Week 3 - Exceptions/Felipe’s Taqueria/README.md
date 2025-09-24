# 🌮 Felipe’s Taqueria

## 📌 Task
Implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).  

After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.  

---

## ⚙️ Requirements
- Input must be treated **case-insensitively**.  
- Ignore any input that isn’t a valid item on the menu.  
- Menu items will always be **titlecased** (e.g., `"Burrito"`, `"Taco"`).  
- Totals must be shown with **two decimal places**.  
- Program ends with **Control-D** (EOF).  

---

## 💡 Hint
You may want to use a `dict` to store menu items and their prices,  
and update the running total after each input.  

---

## 💻 Solution
👉 [taqueria.py](taqueria.py)

🔗 **Official exercise**: [Felipe’s Taqueria — CS50 Python, Pset 3](https://cs50.harvard.edu/python/psets/3/taqueria/)
