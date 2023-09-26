from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class MenuItemImg(db.Model, UserMixin):
    __tablename__ = 'menu_item_imgs'

    def add_prefix_for_prod(attr):
        if environment == "production":
            return f"{SCHEMA}.{attr}"
        else:
            return attr
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    menu_item_id = db.Column(db.Integer)
    url = db.Column(db.Text,nullable=False)
    preview = db.Column(db.Boolean,nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.now())
    updated_at=db.Column(db.DateTime, default=datetime.now())

    menu_item = db.relationship("MenuItem", back_populates='menu_items_image')




    def to_dict(self):
        return {
          'id': self.id,
          'menu_item_id': self.menu_item_id,
          'url': self.url,
          'preview': self.preview
      }
