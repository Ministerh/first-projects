import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("minister turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()



screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #create the cars
    car.create_cars()

    #make the cars move
    car.move_car()


    #detects if turtle has crossed over and then level upgrade
    if player.cross_over():
        player.new_level()
        car.increase_move()
        score.update_level()
        print(car.car_speed)

    #detect collision of turtle with car
    for cars in car.all_cars:
        if player.distance(cars) < 20 :
            game_is_on = False
            score.game_over()



    

screen.exitonclick()
