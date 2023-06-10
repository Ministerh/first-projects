from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in POSITIONS:
            self.add_snake(i)

    def add_snake(self, position):
        huz = Turtle()
        huz.shape("square")
        huz.color("white")
        huz.penup()
        huz.goto(position)
        self.snake.append(huz)

    def extend(self):
       # extends the length of the snake
        self.add_snake(self.snake[-1].position())

    def reset(self):
        for body in self.snake:
            body.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]


    def move(self):
        for square in range(len(self.snake)- 1, 0, -1):
            new_x = self.snake[square - 1].xcor()
            new_y = self.snake[square - 1].ycor()
            self.snake[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self): 
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)