## 📌 Task
Implement a program in **Python** that prompts the user to input the name of a **fruit** (case-insensitively)  
and then outputs the **number of calories** in one portion of that fruit, according to the **FDA’s nutrition poster**.  

- Assume that users will input fruits **exactly as written** in the poster (e.g., `"strawberries"`, not `"strawberry"`).  
- Ignore any input that isn’t a fruit from the list.  

---

### ⚙️ Requirements
- Input: A **string** representing the fruit name.  
- Input should be treated **case-insensitively** (e.g., `"Apple"` = `"apple"`).  
- Output: An **integer** representing the calories in one portion of that fruit.  
- If the fruit is **not in the poster**, produce no output.  

---

### 💡 Hints

- Use a dictionary to map fruits to their calorie counts.  
- Use `.lower()` to handle case-insensitive input.  
- Compare the cleaned input directly to the dictionary keys.  


---

## 💻 Solution
👉 [nutrition.py](nutrition.py)
