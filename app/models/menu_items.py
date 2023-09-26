from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class MenuItem(db.Model, UserMixin):
    __tablename__ = 'menu_items'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(
        'restaurants.id'), nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float(10, 2), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    shopping_cart_id = db.Column(
        db.Integer, db.ForeignKey('shopping_carts.id'))
    picture = db.Column(db.Text, nullable=False)

    restaurant = db.relationship('Restaurant', back_populates='menu_items')
    shopping_cart = db.relationship(
        "ShoppingCart", back_populates="menu_items")
    menu = db.relationship("Menu", back_populates='menu_items')


    def to_dict(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'menu_id': self.menu_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'type': self.type,
            'shopping_cart_id': self.shopping_cart_id,
            'picture': self.picture
        }
