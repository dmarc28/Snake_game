import random
from turtle import Turtle
from turtle import *

x_position = [0, 10, 25]

blockade = (random.randint, random.randint)

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.color("blue")
            new_segment.shapesize(stretch_wid=-0.7)
            new_segment.speed("fastest")
            new_segment.penup()
            new_segment.goto(x=x_position[segment], y=0)
            self.segments.append(new_segment)

    def add_segment(self):
        for segment in range(2):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.goto(self.segments[-1].position())
            self.segments.append(new_segment)
            new_segment.color("blue")
            new_segment.shapesize(stretch_wid=-0.7)
            new_segment.speed("fastest")

    def move(self):
        for new_segment in range(len(self.segments) - 1, 0, -1):
            x = self.segments[new_segment - 1].xcor()
            y = self.segments[new_segment - 1].ycor()
            self.segments[new_segment].goto(x, y)
        self.segments[0].forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
