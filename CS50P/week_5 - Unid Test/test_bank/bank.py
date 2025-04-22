def main():
    greeting = input("Greeting: ")
    v = value(greeting)

    print(f'${v}')

def value(greeting):
    if greeting.split(' ', maxsplit=1)[0].lower() == 'hello':
        return 0
    elif greeting[0].lower() == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()