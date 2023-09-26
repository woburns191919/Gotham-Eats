from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class ShoppingCart(db.Model, UserMixin):
    __tablename__ = 'shopping_carts'

    def add_prefix_for_prod(attr):
        if environment == "production":
           return f"{SCHEMA}.{attr}"
        else:
           return attr

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    menu_item_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("menu_items.id")))
    quantity = db.Column(db.Integer, nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.now())
    updated_at=db.Column(db.DateTime, default=datetime.now())

    menu_items = db.relationship("MenuItem", back_populates="shopping_cart")
    user = db.relationship("User", back_populates="shopping_cart")

    def to_dict(self):
      return {
          'id': self.id,
          'user_id': self.user_id,
          'menu_item_id': self.menu_item_id,
          'quantity': self.quantity,
            }
