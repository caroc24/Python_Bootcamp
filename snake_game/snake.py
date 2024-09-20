from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20,0), (-40,0)]

class Snake:
    """Models the snake that plays the game"""
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(0, 3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(STARTING_POSITIONS[i])
            self.segments.append(new_segment)


