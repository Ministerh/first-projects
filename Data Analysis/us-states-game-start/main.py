import turtle

screen = turtle.Screen()
screen.title("U.S States Game" )
#to use image as background in turtle then it has to be saved in gif format
image = './Data Analysis/us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
actual_guess = 50

import pandas
data = pandas.read_csv("./Data Analysis/us-states-game-start/50_states.csv")
state_data = data.state.to_list()
all_state = []

while len(all_state) < actual_guess:
    guess = screen.textinput(title=f"{len(all_state)}/{actual_guess} States Correct", prompt= "what's another sate").title()

    if guess == "Exit":
        missing_state = [state for state in state_data if state not in all_state ]
        #missing_state = []
        # for state in state_data:
        #     if state not in all_state:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("./Data Analysis/states to learn.csv")
        break
    if guess in state_data:
        all_state.append(guess)
        d_state = data[data.state == guess] 
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(d_state.x), int(d_state.y))
        t.write(guess)
            

#To get coordinates on turtle screen use this
# def get_coord_with_mouse(x, y):
#     print(x, y)

# turtle.onscreenclick(get_coord_with_mouse)


# or use exitonclick method

