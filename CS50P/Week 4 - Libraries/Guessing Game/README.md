# 🎯 Guessing Game

## 📌 Task
Implement a program that:  

1. Prompts the user for a **level `n`**.  
   - If the user does not input a positive integer, the program should prompt again.  
2. Randomly generates an integer between `1` and `n` (inclusive) using the **`random`** module.  
3. Prompts the user to **guess** that integer.  
   - If the guess is not a positive integer, reprompt.  
   - If the guess is smaller than the number, output **`Too small!`** and reprompt.  
   - If the guess is larger than the number, output **`Too large!`** and reprompt.  
   - If the guess matches the number, output **`Just right!`** and exit.  

---

## ⚙️ Requirements
- Validate all user input as **positive integers**.  
- Use `random.randint(1, n)` to generate the secret number.  
- Keep prompting until the correct guess is made.  
- Print exactly one of:  
  - `Too small!`  
  - `Too large!`  
  - `Just right!`  

---

## 💡 Hint
- Wrap input requests in a **loop** until valid.  
- Use **`try/except`** with `ValueError` to handle invalid integer input.  
- The `random` module is built-in:  
  ```python
  import random
  number = random.randint(1, n)
  ```

---
## 💻 Solution

👉 [game.py](game.py)

🔗 **Official exercise**: [Guessing Game — CS50 Python, Pset 4](https://cs50.harvard.edu/python/psets/4/guess/)
