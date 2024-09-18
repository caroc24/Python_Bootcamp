from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-75, -45, -15, 15, 45, 75]

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_pos[i])

# makes sure race doesn't start until user places bet
if user_bet:
    is_race_on = True

while is_race_on:

screen.exitonclick()