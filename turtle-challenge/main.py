from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)
tim.color(0, 255, 0)

tim.speed("fastest")

colors = ["CornflowerBlue", "DarkOrchid", "DeepSkyBlue", "SlateGray", "SeaGreen", "blue", "red", "orange", "pink",
          "indigo", "turquoise", "green", "yellow", "violet", "navy", "wheat"]


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


# draw a square
def draw_square():
  for _ in range(4):
    tim.forward(100)
    tim.right(90)


# draw a dotted line
def draw_line():
    for _ in range(10):
        tim.forward(5)
        tim.penup()
        tim.forward(5)
        tim.pendown()


# draw triangle, square, all the way to a decagon
def draw_shape(num_sides, num):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

    for i in range(3, 11):
        tim.color(random_color())
        draw_shape(num)


# draw a random walk in different colors, quickly:

def random_walk():
    tim.color(random_color())
    tim.forward(random.randint(50, 100))


def random_direction():
    direction = [0, 90, 180, 270]
    tim.left(random.choice(direction))


def circle_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + gap_size)


circle_spirograph(2)


screen.exitonclick()