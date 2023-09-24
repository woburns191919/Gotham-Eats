from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User
from sqlalchemy import or_


# def user_exists(form, field):
#     # Checking if user exists
#     # email = field.data
#     email = str(field.data)
#     print(type(email), email)
#     user = User.query.filter(User.email == email).first()
#     if not user:
#         raise ValidationError('Email provided not found.')


# def password_matches(form, field):
#     # Checking if password matches
#     password = field.data
#     email = form.data['email']
#     user = User.query.filter(User.email == email).first()
#     if not user:
#         raise ValidationError('No such user exists.')
#     if not user.check_password(password):
#         raise ValidationError('Password was incorrect.')
# ================================================================
# def user_exists(form, field):

#     email = str(field.data)
#     user = User.query.filter(User.email == email).first()
#     if not user:
#         raise ValidationError('Email provided not found.')

# def password_matches(form, field):

#     password = str(field.data)
#     email = str(form.data['email'])
#     user = User.query.filter(User.email == email).first()
#     if not user or not user.check_password(password):
#         raise ValidationError('Incorrect email or password.')


# class LoginForm(FlaskForm):
#     email = StringField('email', validators=[DataRequired(), user_exists])
#     password = StringField('password', validators=[DataRequired(), password_matches])
# ================================================================


def credential_exists(form, field):
    credential = str(field.data)
    user = User.query.filter(or_(User.email == credential, User.phone == credential)).first()
    if not user:
        raise ValidationError('Provided email or phone number not found.')


def password_matches(form, field):
    password = str(field.data)
    credential = str(form.data['credential'])
    user = User.query.filter(or_(User.email == credential, User.phone == credential)).first()
    if not user or not user.check_password(password):
        raise ValidationError('Incorrect email/phone or password.')

class LoginForm(FlaskForm):
    credential = StringField('credential', validators=[DataRequired(), credential_exists])
    password = StringField('password', validators=[DataRequired(), password_matches])
