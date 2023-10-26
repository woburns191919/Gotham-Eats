from flask import Blueprint, request, jsonify
from app.models import db, MenuItem, MenuItemImg

menu_items = Blueprint('menu_items', __name__)

@menu_items.route('/', methods=['POST'])
def create_menu_item(restaurant_id):
    try:
        data = request.get_json()

        counter = 588

        new_menu_item = MenuItem(
            restaurant_id=restaurant_id,
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            type=data.get('type'),
            menu_item_img_id=counter+1,
            itm_img_url=data.get("itm_img_url")

        )

        db.session.add(new_menu_item)
        db.session.commit()

        if data.get('url'):
            new_menu_item_img = MenuItemImg(
                menu_item_id=new_menu_item.id,
                url=data.get('url')
            )

            db.session.add(new_menu_item_img)
            db.session.commit()

        return jsonify(message="Successfully created a new menu item", id=new_menu_item.id), 201
    except Exception as e:
        return jsonify(error=str(e)), 500

@menu_items.route('/<int:menu_item_id>', methods=['DELETE'])
def delete_menu_item(restaurant_id, menu_item_id):
    try:

        menu_item = MenuItem.query.get(menu_item_id)

        if menu_item:
            if menu_item.restaurant_id == restaurant_id:
                db.session.delete(menu_item)
                db.session.commit()
                return jsonify(message="Menu item deleted successfully"), 200
            else:
                return jsonify(error="Menu item does not belong to the specified restaurant"), 403
        else:
            return jsonify(error="Menu item not found"), 404
    except Exception as e:
        return jsonify(error=str(e)), 500
