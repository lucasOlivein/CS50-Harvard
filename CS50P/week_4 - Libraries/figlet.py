from sys import argv, exit
from random import choice
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    if len(argv) == 1:
        font = choice (figlet.getFonts())
    elif all([len(argv) == 3, argv[1] in ('-f','--font')]):
        font = argv[2]
    else:
        exit(1)

    figlet.setFont(font=font)

    str = input("Input: ")
    print(figlet.renderText(str))


main()