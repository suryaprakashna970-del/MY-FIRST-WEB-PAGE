from flask import Flask, render_template, request
import pandas as pd

df = pd.read_csv("surya.csv")
tedf = pd.read_csv("teacher.csv")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calcualte.html')


@app.route('/post', methods=["POST"])
def post_data():

    email = request.form.get("username")
    password = request.form.get("password")

    login = (df["email"] == email) & (df["password"] == password)
    teacher_login = (tedf["email"] == email) & (tedf["password"] == password)

    if login.any():
        return render_template("student.html")

    elif teacher_login.any():
        return render_template("teacher.html")

    else:
        return render_template("calcualte.html", error="Invalid Login")


if __name__ == "__main__":
    app.run(debug=True)