def main():
    str = input("input: ")
    str = shorten(str)

    print(str)

def shorten(word):
    short = str()
    for letter in word:
        if letter in 'AEIOUaeiou':
            continue
        else:
            short += letter

    return short

if __name__ == "__main__":
    main()