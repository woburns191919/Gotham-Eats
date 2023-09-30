from flask import Blueprint, jsonify, request,redirect, url_for, abort
import app
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Restaurant, Review, db, MenuItem,MenuItemImg
from sqlalchemy import func, distinct, or_, desc
from ..forms import RestaurantForm
import json
home_restaurants = Blueprint('restaurants', __name__)

@home_restaurants.route("/new", methods=["POST"])
def create_new_restaurant():

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
    """delete a restaurant based on restaurant id"""
    restaurant_to_delete = Restaurant.query.get(id)
    print(restaurant_to_delete)
    db.session.delete(restaurant_to_delete)
    db.session.commit()
    return redirect("/restaurants")

@home_restaurants.route("/manage/<int:id>")

def get_my_restaurants(id):
  print('at least inside my rourte ********')
  my_restaurants= db.session.query(Restaurant).filter(Restaurant.owner_id==current_user.id).all()
  if my_restaurants:
        restaurant_data=[restaurant.to_dict() for restaurant in my_restaurants]
        all_restaurants = {'restaurants':restaurant_data}
        return jsonify(restaurant_data), 200
  else:
        abort(404,"You don't  have any spots")
##ALEX WORKED HERE.  I DO THIS SO MERGES EASIER##
@home_restaurants.route("/getMenuItemDeets/<int:id>")
def Get_menu_item_deets(id):
    the_deets = db.session.query(MenuItem, MenuItemImg).join(MenuItemImg, MenuItem.menu_item_img_id == MenuItemImg.id).filter(MenuItem.restaurant_id == id).all()

    organized_deets = {
        "entree": [],
        "drink": [],
        "dessert": [],
        "side": []
    }

    for menu_item, menu_item_img in the_deets:
        menu_item_dict = menu_item.to_dict()
        menu_item_dict["url"] = menu_item_img.url
        menu_item_dict["preview"] = menu_item_img.preview

        organized_deets[menu_item_dict["type"]].append(menu_item_dict)

    return jsonify(organized_deets)

##END ALEX WORK##

@home_restaurants.route("/")
def get_popular_restaurants():
    """returns a all restaurant order by popularity"""
    restaurants = db.session.query(Restaurant).all()
    print('restaurants***', restaurants)

    all_restaurants = {'restaurants': [restaurant.to_dict() for restaurant in restaurants]}

    return jsonify(all_restaurants)

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
