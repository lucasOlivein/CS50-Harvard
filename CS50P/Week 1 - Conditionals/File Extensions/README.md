# 📄 File Extensions  

## 📌 Task

Implement a program in **Python** that prompts the user for the **name of a file**  
and then outputs that file’s **media type (MIME type)** if the file’s name ends,  
case-insensitively, with one of the following suffixes:

- 🖼️ `.gif` → `image/gif`  
- 🖼️ `.jpg` → `image/jpeg`  
- 🖼️ `.jpeg` → `image/jpeg`  
- 🖼️ `.png` → `image/png`  
- 📄 `.pdf` → `application/pdf`  
- 📄 `.txt` → `text/plain`  
- 📦 `.zip` → `application/zip`  

If the file extension is unknown, the program should output **`application/octet-stream`**.

---

### ⚙️ Requirements
- Input must be handled **case-insensitively** (e.g., `IMAGE.JPG` → `image/jpeg`).  
- Only the listed suffixes should be recognized explicitly.  
- Any other extension should return the **default MIME type**.  

---
### 💡 Hints

- Recall that a str comes with quite a few methods

---

## 💻 Solution
👉 [extensions.py](extensions.py)

🔗 **Official exercise**: [File Extensions — CS50 Python, Pset 1](https://cs50.harvard.edu/python/psets/1/extensions/)

