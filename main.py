import time
from scoreboard import Score
from food import Food
from snake import Snake
from turtle import *
from barrier import Barrier
import random

screen = Screen()
screen.setup(500, 500)
screen.tracer(0)


screen.listen()

segments = []

x_position = [0, 15, 30]

snake = Snake()
food = Food()
score = Score()
barrier = Barrier()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True
while game_on:
    screen.update()
    time.sleep(.3)
    snake.move()

    if snake.head.distance(food) < 15:
        barrier = Barrier()
        score.increase_score()
        food.hideturtle()
        print("Yay!!!")
        food = Food()
        add = snake.add_segment()
        # snake_position = snake.head.position()
        # if barrier.check_barrier():
        #     game_on = False
        #     score.game_over()

        # if snake.head.distance(barrier.all_pos_x) < 10:
        #     print("hit a barrier. Game End!!!")
        #     game_on = False
        #     score.game_over()
    elif snake.head.xcor() > 245 or snake.head.xcor() < -245:
        print("hit the wall. Game End!!!")
        game_on = False
        score.game_over()

    elif snake.head.ycor() > 245 or snake.head.ycor() < -245:
        print("hit the wall. Game End!!!")
        game_on = False
        score.game_over()

    elif snake.head.distance(barrier) < 5:
        print("hit a barrier. Game End!!!")
        game_on = False
        score.game_over()












# for position in POSITION:
#     new_segment.position(POSITION)


screen.exitonclick()
