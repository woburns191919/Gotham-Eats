from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class MenuItemImg(db.Model, UserMixin):
    __tablename__ = 'menu_item_imgs'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}




    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer,nullable=False)
    url = db.Column(db.Text,nullable=False)
    preview = db.Column(db.Boolean,nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.now())
    updated_at=db.Column(db.DateTime, default=datetime.now())



    def to_dict(self):
        return {
          'id': self.id,
          'restaurant_id': self.restaurant_id,
          'url': self.url,
          'preview': self.preview
      }
