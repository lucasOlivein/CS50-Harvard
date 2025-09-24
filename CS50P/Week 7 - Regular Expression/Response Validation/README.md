# 💬 RESPONSE

## 📌 Task
- Implement a program that prompts the user for an email address.  
- The program should print `Valid` if the input is a syntactically valid email address, or `Invalid` otherwise.  
- Do **not** validate whether the domain actually exists.  
- Do **not** use regular expressions (`re`).  

---

### ⚙️ Requirements
- You may use a library such as `validator-collection` or `validators` from PyPI.  
- Prompt the user using `input` and print the result.  
- Handle common invalid formats, such as multiple `@` symbols or misplaced periods.  
- The program must run without errors for any string input.  

---

### 💡 Hints
- Install the library with:
  - `pip install validator-collection` **or**
  - `pip install validators`  
- Use the library’s email validation function to check the input.  
- Test with valid emails (`name@example.com`) and invalid ones (`malan@@harvard.edu`, `name@.com`).  

---

## 💻 Solution
👉 [response.py](response.py)

🔗 **Official exercise**: [Response Validation — CS50 Python, Pset 7](https://cs50.harvard.edu/python/psets/7/response/)

