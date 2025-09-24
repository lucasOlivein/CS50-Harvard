# 🎥 WATCH ON YOUTUBE

## 📌 Task
- Implement a function `parse` that extracts YouTube video URLs from HTML input.  
- The function should return the shorter, shareable `youtu.be` URL equivalent.  
- If the HTML contains no valid YouTube URL, return `None`.  
- Expect `src` values of `iframe` elements in formats like:
  - `http://youtube.com/embed/VIDEO_ID`
  - `https://youtube.com/embed/VIDEO_ID`
  - `https://www.youtube.com/embed/VIDEO_ID`

---

### ⚙️ Requirements
- Accept a string of HTML as input.  
- Extract the video ID from the `src` attribute of the `iframe`.  
- Convert the extracted URL to the `https://youtu.be/VIDEO_ID` format.  
- Do **not** import any libraries beyond `re` and `sys`.  
- Structure your program with a `main` function that prompts the user for input.  

---

### 💡 Hints
- Use raw strings (`r"pattern"`) for regex patterns.  
- Use `re.search` with capturing groups to extract the video ID.  
- Test input with different `iframe` src formats and with no iframe.  
- Remember that backslashes in regex need raw string notation.  

---

## 💻 Solution
👉 [watch.py](watch.py)

🔗 **Official exercise**: [Watch on YouTube — CS50 Python, Pset 7](https://cs50.harvard.edu/python/psets/7/watch/)

