from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime



class MenuItem(db.Model, UserMixin):
    __tablename__ = 'menu_items'

    def add_prefix_for_prod(attr):
        if environment == "production":
            return f"{SCHEMA}.{attr}"
        else:
            return attr

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('restaurants.id')))
    menu_item_img_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('menu_item_imgs.id')))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float(10, 2), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    shopping_cart_id = db.Column(db.Integer)

    restaurant = db.relationship('Restaurant', back_populates='menu_items')
    menu_items_image = db.relationship('MenuItemImg', back_populates='menu_item', uselist=False)
    shopping_cart = db.relationship("ShoppingCart", back_populates="menu_items")


    def to_dict(self):

        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'menu_item_img_id': self.menu_item_img_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'type': self.type,
            'shopping_cart_id': self.shopping_cart_id,
        }
