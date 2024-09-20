from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

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

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        for seg_num in range(0, len(self.segments)):
            self.segments[seg_num].setheading(0)

    def down(self):
        for seg_num in range(0, len(self.segments)):
            self.segments[seg_num].setheading(180)

    def left(self):
        for seg_num in range(0, len(self.segments)):
            self.segments[seg_num].setheading(270)

    def right(self):
        for seg_num in range(0, len(self.segments)):
            self.segments[seg_num].setheading(90)