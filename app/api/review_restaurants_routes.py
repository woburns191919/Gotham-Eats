from flask import Blueprint, jsonify, request, abort
from flask_login import login_required, current_user
from app.models import User, Restaurant, db, Review



review_restaurants_routes = Blueprint("reviews", __name__)

@review_restaurants_routes.route("/api/restaurants/<int:restaurant_id>/reviews", methods=["GET"])
def get_reviews_for_restaurant(restaurant_id):
    reviews = Review.query.filter_by(restaurant_id=restaurant_id).all()
    review_data = [review.to_dict() for review in reviews]
    return jsonify(reviews=review_data)


@review_restaurants_routes.route("/api/restaurants/<int:restaurant_id>/reviews", methods=["POST"])
@login_required
def create_review(restaurant_id):
    data = request.json
    review_text = data.get("review")
    stars = data.get("stars")

    if not review_text or not stars:
        return jsonify(message="Review and stars are required."), 400

    review = Review(
        user_id=current_user.id,
        restaurant_id=restaurant_id,
        review=review_text,
        stars=stars,
    )

    db.session.add(review)
    db.session.commit()

    return jsonify(review=review.to_dict()), 201

@review_restaurants_routes.route("/api/restaurants/<int:restaurant_id>/reviews/<int:review_id>", methods=["PUT"])
@login_required
def update_review(restaurant_id, review_id):
    data = request.json
    updated_review_text = data.get("review")

    review = Review.query.get(review_id)

    if not review or review.restaurant_id != restaurant_id or review.user_id != current_user.id:
        return jsonify(message="Review not found or unauthorized to update."), 404

    review.review = updated_review_text
    review.updated_at = datetime.now()

    db.session.commit()

    return jsonify(review=review.to_dict())

@review_restaurants_routes.route("/api/restaurants/<int:restaurant_id>/reviews/<int:review_id>", methods=["DELETE"])
@login_required
def delete_review(restaurant_id, review_id):
    review = Review.query.get(review_id)

    if not review or review.restaurant_id != restaurant_id or review.user_id != current_user.id:
        return jsonify(message="Review not found or unauthorized to delete."), 404

    db.session.delete(review)
    db.session.commit()

    return jsonify(message="Review deleted successfully.")




# @review_restaurants_routes("/review/<int:restaurant_id>")
# def show_review_form(restaurant_id):
#   restaurant = Restaurant.query.get(restaurant_id)
#   """Displays review form for specific restaurant"""

#   review_form_html = """
#   <html>
#   <head>
#     <title>Create a Restaurant</title>
#   </head>
#     <body>
#       <h1>Review a Restaurant</h1>

#       <form method="POST" action="/restaurants/new">

#         <label for="name">Name:</label>
#         <input type="text" required /> <br /><br />

#         <label for="streetAddress">Street Address:</label>
#         <input type="text" required /> <br /><br />

#         <label for="city">City:</label>
#         <select name="city">
#           <option value="Gotham"></option>
#         </select>
#         <br /><br />

#         <label for="state">State:</label>
#         <select name="state">
#           <option value="New York"></option>
#         </select>
#         <br /><br />

#         <label for="postalCode">Postal Code:</label>
#         <input type="text" required /> <br /><br />

#         <label for="country">Country:</label>
#         <select name="country">
#           <option value="United States"></option>
#         </select>
#         <br /><br />


#         <label for="name">Name:</label>
#         <input type="text" required /> <br /><br />

#         <label for="description">Description:</label>
#         <input type="textarea" required /> <br /><br />

#         <label for="hours">Hours:</label>
#         <input type="textarea" required /> <br /><br />

#         <label for="submit">Create Restaurant:</label>
#         <input type="text" />
#       </form>
#     </body>

# </html>
#   """

#   if not restaurant:
#     return "Restaurant not found", 404
#   return review_form_html
