fruits = {
     "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantoloupe" : 50,
    "grapefruit" :60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80,
}

def nutritiion(f):
    if f in fruits.keys():
        print ("Calors:", fruits[f])


def main():
    f = input("Item: ").lower()
    nutritiion(f)

    

main()