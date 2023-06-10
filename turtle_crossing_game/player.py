from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.new_level()
        self.setheading(90)
        

    def move(self):
        #y_axis = self.ycor() + MOVE_DISTANCE
        #self.goto(self.xcor(), y_axis)
        self.forward(MOVE_DISTANCE)

    def cross_over(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
            
    def new_level(self):
        self.goto(STARTING_POSITION)

    


