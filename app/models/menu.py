from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Menu(db.Model, UserMixin):
  __tablename__ = 'menus'


  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

        id = db.Column(db.Integer, primary_key=True)
        restaurant_id = db.Column(db.Integer,nullable=False)



  def to_dict(self):
      return {
          'id': self.id,
          'restaurant_id': self.restaurant_id,
      }
