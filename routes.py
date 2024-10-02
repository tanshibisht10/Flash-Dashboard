from application import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html',title = "index",div="School",href="/layout",h4="Student")

@app.route("/layout")
def layout():
    return render_template('layout.html',title = "layout",div="Student",href="/",h4="School")