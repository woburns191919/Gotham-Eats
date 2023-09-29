from datetime import datetime

from flask import Blueprint, jsonify, request, current_app as app
from flask_login import login_required, current_user
from app.models import db, Review, Restaurant
import logging

 # Import your Review and Restaurant models here

review_restaurants_routes = Blueprint('reviews', __name__)

@review_restaurants_routes.route("/restaurant/<int:restaurant_id>/reviews")
def get_restaurant_reviews(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        reviews = Review.query.filter_by(restaurant_id=restaurant_id).all()
        reviews_data = [review.to_dict() for review in reviews]
        return jsonify({'reviews': reviews_data}), 200
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@review_restaurants_routes.route("/")
def get_all_reviews():
    reviews = db.session.query(Review).all()
    if reviews:
        reviews_data = [review.to_dict() for review in reviews]
        return jsonify({'reviews': reviews_data}), 200
    else:
        return jsonify({'error': 'Reviews not found'}), 404




# @review_restaurants_routes.route("/api/restaurants/<int:restaurant_id>/reviews", methods=["POST"])
# @login_required
# def create_review(restaurant_id):
#     data = request.json
#     review_text = data.get("review")
#     stars = data.get("stars")

#     if not review_text or not stars:
#         return jsonify(message="Review and stars are required."), 400

#     review = Review(
#         user_id=current_user.id,
#         restaurant_id=restaurant_id,
#         review=review_text,
#         stars=stars,
#     )

#     db.session.add(review)
#     db.session.commit()

#     return jsonify(review=review.to_dict()), 201

# @review_restaurants_routes.route("/api/restaurants/<int:restaurant_id>/reviews/<int:review_id>", methods=["PUT"])
# @login_required
# def update_review(restaurant_id, review_id):
#     data = request.json
#     updated_review_text = data.get("review")

#     review = Review.query.get(review_id)

#     if not review or review.restaurant_id != restaurant_id or review.user_id != current_user.id:
#         return jsonify(message="Review not found or unauthorized to update."), 404

#     review.review = updated_review_text
#     review.updated_at = datetime.now()

#     db.session.commit()

#     return jsonify(review=review.to_dict())

# @review_restaurants_routes.route("/api/restaurants/<int:restaurant_id>/reviews/<int:review_id>", methods=["DELETE"])
# @login_required
# def delete_review(restaurant_id, review_id):
#     review = Review.query.get(review_id)

#     if not review or review.restaurant_id != restaurant_id or review.user_id != current_user.id:
#         return jsonify(message="Review not found or unauthorized to delete."), 404

#     db.session.delete(review)
#     db.session.commit()

#     return jsonify(message="Review deleted successfully.")
