from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Restaurant(db.Model, UserMixin):
  __tablename__ = 'restaurants'



  id = db.Column(db.Integer, primary_key=True)
  owner_id = db.Column(db.Integer, db.ForeignKey("users.id"),nullable=False)
  streetAddress = db.Column(db.String(255),nullable=False)
  city = db.Column(db.String(255), nullable=False)
  state = db.Column(db.String(50), nullable=False)
  postalCode=db.Column(db.String(50), nullable=False)
  country =db.Column(db.String(50),nullable=False)
  name = db.Column(db.String(255),nullable=False)
  description=db.Column(db.Text, nullable=False)
  hours = db.Column(db.Text, nullable=False)
  previmg=db.Column(db.Text)

  created_at=db.Column(db.DateTime, default=datetime.now())
  updated_at=db.Column(db.DateTime, default=datetime.now())

  user = db.relationship("User", back_populates="restaurants")
  reviews= db.relationship("Review", back_populates="restaurant")
  menu_items=db.relationship('MenuItem', back_populates='restaurant')
  menu=db.relationship('Menu',back_populates='restaurant',uselist=False)

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}


  def to_dict(self):
      return {
          'id': self.id,
          'owner_id': self.owner_id,
          'streetAddress': self.streetAddress,
          'city': self.city,
          'state': self.state,
          'postalCode': self.postalCode,
          'country': self.country,
          'name': self.name,
          'description': self.description,
          'hours': self.hours,
          'previmg': self.previmg
      }
