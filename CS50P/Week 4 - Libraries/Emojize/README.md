## 📌 Task
Implement a program that prompts the user for a **string** in English and then outputs the **“emojized”** version of that string,  
converting any emoji codes (aliases) contained within to their corresponding emoji characters.  

---

## ⚙️ Requirements
- Prompt the user for a string.  
- Convert any recognized emoji codes (e.g., `:smile:`, `:heart:`) into their corresponding emoji.  
- If no codes are present, output the string unchanged.  
- Use the **`emoji`** library (`emoji.emojize`) for conversion.  

---

## 💡 Hint
- Import the **`emoji`** package:  
  ```python
  import emoji
  ```
- Use emoji.emojize(text, language="alias") to replace aliases with emojis.
- Be mindful of spacing and punctuation in user input.

---

## 💻 Solution
👉 [emojize.py](emojize.py)