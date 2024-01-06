from flask import Flask ,request ,render_template

#configure app
app= Flask(__name__) # main App


@app.route("/") # root directory
@app.route("/<user>")
def index(user=None):
    return render_template("user.html",user=user)


@app.route("/world")
def world():
    return "<h2>Hello World</h2>"

#using variables
@app.route("/profile/<username>")
def profile(username):
    return "Hi %s" %username

@app.route("/post/<int:post_id>")
def post(post_id):
    return "Post No. %s" %post_id

@app.route("/method_get")
def method_get():
    return "Method Used: %s" %request.method

@app.route("/method",methods=['GET','POST'])
def method():
    if request.method=='POST':
        return "Method: POST"
    else:
        return "Method: GET"

@app.route("/account/<name>")
def account(name):
    return render_template("account.html",name=name)

@app.route("/shopping")
def shopping():
    food=["cheese","Salt","Pea","salmon"]
    return render_template("shop.html",food=food)


if __name__ == '__main__':
    app.run(debug=True)

