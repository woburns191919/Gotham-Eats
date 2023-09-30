from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('username is already in use.')

def is_numeric(form, field):

    if not field.data.isdigit():
        raise ValidationError("This field must contain only numbers.")


class SignUpForm(FlaskForm):
    firstName = StringField('firstName', validators=[DataRequired()])
    lastName = StringField('lastName', validators=[DataRequired()])
    username = StringField('username', validators=[ username_exists])
    password = StringField('password', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), user_exists])
    streetAddress = StringField('streetAddress', validators=[DataRequired()])
    city = StringField("City")
    state = StringField("State")
    postalCode = StringField("Postal Code")
    country = StringField("Country")
    phone = StringField('phone', validators=[DataRequired()])
