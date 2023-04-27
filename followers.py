from day14 import footballers
import random
from followers_art import logo, vs
def players(account):
    '''this format the selected list and return the names'''
    account_name = account['name']
    account_info = account['description']
    return f" {account_name} {account_info}"

def answer_check(guess, followers1, followers2):
    '''take the user guess and followers number and return if the user gets it right'''

    if followers1 > followers2 and guess == 'a':
        return  True
    elif followers1 < followers2 and guess == 'a':
        return False
    elif followers2 > followers1 and guess == 'b':
        return True
    elif followers2 < followers1 and guess == 'b':
        return False

    # if followers1 > followers2:
    #     return guess == 'a'
    # else:
    #     return guess == 'b'

print(logo)

score = 0
game_continues = True

while game_continues:
    account_a = random.choice(footballers)
    account_b = random.choice(footballers)

    if account_a == account_b:
        account_b = random.choice(footballers)    

    print(f"Compare A:{players(account_a)}")
    print(vs)
    print(f"Against B: {players(account_b)}")

    user_ans= input("Who has more followers.Type 'A' or 'B'? ").lower()

    followers_number1 = account_a['number_of_followers']
    followers_number2 = account_b["number_of_followers"]
    

    
    
    correct_ans = answer_check(guess= user_ans,followers1=followers_number1, followers2=followers_number2 )
    #clear()
    #print(logo)
    if correct_ans:
        score += 1
        print(f"You got it right current score is {score}")
    else:
        game_continues = False
        print(f"You got it wrong your score is {score}")