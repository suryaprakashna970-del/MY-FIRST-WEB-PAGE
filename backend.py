from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        choice = request.form["choice"]
        number = request.form["number"]

        if choice == "Binary to Decimal":
            result = int(number, 2)

        elif choice == "Decimal to Binary":
            result = bin(int(number))[2:]
        
        elif choice == "Decimal to hexadecimal":
           result = hex(int(number))[2:]

    return render_template("calcualte.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)