#print("Welcome to the Band Name Generator.")
#question1 = input ("What's name of the city you grew up in?\n")
#question2 = input ("what is the name of your pet?\n")
#print("Your band name could " + question1 + " " + question2 )
#get your treasure map at ascii art gallery
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
step1 = input('There is a trap ahead of you, where would you like to pass. type "left" or "right"\n').lower()
if step1 == "left":
    print("Awesome You've overcome the trap")
    step2 = input('Now you\'ve reached an ocean, a boat is a coming if you can wait, or would you like to swim across how would you like to cross. type"swim" or "wait"\n').lower()
    if step2 == "wait":
        print("You've reached the island safely,now there are three entrances")
        step3= input('Which entrance would you like to take."red", "yellow", and "blue" choose a color\n').lower()
        if step3 == "yellow":
            print("You've succesfully found the treasure.\n You Win!")
        elif step3 == "blue":
            print("you've entered a room full of beast, Game Over!")
        elif step3 == "red":
            print("This room is empty, Game Over!")
        else:
            print("this room does not exist, Game Over!")
    else:
        print("You've been swallowed by a whale. Game Over!")
else:
    print("Oops! you fell into a trap,  Game over!") 
#100daysofcode @londonappbrewry twitter