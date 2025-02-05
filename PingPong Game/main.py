from turtle import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")




game_is_on = True

def go_up():
    y_cord = paddle.ycor() + 30
    paddle.goto(paddle.xcor(), y_cord)

def go_down():
    y_cord = paddle.ycor() - 30
    paddle.goto(paddle.xcor(),y_cord)

screen.listen()
screen.onkey(go_up,"Up" )
screen.onkey(go_down,"Down" )

screen.exitonclick()