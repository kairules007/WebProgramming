from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route("/")
def index():  
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", students = students)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    game = request.form.get("game")

    if not name or not game:
        return render_template("failure.html")

    students.append(f"{name} voted for {game}")
    return redirect("/registrants")    