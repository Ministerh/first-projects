from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("./Flashcard_App/data/unknown_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./Flashcard_App/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# --------------------------- SWITCHING CARDS ------------------------------ #
def switch_cards():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white" )
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


#----------------------------BUTTON COMMAND ---------------------------------#
def next_card():
    global current_card, time_switch
    window.after_cancel(time_switch)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black" )
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    time_switch = window.after(3000, switch_cards)

def is_known():
    to_learn.remove(current_card)
    unknown= pandas.DataFrame(to_learn)
    unknown.to_csv("./Flashcard_App/data/unknown_words.csv",index=False)
    next_card()



# -------------------------------- UI SETUP -----------------------------------#
window = Tk()
window.title("Flascard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
time_switch = window.after(3000, switch_cards)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./Flashcard_App/images/card_front.png")
card_back_img = PhotoImage(file="./Flashcard_App/images/card_back.png")
card_img = canvas.create_image(400, 263, image= card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title =canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
card_word = canvas.create_text(400, 263, text="word",font=("Arial", 40, "bold") )
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./Flashcard_App/images/wrong.png")
unknown_button = Button(image=wrong_image, command=next_card)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="./Flashcard_App/images/right.png")
known_button = Button(image=right_image, command=is_known)
known_button.grid(row=1, column=1)

#to start with the words

next_card()












window.mainloop()
