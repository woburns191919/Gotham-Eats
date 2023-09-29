from ..models import db, User,Restaurant,Review, environment, SCHEMA
from sqlalchemy.sql import text
import random
reviews_list = [
{"restaurant_id":1, "user_id":1,
"review":"The service was as meticulous as I am with Master Wayne's suits. Quite splendid.", "stars":4},
{"restaurant_id":1, "user_id":2,
"review":"Puddin' would have loved the desserts here! Teehee!", "stars":5},
{"restaurant_id":1, "user_id":3,
"review":"Great spot for a quick bite after patrol. Felt right at home.", "stars":4},
{"restaurant_id":2, "user_id":1,
"review":"Reminds me of the lavish dinners in Wayne Manor. Top-notch.", "stars":5},
{"restaurant_id":2, "user_id":2,
"review":"Not chaotic enough for my taste, but the food's not bad.", "stars":3},
{"restaurant_id":2, "user_id":3,
"review":"Had a quiet corner perfect for keeping an eye on the entrance. Food was great too.", "stars":4},
{"restaurant_id":3, "user_id":1,
"review":"A bit too noisy, but the tea was brewed perfectly.", "stars":4},
{"restaurant_id":3, "user_id":2,
"review":"Oh, the colors! Loved the vibrant atmosphere. More candy, please!", "stars":5},
{"restaurant_id":3, "user_id":3,
"review":"They've got a rooftop seating. Perfect view for any activities.", "stars":5},
{"restaurant_id":4, "user_id":1,
"review":"Their soup of the day took me back to London.", "stars":4},
{"restaurant_id":4, "user_id":2,
"review":"Had a blast with their musical chairs! Food's yum too.", "stars":5},
{"restaurant_id":4, "user_id":3,
"review":"Lighting was a bit too bright for my taste. Food was decent.", "stars":3},
{"restaurant_id":5, "user_id":1,
"review":"Their classic English breakfast was heartwarming.", "stars":4},
{"restaurant_id":5, "user_id":2,
"review":"Fun and lively! Could use more sprinkles though.", "stars":4},
{"restaurant_id":5, "user_id":3,
"review":"Convenient location for those late-night stakeouts.", "stars":3},
{"restaurant_id":6, "user_id":1,
"review":"The wine selection is nothing short of exquisite.", "stars":5},
{"restaurant_id":6, "user_id":2,
"review":"Meh, needed more pizzazz! But the pie was good.", "stars":3},
{"restaurant_id":6, "user_id":3,
"review":"Relaxing ambiance. Could use this as a good meetup spot.", "stars":4},
{"restaurant_id":7, "user_id":1,
"review":"The ambiance reminds me of the old days, quite nostalgic.", "stars":4},
{"restaurant_id":7, "user_id":2,
"review":"A rollercoaster of flavors! Whee!", "stars":5},
{"restaurant_id":7, "user_id":3,
"review":"A decent place to chill. The espresso shot was on point.", "stars":4},
{"restaurant_id":8, "user_id":1,
"review":"Subtle and refined flavors. Quite the culinary experience.", "stars":5},
{"restaurant_id":8, "user_id":2,
"review":"Boop-oop-a-doop! I liked the carnival theme!", "stars":5},
{"restaurant_id":8, "user_id":3,
"review":"Good rooftop views, and the food wasn't half bad.", "stars":4},
{"restaurant_id":9, "user_id":1,
"review":"Reminded me of the cafes in Paris. Delightful!", "stars":5},
{"restaurant_id":9, "user_id":2,
"review":"Could use a mallet on their menu, but overall fun!", "stars":4},
{"restaurant_id":9, "user_id":3,
"review":"Fast service. Got my meal and was out in a flash.", "stars":4},
{"restaurant_id":10, "user_id":1,
"review":"A serene experience, away from the chaos of Gotham.", "stars":4},
{"restaurant_id":10, "user_id":2,
"review":"Wacky interiors! And oh, those cupcakes!", "stars":5},
{"restaurant_id":10, "user_id":3,
"review":"Solid meal options. Keeps my energy up for the night.", "stars":4},
{"restaurant_id":11, "user_id":1,
"review":"A culinary orchestra of flavors. Impressed.", "stars":5},
{"restaurant_id":11, "user_id":2,
"review":"Twirls and swirls! Loved their ice cream selection.", "stars":5},
{"restaurant_id":11, "user_id":3,
"review":"Bit crowded, but a decent place to hang with the crew.", "stars":3},
{"restaurant_id":12, "user_id":1,
"review":"An exquisite fusion of Eastern and Western flavors.", "stars":5},
{"restaurant_id":12, "user_id":2,
       "review":"Hee-hee! Their live band was just my kind of crazy!", "stars":5},
{"restaurant_id":12, "user_id":3,
"review":"Perfectly balanced meals. Great for staying in shape.", "stars":4},
{"restaurant_id":13, "user_id":1,
"review":"Simple, yet elegant. Reminds me of home.", "stars":4},
{"restaurant_id":13, "user_id":2,
"review":"Could use a bit more chaos, but the food was explosive!", "stars":4},
{"restaurant_id":13, "user_id":3,
"review":"Diverse menu. Something for every kind of night out.", "stars":4},
{"restaurant_id":14, "user_id":1,
"review":"A delightful gourmet experience. Felt like a trip around the world.", "stars":5},
{"restaurant_id":14, "user_id":2,
"review":"So many shiny things! And oh, the cakes were good too.", "stars":5},
{"restaurant_id":14, "user_id":3,
"review":"Nice and quiet. Perfect for some downtime after action.", "stars":4},
{"restaurant_id":15, "user_id":1,
"review":"Their selection of teas is unparalleled. A comforting experience.", "stars":5},
{"restaurant_id":15, "user_id":2,
"review":"Bright, colorful, and sparkly! Just like moi!", "stars":5},
{"restaurant_id":15, "user_id":3,
"review":"Healthy options. Keeps me agile and ready.", "stars":4},
{"restaurant_id":16, "user_id":1,
"review":"A fine dining experience reminiscent of European elegance.", "stars":5},
{"restaurant_id":16, "user_id":2,
"review":"Boom! Pow! Their spicy dishes packed a punch!", "stars":4},
{"restaurant_id":16, "user_id":3,
"review":"A good mix of protein-packed dishes. Excellent for training.", "stars":4},
{"restaurant_id":17, "user_id":1,
"review":"Quite the cozy spot with a vintage touch. Lovely.", "stars":4},
{"restaurant_id":17, "user_id":2,
"review":"Playful and quirky! Their dessert menu was a riot!", "stars":5},
{"restaurant_id":17, "user_id":3,
"review":"Open space, easy exits. And the food's great too.", "stars":4},
{"restaurant_id":18, "user_id":1,
"review":"Top-tier service and a delightful culinary presentation.", "stars":5},
{"restaurant_id":18, "user_id":2,
"review":"More sprinkles! But the juggling waiter was fun.", "stars":4},
{"restaurant_id":18, "user_id":3,
"review":"Comfort food that hits the spot. Just what I needed.", "stars":4},
{"restaurant_id":19, "user_id":1,
"review":"Their afternoon tea set is second to none.", "stars":5},
{"restaurant_id":19, "user_id":2,
"review":"Pop! Bang! Zing! Loved the sizzlers!", "stars":5},
{"restaurant_id":19, "user_id":3,
"review":"Feels like a place where you can just be yourself. Good vibes.", "stars":4},
{"restaurant_id":20, "user_id":1,
"review":"Perhaps a bit too modern for my old taste, but the cuisine is impeccable.", "stars":4},
{"restaurant_id":20, "user_id":2,
"review":"Wish they had a bigger dessert menu, but the ambiance was fun!", "stars":4},
{"restaurant_id":20, "user_id":3,
"review":"Solid place to grab a meal. Would come back.", "stars":4},
{"restaurant_id":21, "user_id":1, "review":"A bit too avant-garde for my liking, but impeccably presented dishes.", "stars":3},
{"restaurant_id":21, "user_id":2, "review":"Hee hee! Their funky drinks were something else!", "stars":4},
{"restaurant_id":21, "user_id":3, "review":"A bit fancy, but the food was top-notch.", "stars":4},




{"restaurant_id":22, "user_id":1, "review":"The chefs truly understand the essence of traditional cooking.", "stars":5},
{"restaurant_id":22, "user_id":2, "review":"More glitter, please! But the burgers were to die for.", "stars":4},
{"restaurant_id":22, "user_id":3, "review":"Liked their quick service. Ideal for a quick refuel.", "stars":4},




{"restaurant_id":23, "user_id":1, "review":"A lovely establishment reminiscent of countryside inns.", "stars":4},
{"restaurant_id":23, "user_id":2, "review":"Teehee! Their fun-themed nights are a blast!", "stars":5},
{"restaurant_id":23, "user_id":3, "review":"The outdoor seating is great for people-watching.", "stars":4},




{"restaurant_id":24, "user_id":1, "review":"The seafood selection was exquisite. Very fresh.", "stars":5},
{"restaurant_id":24, "user_id":2, "review":"I'd prefer more pinks and reds, but the pie! Yum!", "stars":4},
{"restaurant_id":24, "user_id":3, "review":"Had a hearty meal. Would recommend the steak.", "stars":4},




{"restaurant_id":25, "user_id":1, "review":"The sommelier's choices were impeccable.", "stars":5},
{"restaurant_id":25, "user_id":2, "review":"Not enough fireworks in their dishes, but tasty!", "stars":3},
{"restaurant_id":25, "user_id":3, "review":"Good spot to discuss strategies with the team.", "stars":4},




{"restaurant_id":26, "user_id":1, "review":"The dessert menu took me on a trip down memory lane.", "stars":5},
{"restaurant_id":26, "user_id":2, "review":"Pop, fizz, and sparkle! Loved their soda selection.", "stars":5},
{"restaurant_id":26, "user_id":3, "review":"Quick bites perfect for the on-the-go lifestyle.", "stars":4},




{"restaurant_id":27, "user_id":1, "review":"The live piano performance added a touch of class.", "stars":4},
{"restaurant_id":27, "user_id":2, "review":"Dance floor + snacks : Perfect evening!", "stars":5},
{"restaurant_id":27, "user_id":3, "review":"A mix of casual and classy. Liked the balance.", "stars":4},




{"restaurant_id":28, "user_id":1, "review":"An ambiance that takes one back to the glory days.", "stars":5},
{"restaurant_id":28, "user_id":2, "review":"More toys would be fun, but the candy was delish!", "stars":4},
{"restaurant_id":28, "user_id":3, "review":"The salad bar was diverse and fresh. Kudos!", "stars":4},




{"restaurant_id":29, "user_id":1, "review":"Their fusion dishes are a treat for the taste buds.", "stars":4},
{"restaurant_id":29, "user_id":2, "review":"Twisty, twirly, fun desserts! More, please!", "stars":5},
{"restaurant_id":29, "user_id":3, "review":"The lighting set the mood right. And great food to boot.", "stars":4},




{"restaurant_id":30, "user_id":1, "review":"An elegant evening guaranteed. Top-tier service.", "stars":5},
{"restaurant_id":30, "user_id":2, "review":"Loved the quirky interiors! And the jello!", "stars":5},
{"restaurant_id":30, "user_id":3, "review":"Stealthy corner spots and good food. Win-win.", "stars":4},
{"restaurant_id":31, "user_id":1, "review":"The tapas here are reminiscent of my travels to Spain.", "stars":4},
{"restaurant_id":31, "user_id":2, "review":"Whoopee! The dance performances added to the dining experience.", "stars":5},
{"restaurant_id":31, "user_id":3, "review":"Good portion sizes. Fuel up before the mission.", "stars":4},




{"restaurant_id":32, "user_id":1, "review":"The wine pairing was impeccable. A treat for the senses.", "stars":5},
{"restaurant_id":32, "user_id":2, "review":"Bright lights and fun drinks! My kinda place.", "stars":5},
{"restaurant_id":32, "user_id":3, "review":"Efficient and quiet. Can strategize while dining.", "stars":4},




{"restaurant_id":33, "user_id":1, "review":"The sushi chef is a master of his craft.", "stars":5},
{"restaurant_id":33, "user_id":2, "review":"More glittery sushi rolls, please! But oh, the taste!", "stars":4},
{"restaurant_id":33, "user_id":3, "review":"Healthy options, keeps me in top form.", "stars":4},




{"restaurant_id":34, "user_id":1, "review":"The pastries are as delightful as an English morning.", "stars":5},
{"restaurant_id":34, "user_id":2, "review":"Twirl and spin! Loved the live music and cake.", "stars":5},
{"restaurant_id":34, "user_id":3, "review":"Quiet nooks to relax and enjoy the brew.", "stars":4},




{"restaurant_id":35, "user_id":1, "review":"The handcrafted cocktails are the highlight.", "stars":5},
{"restaurant_id":35, "user_id":2, "review":"Fireworks and fizzes! What an exciting menu!", "stars":5},
{"restaurant_id":35, "user_id":3, "review":"A great selection of protein dishes. Keeps me going.", "stars":4},




{"restaurant_id":36, "user_id":1, "review":"The truffles here are second to none.", "stars":5},
{"restaurant_id":36, "user_id":2, "review":"Bouncy and bubbly! Loved the atmosphere.", "stars":4},
{"restaurant_id":36, "user_id":3, "review":"High-quality ingredients make for a great meal.", "stars":4},




{"restaurant_id":37, "user_id":1, "review":"Every dish tells a story. An epicurean journey.", "stars":5},
{"restaurant_id":37, "user_id":2, "review":"Swoosh and splash! Their water-themed night was a blast.", "stars":5},
{"restaurant_id":37, "user_id":3, "review":"Plenty of greens and lean meats. Ideal.", "stars":4},




{"restaurant_id":38, "user_id":1, "review":"Their caviar selection is world-class.", "stars":5},
{"restaurant_id":38, "user_id":2, "review":"Wish there was a slide, but the food made up for it!", "stars":4},
{"restaurant_id":38, "user_id":3, "review":"A discreet spot with outstanding dishes.", "stars":4},




{"restaurant_id":39, "user_id":1, "review":"The chef's tasting menu was a revelation.", "stars":5},
{"restaurant_id":39, "user_id":2, "review":"Zap! Pow! Their spicy noodles are electrifying!", "stars":5},
{"restaurant_id":39, "user_id":3, "review":"The balance of flavors is just right. Keeps the senses sharp.", "stars":4},




{"restaurant_id":40, "user_id":1, "review":"A gastronomic wonderland. Truly a delight.", "stars":5},
{"restaurant_id":40, "user_id":2, "review":"Rollercoaster of tastes and textures! Wee!", "stars":5},
{"restaurant_id":40, "user_id":3, "review":"Prime spot for recon and food both.", "stars":4},
{"restaurant_id":41, "user_id":1, "review":"A taste of authentic Mediterranean cuisine. A pleasant surprise.", "stars":4},
{"restaurant_id":41, "user_id":2, "review":"Juggling olives and twirling pasta! Such a festive mood.", "stars":5},
{"restaurant_id":41, "user_id":3, "review":"Nutritious dishes that don't compromise on flavor.", "stars":4},




{"restaurant_id":42, "user_id":1, "review":"The aged cheeses here remind me of the old European charm.", "stars":5},
{"restaurant_id":42, "user_id":2, "review":"Whee! The pizza spinning show was exhilarating!", "stars":5},
{"restaurant_id":42, "user_id":3, "review":"Carb-rich menu. Good for an energy boost.", "stars":4},




{"restaurant_id":43, "user_id":1, "review":"The coffee brews are sourced from the finest beans.", "stars":5},
{"restaurant_id":43, "user_id":2, "review":"More froth, more fun! Their lattes are a treat.", "stars":4},
{"restaurant_id":43, "user_id":3, "review":"A good vantage point and a strong brew. Ideal combination.", "stars":4},




{"restaurant_id":44, "user_id":1, "review":"Their seafood platter is fresh from the ocean.", "stars":5},
{"restaurant_id":44, "user_id":2, "review":"Splash and dash! Loved the marine-themed night.", "stars":5},
{"restaurant_id":44, "user_id":3, "review":"High in Omega-3. Perfect for brain and brawn.", "stars":4},




{"restaurant_id":45, "user_id":1, "review":"The sommelier's recommendations were on point.", "stars":5},
{"restaurant_id":45, "user_id":2, "review":"Pop the cork and let's dance! Vivacious atmosphere.", "stars":5},
{"restaurant_id":45, "user_id":3, "review":"Balanced meals with a good range of wine. Ideal for a night out.", "stars":4},




{"restaurant_id":46, "user_id":1, "review":"The desserts are both delicate and rich. A fine balance.", "stars":5},
{"restaurant_id":46, "user_id":2, "review":"Spin, twirl, and dessert whirl! A carnival of sweetness.", "stars":4},
{"restaurant_id":46, "user_id":3, "review":"Sweet treats that keep the spirits high.", "stars":4},




{"restaurant_id":47, "user_id":1, "review":"The charcuterie board was a symphony of flavors.", "stars":5},
{"restaurant_id":47, "user_id":2, "review":"Jazz and cheese, please! What a combination.", "stars":5},
{"restaurant_id":47, "user_id":3, "review":"Good protein options and easy access. Will return.", "stars":4},




{"restaurant_id":48, "user_id":1, "review":"The vegan options are crafted with care.", "stars":5},
{"restaurant_id":48, "user_id":2, "review":"Green, clean, and oh so fun! The plant-based menu rocks.", "stars":5},
{"restaurant_id":48, "user_id":3, "review":"Healthy and delicious. Keeps me agile.", "stars":4},




{"restaurant_id":49, "user_id":1, "review":"The dishes evoke memories of my travels in Asia.", "stars":5},
{"restaurant_id":49, "user_id":2, "review":"Bam! Pow! The spices hit just right.", "stars":5},
{"restaurant_id":49, "user_id":3, "review":"Variety of cuisines. Keeps things interesting.", "stars":4},




{"restaurant_id":50, "user_id":1, "review":"The gourmet burger here is a class apart.", "stars":5},
{"restaurant_id":50, "user_id":2, "review":"Flip, flop, and hop! Burger nights are the best.", "stars":5},
{"restaurant_id":50, "user_id":3, "review":"Quick bites that pack a punch. Energizing.", "stars":4}
]




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
        hours='9-5'),


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
        hours='9-5'




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
        hours='9-5'




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
        hours='9-5'




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
        hours='9-5'




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
        hours='9-5'




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
        hours='9-5'




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
        hours='9-5'




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
        hours='9-5'




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
        hours='9-5'




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
        hours='9-5'




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
        hours='9-5'




    ),








]




user_list=[
    User(
        firstName="Alfred",
        lastName="Pennyworth",
        username='Demo',
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
        email='catwoman@gotham.com',
        streetAddress="456 Feline Alley",
        city="Gotham",
        state="New Jersey",
        postalCode="10303",
        country="United States",
        phone='710-681-2839'),




    User(
        firstName="Osward",
        lastName="Cobblepot",
        username='ThePenguin',
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
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
        password="password",
        email='cassandra@gotham.com',
        streetAddress="2222 Bat Street",
        city="Gotham",
        state="New Jersey",
        postalCode="11515",
        country="United States",
        phone='710-681-2851')
]
def seed_users():
    new_user_list=[]








    for ele in user_list:
        db.session.add(ele)
        db.session.commit()
        new_user_list.append(ele)


    restaurant_counter=1
    our_owner_id=0
    for ele in restaurant_list:
        if restaurant_counter<=13:
            our_owner_id=new_user_list[0].id


        #Harley
        elif restaurant_counter<=15:
            our_owner_id=new_user_list[1].id
        #Nightwing
        elif restaurant_counter==16:
            our_owner_id=new_user_list[2].id
            #Joker
        elif restaurant_counter<=19:
            our_owner_id=new_user_list[3].id
            #Catwoman
        elif restaurant_counter<=22:
            our_owner_id=new_user_list[4].id
        elif restaurant_counter<=25:
            our_owner_id=new_user_list[5].id
            #Riddler
        elif restaurant_counter<=28:
            our_owner_id=new_user_list[6].id
            #Two face
        elif restaurant_counter<=31:
            our_owner_id=new_user_list[7].id
            #mr freeze
        elif restaurant_counter<=33:
            our_owner_id=new_user_list[8].id
            #scarecrow
        elif restaurant_counter<=35:
            our_owner_id=new_user_list[9].id
            #Rachel Dawes
        elif restaurant_counter<=38:
            our_owner_id=new_user_list[10].id
            #Lucious
        elif restaurant_counter<=40:
            our_owner_id=new_user_list[11].id
            #Oracle
        elif restaurant_counter<=42:
            our_owner_id=new_user_list[12].id
            #Tim
        elif restaurant_counter<=44:
            our_owner_id=new_user_list[13].id
        elif restaurant_counter<=46:
            our_owner_id=new_user_list[14].id
        elif restaurant_counter<=48:
            our_owner_id=new_user_list[15].id




        else:
            our_owner_id=new_user_list[16].id




        ele.owner_id=our_owner_id
        restaurant_counter+=1
        db.session.add(ele)
    db.session.commit()
    counterTo3=0
    counterTo50=0
    add_all_reviews=[]
    owner_fallback_id=4
    for index,ele in enumerate(reviews_list):
        counterTo50 = index // 3
        counterTo3 = index % 3


        ele["restaurant_id"]=restaurant_list[counterTo50].id


        if restaurant_list[counterTo50].owner_id == user_list[counterTo3].id:
            ele["user_id"]=user_list[counterTo3].id if restaurant_list[counterTo50].owner_id!=user_list[counterTo3].id else 4
        else:
            ele["user_id"] = user_list[counterTo3].id


        newReview=Review(restaurant_id=ele["restaurant_id"],
                         user_id=ele["user_id"],
                         review=ele["review"],
                         stars=ele["stars"])
        add_all_reviews.append(newReview)
    db.session.add_all(add_all_reviews)
    db.session.commit()




































def undo_users():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.restaurants RESTART IDENTITY CASCADE;")
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")




    else:
        db.session.execute(text("DELETE FROM reviews"))
        db.session.execute(text("DELETE FROM restaurants"))
        db.session.execute(text("DELETE FROM users"))




    db.session.commit()



