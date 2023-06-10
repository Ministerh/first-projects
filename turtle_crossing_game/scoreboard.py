from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font = FONT)
        
    def update_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write ("GAME OVER", align= "CENTER",   font=FONT)
    
