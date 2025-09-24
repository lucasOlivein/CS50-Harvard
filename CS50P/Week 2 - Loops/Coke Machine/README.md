# 🥤 Coke Machine

## 📌 Task

Implement a program in **Python** that simulates a **coke vending machine**.  

The program should:  
1. Prompt the user to insert a coin (one at a time).  
2. Each time, inform the user of the **amount still due**.  
3. Once the user has inserted at least **50 cents**, output the **change owed**.  

---

### ⚙️ Requirements
- Accepted coin denominations: **25¢, 10¢, 5¢**.  
- Ignore any other integer input.  
- Continue prompting until the total inserted is **≥ 50**.  
- If the amount exceeds 50, output the **change owed**.  

---

### 💡 Hints

- Use a `while` loop until the total reaches at least 50.  
- Only accept coins of 25, 10, or 5.  
- Calculate the change as total inserted minus 50.  
 

---

## 💻 Solution
👉 [coke.py](coke.py)

🔗 **Official exercise**: [Coke Machine — CS50 Python, Pset 2](https://cs50.harvard.edu/python/psets/2/coke/)

