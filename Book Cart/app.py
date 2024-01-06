from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = '789'  # Replace with a secure secret key
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

db = sqlite3.connect('store.db', check_same_thread=False)
db.row_factory = sqlite3.Row

@app.route("/")
def index():
    c = db.cursor()
    books = c.execute("SELECT * FROM books")
    return render_template("books.html", books=books)

@app.route("/cart", methods=["POST", "GET"])
def cart():
    if "cart" not in session:
        session["cart"] = []

    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            session["cart"].append(book_id)
        return redirect("/cart")

    if session["cart"]:
        c = db.cursor()
        placeholders = ",".join(["?"] * len(session["cart"]))
        query = "SELECT * FROM books WHERE id IN ({})".format(placeholders)
        books = c.execute(query, session["cart"]).fetchall()
        return render_template("cart.html", books=books)

    return render_template("cart.html", books=[])

if __name__ == '__main__':
    app.run(debug=True)
