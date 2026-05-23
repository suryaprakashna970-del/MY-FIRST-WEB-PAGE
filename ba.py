from flask import Flask, render_template, request
import pandas as pd

df = pd.read_csv("surya.csv")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calcualte.html')


@app.route('/post', methods=["POST"])
def post_data():

    email = request.form.get("username")
    password = request.form.get("password")

    login = (df["email"] == email) & (df["password"] == password)

    if login.any(): # student login 
        return render_template("succecs_massage.html")
    else:
        return "Invalid Login"


if __name__ == "__main__":
    app.run(debug=True)