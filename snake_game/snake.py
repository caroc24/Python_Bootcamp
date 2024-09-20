from turtle import Turtle
class Snake:
    """Models the snake that plays the game"""
    def __init__(self):
        snake_body = []
        for i in range(0, 3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=i * -20, y=0)
            snake_body.append(new_segment)


