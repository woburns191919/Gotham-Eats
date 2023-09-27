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

    @property
    def get_images(self):
        menu_items = MenuItem.query.filter_by(restaurant_id=self.id).all()
        menu_item_image_urls = [menu_item.picture for menu_item in menu_items]
        preview_image = menu_item_image_urls[0] if menu_item_image_urls else None
        images = {
            'menu_item_images': menu_item_image_urls,
            'preview_image': preview_image
        }
        return images

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
            # 'images': self.images
        }
