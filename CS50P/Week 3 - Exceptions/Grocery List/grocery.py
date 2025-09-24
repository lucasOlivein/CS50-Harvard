grocery_list = dict()

def grocery(str):
    if str not in grocery_list.keys():
        grocery_list[str] = 1
    else:
        grocery_list[str] += 1


def main():
    while True:
        try:
            grocery(input().upper())
        except EOFError:
            break
    
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item}")

main()