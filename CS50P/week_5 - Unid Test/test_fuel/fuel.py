import sys

def main():
    fraction = input("Input: ")
    percentage = convert(fraction)


def convert(fraction):
    
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    return round(x/y *100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage < 99:
        return f"{percentage}%"
    else:
        return 'F'


if __name__ == "__main__":
    main()