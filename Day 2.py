#Data types
#string
#integer: Numbers without any decimal point 123_4565_768
#float: Numebrs with decimal point 1325.456
#boolean: True of False value
#print("Hello" [3])
#print(123 + 420)
#casting means converting of variables to another variable
#new_v = len(input("what isn your name?"))
#v = str(new_v) the new variable has now been converted to string instead of an integer
#print("your name has a total of " + v + " characters")
#the type function is used to know the type of data you're working on
#print(type(len(input("what isn your name?"))))
#test_one  = input("type any two digit number")
#convo_one = int(test_one[0])
#convo_two = int(test_one[1])
#print(convo_one + convo_two)
#when there is multiple arithmetic opersaatrioon on a line python follows the PEMDASLR RLUE
#PARENTHESIS ()
#EXPONENT **
#MULTIPLICATION *
#DIVISION / AND // the division won't give float result and will ignore every valiue after the decimal
#ADDITION +
#SUBTRACTION -
#LEFT TO RIGHT
#Note it focus more on the arithmetic to the left side when the order is far apart e.g
#print(3 * 3 + 3 / 3 - 3)
#height = float(input ("enter your  height in m:"))
#weight = int(input ("enter your weight in kg:"))
#result = weight / height ** 2
#result_conv = int(result)
#print(result_conv)
#print(round(7 / 3))
#to determine the round up value, you s[ecify with
#print(round(7/3, 2))
#f-string this helps to cinvert every other data types to str when printing
#age = 20
#height = 1.55
#weight = 62
#print(f"you are {20} years old, your height is {height}, and your wieght is {weight}")
#365days,52weeks and 12months
#question = input("what is your age currently? ")
#arith = 90 
#arith2 = arith - int(question)
#arith3 = arith2 * 365
#arith4 = arith2  * 52
#arith5 = arith2 * 12
#print(f"you have {arith3} days, {arith4} weeks, and  {arith5} months left.")
#print("Welcome to the tip calculator.")
#total_bill = float(input("what was the total bill? $"))
#percentage_tip = float(input("what percentage would you like to give? 10, 12, or 15?"))
#number_of_people = float(input("How many people are to split the bill?"))
#total1 = (total_bill * percentage_tip) / 100
#total2 = (total1 + total_bill) / number_of_people
#total3 = round(total2, 2)
#to get exactly two fig after the decimal use the format function
#total3 = "{:.2f}".format(total2)
#print(f"Each person should pay: ${total3}")