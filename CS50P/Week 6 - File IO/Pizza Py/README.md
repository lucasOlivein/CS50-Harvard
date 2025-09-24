## 📌 Task

Implement a program that reads a **CSV file** representing a pizza menu  
and prints it in a neatly formatted table using the `tabulate` library.

---

### ⚙️ Requirements

- Take exactly one command-line argument: the path to a CSV file.  
- If too few or too many arguments are provided, exit with an error message.  
- Read the CSV file and display it as a table with format `"grid"`.  
- The table should include headers.  

---

### 💡 Hints

- Use `csv.DictReader` to read rows as dictionaries.  
- Use `tabulate(rows, headers="keys", tablefmt="grid")` to render the table.  
- Validate `len(sys.argv)` before proceeding.  
- Install `tabulate` if not already available.  

---

## 💻 Solution

👉 [pizza.py](pizza.py)
