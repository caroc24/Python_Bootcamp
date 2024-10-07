import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

num_correct = 0
correct_guesses = []
game_is_on = True

while len(correct_guesses) < 50:
    title = f"{num_correct}/50 States Correct"
    answer_state = screen.textinput(title=title, prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        need_to_learn = [state for state in states_list if state not in correct_guesses]
        # for state in states_list:
        #     if state not in correct_guesses:
        #         need_to_learn.append(state)
        new_data = pandas.DataFrame(need_to_learn)
        new_data.to_csv("states_to_learn")

    if answer_state in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

        num_correct += 1
        correct_guesses.append(answer_state)

screen.exitonclick()
