from turtle import *


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 120)
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align='center', font=('arial', 12, 'normal'))

    def game_over(self):
        self.goto(0, 20)
        self.write("Game Over!!!", align='center', font=('arial', 12, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

