from flask import Flask, redirect, render_template, Blueprint
from app import app
from models.wizard import Wizard
import repositories.wizard_repository as wiz_repo

@app.route('/')
def home():
    wizards = wiz_repo.select_all()
    return render_template('wizards/index.html', title = 'Home', wizards=wizards)

@app.route('/<name>') 
def greet(name): 
    return f"Hello {name}!"