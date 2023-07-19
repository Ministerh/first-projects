# Catching an exception requires for keys 
#try: this block contains something that might cause an error or an exception
#except: this block will execute if there truely was an exception 
#else: this block will block will excute if there was no exceptions
#finally: this block will be carried out irregardless tjhere was an exception or not

#FileNotFound
#this file does not exist
# try:
#     file = open("./Errors_and_exceptions/exception_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     #errors can be catched using the name of the error which means any other  error in the try block will still show
#     file = open("./Errors_and_exceptions/exception_file.txt", "w")
#     file.write("Errors and exceptions")
# except KeyError as error_message :
#     print(f"the key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     #this is triggered at all cost
#     file.close()
#     #raising an error will will crash the code even if there were no error
#     raise TypeError("I just want there to be an error")

# height = float(input("height: "))
# weight = int(input("weight:  "))

# # since hu,am height should not be more than 3 meters
# if height  > 3:
#     raise ValueError("the height should not be higher than 3")
# bmi = weight / height ** 2
# print(bmi)

fruits = ["Apple", "Orane", "Pear"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + "pie")


make_pie(2)
