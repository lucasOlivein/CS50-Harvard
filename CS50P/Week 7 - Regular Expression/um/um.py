import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if um := re.findall(r"\bum\W", s, re.I):
        return len(um)
    return 0

if __name__ == "__main__":
    main()