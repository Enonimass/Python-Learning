from turtle import *

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):  #Create the snake
        for place in POSITIONS:
            self.add_section(place)

    def add_section(self, place):       # Add a section to the snake
        new_section = Turtle(shape="square")
        #new_section.hideturtle()
        new_section.penup()
        new_section.color("white")
        new_section.goto(place)
        self.segments.append(new_section)

    def extend(self):
        self.add_section(self.segments[-1].position())

    def move(self):  #funtion to move the snake
        for seg_num in range(len(self.segments)-1, 0, -1):  #Count the length from the last to the first
            new_xcor = self.segments[seg_num - 1].xcor()
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
