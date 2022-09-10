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

# HIGHER OR LOWER PART OF GAME
# WHAT SHOULD HAPPEN
# 2 System chooses random card as the hole card
# 3 Player chooses if next card will be higher or lower then chosen card
# 4 System chooses another random card and checks if this was higher or lower then the hole card
# 6 System then checks if user was correct
# 7a If player is correct then let them know they won
# 7b If player is incorrect then let them know they have lost

import random

deck_size = 2
# Request system to generate 2 random numbers between 1 and 13
# to stop any repeats I added None to indicate end of deck
deck = random.sample(range(1, 14), deck_size) + [None]

# Splits the 2 chosen numbers into chosen card (hole_card and next_card)
for hole_card, next_card in zip(deck[:-1],deck[1:]):
# Winner arguement
    if next_card == None: 
        print('Winner')
        break

# Arguement to say that if the next card is greater then hole card then this is higher otherwise it is lower
    correct_guess = 'h' if next_card > hole_card else 'l'

# Player chooses higher or lower
    guess = input(f'current card is {hole_card} is the next higher or lower? ') 

# System checks if player was correct or incorrect
# If player was correct then change nextcard to be None and run lines 19 to 21
# If play was incorret then print following statement
    if guess != correct_guess:
        print(f'You loose the next card was {next_card}')