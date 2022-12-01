import random
from turtle import Turtle

# len_list = []
# for i in range(0, 80):
#     i += 1
#     len_list.append(i)


class Barrier:
    def __init__(self):
        # super.__init__()
        self.barrier = []
        # self.create_barrier()
        # self.head_barrier = self.barrier[0]

    # def create_barrier(self):
    #     screen_width_len = [()]
    #     start_point = random.choice(len_list)
    #     x_position = [start_point, start_point - 10, start_point - 20, start_point - 30,
    #                       start_point - 40, start_point - 50, start_point - 60]
    #     hurdle_len = random.randint(2, 7)
    #     y_cor_start = random.randint(0, 140)
    #     for segment in range(hurdle_len):
    #         new_segment = Turtle(shape="square")
    #         new_segment.color("red")
    #         new_segment.shapesize(stretch_wid=-0.5)
    #         new_segment.speed("fastest")
    #         new_segment.penup()
    #         # x_cor = random.randint(0, 240)
    #         # y_cor = random.randint(0, 240)
    #         new_segment.goto(x=x_position[segment], y=y_cor_start)
    #         self.barrier.append(new_segment)

    def hide_barrier(self):
        for segments in self.barrier:
            segments.hideturtle()
