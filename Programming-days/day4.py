#Randomisation askpyhton.
import random
#random_integer = random.randint(1, 20)
#print(random_integer)
#join two files using import and the file name
#import Day1prohjecte 
#print(Day1prohject.py)
#random_float = random.random() * 5
#print(random_float)
#coin_toss = random.randint(0, 1)
#if coin_toss == 1:
#    print("heads") 
#else:
#    print("tails")
#lists in pyhton starts with open square bracket and ends with it. ithelps to store data of different forms in
#same variable.it also stores in other in which you want your data to be and that is how it should be listed
#states_of_nigeria = ["Adamawa", "Akwaibom", "Ogun","Lagos", "Oyo" ]
#states_of_nigeria[1] = "akwayibom"
#apeend is  used to add to the end of the list,
#states_of_nigeria.append("Osun")
#print(states_of_nigeria[1])
#(states_of_nigeria[-1])
#states_of_nigeria.extend(["Delta", "Imo", "Jigawa"])
#print(states_of_nigeria)\
#name = input("type everybody's name separated by comma")
#names = name.split(",")
#length = len(names)
#choice = random.randint(0, length - 1)
#buyer = names[choice]
#buyer =  random.choice(names)
#print(buyer + " is going to buy the meals today")
#from tkinter.tix import COLUMN


#row1 = [" ", " ", " "]
#row2 = [" ", " ", " "]
#row3 = [" ", " ", " "]
#map = [row1, row2, row3]
#print (f"{row1}\n {row2}\n {row3}")
#position = int(input("Where do you want to put the treasure? "))
#column = (position[0])
#row = (position[1])
#selected = map[row - 1] 
#selected[column - 1] = "x"
#map[row - 1][column - 1] = "x"

#print (f"{row1}\n {row2}\n {row3}")


#lst = [["ade", "ayo", "omo", "idowu"], ["akin", "umar", "alaba", "igan", "iyo"], ["ede", "edo", "imo"]]
#print(lst[0][1])
#rock wins against scissors
#scissors win against paper
#paper wins against rock

rock = '''------)
    (_______!
    ------@----
______|===!-----_____'''

paper = '''______|-------
    (====------)
    _____[----
    ------````
~~~~~|_______'''

scissors = '''~~~~~~(`````------
    ______]-----
        |~~~~~~
        ;;;;;;;~~~~~~~~
````|_____'''
image= [rock, paper, scissors]  
user = int(input("What would you like to choose. type 0 for rock, 1 for paper, 2 for scissors\n"))
if user >= 3: 
    print("You've entered an invalid number")
else:
    print(image[user])
    computer = random.randint(0, 2)
    print("computer choose: ")
    print(image[computer])
    if user == 0 and computer == 2:
        print("You win")
    elif user == 2 and computer == 0:
        print("You lose")
    elif user == 1 and computer == 0:
        print("You win")
    elif user == 0 and computer == 1:
        print("You lose")
    elif user == 2 and computer == 1:
        print("You win")
    elif user == 1 and computer == 2:
        print("You lose") 
    elif user == computer and computer == user:
        print("It's a draw")

  