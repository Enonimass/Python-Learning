import random
from turtle import *

MOVE_DISTANCE = 20
colors = ["orange", "blue", "yellow", "green", "red", "purple"]
MOVE_INCREMENT = 3


class Cars:
    def __init__(self):
        self.car_list = []
        self.car_speed = MOVE_INCREMENT

    def create_cars(self):
        random_choice = random.randint(1,6)
        if random_choice == 1 :
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            random_y = random.randint(-260, 280)
            new_car .goto(270, random_y)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(MOVE_DISTANCE)

    def clear_car(self):
        for car in self.car_list:
            car.hideturtle()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


