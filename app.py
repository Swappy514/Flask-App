from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    """" if username == "swappy!" and password == "514":
        return render_template("welcome.html", name=username) """

    valid_user = {
        "swappy!": "514",
        "admin": "123",
        "user": "pass"
    }
    if username in valid_user and password == valid_user[username]:
        return render_template("welcome.html", name=username)
    else:
        return "Invalid credentials"


if __name__ == "__main__":
    app.run(debug=True)
