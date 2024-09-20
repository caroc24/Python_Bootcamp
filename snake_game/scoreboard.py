from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
