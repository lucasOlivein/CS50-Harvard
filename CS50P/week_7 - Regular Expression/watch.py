import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r"^<iframe.*src=\"(?:https?)://(?:www.)?youtube\.com/embed/(.+)\".*</iframe>$", s):
        return f"https://youtu.be/{url.group(1)}"
    
    return None



if __name__ == "__main__":
    main()