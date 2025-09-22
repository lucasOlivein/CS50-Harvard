def fuel(x, y):
    indicator = x/y

    if indicator <= 0.01:
        print("E")
    elif indicator < 0.99:
        print(f"{round(indicator * 100)}%")
    else:
        print("F") 


def main():
    while True:
        try:
            x, y = input("Fraction: ").split('/')
            x = int(x)
            y = int(y)

            if x > y:
                raise ValueError
            if y == 0:
                raise ZeroDivisionError
            
            fuel(x,y)
            break
        except (ValueError, ZeroDivisionError):
            pass

main()