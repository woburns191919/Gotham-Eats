from ..models import db, environment, SCHEMA, Restaurant, Menu
from sqlalchemy.sql import text
import json

restaurant_list = [
    Restaurant(
        owner_id=6,
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
        previmg="https://w7.pngwing.com/pngs/601/465/png-transparent-hamburger-cheeseburger-fast-food-steak-burger-sandwich-food-recipe-cheeseburger-thumbnail.png"
    ),

    Restaurant(
        owner_id=7,
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
        previmg="https://w7.pngwing.com/pngs/10/294/png-transparent-potato-fries-french-fries-fast-food-delicatessen-chicken-fingers-buffalo-wing-hd-fries-food-breakfast-eating-thumbnail.png"
    ),

    Restaurant(
        owner_id=5,
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
        previmg="https://w7.pngwing.com/pngs/999/253/png-transparent-shawarma-fast-food-hamburger-kebab-bacon-kebab-food-recipe-chicken-meat-thumbnail.png"
    ),

    Restaurant(
        owner_id=8,
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
        previmg="https://w7.pngwing.com/pngs/822/979/png-transparent-hamburger-cheese-sandwich-steak-sandwich-vegetable-sandwich-fast-food-grilled-sandwich-food-recipe-cafe-thumbnail.png"
    ),

    Restaurant(
        owner_id=10,
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
        owner_id=5,
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
        owner_id=4,
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
        owner_id=9,
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
        owner_id=7,
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
        owner_id=9,
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
        owner_id=6,
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
        owner_id=15,
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
        owner_id=16,
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
        owner_id=17,
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
        owner_id=13,
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
        owner_id=8,
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
        owner_id=14,
        streetAddress="Wayne Manor 1",
        city="Gotham",
        state="New Jersey",
        postalCode="10024",
        country="United States",
        name="Alfred's Gourmet Dining",
        description="Savor exquisite dishes crafted by the legendary butler himself.",
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
        owner_id=10,
        streetAddress="Fear Lane 29",
        city="Gotham",
        state="New Jersey",
        postalCode="10025",
        country="United States",
        name="Fearless Fried Chicken",
        description="Conquer your fears and spice up your life with our fiery fried chicken!",
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
        owner_id=7,
        streetAddress="Mystery Street 42",
        city="Gotham",
        state="New Jersey",
        postalCode="10026",
        country="United States",
        name="Riddler's Enigma Eats",
        description="Solve culinary conundrums while you dine!",
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
        owner_id=9,
        streetAddress="Iceberg Lane 7",
        city="Gotham",
        state="New Jersey",
        postalCode="10027",
        country="United States",
        name="Frosty Delights",
        description="Chill out with Mr. Freeze's frozen treats and icy specialties.",
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
        owner_id=11,
        streetAddress="Legal Lane 3",
        city="Gotham",
        state="New Jersey",
        postalCode="10028",
        country="United States",
        name="Dawes Diner",
        description="Where justice and great food prevail!",
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
        owner_id=12,
        streetAddress="Innovation Avenue 21",
        city="Gotham",
        state="New Jersey",
        postalCode="10029",
        country="United States",
        name="Lucius's Techno Bistro",
        description="Cutting-edge cuisine for the tech-savvy heroes.",
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
        owner_id=4,
        streetAddress="Chaos Court 8",
        city="Gotham",
        state="New Jersey",
        postalCode="10030",
        country="United States",
        name="Joker's Ha-Ha Hut",
        description="Laugh and dine at the craziest restaurant in town!",
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
        owner_id=5,
        streetAddress="Feline Alley 12",
        city="Gotham",
        state="New Jersey",
        postalCode="10031",
        country="United States",
        name="Catwoman's Catnip Cafe",
        description="Purr-fectly delicious dishes for cat lovers.",
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
        owner_id=14,
        streetAddress="Wayne Manor 2",
        city="Gotham",
        state="New Jersey",
        postalCode="10032",
        country="United States",
        name="Tim's Batwing Bistro",
        description="A dining experience inspired by the Dark Knight's sidekick.",
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
        owner_id=8,
        streetAddress="Double-Dealing Drive 5",
        city="Gotham",
        state="New Jersey",
        postalCode="10033",
        country="United States",
        name="Two-Face's Coin Flip Diner",
        description="Will your meal be good or bad? Leave it to chance!",
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
        owner_id=6,
        streetAddress="Iceberg Lounge 13",
        city="Gotham",
        state="New Jersey",
        postalCode="10034",
        country="United States",
        name="Penguin's Seafood Soiree",
        description="Dine like royalty with Gotham's shrewdest bird.",
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
        owner_id=13,
        streetAddress="Oracle's Insight 9",
        city="Gotham",
        state="New Jersey",
        postalCode="10035",
        country="United States",
        name="Oracle's Virtual Cafe",
        description="Sip and byte your way through the digital world.",
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
        streetAddress="Butler's Lane 1",
        city="Gotham",
        state="New Jersey",
        postalCode="10036",
        country="United States",
        name="Alfred's Gourmet Mansion",
        description="Fine dining and impeccable service in Wayne Manor.",
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
        streetAddress="Mad Love Street 5",
        city="Gotham",
        state="New Jersey",
        postalCode="10037",
        country="United States",
        name="Harley's Circus Grill",
        description="A chaotic dining experience with a touch of madness.",
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
        streetAddress="Acrobat Avenue 8",
        city="Gotham",
        state="New Jersey",
        postalCode="10038",
        country="United States",
        name="Nightwing's Night Bites",
        description="A place for acrobats to dine in style.",
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
        owner_id=15,
        streetAddress="Hooded Alley 3",
        city="Gotham",
        state="New Jersey",
        postalCode="10039",
        country="United States",
        name="RedHood's Roastery",
        description="Serving up a blend of justice and great coffee.",
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
        owner_id=16,
        streetAddress="Demon's Lair 7",
        city="Gotham",
        state="New Jersey",
        postalCode="10040",
        country="United States",
        name="Damian's Ninja Noodles",
        description="Exquisite noodles crafted by the League of Assassins.",
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
        owner_id=17,
        streetAddress="Batty Lane 6",
        city="Gotham",
        state="New Jersey",
        postalCode="10041",
        country="United States",
        name="Batgirl's Bat Bites",
        description="Fueling vigilantes one bite at a time.",
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
        owner_id=4,
        streetAddress="Joker's Funhouse 11",
        city="Gotham",
        state="New Jersey",
        postalCode="10042",
        country="United States",
        name="Joker's Laugh Lounge",
        description="Where the joke's on you, and the food's on the house.",
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
        owner_id=5,
        streetAddress="Feline Alley 4",
        city="Gotham",
        state="New Jersey",
        postalCode="10043",
        country="United States",
        name="Catwoman's Cat Cafe",
        description="Purr-fectly brewed coffee and cunning pastries.",
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
        owner_id=7,
        streetAddress="Riddle Lane 2",
        city="Gotham",
        state="New Jersey",
        postalCode="10044",
        country="United States",
        name="The Riddler's Enigma Eats",
        description="Puzzle your taste buds with enigmatic dishes.",
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
        owner_id=9,
        streetAddress="Cold Storage 12",
        city="Gotham",
        state="New Jersey",
        postalCode="10045",
        country="United States",
        name="Mr. Freeze's Icy Delights",
        description="Chill out with frozen treats and frosty beverages.",
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
        owner_id=6,
        streetAddress="Iceberg Lounge 9",
        city="Gotham",
        state="New Jersey",
        postalCode="10046",
        country="United States",
        name="Penguin's Seafood Shack",
        description="Feast on the finest seafood in the city, with a side of underworld charm.",
        hours=json.dumps({
            "Monday": {"open": "10:00:00", "close": "22:00:00"},
            "Tuesday": {"open": "10:00:00", "close": "22:00:00"},
            "Wednesday": {"open": "10:00:00", "close": "22:00:00"},
            "Thursday": {"open": "10:00:00", "close": "22:00:00"},
            "Friday": {"open": "10:00:00", "close": "22:00:00"},
            "Saturday": {"open": "11:00:00", "close": "23:00:00"},
            "Sunday": {"open": "11:00:00", "close": "23:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),
    Restaurant(
        owner_id=8,
        streetAddress="Two-Face Drive 7",
        city="Gotham",
        state="New Jersey",
        postalCode="10047",
        country="United States",
        name="Two-Face's Diner",
        description="A coin toss decides your meal's fate: delicious or daring?",
        hours=json.dumps({
            "Monday": {"open": "08:00:00", "close": "20:00:00"},
            "Tuesday": {"open": "08:00:00", "close": "20:00:00"},
            "Wednesday": {"open": "08:00:00", "close": "20:00:00"},
            "Thursday": {"open": "08:00:00", "close": "20:00:00"},
            "Friday": {"open": "08:00:00", "close": "20:00:00"},
            "Saturday": {"open": "09:00:00", "close": "21:00:00"},
            "Sunday": {"open": "09:00:00", "close": "21:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),
    Restaurant(
        owner_id=10,
        streetAddress="Fear Street 4",
        city="Gotham",
        state="New Jersey",
        postalCode="10048",
        country="United States",
        name="Scarecrow's Haunted Cafe",
        description="Dine in your deepest fears and darkest nightmares.",
        hours=json.dumps({
            "Monday": {"open": "18:00:00", "close": "02:00:00"},
            "Tuesday": {"open": "18:00:00", "close": "02:00:00"},
            "Wednesday": {"open": "18:00:00", "close": "02:00:00"},
            "Thursday": {"open": "18:00:00", "close": "02:00:00"},
            "Friday": {"open": "18:00:00", "close": "02:00:00"},
            "Saturday": {"open": "20:00:00", "close": "04:00:00"},
            "Sunday": {"open": "20:00:00", "close": "04:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),
    Restaurant(
        owner_id=11,
        streetAddress="Dawes Lane 6",
        city="Gotham",
        state="New Jersey",
        postalCode="10049",
        country="United States",
        name="Rachel's Bistro",
        description="Elegant dining with a touch of Gotham's grace.",
        hours=json.dumps({
            "Monday": {"open": "11:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "11:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "11:00:00", "close": "23:00:00"},
            "Thursday": {"open": "11:00:00", "close": "23:00:00"},
            "Friday": {"open": "11:00:00", "close": "23:00:00"},
            "Saturday": {"open": "12:00:00", "close": "24:00:00"},
            "Sunday": {"open": "12:00:00", "close": "24:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),
    Restaurant(
        owner_id=12,
        streetAddress="Fox Lane 8",
        city="Gotham",
        state="New Jersey",
        postalCode="10050",
        country="United States",
        name="Lucius's Tech Cafe",
        description="A tech-savvy dining experience with cutting-edge cuisine.",
        hours=json.dumps({
            "Monday": {"open": "09:00:00", "close": "21:00:00"},
            "Tuesday": {"open": "09:00:00", "close": "21:00:00"},
            "Wednesday": {"open": "09:00:00", "close": "21:00:00"},
            "Thursday": {"open": "09:00:00", "close": "21:00:00"},
            "Friday": {"open": "09:00:00", "close": "21:00:00"},
            "Saturday": {"open": "10:00:00", "close": "22:00:00"},
            "Sunday": {"open": "10:00:00", "close": "22:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),
    Restaurant(
        owner_id=13,
        streetAddress="Oracle Plaza 2",
        city="Gotham",
        state="New Jersey",
        postalCode="10051",
        country="United States",
        name="Oracle's Cyber Cafe",
        description="Connect with the digital world while savoring delicious bites.",
        hours=json.dumps({
            "Monday": {"open": "08:00:00", "close": "20:00:00"},
            "Tuesday": {"open": "08:00:00", "close": "20:00:00"},
            "Wednesday": {"open": "08:00:00", "close": "20:00:00"},
            "Thursday": {"open": "08:00:00", "close": "20:00:00"},
            "Friday": {"open": "08:00:00", "close": "20:00:00"},
            "Saturday": {"open": "09:00:00", "close": "21:00:00"},
            "Sunday": {"open": "09:00:00", "close": "21:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),
    Restaurant(
        owner_id=14,
        streetAddress="Drake Street 1",
        city="Gotham",
        state="New Jersey",
        postalCode="10052",
        country="United States",
        name="Tim's Comic Cafe",
        description="Comic books, coffee, and delicious treats for every hero.",
        hours=json.dumps({
            "Monday": {"open": "10:00:00", "close": "20:00:00"},
            "Tuesday": {"open": "10:00:00", "close": "20:00:00"},
            "Wednesday": {"open": "10:00:00", "close": "20:00:00"},
            "Thursday": {"open": "10:00:00", "close": "20:00:00"},
            "Friday": {"open": "10:00:00", "close": "20:00:00"},
            "Saturday": {"open": "11:00:00", "close": "21:00:00"},
            "Sunday": {"open": "11:00:00", "close": "21:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),
    Restaurant(
        owner_id=15,
        streetAddress="Red Hood Alley 5",
        city="Gotham",
        state="New Jersey",
        postalCode="10053",
        country="United States",
        name="Red Hood's Hideout",
        description="A haven for anti-heroes with a taste for great food and justice.",
        hours=json.dumps({
            "Monday": {"open": "12:00:00", "close": "00:00:00"},
            "Tuesday": {"open": "12:00:00", "close": "00:00:00"},
            "Wednesday": {"open": "12:00:00", "close": "00:00:00"},
            "Thursday": {"open": "12:00:00", "close": "00:00:00"},
            "Friday": {"open": "12:00:00", "close": "00:00:00"},
            "Saturday": {"open": "14:00:00", "close": "02:00:00"},
            "Sunday": {"open": "14:00:00", "close": "02:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),
    Restaurant(
        owner_id=16,
        streetAddress="Wayne Manor 1",
        city="Gotham",
        state="New Jersey",
        postalCode="10054",
        country="United States",
        name="Damian's Gourmet Grub",
        description="Fine dining fit for the youngest heir of Wayne Enterprises.",
        hours=json.dumps({
            "Monday": {"open": "19:00:00", "close": "23:00:00"},
            "Tuesday": {"open": "19:00:00", "close": "23:00:00"},
            "Wednesday": {"open": "19:00:00", "close": "23:00:00"},
            "Thursday": {"open": "19:00:00", "close": "23:00:00"},
            "Friday": {"open": "19:00:00", "close": "23:00:00"},
            "Saturday": {"open": "20:00:00", "close": "00:00:00"},
            "Sunday": {"open": "20:00:00", "close": "00:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    ),
    Restaurant(
        owner_id=17,
        streetAddress="Gordon Avenue 3",
        city="Gotham",
        state="New Jersey",
        postalCode="10055",
        country="United States",
        name="Batgirl's Bat Bites",
        description="Superhero-inspired snacks for the crime-fighter in you.",
        hours=json.dumps({
            "Monday": {"open": "10:00:00", "close": "22:00:00"},
            "Tuesday": {"open": "10:00:00", "close": "22:00:00"},
            "Wednesday": {"open": "10:00:00", "close": "22:00:00"},
            "Thursday": {"open": "10:00:00", "close": "22:00:00"},
            "Friday": {"open": "10:00:00", "close": "22:00:00"},
            "Saturday": {"open": "11:00:00", "close": "23:00:00"},
            "Sunday": {"open": "11:00:00", "close": "23:00:00"}
        }),
        previmg="http://www.dog1.jpg/"
    )
]

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
