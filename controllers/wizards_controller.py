from flask import Flask, redirect, render_template, Blueprint
from app import app

@app.route('/')
def index():
    return "Hello, World!"



# wizards_blueprint = Blueprint("wizards", __name__)

# @wizards_blueprint.route("/wizards")
# def tasks():
#     return render_template("wizards/index.html")