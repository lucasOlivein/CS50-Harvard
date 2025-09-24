## 📌 Task

Implement a program that “cleans up” student data in a CSV file:

- The input CSV has a column `name` in the format `"last, first"`  
- The output CSV must split `name` into `first` and `last`  
- All other columns (e.g. `house`) must be preserved  

The user supplies **two** command-line arguments:  
1. Input CSV filename  
2. Output CSV filename

---

### ⚙️ Requirements

- Expect exactly two command-line arguments.  
- If wrong number of arguments, exit with error.  
- Read from input using `csv.DictReader`.  
- Write to output using `csv.DictWriter`, with `first`, `last`, and other columns.  
- Split names correctly and save results.  

---

### 💡 Hints

- Use `split(",")` or `split(", ")` carefully (trim whitespace).  
- When creating the writer, specify `fieldnames` in order.  
- Use `writeheader()` before writing rows.  
- Always validate arguments before opening files.  

---

## 💻 Solution

👉 [scourgify.py](scourgify.py)
