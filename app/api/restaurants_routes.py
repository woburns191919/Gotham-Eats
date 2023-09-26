from flask import Blueprint, jsonify, request
import app
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Restaurant, Review, db
from sqlalchemy import func, distinct, or_, desc
from ..forms import RestaurantForm
# from ..models.restaurants import

home_restaurants = Blueprint('restaurants', __name__)
# print("******************current_user: ", current_user.get_id())
# print("******************Restaurant.owner_id: ", Restaurant.query.get(id).owner_id)

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

# @home_restaurants.route("/update/<int:id>", methods=["GET", "POST"])
# def update_post(id):
#    """update a restaurant if the user owns the restaurant"""
#    form = RestaurantForm()
#    restaurant_to_update = Restaurant.query.get(id)
#    if restaurant_to_update.owner_id == current_user.id:
#         if form.validate_on_submit():
#           restaurant_to_update.name = form.name.data
#           restaurant_to_update.streetAddress = form.streetAddress.data
#           restaurant_to_update.city = form.city.data
#           restaurant_to_update.state = form.state.data
#           restaurant_to_update.postalCode = form.postalCode.data
#           restaurant_to_update.country = form.country.data
#           restaurant_to_update.description = form.description.data
#           restaurant_to_update.hours = form.hours.data
#           restaurant_to_update.previmg = form.previmg.data

#           db.session.commit()
#           return jsonify(message="Restaurant updated successfully"), 200
#         elif form.errors:
#            return jsonify(errors=form.errors), 400
#    return jsonify(message="You are not the owner of this restaurant"), 403


  #  if restaurant_to_update.owner_id == current_user.id:
    #  if form.validate_on_submit():

      # user = User.query.get()
@home_restaurants.route("/update/<int:id>", methods=["GET", "PUT"])
def update_post(id):
    """update a restaurant if the user owns the restaurant"""

    restaurant_to_update = Restaurant.query.get_or_404(id)
    print("current_user.id:", current_user.id)
    print("restaurant_to_update.owner_id:", restaurant_to_update.owner_id)

    # Check if the user is authenticated and if they are the owner
    if not current_user.is_authenticated:
        return jsonify(message="You need to be logged in"), 401

    if restaurant_to_update.owner_id != current_user.id:
        return jsonify(message="You are not the owner of this restaurant"), 403

    form = RestaurantForm()

    if request.method == 'GET':
        form.name.data = restaurant_to_update.name
        # ... (populate other fields in the same manner)

    if form.validate_on_submit():
        restaurant_to_update.name = form.name.data
        restaurant_to_update.streetAddress = form.streetAddress.data
        # ... (set other attributes in the same manner)

        db.session.commit()
        return jsonify(message="Restaurant updated successfully"), 200
    elif form.errors:
        return jsonify(errors=form.errors), 400
