from ..models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


def seed_users():
    alfred = User(
        firstName="Alfred",
        lastName="Pennyworth",
        username='Demo',
        hashedPassword="password",
        email='alfred@waynemanor.com',
        streetAddress="1007 Mountain Drive",
        city="Gotham",
        state="New Jersey",
        postalCode="10007",
        country="United States",
        phone='710-681-2835')

    harley = User(
        firstName="Harleen",
        lastName="Quinzel",
        username='HarleyQuinn',
        hashedPassword="password",
        email='harley@arkham.com',
        streetAddress="100 Arkham Asylum",
        city="Gotham",
        state="New Jersey",
        postalCode="10101",
        country="United States",
        phone='710-681-2836')

    nightwing = User(
        firstName="Dick",
        lastName="Grayson",
        username='Nightwing',
        hashedPassword="password",
        email='nightwing@gotham.com',
        streetAddress="200 Oracle Tower",
        city="Gotham",
        state="New Jersey",
        postalCode="10202",
        country="United States",
        phone='710-681-2837')

    db.session.add(alfred)
    db.session.add(harley)
    db.session.add(nightwing)
    db.session.commit()


def undo_users():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
    db.session.commit()


