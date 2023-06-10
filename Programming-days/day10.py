#functions with output
#def formar_name(f_name, l_name):
    #to format a name the fuction title can be used
#    fname = f_name.title()
#    lname = l_name.title()
#    print(f"{fname} {lname}")
#formar_name('HUZZAIN', "OLAIde")


#def formar_name(f_name, l_name):
    #to format a name the fuction title can be used and printed using return fuction
#    fname = f_name.title()
#    lname = l_name.title()
#    return f"{fname} {lname}"
#print(formar_name('HUZZAIN', "OLAIde"))

# def is_leap (year):
#     if year % 4 == 0:
#         return True
#     if not year % 4 == 0:
#         return False
    
        
# How to document my functions after defining them
# It is called Dcostring and it has to come in gthe secomd line immediately after the derined fucntiom   
# def days_in_month(year,month):
#     '''input a year and a month to determie if the year is a 
#     leap year or not and to know the numnber of days in the month '''
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year)== True and month == 2:
#         return 29
#     return month_days[month - 1]

# #    return f"there are {current_month} days in the month"

# year = int(input("Enter a year"))
# month = int(input("Enter a month"))
# days = days_in_month(year, month)
# print (days)

# calculator
# Add
def add (n1, n2):
    return n1 + n2

#subtract
def subtract (n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2
from calculatorart import logo
def calculator():
    print(logo)
    operator = { 
        "+": add,
        "-": subtract,
        "*": multiply, 
        "/":divide
        }

    num1 = int(input("what's the first number "))
    num2 = int(input("what's the second number "))
    for key in operator:
        print(key)

    operand = input("What opetrator would you like to use from the above operator ")
    function = operator[operand]
    answer =function(num1, num2)
    print(f"{num1} {operand} {num2} = {answer}")

    last_operation = True
    while last_operation:
        more_operation = input(f"type 'y'to continue calculating with {answer}, or type'n' to start a new calculation.:")
        if more_operation == 'y':
            num1 = answer
            operand = input("pick an operator ")
            num2 = int(input("what's your next number"))
            function = operator[operand]
            answer =function(num1, num2)
            print(f"{num1} {operand} {num2} = {answer}")
        elif more_operation == 'n':
            last_operation = False
            #recurssion: it refers to function that calls itself. condition should be set so it will not be an infinite loop
            calculator()


calculator()
        
        




