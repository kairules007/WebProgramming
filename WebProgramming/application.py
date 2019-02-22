from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():  
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    game = request.form.get("game")

    if not name or not game:
        return render_template("failure.html")
    return render_template("success.html")    