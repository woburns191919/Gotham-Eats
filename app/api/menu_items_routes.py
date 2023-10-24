from flask import Blueprint, Flask, request, jsonify, redirect, url_for, abort
import app
from app.models import User, Restaurant, Review, db, MenuItem,MenuItemImg
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Restaurant, Review, db, MenuItem,MenuItemImg
from sqlalchemy import func, distinct, or_, desc
from ..forms import MenuItemForm
import json


menu_items = Blueprint('menu_items', __name__)


@menu_items.route('/', methods=['POST'])
def create_menu_item(restaurant_id):
    form = MenuItemForm()
    data = request.get_json()


    form.name.data = data.get('name')
    form.description.data = data.get('description')
    form.price.data = data.get('price')
    form.type.data = data.get('type')


    # if form.validate():
    new_menu_item = MenuItem(
        restaurant_id=restaurant_id,
        name=form.name.data,
        description=form.description.data,
        price=form.price.data,
        type=form.type.data
    )


    db.session.add(new_menu_item)
    db.session.commit()
    return jsonify(message="Successfully created new menu item", id=new_menu_item.id), 201
    # else:
    #     return jsonify(errors=form.errors), 400




# menu_items = Blueprint('menu_items', __name__)


# @menu_items.route('/new', methods=['POST'])
# def create_menu_item():
#     form =  MenuItemForm()
#     data = request.get_json()


#     form.restaurant_id.data = data.get('restaurant_id')
#     # form.menu_item_img_id.data = data.get('menu_item_img_id')
#     form.name.data = data.get('name')
#     form.description.data = data.get('description')
#     form.price.data = data.get('price')
#     form.type.data = data.get('type')


#     restaurant = Restaurant.query.get(form.restaurant_id.data)
#     if restaurant is None:
#         return jsonify(error="Restaurant not found"), 404


#     if form.validate():
#         new_menu_item = MenuItem(
#             restaurant_id=form.restaurant_id.data,
#             menu_item_img_id=form.menu_item_img_id.data,
#             name=form.name.data,
#             description=form.description.data,
#             price=form.price.data,
#             type=form.type.data
#         )


#         db.session.add(new_menu_item)
#         db.session.commit()
#         return jsonify(message="Successfully created new menu item", id=new_menu_item.id), 201
#     else:
#         return jsonify(errors=form.errors), 400
