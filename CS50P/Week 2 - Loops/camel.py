def camel(str):
    i = 0
    for char in str:
        if char.isupper():
            str = str[:i] + "_" + char.lower() + str[i+1:]
            i += 1
        i += 1

    return str


def main():
    str = input("CamelCase: ")
    str = camel(str)

    print("snake_case: ", str )


main()