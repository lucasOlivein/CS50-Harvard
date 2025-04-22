def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    #Each plate must contain at least 2 characters and the
    #maximum of 6
    if len(s) < 2 or len(s) > 6:
        return False

    #Each plate must start with at least two (2) letters
    for i in range(2):
        if not s[i].isalpha():
            return False
    
    #Number must come at the end not at the middle
    for i in range(2, len(s)):
        if s[i].isalnum():
            if s[i] == '0':
                return False
            for j in range(i, len(s)):
                if s[j].isalpha():
                    return False
            break
    
    #"No periods, spaces, or punctuation marks are allowed"
    for i in range(2, len(s)):
        if not s[i].isalpha() and not s[i].isalnum():
            return False
        
    return True


if __name__ == "__main__":
    main()
