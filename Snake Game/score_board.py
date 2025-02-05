from turtle import *

FONT = ('Courier', 15, 'normal')
ALIGNMENT = "Center"
HIGHSCORE = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        with open(r"C:\Users\mkiam\Documents\Python Learning\100 days\Snake Game\data.txt") as data:
            self.high_score = float(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

    def show_score(self):
        self.clear()
        self.write(f"Score {self.scoreboard} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.scoreboard > self.high_score:
            self.high_score = self.scoreboard
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.scoreboard = 0
        self.show_score()

    def update_score(self):
        self.scoreboard += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
