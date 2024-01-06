from flask import Flask, render_template, request, redirect, session
import secrets

app = Flask(__name__)

# Securely generate a secret key
app.secret_key = secrets.token_hex(16)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("name", None)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
