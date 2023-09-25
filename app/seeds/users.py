from ..models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

user_list=[
      User(
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
        phone='710-681-2835'),

    User(
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
        phone='710-681-2836'),

    User(
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
        phone='710-681-2837'),

    User(
        firstName="Joker",
        lastName="Unknown",
        username='TheJoker',
        hashedPassword="password",
        email='joker@arkham.com',
        streetAddress="123 Laugh Lane",
        city="Gotham",
        state="New Jersey",
        postalCode="10102",
        country="United States",
        phone='710-681-2838'),

    User(
        firstName="Selina",
        lastName="Kyle",
        username='Catwoman',
        hashedPassword="password",
        email='catwoman@gotham.com',
        streetAddress="456 Feline Alley",
        city="Gotham",
        state="New Jersey",
        postalCode="10303",
        country="United States",
        phone='710-681-2839'),

    User(
        firstName="Oswald",
        lastName="Cobblepot",
        username='ThePenguin',
        hashedPassword="password",
        email='penguin@gotham.com',
        streetAddress="789 Iceberg Avenue",
        city="Gotham",
        state="New Jersey",
        postalCode="10404",
        country="United States",
        phone='710-681-2840'),

    User(
        firstName="Edward",
        lastName="Nigma",
        username='TheRiddler',
        hashedPassword="password",
        email='riddler@gotham.com',
        streetAddress="1010 Enigma Lane",
        city="Gotham",
        state="New Jersey",
        postalCode="10505",
        country="United States",
        phone='710-681-2841'),

    User(
        firstName="Harvey",
        lastName="Dent",
        username='TwoFace',
        hashedPassword="password",
        email='twoface@gotham.com',
        streetAddress="1313 Coin Street",
        city="Gotham",
        state="New Jersey",
        postalCode="10606",
        country="United States",
        phone='710-681-2842'),

    User(
        firstName="Victor",
        lastName="Fries",
        username='MrFreeze',
        hashedPassword="password",
        email='mr.freeze@gotham.com',
        streetAddress="1414 Ice Lane",
        city="Gotham",
        state="New Jersey",
        postalCode="10707",
        country="United States",
        phone='710-681-2843'),

    User(
        firstName="Jonathan",
        lastName="Crane",
        username='Scarecrow',
        hashedPassword="password",
        email='scarecrow@gotham.com',
        streetAddress="1515 Fear Street",
        city="Gotham",
        state="New Jersey",
        postalCode="10808",
        country="United States",
        phone='710-681-2844'),

    User(
        firstName="Rachel",
        lastName="Dawes",
        username='RachelDawes',
        hashedPassword="password",
        email='rachel@gotham.com',
        streetAddress="1616 Attorney Avenue",
        city="Gotham",
        state="New Jersey",
        postalCode="10909",
        country="United States",
        phone='710-681-2845'),

    User(
        firstName="Lucius",
        lastName="Fox",
        username='LuciusFox',
        hashedPassword="password",
        email='lucius@waynecorp.com',
        streetAddress="1717 Innovation Street",
        city="Gotham",
        state="New Jersey",
        postalCode="11010",
        country="United States",
        phone='710-681-2846'),

    User(
        firstName="Barbara",
        lastName="Gordon",
        username='Oracle',
        hashedPassword="password",
        email='barbara@gotham.com',
        streetAddress="1818 Clock Tower",
        city="Gotham",
        state="New Jersey",
        postalCode="11111",
        country="United States",
        phone='710-681-2847'),

    User(
        firstName="Tim",
        lastName="Drake",
        username='Robin',
        hashedPassword="password",
        email='tim@gotham.com',
        streetAddress="1919 Drake Street",
        city="Gotham",
        state="New Jersey",
        postalCode="11212",
        country="United States",
        phone='710-681-2848'),

    User(
        firstName="Jason",
        lastName="Todd",
        username='RedHood',
        hashedPassword="password",
        email='jason@gotham.com',
        streetAddress="2020 Hood Lane",
        city="Gotham",
        state="New Jersey",
        postalCode="11313",
        country="United States",
        phone='710-681-2849'),

    User(
        firstName="Damian",
        lastName="Wayne",
        username='DamianWayne',
        hashedPassword="password",
        email='damian@waynemanor.com',
        streetAddress="2121 Sword Lane",
        city="Gotham",
        state="New Jersey",
        postalCode="11414",
        country="United States",
        phone='710-681-2850'),

   User(
        firstName="Cassandra",
        lastName="Cain",
        username='Batgirl',
        hashedPassword="password",
        email='cassandra@gotham.com',
        streetAddress="2222 Bat Street",
        city="Gotham",
        state="New Jersey",
        postalCode="11515",
        country="United States",
        phone='710-681-2851')
]
def seed_users():

     for ele in user_list:
        db.session.add(ele)
     db.session.commit()



def undo_users():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
    db.session.commit()
