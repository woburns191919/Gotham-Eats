from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Menu(db.Model, UserMixin):
  __tablename__ = 'menus'


  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

        id = db.Column(db.Integer, primary_key=True)
        restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurants.id'),nullable=False)
        menu_items=db.relationship('MenuItem',back_populates='menu')
        restaurant=db.relationship('Restaurant',back_populates='menu')


  def to_dict(self):
      return {
          'id': self.id,
          'restaurant_id': self.restaurant_id,
      }
