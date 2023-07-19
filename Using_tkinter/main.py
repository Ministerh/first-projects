#this will import every class
from tkinter import *

#this will create a window screen
window = Tk()
window.title("My first GUI program")
window.minsize(width= 500, height= 500)
#to add padding to the entire  screen
window.config(padx=15, pady=15)

#Label to write to screen
my_label = Label(text="I Am the label", font=("arial", 15, "bold"))
#grid method allows the written to dispplayed by specifying the rpws and column
#pack can also be used specifying the postion right, left or center
#place can also be sue dby specifying the x and y coordiates
my_label.grid(column=0, row=0)

def button_clicked():
    my_label.config(text=input.get())

button = Button(text="click here", command=button_clicked)
button.grid(column=2, row= 2)

# this is used to create an entry like placeholder
input = Entry(width=25)
#Add some text to begin with
input.insert(END, string="Start wiht this")
input.grid(column=4, row=4)
#this return the text in the entry
input.get()

new_button = Button(text="the new buton")
new_button.grid(column=3, row=0)

#Text
# text = Text(height=5, width=25)
# #this puts cursor in a textbox
# text.focus()
# #Add sokme text to begin with
# text.insert(END, "Example multi-line text entry")
# #get's current value in textbox at line 1,
# print(text.get("1.0", END))
# text.pack()

# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox
#     print(spinbox.get())

# spinbox= Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# #Scale
# #holds ther current scale value
# def scale_used(value):
#     print(value)

# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# #checkbutton
# def check_button():
#     #PRints 1 if on button checked, otherwise 0
#     print(checked_state.get())

# checked_state = IntVar()
# Checkbutton = Checkbutton(text="Is on?", Variable=checked_state, command= check_button)

# #radio buitton
# def radio_used():
#     print(radio_state.get())

# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command= radio_used)
# radiobutton2 = Radiobutton(text="Option1", value=2, variable=radio_state, command= radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

# #listbox
# def list_box_used(event):
#     #Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple", "pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)

# listbox.bind("<<ListboxSelect>>", list_box_used)
# listbox.pack()




window.mainloop()