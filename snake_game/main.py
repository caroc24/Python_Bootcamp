from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[seg_num - 1].xcor()
        new_y = snake_body[seg_num - 1].ycor()
        snake_body[seg_num].goto(new_x, new_y)
    snake_body[0].forward(20)

screen.exitonclick()