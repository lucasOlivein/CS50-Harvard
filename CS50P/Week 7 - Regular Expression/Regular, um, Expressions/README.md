# 🗣️ UM

## 📌 Task
- Implement a function `count` that counts how many times the word `"um"` appears in a given string.  
- The function should be case-insensitive.  
- Only count `"um"` as a standalone word, not as part of another word (e.g., `"yummy"` should **not** count).  
- Prompt the user for input and print the number of occurrences.  

---

### ⚙️ Requirements
- You may use `re` and `sys`, but no other libraries.  
- Structure your program with a `main` function and a `count` function.  
- Include a separate test file with at least three test functions using `pytest`.  
- Tests should cover:
  - Single occurrences (`"hello, um, world"` → 1)  
  - Multiple occurrences (`"Um, thanks, um..."` → 2)  
  - Edge cases (`"yummy"` → 0, `"Um?"` → 1)  

---

### 💡 Hints
- Use `re.findall` with a word boundary pattern (`\b`) to match `"um"` as a word.  
- Use raw strings (`r"pattern"`) for regex patterns.  
- Convert input to lowercase for case-insensitive counting.  
- Test thoroughly with various sentences and punctuation.  

---

## 💻 Solution
👉 [um.py](um.py)

🔗 **Official exercise**: [Regular, um, Expressions — CS50 Python, Pset 7](https://cs50.harvard.edu/python/psets/7/um/)

