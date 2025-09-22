def twttr(str):
    twttr = ''
    for char in str:
        if char.lower() in ('a','e','i','o','u'):
            continue
        twttr += char

    return twttr

def main():
    str = input("Input: ")
    str = twttr(str)
    print("Output: ", str)

main()