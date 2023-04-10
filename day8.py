#simple fucntion
#def greet():

#    print('Hello')
#    print('how do yoou do')
#    print("isn't the weather nice today?")
#greet()

#function with input
#def greet_with_name(name):
#    print(f"Hello {name}")
#    print(f"How are you doing {name}")
#greet_with_name('Huzzain')

#function with mofe than 1 input
#def multi_input(name, location):
#    print(f"Hello {name}")
#    print(f"where are you at {location}")
#position argumment
#multi_input("Huzzain","ilaro")\

#keyword argument
#multi_input(location="ilaro" , name="Huzzain")
#to rond to nearest whole number 

#import math
#def Area_calc(height, width, cover):
#    area = height * width
#    num_of_can = math.ceil(area/cover)
#    print(f"you'll need {num_of_can} cans of paint")

#test_h = int(input("Height of wall:"))
#test_w = int(input("width of wall:"))
#coverage = 5
#Area_calc(height = test_h, width = test_w,  cover = coverage)

#def  prime_checker(number):
#    prime = True
#    for i in range(2, number):
#        if number % i == 0:
#            prime = False
#    if prime:
#        print("it's a prime number")
#    else:
#        print("it's not a prime")
#n = int(input("enter a number"))
#prime_checker(number = n)

def caesar(d_text, d_shift, d_direction):
    coder = ""
    if d_direction == "decode":
        d_shift *= -1
    for char in d_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + d_shift
            coder += alphabet[new_position]

        else:
            coder += char     
    print(f"The {d_direction} text is {coder}")

redo = True
while redo:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("type the shift number"))

    shift = shift % 26

    caesar (d_text= text, d_shift= shift, d_direction = direction)
    result = input("Type 'yes' if you want to retry, if not type 'no'.\n").lower()
    if result == "no":
        redo = False
        print("Goodbye")
        
    
#def encrypt(d_text, d_shift):
#    cipher_text = ""
#    for letter in d_text:
#        position = alphabet.index(letter)
#        new_position = position + shift
#        new_letter = alphabet[new_position]
#        cipher_text += new_letter
#    print(f"the encrypted text is {cipher_text}")

#def decrypt(d_text, d_shift):
#    cipher_text = ""
#    for letter in d_text:
#        position = alphabet.index(letter)
#        new_position = position - shift
#        new_letter = alphabet[new_position]
#        cipher_text += new_letter
#    print(f"the decrypted text is {cipher_text}")

#if direction == "encode":
#    encrypt(d_text = text, d_shift = shift)
#elif direction == "decode":
#    decrypt(d_text = text, d_shift = shift)
