from flask import Flask, render_template
import random
from datetime import datetime
import requests


app = Flask(__name__)

@app.route("/")
def index():
    random_number = random.randint(10, 20)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year= current_year)

@app.route("/guess/<name>")
def guess(name):
    age_prediction = f"https://api.agify.io?name={name}"
    response = requests.get(url=age_prediction)
    age = response.json()["age"]
    gender_predictor = f"https://api.genderize.io?name={name}"
    responsed = requests.get(url=gender_predictor)
    gender = responsed.json()["gender"]
    return render_template("index1.html", my_name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)
