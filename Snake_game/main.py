from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()
    #detects collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor()< -290 or snake.head.ycor()>290 or snake.head.ycor()< -290:
        score.reset()
        snake.reset()
        

    #detects collision with tail
    for body in snake.snake[1:]:
        #if body == snake.head:
        #    pass
        #using slicing
        if snake.head.distance(body) < 10:
            score.reset()
            snake.reset()
            


        
            





screen.exitonclick()