from flask import Flask, render_template, request, redirect
import csv 

app = Flask(__name__)

students = []

@app.route("/")
def index():  
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    file = open("registered.csv","r")
    reader = csv.reader(file)
    students = list(reader)
    return render_template("registered.html",students=students)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    game = request.form.get("game")

    if not name or not game:
        return render_template("failure.html")

    file = open("registered.csv","a")
    writer = csv.writer(file)
    writer.writerow((name,game))
    file.close
    return redirect("/registrants")