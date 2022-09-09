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

red_cards = list(range(1, 14))* 2
black_cards = list(range(1, 14))* 2

#setting the atmosphere for the game
print("Let's play...")
sleep(2)
print("===== RIDE THE BUS =====")
sleep(2)
print("*applause*")
sleep(2)

response = str(input("Do you know how to play? Y/N "))
if response == "Y":
    print("Let's go then!")
elif response == "N":
    print("Aim of the game: Guess all three rounds correctly to win.\nHow to play:\nThe dealer has shuffled a pack of 52 cards and will deal you one card for each round.\nbefore the card is revealed you will be asked a question.\nIf you guessed correctly the game continues until you have completeted all three rounds.\nIf you guessed incorrectly, you lose, try again.")

# starting first level of game, red or black?
# user is dealt a card from shuffled deck

# user makes a guess
print("Red or Black?")


