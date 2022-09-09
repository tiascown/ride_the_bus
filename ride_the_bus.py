'''
===== RIDE THE BUS =====
1 PLAYER
3 LEVELS

Aim: User is trying to make the correcr guess on each card they are dealt.

    1. red or black
    2. higher or lower
    3. inside or outside
'''
from time import sleep
rules = open('README.md') #allows README.md to be read as the rules

red_cards = list(range(1, 14))* 2
black_cards = list(range(1, 14))* 2

#setting the atmosphere for the game
print("Let's play...")
sleep(1)
print("===== RIDE THE BUS =====")
sleep(1)
print("*applause*")
sleep(1)

def begin(): #game introduction/rules
    response = str(input("Do you know how to play? Y/N "))
    if response == "Y":
        print("Let's Go!")
        sleep(1)
    elif response == "N":
        print("\n Aim: Guess all 3 rounds correctly to win\n\n" + rules.read())
        ready_input = input("Ready to play? Y/N ")
        if ready_input == "Y":
            print("Let's Go!")
            sleep(1)
        elif ready_input == "N":
            print("You are the weakest link.. goodbye")
            exit()
        else:
            print("Please answer with Y or N")
            begin()
    else:
        print("Please answer with Y or N")
        begin()

begin()
# starting first level of game, red or black?
# user is dealt a card from shuffled deck

# user makes a guess
r_or_b = input('Red or Black? R/B ')


