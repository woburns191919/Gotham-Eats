from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255),nullable=False)
    lastName = db.Column(db.String(255),nullable=False)

    username = db.Column(db.String(40), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    email = db.Column(db.String(255), nullable=False, unique=True)
    streetAddress=db.Column(db.String(255),nullable=False)
    city= db.Column(db.String(255), nullable=False)
    state=db.Column(db.String(50), nullable=False)
    postalCode=db.Column(db.Integer, nullable=False)
    country=db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.now())
    updated_at=db.Column(db.DateTime, default=datetime.now())

    restaurants = db.relationship("Restaurant", back_populates="user")
    reviews = db.relationship("Review", back_populates="user")
    shopping_cart = db.relationship("ShoppingCart", back_populates="user", uselist=False)


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'username': self.username,
            'email': self.email,
            'streetAddress': self.streetAddress,
            'city': self.city,
            'state': self.state,
            'postalCode': self.postalCode,
            'country': self.country,
            'phone': self.phone
        }
