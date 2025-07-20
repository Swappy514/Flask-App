from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"

# homepage login page


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username  # store user in session
            return redirect(url_for("Welcome"))
        else:
            return Response("Invalid credentials", mintype="text/plain")
    return '''
        <h2>Login Page</h2>
        <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
        </form>
    '''

# welcome page after login


@app.route("/welcome")
def Welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session["user"]}!</h2>
        <a href="{url_for('Logout')}">Logout</a>
    '''
    return redirect(url_for("Login"))

# logout page


@app.route("/logout")
def Logout():
    session.pop("user", None)  # remove user from session
    return redirect(url_for("login"))


# ...existing code...

if __name__ == "__main__":
    app.run(debug=True)
