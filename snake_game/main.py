from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_body = []


def create_snake():
    for i in range(0, 3):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=i*-20, y=0)
        snake_body.append(new_segment)


# def move_forward(snake):
#     for segment in snake_body:
#         segment.forward(20)
#         screen.update()


game_is_on = True
create_snake()
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[seg_num - 1].xcor()
        new_y = snake_body[seg_num - 1].ycor()
        snake_body[seg_num].goto(new_x, new_y)
    snake_body[0].forward(20)

screen.exitonclick()