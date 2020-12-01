from flask import Flask, redirect, render_template, request, Blueprint
from models.item import Item
import repositories.item_repository as item_repo

items_blueprint = Blueprint('items', __name__)

@items_blueprint.route('/items', methods=['GET'])
def home():
    items = item_repo.select_all()
    return render_template('items/index.html', title = 'Home', items=items)