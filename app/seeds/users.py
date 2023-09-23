from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text



def seed_users():
    demo = User(
        firstName="Jimbob", lastName="whale",username='Demo',  hashedPassword='password',email='demo@aa.io', address="123 hampton",phone=9136812837)
    marnie = User(
        firstName="Jerry", lastName="Seinfeld",username='marnie', hashedPassword='password',  email='marnie@aa.io', address="1234 hamdpton",phone=9136812838)
    bobbie = User(
        firstName="Mark", lastName="Zuckerberg",username='bobbie',  hashedPassword='password',email='bobbie@aa.io', address="123 hafdadfasmpton",phone=9136812839)

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()



def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
