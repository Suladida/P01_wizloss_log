from flask import Flask, redirect, render_template, request, Blueprint
from models.wizard import Wizard
import repositories.wizard_repository as wiz_repo

wizards_blueprint = Blueprint('wizards', __name__)

@wizards_blueprint.route('/', methods=['GET'])
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

# EDIT: GET 'wizards/<id>/edit'
@wizards_blueprint.route("/wizards/<id>/edit", methods=['GET'])
def edit_wizard(id):
    wizard = wiz_repo.select(id)
    return render_template('wizards/edit.html', wizard = wizard)

@wizards_blueprint.route('/wizards/<id>', methods=['POST'])
def update_wizard(id):
    wizFirstName = request.form['first_name']
    wizLastName = request.form['last_name']
    wizAge = request.form['age']
    newWizard = Wizard(first_name = wizFirstName, last_name = wizLastName, age = wizAge, id=id)
    wiz_repo.update(newWizard)
    wizards = wiz_repo.select_all()
    return render_template('wizards/wizards.html', title='Home', wizards=wizards)

@wizards_blueprint.route('/wizards/<id>/delete', methods=["POST"])
def delete_wizard(id):
    wiz_repo.delete(id)
    wizards = wiz_repo.select_all()
    return render_template('wizards/wizards.html', title='Home', wizards=wizards)

# SHOW: GET 'wizards/<id>/items'
@wizards_blueprint.route('/wizards/<id>/items', methods=["GET"])
def view_wizard_items(id):
    wizard = wiz_repo.select(id)
    items = wiz_repo.select_all()
    return render_template('items/items.html', title='Home', wizard = wizard, items = items)

@wizards_blueprint.route("/wizards/<id>/new_item", methods=['GET'])
def new_item(id):
    wizard = wiz_repo.select(id)
    # wizard_id = wizard.id
    return render_template('wizards/new_item.html', wizard = wizard)

# "wizards/{{wizard.id}}/items"