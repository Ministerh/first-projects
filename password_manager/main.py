from tkinter import messagebox
from random import randint, choice,  shuffle
import json
import pyperclip

# ------------------------------- SEARCH DATA ---------------------------------- #
def get_password():
                # to read json file then save the read file to a variale
                website =web_input.get().title()
                try:
                    with open("./password_manager/web_datails_data.json", mode="r") as file:
                        data = json.load(file)
                except FileNotFoundError:
                    messagebox.showinfo(title= "Error", message="No Data file found")
                else:    
                    if website in data:
                        email = data[website]["email"]
                        password = data[website]["password"]
                        messagebox.showinfo(title=website, message=f"Email: {email}\npassword: {password}")
                    else:
                         messagebox.showinfo(title="Error", message=f"No details for {website} in your file")

                 
              
                

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '?', '@', '+', '*']


    password_letter = [choice(letters) for n in range(randint(8, 10))]
    password_symbol = [choice(symbols) for n in range(randint(2, 4))]
    password_number = [choice(numbers) for n in range(randint(2, 4))]
    password_list =password_letter + password_symbol + password_number
    shuffle(password_list)

    #join method helps to join elements in dictionary or tuple or list

    password = "". join(password_list)
    passw_input.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #


def data_manager():
    website=web_input.get()
    email = email_input.get()
    password =passw_input.get() 
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="eeeh!!", message="You cannot leave the field empty")
        web_input.focus() or passw_input.focus()
    else:
    
        try:
            with open("./password_manager/web_datails_data.json", mode="r") as file:
                # to read json file then save the read file to a variale
                data = json.load(file)
                
            
        except FileNotFoundError:
            with open("./password_manager/web_datails_data.json", mode="w") as file:     
                json.dump(new_data, file, indent=4)
        else:
             # to upate the data
            data.update(new_data)
            with open("./password_manager/web_datails_data.json", mode="w") as file:
                #To save the updated data
                json.dump(data, file, indent=4)   
        finally:      
                web_input.delete(0, END)
                passw_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()
window.title("My_password manager")
window.config(padx=50, pady=50)

canvas= Canvas(width=200, height=200)
logo = PhotoImage(file="./password_manager/logo.png")
#it will center the image in the canvas
canvas.create_image(100, 100, image= logo)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
#entry for website
web_input = Entry(width=32)
web_input.grid(row=1, column=1)
#this will focus cursor on then entry at launch
web_input.focus()

email_label = Label(text="Email/username:")
email_label.grid(column=0, row=2)
#entry for email
email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "pythonminister@gmail.com")

passw_label = Label(text="password:")
passw_label.grid(column=0, row=3)
#entry for password
passw_input = Entry(width=32)
passw_input.grid(row=3, column=1)

#BUttons
generator_button = Button(text="Generate Passwrod", command=generate_password)
generator_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=data_manager)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="serach", width=14, command=get_password)
search_button.grid(column=2, row=1)















window.mainloop()