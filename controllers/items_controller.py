from flask import Flask, redirect, render_template, request, Blueprint
from models.item import Item
import repositories.item_repository as item_repo
from models.wizard import Wizard
import repositories.wizard_repository as wiz_repo

items_blueprint = Blueprint('items', __name__)

@items_blueprint.route('/items', methods=['GET'])
def home():
    items = item_repo.select_all()
    return render_template('items/index.html', title = 'Home', items=items)

@items_blueprint.route('/items/new', methods=['GET'])
def new():
    return render_template('items/new.html')

@items_blueprint.route('/edit')
def edit():
    return render_template('items/edit.html')

@items_blueprint.route('/items', methods=['POST'])
def add_item():
    item_type = request.form['type']
    item_colour = request.form['colour']
    item_style = request.form['style']
    wizard_id = request.form['wizard_id']
    item_wizard = wiz_repo.select(wizard_id)
    newItem = Item(type = item_type, colour = item_colour, style = item_style, wizard = item_wizard)
    item_repo.save(newItem)
    items = item_repo.select_all()
    return render_template('items/items.html', title='Home', items=items)

@items_blueprint.route("/items/<id>/edit", methods=['GET'])
def edit_item(id):
    item = item_repo.select(id)
    wizard = item.wizard.id
    return render_template('items/edit.html', item = item, wizard=wizard)

    # FINISH THIS