#day 3 is all about condition statement i.e if, else etc logical operatiors, scope etc
#print("Welcome to roller cosater!")
#height = float(input("What is your height"))
#if height >= 120:
#    print("You can ride the rollercoaster")
#    age = int(input("What is your age"))
#    if age < 12:
#        bill = 5
#        print("Child tickets are $5.")
#    elif age <= 18:
#        bill = 7
#        print("Youth tickets are $7.")
#        elif age>= 45 and age <= 55:
#            print("everything is gonna be okay, you get a free ride on us") 
#     else:           
#        bill =  12
#        print("Adult tickets are $12.")   
#    photo = input(f"Do you want a photo taken? Y or N.")
#    if  photo == "Y":
#        bill += 3
#        print(f"Your final bill is {bill}")
#else:
#    print("Sorry, you have to grow taller before you can ride.")
#condition operators include (>, <, >=, <=, ==, !=)
#print("Determinant of number")
#ven = int(input("Enter any number "))
#even_number = even % 2
#if even_number >= 1:
 #   print("this is an odd number")
#else:
 #   print("this is an even number")
#if even % 2 == 0:
 #   print("This is an even number")
#else:
 #   print("This is an odd number")
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
#BMI = weight / height ** 2
#random = round(BMI)
#if BMI < 18.5:
#    print(f"Your BMI is {random}, you are underweight")
#elif BMI <25:
#    print(f"Your BMI is {random}, you have a normal weight")
#elif BMI <30:
#    print(f"Your BMI is {random}, you are slightly overweight")
#elif BMI <35:
#    print(f"Your BMI is {random}, you are obese")
#else:
#    print(f"Your BMI is {random}, you are clinically obese")
#print("This will help you know if it's a leap year")
#year = int(input("enter the year "))
#leap_year = year % 4
#if leap_year >= 1:
#    print("This year is not a leap year")
#else:
#    print("This year is a leap year")
#it can also be checked in this format
#if year % 4 == 0:
#    if year % 100 == 0:
#        if year % 400 == 0:
#            print("Leap year")
#        else:
#            print("Not leap year")
#    else:
#        print("Not leap year")
#else:
#    print("Not leap year")
#Combining multiple if statement 
#print("Welcome to Python Pizza Deliveries")
#size = input("What size pizza do you want? S, M, or L ")
#pepperoni = input("Do you want pepperoni? Y or N" )
#extra_cheese = input("Do you want extra cheese? Y or N ")
#bill = 0
#if size == "S":
#    bill += 15
#elif size == "M":
#    bill += 20
#else:
#    bill += 25
#if pepperoni == "Y":
#    if size == "S":
#        bill += 2
#    else:
#        bill += 3
#if extra_cheese == "Y":
#    bill += 1 
#print(f"Your final bill is ${bill}")
#Combination of the logic operators (AND), (OR), (NOT)
#When using AND, both statement has to be true to get a true answer. if one is false the output will be false
#example: a = 12, 
#a > 10 and a < 13
#True
#a > 10 and a > 13
#False
#When using OR, only one or both has to be true to get a true answer, it can only be false when both value is false.
#example a = 12
# a > 15 or a < 10
#True . considering only one value of the statement.
#a >15 or a > 14
#False. since both statement are false
#When using NOT it reverse the condition i.e irony of the statement giving false to true and true to false.
# a = 12
# not a >15
#True. opposite of the real answer
#Love calculator
from re import T


#print ("Welcome to the love calculator!")
#name1 = input("What is your name? \n")
#name2 = input("what is their name? \n")
#combined = name1 + name2
#lower_case = combined.lower()
#t = lower_case.count("t")
#r = lower_case.count("r")
#u = lower_case.count("u")
#e = lower_case.count("e")
#true = t + r + u + e
#l = lower_case.count("l")
#o = lower_case.count("o")
#v = lower_case.count("v")
#e = lower_case.count("e")
#love = l + o + v + e
#true_love = int(str(true)) + int(str(love))
#if true_love < 10 or true_love > 90:
#    print(f"Your love score is {true_love}, you go like coke and mentos")
#elif true_love >=40 and true_love <= 50:
#    print(f"Your score is {true_love}, you are alright together. ")
#else:
#    print(f"your score is {true_love}")