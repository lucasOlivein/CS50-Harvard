# 🐦 TESTING MY TWTTR

## 📌 Task

### Reimplementation
- Reimplement **Setting up my twttr** from **CS50 Python, Pset 2**.  
- Restructure your code into functions:
  - `main`: prompts the user for input and prints output.  
  - `shorten`: takes a string as input and returns that string with all vowels (A, E, I, O, U) removed, case-insensitive.  
- Only `main` should call `print`.  

### Testing
- In a separate file `test_twttr.py`, implement one or more functions to test `shorten` thoroughly.  
- Each test function’s name should start with `test_` so that you can execute your tests with:

    pytest test_twttr.py  

- Include at the top of `test_twttr.py`:

    import twttr

or

    from twttr import shorten

- Ensure `shorten` **returns** a string, do not `print` inside it.  

---

### ⚙️ Requirements
- Implement `main()` and `shorten(word)` in your program.  
- Use `pytest` for testing and ensure test function names start with `test_`.  
- Include proper imports in the test file.  

---

### 💡 Hints
- Only `main` should call `print`.  
- Test `shorten` with strings containing uppercase and lowercase vowels.  
- Use `pytest test_twttr.py` to run your tests.  

---

## 💻 Solution
👉 [twttr.py](twttr.py)

🔗 **Official exercise**: [Testing my twttr — CS50 Python, Pset 5](https://cs50.harvard.edu/python/psets/5/twttr/)

