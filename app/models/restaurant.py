from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Restaurant(db.Model, UserMixin):
  __tablename__ = 'restaurants'

  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

  id = db.Column(db.Integer, primary_key=True)
  owner_id = db.Column(db.Integer,nullable=False)
  address = db.Column(db.String(100),nullable=False)
  hours = db.Column(db.Text, nullable=False)
  city = db.Column(db.String(40), nullable=False)
  state = db.Column(db.String(40), nullable=False)
  country =db.Column(db.String(40),nullable=False)
  name = db.Column(db.String(40),nullable=False)
  description=db.Column(db.Text, nullable=False)
  created_at=db.Column(db.DateTime, default=datetime.now())
  updated_at=db.Column(db.DateTime, default=datetime.now())


  def to_dict(self):
      return {
          'id': self.id,
          'owner_id': self.owner_id,
          'address': self.address,
          'hours': self.hours,
          'city': self.city,
          'state': self.state,
          'country': self.country,
          'name': self.name,
          'description': self.description,
      }
