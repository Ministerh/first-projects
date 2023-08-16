from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

api = " https://api.npoint.io/c790b4d5cab58020d391"

@app.route("/")
def home_page():
    response = requests.get(url=api).json()
    now = datetime.now()
    return render_template("index.html", blog = response, date = now)

@app.route("/about")
def about_page():
    
    return render_template('about.html')

@app.route("/contact")
def contact_page():
    return render_template('contact.html')


if __name__ == "__main__" :

    app.run(debug=True)

