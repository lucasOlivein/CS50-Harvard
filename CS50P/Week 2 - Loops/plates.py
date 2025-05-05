def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    firstNum = True

    if len(s) < 2:
        return False

    for i, char in enumerate(s):
        if i < 2:
            if char.isnumeric():
                return False
            continue

        if not char.isnumeric() and not char.isalpha():
            return False
        
        if char.isnumeric() and firstNum:
            if char == '0':
                return False
            firstNum = False
            continue

        if not firstNum:
            if char.isalpha():
                return False
            
        if i > 5:
            return False
    return True

main()