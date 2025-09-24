# 🔢 Little Professor

## 📌 Task
Implement a program that:  

1. Prompts the user for a **level `n`**.  
   - If the user does not input `1`, `2`, or `3`, reprompt.  
2. Randomly generates **ten (10) math problems** formatted as `X + Y =`,  
   - Each of `X` and `Y` is a non-negative integer with `n` digits.  
   - Use random pairs `(x, y)` for each problem (generate one pair at a time).  
   - Only addition (`+`) is required.  
3. Prompts the user to solve each problem.  
   - If the answer is **incorrect or not a number**, print `EEE` and reprompt.  
   - Allow up to **3 attempts per problem**.  
   - After 3 failed attempts, show the **correct answer**.  
4. After all 10 problems, output the user’s **score** (number of correct answers out of 10).  

---

## ⚙️ Requirements
- Define two functions:  
  - `get_level()` → prompts (and reprompts) until returning `1`, `2`, or `3`.  
  - `generate_integer(level)` → returns a non-negative integer with `level` digits,  
    or raises `ValueError` if level is invalid.  
- Use the `random` module (`random.randint`) to generate integers.  
- Track the score across all 10 problems.  
- Print results in the required format (`EEE`, correct answer, score).  

---

## 💡 Hint
- To ensure `n` digits:  
  - For level 1 → numbers from `0` to `9`.  
  - For level 2 → numbers from `10` to `99`.  
  - For level 3 → numbers from `100` to `999`.  
- Use a **loop with counter** to generate exactly 10 problems.  
- Wrap user input in a **try/except** to catch non-integers.  
- Keep a **score variable** to count correct answers.  

---

## 💻 Solution
👉 [professor.py](professor.py)

🔗 **Official exercise**: [Little Professor — CS50 Python, Pset 4](https://cs50.harvard.edu/python/psets/4/little/)
