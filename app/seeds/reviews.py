from ..models import db, environment, SCHEMA, Review
from sqlalchemy.sql import text
import json

reviews_list = [
    Review(restaurant_id=1, user_id=1,
           review="The service was as meticulous as I am with Master Wayne's suits. Quite splendid.", stars=4),
    Review(restaurant_id=1, user_id=2,
           review="Puddin' would have loved the desserts here! Teehee!", stars=5),
    Review(restaurant_id=1, user_id=3,
           review="Great spot for a quick bite after patrol. Felt right at home.", stars=4),
    Review(restaurant_id=2, user_id=1,
           review="Reminds me of the lavish dinners in Wayne Manor. Top-notch.", stars=5),
    Review(restaurant_id=2, user_id=2,
           review="Not chaotic enough for my taste, but the food's not bad.", stars=3),
    Review(restaurant_id=2, user_id=3,
           review="Had a quiet corner perfect for keeping an eye on the entrance. Food was great too.", stars=4),
    Review(restaurant_id=3, user_id=1,
           review="A bit too noisy, but the tea was brewed perfectly.", stars=4),
    Review(restaurant_id=3, user_id=2,
           review="Oh, the colors! Loved the vibrant atmosphere. More candy, please!", stars=5),
    Review(restaurant_id=3, user_id=3,
           review="They've got a rooftop seating. Perfect view for any activities.", stars=5),
    Review(restaurant_id=4, user_id=1,
           review="Their soup of the day took me back to London.", stars=4),
    Review(restaurant_id=4, user_id=2,
           review="Had a blast with their musical chairs! Food's yum too.", stars=5),
    Review(restaurant_id=4, user_id=3,
           review="Lighting was a bit too bright for my taste. Food was decent.", stars=3),
    Review(restaurant_id=5, user_id=1,
           review="Their classic English breakfast was heartwarming.", stars=4),
    Review(restaurant_id=5, user_id=2,
           review="Fun and lively! Could use more sprinkles though.", stars=4),
    Review(restaurant_id=5, user_id=3,
           review="Convenient location for those late-night stakeouts.", stars=3),
    Review(restaurant_id=6, user_id=1,
           review="The wine selection is nothing short of exquisite.", stars=5),
    Review(restaurant_id=6, user_id=2,
           review="Meh, needed more pizzazz! But the pie was good.", stars=3),
    Review(restaurant_id=6, user_id=3,
           review="Relaxing ambiance. Could use this as a good meetup spot.", stars=4),
    Review(restaurant_id=7, user_id=1,
           review="The ambiance reminds me of the old days, quite nostalgic.", stars=4),
    Review(restaurant_id=7, user_id=2,
           review="A rollercoaster of flavors! Whee!", stars=5),
    Review(restaurant_id=7, user_id=3,
           review="A decent place to chill. The espresso shot was on point.", stars=4),
    Review(restaurant_id=8, user_id=1,
           review="Subtle and refined flavors. Quite the culinary experience.", stars=5),
    Review(restaurant_id=8, user_id=2,
           review="Boop-oop-a-doop! I liked the carnival theme!", stars=5),
    Review(restaurant_id=8, user_id=3,
           review="Good rooftop views, and the food wasn't half bad.", stars=4),
    Review(restaurant_id=9, user_id=1,
           review="Reminded me of the cafes in Paris. Delightful!", stars=5),
    Review(restaurant_id=9, user_id=2,
           review="Could use a mallet on their menu, but overall fun!", stars=4),
    Review(restaurant_id=9, user_id=3,
           review="Fast service. Got my meal and was out in a flash.", stars=4),
    Review(restaurant_id=10, user_id=1,
           review="A serene experience, away from the chaos of Gotham.", stars=4),
    Review(restaurant_id=10, user_id=2,
           review="Wacky interiors! And oh, those cupcakes!", stars=5),
    Review(restaurant_id=10, user_id=3,
           review="Solid meal options. Keeps my energy up for the night.", stars=4),
    Review(restaurant_id=11, user_id=1,
           review="A culinary orchestra of flavors. Impressed.", stars=5),
    Review(restaurant_id=11, user_id=2,
           review="Twirls and swirls! Loved their ice cream selection.", stars=5),
    Review(restaurant_id=11, user_id=3,
           review="Bit crowded, but a decent place to hang with the crew.", stars=3),
    Review(restaurant_id=12, user_id=1,
           review="An exquisite fusion of Eastern and Western flavors.", stars=5),
    Review(restaurant_id=12, user_id=2,
           review="Hee-hee! Their live band was just my kind of crazy!", stars=5),
    Review(restaurant_id=12, user_id=3,
           review="Perfectly balanced meals. Great for staying in shape.", stars=4),
    Review(restaurant_id=13, user_id=1,
           review="Simple, yet elegant. Reminds me of home.", stars=4),
    Review(restaurant_id=13, user_id=2,
           review="Could use a bit more chaos, but the food was explosive!", stars=4),
    Review(restaurant_id=13, user_id=3,
           review="Diverse menu. Something for every kind of night out.", stars=4),
    Review(restaurant_id=14, user_id=1,
           review="A delightful gourmet experience. Felt like a trip around the world.", stars=5),
    Review(restaurant_id=14, user_id=2,
           review="So many shiny things! And oh, the cakes were good too.", stars=5),
    Review(restaurant_id=14, user_id=3,
           review="Nice and quiet. Perfect for some downtime after action.", stars=4),
    Review(restaurant_id=15, user_id=1,
           review="Their selection of teas is unparalleled. A comforting experience.", stars=5),
    Review(restaurant_id=15, user_id=2,
           review="Bright, colorful, and sparkly! Just like moi!", stars=5),
    Review(restaurant_id=15, user_id=3,
           review="Healthy options. Keeps me agile and ready.", stars=4),
    Review(restaurant_id=16, user_id=1,
           review="A fine dining experience reminiscent of European elegance.", stars=5),
    Review(restaurant_id=16, user_id=2,
           review="Boom! Pow! Their spicy dishes packed a punch!", stars=4),
    Review(restaurant_id=16, user_id=3,
           review="A good mix of protein-packed dishes. Excellent for training.", stars=4),
    Review(restaurant_id=17, user_id=1,
           review="Quite the cozy spot with a vintage touch. Lovely.", stars=4),
    Review(restaurant_id=17, user_id=2,
           review="Playful and quirky! Their dessert menu was a riot!", stars=5),
    Review(restaurant_id=17, user_id=3,
           review="Open space, easy exits. And the food's great too.", stars=4),
    Review(restaurant_id=18, user_id=1,
           review="Top-tier service and a delightful culinary presentation.", stars=5),
    Review(restaurant_id=18, user_id=2,
           review="More sprinkles! But the juggling waiter was fun.", stars=4),
    Review(restaurant_id=18, user_id=3,
           review="Comfort food that hits the spot. Just what I needed.", stars=4),
    Review(restaurant_id=19, user_id=1,
           review="Their afternoon tea set is second to none.", stars=5),
    Review(restaurant_id=19, user_id=2,
           review="Pop! Bang! Zing! Loved the sizzlers!", stars=5),
    Review(restaurant_id=19, user_id=3,
           review="Feels like a place where you can just be yourself. Good vibes.", stars=4),
    Review(restaurant_id=20, user_id=1,
           review="Perhaps a bit too modern for my old taste, but the cuisine is impeccable.", stars=4),
    Review(restaurant_id=20, user_id=2,
           review="Wish they had a bigger dessert menu, but the ambiance was fun!", stars=4),
    Review(restaurant_id=20, user_id=3,
           review="Solid place to grab a meal. Would come back.", stars=4),
]


def seed_reviews():
    for ele in reviews_list:
        db.session.add(ele)
        db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
        db.session.commit()
