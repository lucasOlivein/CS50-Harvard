## 📌 Task
In a file called **`bank.py`**, reimplement *Home Federal Savings Bank* from Problem Set 1, restructuring your code per the below, wherein `value` expects a **str** as input and returns an **int**:  

- `0` if that str starts with `"hello"`.  
- `20` if that str starts with `"h"` (but not `"hello"`).  
- `100` otherwise.  

The function should treat the string **case-insensitively**, and you may assume the input has **no leading spaces**.  
Only `main` should call `print`.  

```python
def main():
    ...


def value(greeting):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
```
pytest test_bank.py
```

## ⚙️ Requirements

- Implement value(greeting) that returns the correct integer based on greeting rules.
- Implement main() to prompt the user and call value.
- Write at least 3 test functions in test_bank.py:
    - Cover "hello" (in various cases, e.g., "Hello", "HELLO").
    - Cover greetings starting with "h" but not "hello".
    - Cover greetings not starting with "h".

---

## 💡 Hint

- Use .lower() to simplify case-insensitive comparisons.

- Test both expected cases and edge cases (e.g., "hi", "hey", "hola", "good morning").

- Use assert statements in your test functions.

- Run pytest frequently to ensure correctness.

---
## 💻 Solution
👉 [bank.py](bank.py)
👉 [test_bank.py](test_bank.py)

🔗 **Official exercise**: [Back to the Bank — CS50 Python, Pset 5](https://cs50.harvard.edu/python/psets/5/test_bank/)  