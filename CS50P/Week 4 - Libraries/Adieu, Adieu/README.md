## 📌 Task
Implement a program that prompts the user for **names**, one per line, until the user inputs **Control-D** (end-of-file).  
Assume that the user will input at least one name.  

Then bid adieu to those names, separating them with commas and “and” according to English grammar rules:  

- Two names → joined with **“and”**.  
- Three names → two commas and **“and”**.  
- `n` names → `n − 1` commas and one **“and”**.  

Example output:  
 ```
Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
```


---

## ⚙️ Requirements
- Continuously accept input (one name per line).  
- Stop when user presses **Control-D**.  
- Always output a single line beginning with `Adieu, adieu, to ...`.  
- Format names with proper commas and **“and”** before the last element.  

---

## 💡 Hint
- Use a **list** to store names.  
- Apply **string joining** (`", ".join(...)`) for comma separation.  
- Handle the **last element** separately with an **“and”**.  
- To test EOF in Python, wrap input collection in a `try/except EOFError`.  

---

## 💻 Solution
👉 [adieu.py](adieu.py)

