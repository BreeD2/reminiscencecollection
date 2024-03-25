from flask import Flask, request, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Example user storage. In a real application, use a database.
users = {}

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "User already exists!"
        else:
            hashed_password = generate_password_hash(password)
            users[username] = hashed_password
            return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user, password):
            return "Logged in successfully!"
        else:
            return "Invalid credentials!"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
