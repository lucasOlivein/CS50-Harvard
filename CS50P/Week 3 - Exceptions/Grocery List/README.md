# 🛒 Grocery List

## 📌 Task
Implement a program that prompts the user for items, one per line, until the user inputs **control-d** (which is a common way of ending one’s input to a program).  

Then output the user’s grocery list in **all uppercase**, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.  

No need to pluralize the items. Treat the user’s input **case-insensitively**.  

---

## ⚙️ Requirements
- Prompt the user repeatedly for grocery items.  
- Stop reading input when the user presses **control-d**.  
- Count how many times each item appears.  
- Output should:  
  - Be **UPPERCASE**.  
  - Be sorted **alphabetically**.  
  - Prefix each item with its count.  

---

## 💡 Hint
- Use a **dictionary** to keep track of items and their counts.  
- The `dict.get(key, default)` method can simplify counting.  
- `sorted()` will help you order the output alphabetically.  

---

## 💻 Solution
👉 [grocery.py](grocery.py)

🔗 **Official exercise**: [Grocery List — CS50 Python, Pset 3](https://cs50.harvard.edu/python/psets/3/grocery/)
