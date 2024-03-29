from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps = 0
timetr = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    time.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text=None)
    global reps 
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    shor_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        time.config(text="Break", fg= RED)
    elif reps % 2 == 0:
        count_down(shor_break_sec)
        time.config(text="Break", fg= PINK)
    else:
        count_down(work_sec)
        time.config(text="Work", fg= GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    #python dynamic typing allows to change variable data type by assigning new data to teh variable
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    #gets a hold of a canvas text and change it
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        #tk method that helps to loop
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for n in range(work_session):
            marks += "✓"
            check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro - (Tomato in italy)")
window.config(padx=100, pady=50, bg= YELLOW)

time = Label(text="Timer",fg=GREEN,font=(FONT_NAME,35), bg=YELLOW)
time.grid(column=1, row=0)

check_mark = Label(fg=GREEN, bg=YELLOW, font=("Bold"))
check_mark.grid(column=1, row=3)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./Pomodoro project/tomato.png")
canvas.create_image(100, 112, image= tomato_image)
timer_text =canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)


window.mainloop()