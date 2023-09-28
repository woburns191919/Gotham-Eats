from flask import Blueprint, jsonify, request,redirect, url_for,abort
import app
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Restaurant, Review, db, MenuItem
from sqlalchemy import func, distinct, or_, desc
from ..forms import RestaurantForm
import json
# from ..models.restaurants import

home_restaurants = Blueprint('restaurants', __name__)


@home_restaurants.route("/<int:id>")
def get_restaurant_by_id(id):
    """returns a single restaurant and it's reviews by the given id provided as a route parameter"""


    one_restaurant = Restaurant.query.get(id)


    if not one_restaurant:
       return jsonify({"error": "Restaurant not found"}), 404


    reviews = Review.query.filter_by(restaurant_id=id).all()
    review_list = [review.to_dict() for review in reviews]


    response_data = one_restaurant.to_dict()
    response_data['reviews'] = review_list

    return jsonify(response_data)


@home_restaurants.route("/")
def get_popular_restaurants():
  """returns a all restaurant order by popularity"""
  # restaurants= db.session.query(Restaurant).all()
  #your queery dont work bros
  restaurants = db.session.query(Restaurant).join(Review, Restaurant.id == Review.restaurant_id).\
    group_by(Restaurant.id).\
    order_by(func.avg(Review.stars).desc()).\
    all()

  all_restaurants = {'restaurants': [restaurant.to_dict() for restaurant in restaurants]}

  return all_restaurants




@home_restaurants.route("/new")
def display_restaurant_form():
  """displays restaurant form"""
  form_html = """
  <html>
  <head>
    <title>Create a Restaurant</title>
  </head>
    <body>
      <h1>Create a New Restaurant</h1>
      <form method="POST" action="/restaurants/new">
        <label for="name">Name:</label>
        <input type="text" required /> <br /><br />

        <label for="streetAddress">Street Address:</label>
        <input type="text" required /> <br /><br />

        <label for="city">City:</label>
        <select name="city">
          <option value="Gotham"></option>
        </select>
        <br /><br />

        <label for="state">State:</label>
        <select name="state">
          <option value="New York"></option>
        </select>
        <br /><br />

        <label for="postalCode">Postal Code:</label>
        <input type="text" required /> <br /><br />

        <label for="country">Country:</label>
        <select name="country">
          <option value="United States"></option>
        </select>
        <br /><br />

        <label for="description">Description:</label>
        <input type="textarea" required /> <br /><br />

        <label for="hours">Hours:</label>
        <input type="textarea" required /> <br /><br />

        <label for="previmg">Preview Image:</label>
        <input type="text" required /> <br /><br />

        <label for="submit">Create Restaurant:</label>
        <input type="text" />
      </form>
    </body>

</html>
  """
  return form_html



@home_restaurants.route("/new", methods=["POST"])
def create_new_restaurant():
  """creates a new restaurant"""
  form = RestaurantForm()
  # form['csrf_token'].data = request.cookies['csrf_token']

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
    addded_restaurant = db.session.add(new_restaurant)
    db.session.commit()
    return jsonify(message = "Successfully created new restaurant", id = addded_restaurant.id), 201
  return jsonify(errors=form.errors), 400


@home_restaurants.route("/update/<int:id>", methods=["GET", "PUT"])
def update_restaurant(id):
    """update a restaurant if the user owns the restaurant"""

    restaurant_to_update = Restaurant.query.get_or_404(id)

    if not current_user.is_authenticated:
        return jsonify(message="You need to be logged in"), 401

    if restaurant_to_update.owner_id != current_user.id:
        return jsonify(message="You are not the owner of this restaurant"), 403

    form = RestaurantForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if request.method == 'GET':
        return jsonify(restaurant_to_update.to_dict())
    data = request.get_json()


    form.name.data = data['name']
    form.streetAddress.data = data['streetAddress']
    form.city.data = data['city']
    form.state.data = data['state']
    form.postalCode.data = data['postalCode']
    form.country.data = data['country']
    form.description.data = data['description']
    form.hours.data = data['hours']
    form.previmg.data = data['previmg']

    if form.validate_on_submit():
        restaurant_to_update.name = form.name.data
        restaurant_to_update.streetAddress = form.streetAddress.data
        restaurant_to_update.city = form.city.data
        restaurant_to_update.state = form.state.data
        restaurant_to_update.postalCode = form.postalCode.data
        restaurant_to_update.country = form.country.data
        restaurant_to_update.description = form.description.data
        restaurant_to_update.hours = form.hours.data
        restaurant_to_update.previmg = form.previmg.data

        db.session.commit()
        return jsonify(message="Restaurant updated successfully"), 200
    else:
        return jsonify(errors=form.errors), 400


@home_restaurants.route("/delete/<int:id>")
def delete_post(id):

    "RESTAURANTS TESTING"
    """delete a restaurant based on restaurant id"""
    restaurant_to_delete = db.session.query(Restaurant).get(id)
    if restaurant_to_delete:
       if restaurant_to_delete.owner_id==current_user.id:
           db.session.delete(restaurant_to_delete)
           db.session.commit()
           return jsonify(message = f"Succesfully deleted restaurant {id}"), 204
       else:
          abort(403, description="Forbidden. You are not the owner")


    else:
       abort(404,"This spot doesn't exist")

@home_restaurants.route("/manage")
def get_my_restaurants():
   my_restaurants=db.session.query(Restaurant).filter(Restaurant.owner_id==current_user.id).all()
   if my_restaurants:
      restaurant_data=[restaurant.to_dict() for restaurant in my_restaurants]
      print("HEY WE HIT THE MANAGE PAGE. my restaurants looks like this",my_restaurants)
      return jsonify(restaurants=restaurant_data,message="success"), 200
   else:
      abort(404,"You don't  have any spots")
