from turtle import Screen, Turtle
import time
from  paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)


right_paddle = Paddle((360, 0))
left_paddle = Paddle((-360, 0))
ball = Ball()
score = Scoreboard()



screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(left_paddle) <50 and ball.xcor() < -330 or ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.reset_position()
        score.r_point()

    if ball.xcor() < - 390:
        ball.reset_position()
        score.l_point()
        

        









screen.exitonclick()