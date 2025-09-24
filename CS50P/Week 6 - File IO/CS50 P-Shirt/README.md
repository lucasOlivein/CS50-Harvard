# 👕 CS50 P-Shirt

## 📌 Task

Implement a program that expects exactly **two** command-line arguments:

1. The name (or path) of a JPEG or PNG file to read (input)  
2. The name (or path) of a JPEG or PNG file to write (output)  

The program should then:

- Open the input image  
- Resize and crop it to match the size of `shirt.png`  
- Overlay `shirt.png` (which has a transparent background) on top  
- Save the result to the output file  

---

### ⚙️ Requirements

- If the user does not provide exactly two arguments, exit with `sys.exit`.  
- Exit if the filenames do not end in `.jpg`, `.jpeg`, or `.png` (case-insensitive).  
- Exit if input and output extensions are different.  
- Exit if the input file does not exist.  

- Use Pillow (`pip install Pillow`):  
  - `Image.open` to open images  
  - `ImageOps.fit` to resize and crop the input  
  - `Image.paste` to overlay the shirt with transparency  
  - `Image.save` to write the result  

---

### 💡 Hints

- Use `os.path.splitext` to check extensions.  
- Catch `FileNotFoundError` if the input file doesn’t exist.  
- Get shirt dimensions with `shirt.size`.  
- `photo.paste(shirt, shirt)` overlays the shirt with transparency.  
- Try the program with your own photo for fun (optional).  

---

## 💻 Solution

👉 [shirt.py](shirt.py)

🔗 **Official exercise**: [CS50 P-Shirt — CS50 Python, Pset 6](https://cs50.harvard.edu/python/psets/6/shirt/)
