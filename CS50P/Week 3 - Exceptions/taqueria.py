taqueria = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



def order(str):
    str = str.title()
    if str in taqueria.keys():
        return taqueria[str]
    else:
        return False


def main():
    total = 0
    while True:
        try:
            str = input("Item: ")
            if order(str):
                total += order(str)

        except EOFError:
            return
        else:
            if total:
                print(f"Total: ${total:.2f}")    

main()