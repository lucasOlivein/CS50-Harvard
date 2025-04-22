greeting = input("Greeting: ")

if greeting.lower().strip().split(" ", maxsplit=1)[0].find("hello") != -1:
    print("$0")
elif greeting.lower().strip()[0] == "h":
    print("$20")
else:
    print("$100")
