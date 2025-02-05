from turtle import *

class paddle():

    POSITIONS = [(-280,0) (280,0)]

    def create_paddle(self, positions):
        for place in POSITIONS:



paddles = Turtle()
paddles.color("white")
paddles.shape("square")
paddles.penup()
paddles.shapesize(stretch_wid=5, stretch_len=1)
paddles.goto(290, 0)