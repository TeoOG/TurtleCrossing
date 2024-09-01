import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_object_list = []
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

time_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(time_speed)
    # print(f" time speed is {time_speed}\n")
    screen.update()

    new_car = CarManager()
    car_object_list.append(new_car)

    for car in car_object_list:
        car.move()

    if player.ycor() > 280:
        scoreboard.increase_level()
        player.refresh()
        time_speed *= 0.5

    for car in car_object_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
