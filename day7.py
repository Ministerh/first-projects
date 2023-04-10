import random
from hangman_word import word_list 
from hangman_art import stages, logo
chosen_word = random.choice(word_list)

#for letters in chosen_word:
#    if letters == make_guess:
#        print('right')
#    else:
#        print('wrong')
print(logo)
#step 2
print(f"expo!, your word is {chosen_word}")
count = len(chosen_word)
display = []
for letters in range(count):
    display += '_'

lives = 6
game_end = False
while not game_end:
    make_guess = input("Guess a letter  ").lower()

    if make_guess in display:
        print(f"You've already guess {make_guess}")
        
    for position in range(count):
        letter = chosen_word[position]
        if letter == make_guess:
            display[position]= letter

    #if letter != make_guess:
    if make_guess not in chosen_word:
        print(f'Your letter is {make_guess}\n This letter is not in the word ')
        lives -= 1
        if lives <= 0:
            game_end = True
        print('Oops! You\'ve lost a chance, think harder')
    print(f"{' '.join(display)}")
    print(stages[lives])
    if '_' not in display:
        game_end = True
        print('You win')