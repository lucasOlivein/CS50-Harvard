## 📌 Task

Implement a program in **Python** that prompts the user for a **greeting** and outputs a value according to these rules:

- 👋 Starts with **"hello"** → output **$0**  
- 💬 Starts with **"h"** *(but not "hello")* → output **$20**  
- ❌ Any other greeting → output **$100**  

---

### ⚙️ Requirements
- Ignore any **leading whitespace** in the input.  
- The comparison must be **case-insensitive**.  
- Output must be strictly one of: **`0`**, **`20`**, or **`100`** (prefixed with `$`).  

---
### 💡 Hints

- Recall that a str comes with quite a few methods.
- Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.

---

## 💻 Solution
👉 [bank.py](bank.py)
