#scope refers to how things work

#Modifying Global scope
#it has to be declared in the block that it is to be used
# enemies = 1
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"inside enemies {enemies}")

# increase_enemies()
# print(f"outside enemies {enemies}")

# #local scope refers to internsl scopes it is used in a surrounded area like in a block of code
# def portion():
#     portion_strength = 2
#     #this portion strength can only be accsesed if this fuyvntioin is called else it useless
#     print(portion_strength)

# #Global scope refers to one that can be used anywhere in the game it has to be declared at the top
# health_strength = 20
# def health_portion():
#     strength = 5
#     print(health_strength)

#health_portion()
# Namespace refers to how the scope works
# for every declared variable there is a namespace which is the scope the scope will determine how the variable will work


#no block scope in python for instance any  variable that is not created withing a
#function bloack is available anywhere but once it is in a function block then it is limited

#Global constants
#this are variables that you have no intention of changing it value
PI = 3.14159 
from random import randint

print ("Welcome to the Number Guessing game!")
print("I,m thinking of a number between 1 and 100.")
#global variable can be accessed everywhere
#choosing a random number between 1 and 100
thought= randint(1, 100)
print(thought)

hard_level = 7
easy_level = 10


def answer_tracker(user_guess, thought, attempt):
    '''checks the guess against the thought number and return the remain ing attempts'''
    if user_guess > thought:
        print("Too high.")
        print("Guess again.")
        return attempt - 1
    
    elif user_guess < thought:
        print("Too low.")
        print("Guess again.")
        return attempt - 1            
    elif user_guess == thought:
        print(f"You got it right! The answer is {thought}.")

def game():
    def difficulty():
        '''asks the user the difficulty level to choose'''
        game_level = input("Choose a difficulty level, type 'easy' or 'hard' ")
        if game_level == 'easy':
            return easy_level
        else:
            return hard_level

    attempt = difficulty()
    
    user_guess = 0
    while user_guess != thought:
        print(f"You have {attempt} remaining to guess the number") 
        user_guess = int(input("Make a guess: "))

        attempt = answer_tracker(user_guess,thought,attempt)
        if attempt == 0:
            print("You run out of Guesses, you lose")
            return
game()