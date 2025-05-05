expression = input("Expression: ")

x, y, z = expression.split(" ", maxsplit=2)

if y == '+':
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    if z == '0':
        raise ZeroDivisionError
    else:
        print(float(x) / float(z))
