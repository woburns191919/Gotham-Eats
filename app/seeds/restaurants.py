from ..models import db, environment, SCHEMA, Restaurant, Menu
from sqlalchemy.sql import text
import json
restaurant_list = [
    Restaurant(
        owner_id=2,
        streetAddress="Iceberg Lane 101",
        city="Gotham",
        state="New Jersey",
        postalCode="10007",
        country="United States",
        name="Penguin's Icy Diner",
        description="A frosty dining experience with a penguin-theme, known for seafood.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=2,
        streetAddress="Enigma Blvd 42",
        city="Gotham",
        state="New Jersey",
        postalCode="10008",
        country="United States",
        name="Riddler's Riddle Room",
        description="Solve riddles to get your food in this mysterious, enigma-filled diner.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=3,
        streetAddress="Vine St 3",
        city="Gotham",
        state="New Jersey",
        postalCode="10009",
        country="United States",
        name="Ivy's Greenhouse",
        description="Enjoy a meal surrounded by exotic plants, some of them carnivorous!",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=3,
        streetAddress="Duality Dr 50",
        city="Gotham",
        state="New Jersey",
        postalCode="10010",
        country="United States",
        name="Two-Face's Coin Toss Tavern",
        description="Experience the duality, make decisions by a coin toss, and enjoy the thematic drinks and meals!",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=2,
        streetAddress="Fear Farm 13",
        city="Gotham",
        state="New Jersey",
        postalCode="10011",
        country="United States",
        name="Scarecrow's Straw Bistro",
        description="A rustic bistro where fear is the main ingredient. Not for the faint-hearted!",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=3,
        streetAddress="Feline Alley 7",
        city="Gotham",
        state="New Jersey",
        postalCode="10012",
        country="United States",
        name="Catwoman's Feline Feast",
        description="Elegant and sleek, this restaurant offers gourmet dishes, quick thefts not included.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=2,
        streetAddress="Shadow Cave 1",
        city="Gotham",
        state="New Jersey",
        postalCode="10013",
        country="United States",
        name="Bat Cave Grill",
        description="Dine in the dark and enjoy the gothic atmosphere at this secret location.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=2,
        streetAddress="Chaos Court 0",
        city="Gotham",
        state="New Jersey",
        postalCode="10014",
        country="United States",
        name="Joker's Juice Bar",
        description="Get ready to have a blast with the colorful and unpredictable beverages!",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=3,
        streetAddress="Venom Vale 88",
        city="Gotham",
        state="New Jersey",
        postalCode="10015",
        country="United States",
        name="Bane's Buffet",
        description="Feed your strength with a variety of hearty meals. Remember, no pain, no gain!",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=2,
        streetAddress="Subzero St 32",
        city="Gotham",
        state="New Jersey",
        postalCode="10016",
        country="United States",
        name="Mr. Freeze's Chill Lounge",
        description="Cool down with ice-cold beverages and frozen delights in a sub-zero environment.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=3,
        streetAddress="Mud Mound 25",
        city="Gotham",
        state="New Jersey",
        postalCode="10017",
        country="United States",
        name="Clayface's Cafe",
        description="Morph your taste buds with eclectic and ever-changing menu.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=2,
        streetAddress="Pyro Place 66",
        city="Gotham",
        state="New Jersey",
        postalCode="10018",
        country="United States",
        name="Firefly's Grill",
        description="Ignite your senses with fiery flavors and smoky delicacies.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=3,
        streetAddress="Teapot Terrace 10",
        city="Gotham",
        state="New Jersey",
        postalCode="10019",
        country="United States",
        name="Mad Hatter's Tea House",
        description="Delve into madness with a bewildering array of teas and enchanting pastries.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        })
    ),

    Restaurant(
        owner_id=2,
        streetAddress="Owl Orbit 8",
        city="Gotham",
        state="New Jersey",
        postalCode="10020",
        country="United States",
        name="Talon's Takeout",
        description="Swoop into flavors with quick and stealthy takeout options.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=2,
        streetAddress="Magic Manor 77",
        city="Gotham",
        state="New Jersey",
        postalCode="10021",
        country="United States",
        name="Zatanna's Pizzeria",
        description="Experience magical pizza concoctions and enchanting salads.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=3,
        streetAddress="Echo Chamber 15",
        city="Gotham",
        state="New Jersey",
        postalCode="10022",
        country="United States",
        name="Man-Bat Diner",
        description="Feast on nocturnal delights in a bat-friendly environment.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=2,
        streetAddress="Skyline Street 45",
        city="Metropolis",
        state="New York",
        postalCode="10023",
        country="United States",
        name="Metropolis Munch",
        description="Indulge in superfoods and Kryptonian cuisine with a cityscape view.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=2,
        streetAddress="Archers Alley 23",
        city="Star City",
        state="California",
        postalCode="10024",
        country="United States",
        name="Green Arrow Grill",
        description="Aim for taste perfection with gourmet burgers and archer’s pie.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=3,
        streetAddress="Coral Cove 33",
        city="Atlantis",
        state="Ocean",
        postalCode="10025",
        country="United States",
        name="Atlantean Eats",
        description="Submerge your senses in oceanic flavors and seafaring sustenance.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),

    Restaurant(
        owner_id=1,
        streetAddress="Crater Crescent 11",
        city="Apollo",
        state="Moon",
        postalCode="10026",
        country="United States",
        name="Lunar Lunch",
        description="Dine on interstellar delights and moon pies under the stars.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "23:00:00"},
            "Thursday": {"open": "09:00:00", "close": "23:00:00"},
            "Friday": {"open": "09:00:00", "close": "23:00:00"},
            "Saturday": {"open": "00:00:00", "close": "24:00:00"},
            "Sunday": {"open": "00:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"

    ),]


def seed_restaurants():

    for ele in restaurant_list:
        db.session.add(ele)
        db.session.commit()
        menu = Menu(restaurant_id=ele.id)
        db.session.add(menu)
        db.session.commit()


def undo_restaurants():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.restaurants, {SCHEMA}.menus RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurants"))
        db.session.execute(text("DELETE FROM menus"))
    db.session.commit()
