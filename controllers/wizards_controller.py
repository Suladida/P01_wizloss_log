from flask import Flask, redirect, render_template, request, Blueprint
from app import app
from models.wizard import Wizard
import repositories.wizard_repository as wiz_repo

@app.route('/')
def home():
    wizards = wiz_repo.select_all()
    return render_template('wizards/wizards.html', title = 'Home', wizards=wizards)

# @app.route('/<name>') 
# def greet(name): 
#     return f"Hello {name}!"

@app.route('/new')
def new():
    return render_template('wizards/new.html')

@app.route('/wizards', methods=['POST', 'GET'])
def add_wizard():
    wizFirstName = request.form['first_name']
    wizLastName = request.form['last_name']
    wizAge = request.form['age']
    newWizard = Wizard(first_name = wizFirstName, last_name = wizLastName, age = wizAge)
    wiz_repo.save(newWizard)
    wizards = wiz_repo.select_all()
    return render_template('wizards/wizards.html', title='Home', wizards=wizards)
