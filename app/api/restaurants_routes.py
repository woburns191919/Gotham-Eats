from flask import Blueprint, jsonify, request
import app
from flask_login import login_required
from app.models import User, Restaurant, Review, db
from sqlalchemy import func, distinct, or_, desc
from ..forms import RestaurantForm
# from ..models.restaurants import

home_restaurants = Blueprint('restaurants', __name__)


@home_restaurants.route("/")
def get_popular_restaurants():
  """returns a all restaurant order by popularity"""
  restaurants = db.session.query(Restaurant).join(Review, Restaurant.id == Review.restaurant_id).\
    group_by(Restaurant.id).\
    order_by(func.avg(Review.stars).desc()).\
    all()

  all_restaurants = {'restaurants': [restaurant.to_dict() for restaurant in restaurants]}
  print('restaurants**', all_restaurants)
  return all_restaurants

@home_restaurants.route("/<int:id>")
def get_restaurant_by_id(id):
    """returns a single restaurant by the given id provided as a route parameter"""
    one_restaurant = Restaurant.query.get(id).to_dict()
    return one_restaurant

@home_restaurants.route("/new", methods=["POST"])
def create_new_restaurant():
  """creates a new restaurant"""
  form = RestaurantForm()

  data = request.get_json()
  if form.validate_on_submit():
    new_restaurant = Restaurant(
      owner_id = data["owner_id"],
      name = data["name"],
      streetAddress = data["street_address"],
      city = data["city"],
      state = data["state"],
      postalCode = data["postal_code"],
      country = data["country"],
      description = data["description"],
      hours = data["hours"],
      previmg = data["previmg"]
    )

    print(new_restaurant)
    db.session.add(new_restaurant)
    db.session.commit()
    return jsonify(message = "Successfully created new restaurant"), 201
  return jsonify(errors=form.errors), 400

@home_restaurants.route("/update/<int:id", methods=["GET", "POST"])
def update_post(id):

   form = RestaurantForm()

   if form.validate_on_submit():
      restaurant_to_update = Restaurant.query.get(id)
      # user = User.query.get()
      
