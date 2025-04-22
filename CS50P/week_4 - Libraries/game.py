from random import randint
from sys import exit

def game(level):
    guess = 0
    stage = randint(1, level)
    while guess != stage:
        try:
            guess = int(input("Guess: "))
        except:
            pass
        else:
            if guess < stage:
                print("Too small!")
            elif guess > stage:
                print("Too large!")
            else:
                exit("Just Right!")

def main():

    level = 0
    while level <= 0:
        try:
            level = int(input("Level: "))
        except:
            pass
    
    game(level)
    
main()