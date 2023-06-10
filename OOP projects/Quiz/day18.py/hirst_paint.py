import colorgram
# colors = colorgram.extract('hirst.jpg', 15)
# print(colors)
import random
# new_color = []
def coloring():
     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     my_color = (r, g, b)
     return my_color
#     new_color.append(my_color)

import turtle as t
t.colormode(255)

#color_list = [(45, 35, 211), (103, 106, 215), (61, 8, 77), (229, 176, 200), (64, 100, 173), (250, 79, 68), (74, 87, 193), (161, 208, 88), (48, 47, 212), (187, 173, 11), (119, 8, 155), (205, 235, 204), (125, 105, 155), (201, 219, 0), (128, 12, 2), (62, 64, 61), (108, 47, 181), (193, 188, 220), (41, 126, 69), (207, 117, 205)]
paint = t.Turtle()
paint.speed("fastest")
paint.penup()
paint.hideturtle()
paint.setheading(225)
paint.forward(300)
paint.setheading(0)
dots = 161
for dot in range(1, dots):
    paint.dot(20, coloring())
    paint.forward(50)
    if dot % 10 == 0:
        paint.setheading(90)
        paint.forward(30)
        paint.setheading(180)
        paint.forward(500)
        paint.setheading(0)


screen = t.Screen()
screen.exitonclick()
