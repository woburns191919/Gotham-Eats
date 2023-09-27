from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Restaurant

review_restaurants_routes = Blueprint('review_restaurants', __name__)

@review_restaurants_routes("/review/<int:restaurant_id>")
def show_review_form(restaurant_id):
  restaurant = Restaurant.query.get(restaurant_id)
  """Displays review form for specific restaurant"""

  review_form_html = """
  <html>
  <head>
    <title>Create a Restaurant</title>
  </head>
    <body>
      <h1>Review a Restaurant</h1>

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


        <label for="name">Name:</label>
        <input type="text" required /> <br /><br />

        <label for="description">Description:</label>
        <input type="textarea" required /> <br /><br />

        <label for="hours">Hours:</label>
        <input type="textarea" required /> <br /><br />

        <label for="submit">Create Restaurant:</label>
        <input type="text" />
      </form>
    </body>

</html>
  """

  if not restaurant:
    return "Restaurant not found", 404
  return review_form_html
