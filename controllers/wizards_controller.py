from flask import Flask, redirect, render_template, request, Blueprint
from models.wizard import Wizard
import repositories.wizard_repository as wiz_repo

wizards_blueprint = Blueprint('wizards', __name__)

@wizards_blueprint.route('/')
def home():
    wizards = wiz_repo.select_all()
    return render_template('wizards/wizards.html', title = 'Home', wizards=wizards)

@wizards_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('wizards/new.html')

@wizards_blueprint.route('/edit')
def edit():
    return render_template('wizards/edit.html')

@wizards_blueprint.route('/wizards', methods=['POST'])
def add_wizard():
    wizFirstName = request.form['first_name']
    wizLastName = request.form['last_name']
    wizAge = request.form['age']
    newWizard = Wizard(first_name = wizFirstName, last_name = wizLastName, age = wizAge)
    wiz_repo.save(newWizard)
    wizards = wiz_repo.select_all()
    return render_template('wizards/wizards.html', title='Home', wizards=wizards)

# SHOW: GET 'wizards/<id>'
@wizards_blueprint.route("/wizards/<id>", methods=['GET'])
def show_wizard(id):
    wizard = wiz_repo.select(id)
    return render_template('wizards/show.html', wizard = wizard)




# @wizards_blueprint.route("/wizards/<id>", methods=['GET'])
# def show_wizard(id):
#     wizard = wiz_repo.select(id)
#     return render_template('books/show.html', wizard = wizard)


# @wizards_blueprint.route('/show', methods=['POST', 'GET'])
# def edit_wizard():
#     wizFirstName = request.form['first_name']
#     wizLastName = request.form['last_name']
#     wizAge = request.form['age']
#     newWizard = Wizard(first_name = wizFirstName, last_name = wizLastName, age = wizAge)
#     wiz_repo.update(newWizard)
#     wizards = wiz_repo.select_all()
#     return render_template('wizards/show.html', title='Home', wizards=wizards)