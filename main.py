import time
import turtle

from scoreboard import Score
from food import Food
from snake import Snake
from turtle import Screen


screen = Screen()
screen.setup(300, 300)
screen.tracer(0)

screen.listen()

segments = []

snake = Snake()
food = Food()
score = Score()

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
        snake.create_barrier()
        score.increase_score()
        food.hideturtle()
        food = Food()
        add = snake.add_segment()

    elif snake.head.xcor() > 130 or snake.head.xcor() < -130:
        game_on = False
        break

    elif snake.head.ycor() > 130 or snake.head.ycor() < -130:
        game_on = False
        break

    elif snake.check_collision():
        game_on = False
        break

    # elif snake.tail_collision():
    #     game_on = False
    #     break


response = (screen.textinput("Hit a barrier! You Lost!", "Restart? Y or N? :")).lower()
if "y" in response:
    turtle.clearscreen()
    exec(open("main.py").read())
else:
    exit()

screen.exitonclick()
