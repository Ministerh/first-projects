from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface():
    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz_question = quiz
        self.total = len(self.quiz_question.question_list)
        self.window = Tk()
        self.window.title("Trivia Base Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, 
                                                     width=250,
                                                     text="Somme question", 
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        wrong_image = PhotoImage(file="./The_quizzler/images/false.png")
        self.wrong = Button(image=wrong_image, highlightthickness=0, command=self.wrong_button_check)  
        self.wrong.grid(row=2, column=1)

        right_image = PhotoImage(file="./The_quizzler/images/true.png")
        self.right = Button(image=right_image, highlightthickness=0, command= self.right_button_check)
        self.right.grid(row=2, column=0)

        self.score = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        
        self.total_question = Label(text=f"Total: {self.total}", fg="white", bg= THEME_COLOR)
        self.total_question.grid(row=0, column=0)

        self.get_next_question()
        

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.total_question.config(text=f"Total: {self.total}")
        if self.quiz_question.still_has_questions():
            self.score.config(text=f"score: {self.quiz_question.score} of {self.quiz_question.question_number}")
            self.canvas.itemconfig(self.question_text, text= self.quiz_question.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.right.config(state="disabled")
            self.wrong.config(state=DISABLED)
    def right_button_check(self):
        self.total -= 1
        correct =self.quiz_question.check_answer("True")
        self.give_feedback(correct)

    def wrong_button_check(self):
        self.total -= 1
        self.give_feedback(self.quiz_question.check_answer("False"))
        

    def give_feedback(self, feedback):
        if feedback:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        

    