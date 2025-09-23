## 📌 Task
In a file called **`plates.py`**, reimplement *Vanity Plates* from Problem Set 2, restructuring your code per the below, wherein `is_valid` still expects a **str** as input and returns `True` if that str meets all requirements and `False` if it does not.  

`main` should only be called if the value of `__name__` is `"__main__"`:

```python
def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
```
pytest test_plates.py
```
---

## ⚙️ Requirements

- Implement is_valid(s) that checks whether a vanity plate string meets all the requirements.

- Implement main() to prompt the user and validate input.

- Write at least 4 test functions in test_plates.py, each beginning with test_.

- Ensure your tests cover:

    - ✅ Valid plates
    - ❌ Too short / too long plates
    - ❌ Invalid starting characters
    - ❌ Numbers in the wrong place
    - ❌ Illegal characters


---
## 💡 Hint

- Review the vanity plate requirements carefully from Problem Set 2.

- Use assert statements in your test functions.

- Consider splitting tests into categories (length, numbers, characters, etc.).

- Run tests frequently with pytest to confirm correctness.

---

## 💻 Solution

👉 [plates.py](plates.py)
👉 [test_plates.py](test_plates.py)

🔗 **Official exercise**: [Re-requesting a Vanity Plate — CS50 Python, Pset 5](https://cs50.harvard.edu/python/psets/5/test_plates/)  


