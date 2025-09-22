## 📌 Task
Implement a program that:  

1. Expects **zero or two command-line arguments**:  
   - Zero → output text in a **random font**.  
   - Two → output text in a **specific font**, where:  
     - The first must be `-f` or `--font`.  
     - The second must be the **name of the font**.  
2. Prompts the user for a **string of text**.  
3. Outputs that text in the desired font.  
4. If the arguments are invalid (wrong flag or unknown font name), exit via `sys.exit` with an error message.  

---

## ⚙️ Requirements
- Use `sys.argv` to handle command-line arguments.  
- If no arguments are provided → pick a random font.  
- If two arguments are provided → validate both.  
- Prompt the user for input text.  
- Print the text in the chosen font.  

---

## 💡 Hint
- Use the **`pyfiglet`** library:  
  (``.)python
  import pyfiglet, sys, random
  (``.)  
- Example usage:  
  (``.)python
  pyfiglet.figlet_format("Hello, World!", font="slant")
  (``.)  
- You can get a list of fonts with:  
  (``.)python
  pyfiglet.getFonts()
  (``.)  
- Use `random.choice(pyfiglet.getFonts())` if no font is specified.  

---

## 💻 Solution
👉 [figlet.py](figlet.py)
