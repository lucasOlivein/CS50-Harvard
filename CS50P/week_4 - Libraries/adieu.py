import inflect

def print_inflect(name_list):
    p = inflect.engine()

    print("Adieu, adieu, to", p.join(name_list))

def main():
    names = []
    while True:
        try: 
            names.append(input("Name: "))
        except:
            break
    
    print_inflect(names)

main()