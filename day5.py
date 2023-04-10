#we talk about loops it works well with a list
#foods = ["Rice", "Beans", "Porridge", "Egg"]
#for food in foods:
 #   print(food)
  #  print(food + " is delicious")
#students_score = input("Enter list of student scores").split()
#for n in range (0, len(students_score)):
#    students_score[n] = int(students_score[n])
#print(students_score)

#to get the total score using for loop
#score = 0
#for s in students_score:
#    score += s
#print(score)

#to get the number of students
#students = 0
#for n in students_score:
#    students += 1
#print(students)

#To print the maximum value in a list
#highest = 0
#for n in students_score: 
#    if n > highest:
#        highest = n
#print(highest)

#Using for loops in generating numbers (range)
#for n in range(1, 50):
#    print(n)
#The difference between the first and the second number can also be specified by adding it in the rane
#for n in range(1, 50, 2):
#    print(n)

#Using for loop to add numbers
#total = 0
#for n in range(1, 101):
#    total += n
#print(total)

#using the for loop to add even numbers in a range
#even = 0
#for n in range(2, 101, 2):
#    even += n
#print(even)

#even = 0
#for n in range(1, 101):
#    if n % 2 == 0:
#        even += n
#print(even)

#program that will solve children game of fizzbuzz
#the program should generate from 1 to 100 and print Fizz for number divisible by 3, print Buzz for one divisible by 5 and if it's divisible by both 5 and 3 it should print FizzBuzz
#  
#for n in range(1, 101):

#    if n % 3 == 0 and n % 5 == 0:
#        print("FizzBuzz")
#    elif n % 3 == 0:
#        print("Fizz")
#    elif n % 5 == 0:
#        print("Buzz")
#    else:
#        print(n)
#create a password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '?', '@', '+', '*', '-', '_']

print("Welcome to Py-Password Generator! ")
letter = int(input("How many letters do you want in your password?\n"))
symbol = int(input("How many symbols do you want in your password?\n"))
number = int(input("How many numbers do you want in your password?\n "))

#easy level
#passw = ""
#for n in range(1, letter + 1):
#  random_lettr = random.choice(letters)
#  passw += random_lettr

#for n in range(1, symbol + 1):
#  random_symbl = random.choice(symbols)
#  passw += random_symbl

#for n in range(1, number + 1):
#  random_num = random.choice(numbers)
#  passw += random_num
#print(passw)

#hard level

passw = []
for n in range(1, letter + 1):
  random_lettr = random.choice(letters)
  passw += random_lettr

for n in range(1, symbol + 1):
  random_symbl = random.choice(symbols)
  passw += random_symbl

for n in range(1, number + 1):
  random_num = random.choice(numbers)
  passw += random_num
random.shuffle(passw)
password = ""
for n in passw:
  password += n
print(f"Your password is: {passw}")