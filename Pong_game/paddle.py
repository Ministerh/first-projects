from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        '''takes in a tuple for coordinates'''
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.speed("fastest")
        self.goto(position)
    
    def go_up(self):
        y_axis = self.ycor() + 20
        self.goto(self.xcor(), y_axis)

    def go_down(self):
        y_axis = self.ycor() - 20
        self.goto(self.xcor(), y_axis)
