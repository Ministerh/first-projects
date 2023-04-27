#Blackjack CapStone project
# Note: you don't win because you are closer to the value of 21 -- 
# you win because your combined value of the cards is greater than that of dealer.

#Blackjack Strategy
#When the value of dealer's revealed card is 4,5 or 6, it may be fruitful to double your bet with an Ace and 4 in hand.
#You may want to surrender if you have 16 in your hand while the dealer has a 9,10 or A.
#You should always split if you have a pair of Aces.
#If you get a pair of 7s, only press hit if the dealer has 8,9,10 or Ace
from blackjackart import logo
import random
print("Welcome to blackjack ")


def card_dealer():
    '''this function returns randomly selected cards'''
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_deck)
    return card
def calculator(card):
    #this checks for black jack where there is ace + 10 for the user or computer 
    if sum(card) == 21 and  len(card) == 2:
        return 0
    #to check if ace is gonna work as 11 or 1
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    #the sum function helps to add up iterable element

    return sum(card)
def compare(user_score, computer_score):
    '''this function will compare the user and the computer cards'''
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return "Lose, opponent has  a Blackjack"
    elif user_score == 0:
        return "win with a blackjack"   
    elif user_score > 21:
        return "You went over, You lose"
    elif computer_score > 21:
        return "opponent went over, You win"
    elif user_score > computer_score:
        return 'You win'
    else:
        return "You lose"

user_card = []
computer_card = []
def play_game():
    print(logo)

    is_game_over = False
    for n in range(2):
        user_card.append(card_dealer())
        computer_card.append(card_dealer())

    #A loop is needed for this to repeat itself and also cumulate the score
    while not is_game_over:

        user_score=calculator(user_card)
        computer_score = calculator(computer_card)
        print(f"your cards: {user_card}, current score: {user_score}")
        print(f"computer's first card: {computer_card[0]}")

        if  user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over= True
        else:
            #the game has not ended and the user would like ti get another card or pass
            user_deal = input("Type 'y' to get another card, type 'p' to pass: ")
            if user_deal == 'y':
                user_card.append(card_dealer())
            else:
                is_game_over = True

    #once the user is done drawing cards the computer should also deal
    while computer_score != 0 and computer_score < 17:
        computer_card.append(card_dealer())
        #to update the computer score and final hand
        computer_score = calculator(computer_card)

    print(f"Your final hand is {user_card}: score is {user_score} ")
    print(f"Coomputer final hand is {computer_card}: score is {computer_score} ")
    print(compare(user_score, computer_score))

#To restart the game after one ends 

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
