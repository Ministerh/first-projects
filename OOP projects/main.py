#this import the turtle module from the library
#import turtle
# using the module the class Turtle is fetched
#ade = turtle.Turtle()
#the class Turle itself can be imported
# from turtle import Turtle, Screen
# ade = Turtle()
# print(ade)
# ade.shape("turtle")
# ade.color("red")
#ade.forward(100)
# my_screen is the object being modified from the class Screen
#my_screen = Screen()
#the attribute/properties can be tapped using dot(.)
#print(my_screen.canvheight)
#tis helps to  use function called method 
#my_screen isthe object while exitonclick is the method
#my_screen.exitonclick()
from prettytable import PrettyTable
 
table = PrettyTable()
table.add_column("Pokemon Name", ["PIkachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.border = False
print(table)

