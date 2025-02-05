from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(UP)
        self.goto(STARTING_POSITION)

    def move(self):
        if self.heading() != DOWN or self.heading() != RIGHT or self.heading() != LEFT:
            self.forward(MOVE_DISTANCE)

    def go_back(self):
        self.goto(STARTING_POSITION)
