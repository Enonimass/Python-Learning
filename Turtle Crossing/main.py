from turtle import *
import time
from player import Player
from car import Cars

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
cars = Cars()

game_is_on = True
screen.listen()
screen.onkey(player.move, 'Up')

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    # Detect collision with cars
    for car in cars.car_list:
        if player.distance(car) < 15:
            game_is_on = False

    # Detect when player goes to the other side
    if player.ycor() > 300:
        cars.clear_car()
        player.go_back()
