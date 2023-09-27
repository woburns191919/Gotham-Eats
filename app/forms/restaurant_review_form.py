from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, URL, ValidationError



def is_numeric(form, field):

    if not field.data.isdigit():
        raise ValidationError("This field must contain only numbers.")


class RestaurantReviewForm(FlaskForm):

  streetAddress = StringField("Street Address", validators=[DataRequired()])
  city = SelectField("City", choices=['Gotham'])
  state = SelectField("State", choices=['New York'])
  postalCode = StringField("Postal Code", validators=[DataRequired(), Length(min=5, max=5, message="Zip must be 5 characters"), is_numeric])
  country = SelectField("Country", choices=['United States'])
  name = SelectField("Country", choices=['United States'])
  description = TextAreaField("Description", validators=[DataRequired()])
  hours = StringField("Hours", validators=[DataRequired()])
  submit = SubmitField("Create Restaurant")
