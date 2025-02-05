from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]# Rainbow colors fot turtles colors
y_positions = [-150, -100, -50, 50, 0, 100]
turtles_list = []

#Create 6 turtles and ad them to turtles list
for turtles in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtles])
    tim.penup()
    tim.goto(x=-240, y=y_positions[turtles])
    turtles_list.append(tim)

if user_bet:
    is_race_on = True

while is_race_on :
    for turtle in turtles_list:
        if turtle.xcor() >230: # end race when a turle reaches 230
            is_race_on=False
            winner = turtle.pencolor() # get the winning turtle
            if user_bet == winner:
                print(f"Congratulations You won .{winner}  is the winner")
            else:
                print(f"Sorry you lost .{winner}  is the winner")
        random_distance = random.randint(0,10) #make the turtles move at a random distance
        turtle.forward(random_distance)


screen.exitonclick()  # make screen on
