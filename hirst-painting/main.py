from turtle import Turtle, Screen, colormode
import random

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('sanrio.jpg', 15)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# returns [(253, 252, 244), (35, 27, 30), (30, 25, 19), (236, 205, 86), (228, 38, 44),
# (240, 154, 169), (130, 206, 241), (208, 170, 96), (20, 26, 34), (9, 103, 170),
# (19, 26, 21), (249, 246, 248), (143, 56, 62), (112, 93, 73), (247, 251, 249)]

color_list = [(30, 25, 19), (236, 205, 86), (228, 38, 44), (240, 154, 169), (130, 206, 241),
              (208, 170, 96), (20, 26, 34), (9, 103, 170), (19, 26, 21), (249, 246, 248),
              (143, 56, 62), (112, 93, 73), (247, 251, 249)]

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)


def draw_circle():
    tim.pendown()
    color = random.choice(color_list)
    tim.pencolor(color)
    tim.fillcolor(color)
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()
    tim.penup()


def draw_hirst():
    tim.penup()
    tim.goto(-200, -200)
    for i in range(1,11):
        for j in range(0,10):
            draw_circle()
            tim.forward(40)
        tim.goto(-200, -200+(i*40))


draw_hirst()
screen.exitonclick()
