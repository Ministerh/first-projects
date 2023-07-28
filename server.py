from flask import Flask
import random

random_number = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>"Guess a number between 0 and 9</h><p></p>\
            <img src= " https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width= 200px>'
@app.route("/<int:number>")
def lower(number):
    if number <  random_number:
        return '<h1 style=" color: green" >Too low, try again</h1><p></p>\
                <img src="https://giphy.com/clips/bestfriends-best-friends-kittens-animal-sanctuary-WRS4XjSveV8uDIJ8GD" width= 200px>'
    elif number > random_number:
        return '<h1 style= "color: red" >Too low High, try again</h1><p></p>\
                <img src="https://giphy.com/clips/bestfriends-best-friends-adopt-animal-adoption-cwQCUhKible5mGrtMO" width= 200px>'
    else:
        return '<h1 style= "color: blue" >You found me! </h1><p></p>\
                <img src="https://giphy.com/clips/bestfriends-animals-best-friends-adoption-rZRH50AE6g2M02IhTK" width=200px'
if __name__ == "__main__":
    #to run app in debug mode
    app.run(debug=True)