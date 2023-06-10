from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = ("courier",15, "normal" ) 

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_track()

    
    def score_track(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, 
                   font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.score_track()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write ("GAME OVER", align=ALIGNMENT,  font=FONT)
        
    def update_score(self):
        self.score += 1
        self.score_track()
        