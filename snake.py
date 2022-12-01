import random
from turtle import Turtle
from turtle import *
from barrier import Barrier

x_position = [0, 10, 20]

blockade = (random.randint, random.randint)

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Barrier):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.color("blue")
            new_segment.shapesize(stretch_wid=-0.5, stretch_len=-0.5)
            new_segment.speed("fastest")
            new_segment.penup()
            new_segment.goto(x=x_position[segment], y=0)
            self.segments.append(new_segment)

    def add_segment(self):
        for segment in range(1):
            new_segment = Turtle(shape="square")
            new_segment.shapesize(stretch_wid=-0.5, stretch_len=-0.5)
            new_segment.penup()
            new_segment.goto(self.segments[-1].position())
            self.segments.append(new_segment)
            new_segment.color("blue")
            new_segment.speed("fastest")

    def check_collision(self):
        for segment in self.barrier:
            segment_position = segment.position()
            if self.head.distance(segment_position) < 10:
                return True

    def tail_collision(self):
        for segment in self.segments[1:]:
            segment_position = segment.position()
            if self.head.distance(segment_position) < 10:
                return True

    def move(self):
        for new_segment in range(len(self.segments) - 1, 0, -1):
            x = self.segments[new_segment - 1].xcor()
            y = self.segments[new_segment - 1].ycor()
            self.segments[new_segment].goto(x, y)
        self.head.forward(10)

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

    def create_barrier(self):
        barrier_direction = [0, 90, 180]
        len_list = []
        for i in range(-100, 100):
            i += 1
            len_list.append(i)
        start_point = random.choice(len_list)
        x_position = [start_point, start_point - 10, start_point - 20]
        hurdle_len = random.randint(1, 3)
        y_cor_start = random.randint(-140, 140)
        for segment in range(hurdle_len):
            new_segment = Turtle(shape="square")
            new_segment.color("red")
            new_segment.shapesize(stretch_wid=-0.5, stretch_len=-0.5)
            new_segment.speed("fastest")
            new_segment.penup()
            new_segment.goto(x=x_position[segment], y=y_cor_start + 10)
            new_segment.right(random.choice(barrier_direction))
            self.barrier.append(new_segment)
