import turtle as t

#for color
import random
# t.colormode(255)
# def turtle_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_color = (r, g, b)
#     return my_color

def movement():
    move = random.randint(20, 50)
    return move

screen = t.Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? enter a color:")

color = ["red", "blue", "yellow", "green", "black", "grey"]
y_positions =  [70, 40, 10, -20, -50, -80]
turtles = []
race_on = False

for n in range(0, 6):
    new_turtle = t.Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(color[n])
    new_turtle.goto(x= -235, y = y_positions[n])
    turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You've won! the winner is {winner}")
            else:
                print(f"You've lost! The winner is {winner}")
        speed =random.randint(0, 10)
        turtle.forward(speed)

screen.exitonclick()