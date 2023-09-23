from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Review(db.Model, UserMixin):
  __tablename__ = 'reviews'


  if environment == "production":
        __table_args__ = {'schema': SCHEMA}

        id = db.Column(db.Integer, primary_key=True)
        restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'),nullable=False)
        user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
        review = db.Column(db.Text,nullable=False)
        stars = db.Column(db.Integer, nullable=False)
        created_at=db.Column(db.DateTime, default=datetime.now())
        updated_at=db.Column(db.DateTime, default=datetime.now())

        user = db.relationship("User", back_populates="reviews")
        restaurant= db.relationship("Restaurant", back_populates='reviews')

  def to_dict(self):
      return {
          'id': self.id,
          'restaurant_id': self.restaurant_id,
          'user_id': self.user_id,
          'review': self.review,
          'stars': self.stars
      }
