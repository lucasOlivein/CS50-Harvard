## 📌 Task
In a file called **`twttr.py`**, reimplement *Setting up my twttr* from Problem Set 2, restructuring your code per the below, wherein `shorten` expects a **str** as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.  

```python
def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()
```
Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
```
pytest test_twttr.py
```

---

## ⚙️ Requirements

Implement shorten(word) that removes all vowels from the input string.

Ensure both uppercase and lowercase vowels are handled.

Add a main() function that prompts the user and calls shorten.

Write unit tests in test_twttr.py:

Each test function must begin with test_.

Cover multiple scenarios (normal words, mixed case, no vowels, only vowels, etc.).

Run tests using pytest.

---
## 💡 Hint

- Consider using a for loop with string concatenation or "".join() to filter vowels.

- For testing:

    - assert statements check expected vs. actual results.

    - Think about edge cases (empty string, symbols, numbers).

---
## 💻 Solution

👉 [twttr.py](twttr.py)
👉 [test_twttr.py](test_twttr.py)

🔗 **Official exercise**: [Testing my twttr — CS50 Python, Pset 5](https://cs50.harvard.edu/python/psets/5/test_twttr/)  