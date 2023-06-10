from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = ("courier",75, "normal" ) 
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup() 
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self. goto(-100, 190)
        self.write(self.l_score, align = ALIGNMENT, font = FONT)
        self. goto(100, 190)
        self.write(self.r_score, align = ALIGNMENT, font = FONT)

    def r_point(self):
        self.r_score += 1
        self.update()

    def l_point(self):
        self.l_score += 1
        self.update()
        