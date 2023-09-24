from flask import Blueprint, jsonify
import app
from flask_login import login_required
from app.models import User, Restaurant, Review, db
from sqlalchemy import func, distinct, or_, desc
# from ..models.restaurants import

home_restaurants = Blueprint('restaurants', __name__)


@home_restaurants.route("/")
def get_popular_restaurants():

  restaurants = db.session.query(Restaurant).join(Review, Restaurant.id == Review.restaurant_id).\
    group_by(Restaurant.id).\
    order_by(func.avg(Review.stars).desc()).\
    all()

  all_restaurants = {'restaurants': [restaurant.to_dict() for restaurant in restaurants]}
  print('restaurants**', all_restaurants)
  return all_restaurants
