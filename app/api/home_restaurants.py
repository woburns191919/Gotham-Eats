from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Restaurant, Review, db
# from ..models.restaurants import

home_restaurants = Blueprint('restaurants', __name__)


@home_restaurants.route("/")
def get_popular_restaurants():
  restaurants = Restaurant()
  print('confetti****')

  # all_restaurants = Restaurant.query.order_by(Restaurant.avg_stars.desc()).all()
  # print('restaurants****', all_restaurants)
  all_restaurants = db.session.query(restaurants)

  print('restaurants***', all_restaurants)
  # print('all restaurants list****', [restaurant.to_dict() for restaurant in all_restaurants])

#     print('restaurant*****', restaurant.name)
#     print('avg_stars****', restaurant.avg_stars)
get_popular_restaurants()
#   user = User.query.all()
#   print('user instance*******', user)
# review = Review()
# print('reviews****', review.to_dict())
# # print('stars', Restaurant.Review.stars)
