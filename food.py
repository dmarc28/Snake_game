import random
from turtle import *

from snake import Snake


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(-0.5)
        self.color("blue")
        self.speed("fastest")
        x_cor = random.randint(-50, 120)
        y_cor = random.randint(0, 120)
        # for segment in barrier.Barrier:
        #     segment_position_x = segment.xcor()
        #     segment_position_y = segment.ycor()
        #     if segment_position_x != x_cor and segment_position_y != y_cor:
        self.goto(x_cor, y_cor)
