from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)



mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

def button_click():
    km = round((float(mile_value.get()) * 1.609344))
    kilometer_value.config(text=f"{km}")
    

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

mile_value = Entry(width=10)
#mile_value.insert(END, string="0")
mile_value.grid(column=1, row=0)

kilometer_value = Label(text="0")
kilometer_value.grid(column=1, row=1)








window.mainloop()