import turtle
#to import everything ina module using it like working directly i the module use
#from turtle import * the asteric sign does the trick
#You can redefine a module name i.e import turtle as t
import random
turtle.colormode(255)
def turtle_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color

huz = turtle.Turtle()
huz.shape("arrow")
huz.color("blue")
#Draw a square
#for n in range(4):
#    huz.forward(100)
#    huz.right(90)
# Draw a dash line
#    huz.forward(10)
#    huz.penup()
#    huz.forward(10)
#    huz.pendown()
# Draw polygon
#color = ["blue", 'red', "green", "yellow", "orange", "purple", "grey", "palegreen", "pink", "hotpink", "darkblue", "violet", "darkred", "indigo"]
directions = [0, 90, 180, 270]
#huz.pensize(10)
#huz.speed(10)
huz.speed("fastest")
# def shapes(num_of_sides):
#     angle = 360/num_of_sides
#     for n in range(num_of_sides):
#         huz.forward(100)
#         huz.right(angle)
# for n in range(3,11):
#     huz.color(random.choice(color))
#     shapes(n)
# for i in range(200):
#     huz.color(turtle_color())
#     huz.forward(20)
#     huz.setheading(random.choice(directions))

def spirograph(turning_angle):
    for i in range(int(360/turning_angle)):
        huz.color(turtle_color())
        huz.circle(100)
        huz.setheading(huz.heading() + turning_angle)

spirograph(5)
screen = turtle.Screen()
screen.exitonclick()