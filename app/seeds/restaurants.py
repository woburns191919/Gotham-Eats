from ..models import db, environment, SCHEMA, Restaurant
from sqlalchemy.sql import text
import json


restaurant_list = [
    Restaurant(
        owner_id=1,
        streetAddress="Wayne Manor 1",
        city="Gotham",
        state="New Jersey",
        postalCode="10024",
        country="United States",
        name="Alfred's Gourmet Dining",
        description="Savor exquisite dishes crafted by the legendary butler himself.",
        hours='9-5',

    ),
    Restaurant(
        owner_id=1,
        streetAddress="Butler's Lane 1",
        city="Gotham",
        state="New Jersey",
        postalCode="10036",
        country="United States",
        name="Alfred's Fine Eats",
        description="Fine dining and impeccable service in Wayne Manor.",
        hours='9-5',

    ),
    Restaurant(
    owner_id=1,
    streetAddress="Butler Way 3",
    city="Gotham",
    state="New Jersey",
    postalCode="10009",
    country="United States",
    name="Alfred's Greenhouse Gourmet",
    description="Enjoy exquisite dining surrounded by rare and beautifully curated flora!",
    hours='9-5',
),

Restaurant(
    owner_id=1,
    streetAddress="Servitude Street 88",
    city="Gotham",
    state="New Jersey",
    postalCode="10015",
    country="United States",
    name="The Butler's Banquet",
    description="Indulge in a plethora of hearty and meticulously prepared meals, fit for the Wayne family!",
    hours='9-5',
),

Restaurant(
    owner_id=1,
    streetAddress="Elegant Avenue 25",
    city="Gotham",
    state="New Jersey",
    postalCode="10017",
    country="United States",
    name="Pennyworth's Posh Café",
    description="Treat your taste buds to Alfred's eclectic and elegant menu, a symphony of flavors!",
    hours='9-5',
),

Restaurant(
    owner_id=1,
    streetAddress="Refinement Road 66",
    city="Gotham",
    state="New Jersey",
    postalCode="10018",
    country="United States",
    name="Wayne Manor Grills",
    description="Ignite your senses with the smoky and fiery flavors, all prepared under Alfred's watchful eyes.",
    hours='9-5',
),

Restaurant(
    owner_id=1,
    streetAddress="Manor Lane 10",
    city="Gotham",
    state="New Jersey",
    postalCode="10019",
    country="United States",
    name="Alfred's Afternoon Tea",
    description="Immerse yourself in the rich and bewildering array of teas, accompanied by Alfred's signature pastries.",
    hours='9-5',
),

Restaurant(
    owner_id=1,
    streetAddress="Valet Vale 8",
    city="Gotham",
    state="New Jersey",
    postalCode="10020",
    country="United States",
    name="Pennyworth's Quick Platter",
    description="Experience the swift and stealthy takeout options, designed for the hurried and the hungry.",
    hours='9-5',
),

Restaurant(
    owner_id=1,
    streetAddress="Gourmet Grove 77",
    city="Gotham",
    state="New Jersey",
    postalCode="10021",
    country="United States",
    name="Alfred's Culinary Magic",
    description="Be enchanted by Alfred's magical concoctions of pizza and meticulously crafted salads.",
    hours='9-5',
),

Restaurant(
    owner_id=1,
    streetAddress="Serving Lane 15",
    city="Gotham",
    state="New Jersey",
    postalCode="10022",
    country="United States",
    name="Pennyworth's Night Bistro",
    description="Delight in nocturnal gourmet in an environment curated by the iconic butler himself.",
    hours='9-5',
),

Restaurant(
    owner_id=1,
    streetAddress="Cityscape Street 45",
    city="Metropolis",
    state="New York",
    postalCode="10023",
    country="United States",
    name="Metropolis Manor Munch",
    description="Savor the flavors of meticulously prepared superfoods and cuisine, all curated by Alfred.",
    hours='9-5',
),

Restaurant(
    owner_id=1,
    streetAddress="Culinary Court 29",
    city="Gotham",
    state="New Jersey",
    postalCode="10025",
    country="United States",
    name="Butler's Brave Bites",
    description="Brace yourself for Alfred's spicy and bold creations, a true conquest of flavors!",
    hours='9-5',
),

Restaurant(
    owner_id=1,
    streetAddress="Chill Chamber 7",
    city="Gotham",
    state="New Jersey",
    postalCode="10027",
    country="United States",
    name="Alfred's Frosty Confections",
    description="Relax with Alfred's specially crafted frozen delights and cool culinary specialties.",
    hours='9-5',
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
        hours='9-5',

    ),
    Restaurant(
        owner_id=2,
        streetAddress="Quinn Square 8",
        city="Gotham",
        state="New Jersey",
        postalCode="10222",
        country="United States",
        name="Harley's Hysterical Diner",
        description="Unleash your inner wild card and savor explosive flavors. Enjoy chaotic culinary delights inspired by Gotham’s Queen of Anarchy in a whimsically themed setting.",
        hours='9-5',
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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',
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
        hours='9-5',

    ),
    Restaurant(
        owner_id=6,
        streetAddress="Iceberg Lounge 9",
        city="Gotham",
        state="New Jersey",
        postalCode="10046",
        country="United States",
        name="Penguin's Fish and Chips",
        description="Feast on the finest seafood in the city, with a side of underworld charm.",
        hours='9-5',

    ),
    Restaurant(
        owner_id=6,
        streetAddress="Cobblepot Lane 11",
        city="Gotham",
        state="New Jersey",
        postalCode="10101",
        country="United States",
        name="Penguin's Umbrella Eats",
        description="Indulge in an array of dishes so good, it's criminal. Dive into villainous flavors and explore the decadent menu inspired by Gotham's master of fowl play.",
        hours='9-5',
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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

    ),
    Restaurant(
        owner_id=8,
        streetAddress="Double-Dealing Drive 5",
        city="Gotham",
        state="New Jersey",
        postalCode="10033",
        country="United States",
        name="Heads or Tails Tavern",
        description="Will your meal be good or bad? Leave it to chance!",
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

    ),
    Restaurant(
    owner_id=11,
    streetAddress="Dawes Lane 45",
    city="Gotham",
    state="New Jersey",
    postalCode="10028",
    country="United States",
    name="Rachel's Justice Bistro",
    description="A place that honors the spirit of Rachel Dawes, offering a selection of fair, just, and ethically sourced dishes to remind us of the values she stood for.",
    hours='9-5',
),

Restaurant(
    owner_id=11,
    streetAddress="Harbor View 22",
    city="Gotham",
    state="New Jersey",
    postalCode="10029",
    country="United States",
    name="Dawes Harbor Cafe",
    description="Overlooking the harbor, Rachel's Harbor Cafe serves fresh, seasonal, and sustainable seafood dishes, a nod to her tireless work in protecting Gotham's harbor district.",
    hours='9-5',
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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

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
        hours='9-5',

    ),
    Restaurant(
        owner_id=17,
        streetAddress="Gordon Avenue 3",
        city="Gotham",
        state="New Jersey",
        postalCode="10055",
        country="United States",
        name="Batgirl's Diner",
        description="Superhero-inspired snacks for the crime-fighter in you.",
        hours='9-5',

    ),



































































]

def seed_restaurants():

    for ele in restaurant_list:
        db.session.add(ele)
        db.session.commit()
        # menu = Menu(restaurant_id=ele.id)
        # db.session.add(menu)
        # db.session.commit()


def undo_restaurants():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.restaurants RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurants"))
    db.session.commit()
