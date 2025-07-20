from flask import Flask, render_template, url_for, request, redirect, flash
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome, {name}! Your registration was successful.", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)