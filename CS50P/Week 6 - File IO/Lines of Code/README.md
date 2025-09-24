# 📄 Lines of Code

## 📌 Task

Implement a program that, given a source file,  
counts and outputs the number of **lines of code**, **excluding**:

- Blank lines  
- Comments (lines beginning with `#`)

The user will supply the filename as a **command-line argument**.

---

### ⚙️ Requirements

- Accept exactly **one** command-line argument (the file).  
- If too few or too many arguments are provided, exit with an error message.  
- Open the file and iterate through its lines.  
- Count only lines that are **non-empty** and do **not** start with `#`.  
- Print the resulting count as an integer.  

---

### 💡 Hints

- Use `sys.argv` to access command-line arguments.  
- Use `with open(filename) as f:` to open the file safely.  
- Use `.strip()` or `.lstrip()` to detect empty or commented lines.  
- Lines with code followed by a comment (e.g. `x = 1  # init`) should still count.  

---

## 💻 Solution

👉 [lines.py](lines.py)

🔗 **Official exercise**: [Lines of Code — CS50 Python, Pset 6](https://cs50.harvard.edu/python/psets/6/lines/)
