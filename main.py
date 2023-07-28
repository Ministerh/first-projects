from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style= "text-align: center">Hello World!</h1>\
            <p>This is a paragraph</p>\
            <img src="https://media.giphy.com/media/10zxDv7Hv5RF9C/giphy.gif" width=150px>'


#This helps to take variable and convert variable input
@app.route("/<name>/<int:number>")
def greetings(name, number):
    return f"How are you {name}, you are {number} years old"


#make bold
def make_bold(function ):
    def bold():
        return "<b>" + function() + "</b>"
    return bold

def make_emphasis(function):
    def emphasis():
        return "<em>" + function() + "</em>"
    return emphasis

def make_underline(function):
    def underline():
        return "<u>" + function() + "</u>"
    return underline

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def greeting():
    return "Bye!"


if __name__ == "__main__":
    #to run app in debug mode
    app.run(debug=True)