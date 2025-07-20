from flask import Flask, render_template, flash, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            flash("Name is required!")
            return redirect(url_for("form"))
        flash(f"Thank you, {name}!, your feedback was saved")
        return redirect(url_for("thank_you"))
    return render_template("form.html")

@app.route("/thankyou")
def thank_you():
    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)