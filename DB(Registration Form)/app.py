from flask import Flask , render_template ,request , redirect
import sqlite3
import os

app= Flask(__name__)


conn = sqlite3.connect('reg.db',check_same_thread=False)
conn.row_factory = sqlite3.Row

SPORTS=["Football","Baseball","Tennis","Chess","Cricket"]

@app.route("/")
def index():
    return render_template("index.html",sports=SPORTS)

@app.route("/register" , methods=["POST"])
def register():
    name=request.form.get("name")
    if not name:
        return render_template("error.html" , message="missing name")
    sport=request.form.get("sport")
    if not sport:
        return render_template("error.html" , message="missing sport")
    if sport not in SPORTS:
        return render_template("error.html" , message="Invalid sport")

    c =  conn.cursor()
    c.execute("INSERT INTO registrants (name ,sport) VALUES (?,?)",(name, sport))
    conn.commit() 
    
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    c =  conn.cursor()
    registrants=c.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=registrants)


if __name__ == '__main__':
    app.run(debug=True)

