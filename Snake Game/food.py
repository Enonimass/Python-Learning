import random
from turtle import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        #self.food.hideturtle()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()


    def refresh(self):      # the food goes to a random position within the screen
        x_random = random.randint(-270, 270)
        y_random = random.randint(-270, 270)
        self.goto(x_random, y_random)
