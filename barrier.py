import random
from turtle import *


barrier = []

class Barrier(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(-0.5)
        self.color("red")
        self.speed("fastest")
        x_cor = random.randint(0, 240)
        y_cor = random.randint(0, 240)



        self.goto(x_cor, y_cor)
