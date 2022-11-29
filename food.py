import random
from turtle import *


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(-0.5)
        self.color("blue")
        self.speed("fastest")
        x_cor = random.randint(0, 245)
        y_cor = random.randint(0, 245)
        self.goto(x_cor, y_cor)
