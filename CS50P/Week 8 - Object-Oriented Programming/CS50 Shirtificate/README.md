# 👕 SHIRTIFICATE

## 📌 Task
- Implement a program that prompts the user for their name.  
- Generate a PDF “shirtificate” with the following specifications:
  - Portrait orientation, A4 size (210mm × 297mm).  
  - The title “CS50 Shirtificate” centered at the top.  
  - A t-shirt image centered horizontally.  
  - The user’s name overlaid on the shirt in white text.  
- The PDF should be saved as `shirtificate.pdf`.  
- Additional styling (borders, colors, lines) is optional.  

---

### ⚙️ Requirements
- Use the `fpdf2` library (`pip install fpdf2`).  
- You may extend `FPDF` with a subclass or add header/footer manually.  
- Disable automatic page breaks if needed to prevent overflow.  
- Center elements using page width and cell positioning.  
- Ensure that long names do not wrap awkwardly.  

---

### 💡 Hints
- Use `FPDF().add_page()` to create a page.  
- Use `image()` to add the shirt image and `set_xy` or `cell()` for positioning text.  
- Use `set_font` and `set_text_color` to style text.  
- Test with multiple names to verify centering and styling.  
- You can open `shirtificate.pdf` directly in VS Code to verify output.  

---

## 💻 Solution
👉 [shirtificate.py](shirtificate.py)
