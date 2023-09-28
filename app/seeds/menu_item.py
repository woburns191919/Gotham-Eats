from ..models import db, MenuItem,MenuItemImg, environment, SCHEMA
from random import randint
from datetime import datetime
from faker import Faker
import random
# from ..menu_item_translators import entree_translator, dessert_translator, drink_translator, sides_translator
fake = Faker()
drink_translator={
"Cappuccino":f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/cappuccino/img_{randint(1, 5)}.jpeg",
"Gotham Red Wine": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/gotham_red_wine/img_{randint(1, 5)}.jpeg",
"Margarita": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/margarita/img_{randint(1, 5)}.jpeg",
"Redbull": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/redbull/img_{randint(1, 5)}.jpeg",
"Seven and Seven":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/seven_and_seven/img_{randint(1, 5)}.jpeg",
"Sprite": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/sprite/img_{randint(1, 5)}.jpeg",
"Gotham White Wine": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/gotham_white_wine/img_{randint(1, 5)}.jpeg",
"Lemonade": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/lemonade/img_{randint(1, 5)}.jpeg",
"Martini": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/martini/img_{randint(1, 5)}.jpeg",
"Root Beer": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/root_beer/img_{randint(1, 5)}.jpeg",
"Shirley Temple":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/shirley_temple/img_{randint(1, 5)}.jpeg",
"Coffee":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/Coffee/img_{randint(1, 5)}.jpeg",
"Gotham Beer": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/gotham_beer/img_{randint(1, 5)}.jpeg",
"Long Island Iced Tea":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/long_island_iced_tea/img_{randint(1, 5)}.jpeg",
"Pepsi":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/pepsi/img_{randint(1, 5)}.jpeg",
"Rum and Coke":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/rum_and_coke/img_{randint(1, 5)}.jpeg",
"Smoothie": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/smoothie/img_{randint(1, 5)}.jpeg",
}
drink_translator={
"Cappuccino":f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/cappuccino/img_{randint(1, 5)}.jpeg",
"Gotham Red Wine": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/gotham_red_wine/img_{randint(1, 5)}.jpeg",
"Margarita": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/margarita/img_{randint(1, 5)}.jpeg",
"Redbull": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/redbull/img_{randint(1, 5)}.jpeg",
"Seven and Seven":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/seven_and_seven/img_{randint(1, 5)}.jpeg",
"Sprite": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/sprite/img_{randint(1, 5)}.jpeg",
"Gotham White Wine": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/gotham_white_wine/img_{randint(1, 5)}.jpeg",
"Lemonade": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/lemonade/img_{randint(1, 5)}.jpeg",
"Martini": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/martini/img_{randint(1, 5)}.jpeg",
"Root Beer": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/root_beer/img_{randint(1, 5)}.jpeg",
"Shirley Temple":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/shirley_temple/img_{randint(1, 5)}.jpeg",
"Coffee":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/Coffee/img_{randint(1, 5)}.jpeg",
"Gotham Beer": f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/gotham_beer/img_{randint(1, 5)}.jpeg",
"Long Island Iced Tea":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/long_island_iced_tea/img_{randint(1, 5)}.jpeg",
"Pepsi":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/pepsi/img_{randint(1, 5)}.jpeg",
"Rum and Coke":  f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/rum_and_coke/img_{randint(1, 5)}.jpeg",
"Smoothie":     f"https://flask3.s3.amazonaws.com/menu_item_images/drinks/smoothie/img_{randint(1, 5)}.jpeg",
}
entree_translator= {
    "Buffalo Chicken Sandwich": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/buffalo_chicken_sandwich/img_{randint(1, 5)}.jpeg",
    "Chicken Tenders": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/chicken_tenders/img_{randint(1, 5)}.jpeg",
    "Lasagna": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/lasagna/img_{randint(1, 5)}.jpeg",
    "Philly Cheesesteak": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/philly_cheesesteak/img_{randint(1, 5)}.jpeg",
    "Spaghetti": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/spaghetti/img_{randint(1, 5)}.jpeg",
    "Chicken Fajita": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/chicken_fajita/img_{randint(1, 5)}.jpeg",
    "Fettuccine Alfredo": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/fettuccine_alfredo/img_{randint(1, 5)}.jpeg",
    "Gyro": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/gyro/img_{randint(1, 5)}.jpeg",
    "Lobster": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/lobster/img_{randint(1, 5)}.jpeg",
    "Steak": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/steak/img_{randint(1, 5)}.jpeg",
    "BBQ Ribs": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/bbq_ribs/img_{randint(1, 5)}.jpeg",
    "Chicken Parm": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/chicken_parmesean/img_{randint(1, 5)}.jpeg",
    "Fish & Chips": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/fish_and_chips/img_{randint(1, 5)}.jpeg",
    "Hamburger": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/hamburger/img_{randint(1, 5)}.jpeg",
    "Meatball Sandwich": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/meatball_sandwich/img_{randint(1, 5)}.jpeg",
    "Shish Kebab": f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/shish_kebab/img_{randint(1, 5)}.jpeg",
    "Fish Tacos" : f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/fish_tacos/img_{randint(1, 5)}.jpeg",
    "Pizza" : f"https://flask3.s3.amazonaws.com/menu_item_images/entrees/pizza/img_{randint(1, 5)}.jpeg"
}
dessert_translator= {
    'Blueberry tart': f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/blueberry_tart/img_{randint(1, 5)}.jpeg",
    "Chocolate Chip Cookie": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/blueberry_tart/img_{randint(1, 5)}.jpeg",
    "Lava Cake": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/lava_cake/img_{randint(1, 5)}.jpeg",
    "Pumpkin pie": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/pumpkin_pie/img_{randint(1, 5)}.jpeg",
    'Carrot Cake': f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/carrot_cake/img_{randint(1, 5)}.jpeg",
    "Chocolate Mousse": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/chocolate_mousse/img_{randint(1, 5)}.jpeg",
    "Milkshake": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/milkshake/img_{randint(1, 5)}.jpeg",
    "Strawberry Shortcake": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/strawberry_shortcake/img_{randint(1, 5)}.jpeg",
    'Apple Pie': f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/apple_pie/img_{randint(1, 5)}.jpeg",
    "Cheesecake": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/cheesecake/img_{randint(1, 5)}.jpeg",
    "Cupcake": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/cupcake/img_{randint(1, 5)}.jpeg",
    "Peach Cobbler": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/peach_cobbler/img_{randint(1, 5)}.jpeg",
    "Tiramisu": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/tiramisu/img_{randint(1, 5)}.jpeg",
    "Banana Split": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/banana_split/img_{randint(1, 5)}.jpeg",
    "Chocolate Brownie": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/chocolate_brownie/img_{randint(1, 5)}.jpeg",
    "Flan": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/flan/img_{randint(1, 5)}.jpeg",
    "Pistachio Gelato": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/pistachio_gelato/img_{randint(1, 5)}.jpeg",
    "Vanilla IceCream": f"https://flask3.s3.amazonaws.com/menu_item_images/desserts/vanilla_icecream/img_{randint(1, 5)}.jpeg"
}
sides_translator= {
"Chicken Wings": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/chicken_wings/img_{randint(1, 5)}.jpeg",
"Fried Rice": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/fried_rice/img_{randint(1, 5)}.jpeg",
"Green Beans": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/green_beans/img_{randint(1, 5)}.jpeg",
"Mozarella Sticks": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/mozarella_sticks/img_{randint(1, 5)}.jpeg",
"Roasted Veggies": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/roasted_veggies/img_{randint(1, 5)}.jpeg",
"Corn on the Cob": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/corn_on_the_cob/img_{randint(1, 5)}.jpeg",
"Fries": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/fries/img_{randint(1, 5)}.jpeg",
"Lo Mein": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/lo_mein/img_{randint(1, 5)}.jpeg",
"Nachos": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/nachos/img_{randint(1, 5)}.jpeg",
"Sweet Potato Fries": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/sweet_potato_fries/img_{randint(1, 5)}.jpeg",
"Baked Potato": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/baked_potato/img_{randint(1, 5)}.jpeg",
"Creamed Spinach": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/creamed_spinach/img_{randint(1, 5)}.jpeg",
"Garden Salad": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/garden_salad/img_{randint(1, 5)}.jpeg",
"Mac and Cheese": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/mac_and_cheese/img_{randint(1, 5)}.jpeg",
"Onion Rings": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/onion_rings/img_{randint(1, 5)}.jpeg",
"Tater Tots": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/tater_tots/img_{randint(1, 5)}.jpeg",
"Breadsticks": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/breadsticks/img_{randint(1, 5)}.jpeg",
"Edemame": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/edemame/img_{randint(1, 5)}.jpeg",
"Garlic Bread": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/garlic_bread/img_{randint(1, 5)}.jpeg",
"Mashed_Potatoes": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/mashed_potatoes/img_{randint(1, 5)}.jpeg",
"Roasted Cauliflower": f"https://flask3.s3.amazonaws.com/menu_item_images/sides/roasted_cauliflower/img_{randint(1, 5)}.jpeg"

}

entree_names = list(entree_translator.keys())
dessert_names = list(dessert_translator.keys())
drink_names = list(drink_translator.keys())
side_names = list(sides_translator.keys())

# def seed_menu_items():
#     for restaurant_counter in range(1, 51):
#         entree_name = fake.random_element(elements=entree_names)
#         dessert_name = fake.random_element(elements=dessert_names)
#         drink_name = fake.random_element(elements=drink_names)
#         side_name = fake.random_element(elements=side_names)
#         # Create MenuItemImg instances
#         entree_img = MenuItemImg(
#             menu_item_id=restaurant_counter,
#             url=entree_translator[entree_name],
#             preview=True,
#         )

#         dessert_img = MenuItemImg(
#             menu_item_id=restaurant_counter,
#             url=dessert_translator[dessert_name],
#             preview=True,
#         )
#         drink_img = MenuItemImg(
#             menu_item_id=restaurant_counter,
#             url=drink_translator[drink_name],
#             preview=True,
#         )
#         side_img = MenuItemImg(
#             menu_item_id=restaurant_counter,
#             url=sides_translator[side_name],
#             preview=True,
#         )
def seed_menu_items():

    entree_images = [entree_translator[name] for name in entree_names]
    dessert_images = [dessert_translator[name] for name in dessert_names]
    drink_images = [drink_translator[name] for name in drink_names]
    side_images = [sides_translator[name] for name in side_names]

    for restaurant_counter in range(1, 51):
        entree_name = fake.random_element(elements=entree_names)
        dessert_name = fake.random_element(elements=dessert_names)
        drink_name = fake.random_element(elements=drink_names)
        side_name = fake.random_element(elements=side_names)

        entree_img = MenuItemImg(
            menu_item_id=restaurant_counter,
            url=random.choice(entree_images),
            preview=True,
        )

        dessert_img = MenuItemImg(
            menu_item_id=restaurant_counter,
            url=random.choice(dessert_images),
            preview=True,
        )

        drink_img = MenuItemImg(
            menu_item_id=restaurant_counter,
            url=random.choice(drink_images),
            preview=True,
        )

        side_img = MenuItemImg(
            menu_item_id=restaurant_counter,
            url=random.choice(side_images),
            preview=True,
        )

        # Create MenuItem instances
        entree_item = MenuItem(
            restaurant_id=restaurant_counter,
            menu_item_img=entree_img,
            name=entree_name,
            description=fake.sentence(),
            price=fake.random_element(elements=(5.99, 8.99, 10.99)),
            type="Entree",
        )

        dessert_item = MenuItem(
            restaurant_id=restaurant_counter,
            menu_item_img=dessert_img,
            name=dessert_name,
            description=fake.sentence(),
            price=fake.random_element(elements=(3.99, 4.99, 6.99)),
            type="Dessert",
        )

        drink_item = MenuItem(
            restaurant_id=restaurant_counter,
            menu_item_img=drink_img,
            name=drink_name,
            description=fake.sentence(),
            price=fake.random_element(elements=(1.99, 2.99, 3.49)),
            type="Drink",
        )

        side_item = MenuItem(
            restaurant_id=restaurant_counter,
            menu_item_img=side_img,
            name=side_name,
            description=fake.sentence(),
            price=fake.random_element(elements=(2.99, 3.49, 4.99)),
            type="Side",
        )

        db.session.add(entree_img)
        db.session.add(dessert_img)
        db.session.add(drink_img)
        db.session.add(side_img)

        db.session.add(entree_item)
        db.session.add(dessert_item)
        db.session.add(drink_item)
        db.session.add(side_item)

    db.session.commit()

if __name__ == '__main__':
    seed_menu_items()

def undo_menu_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menu_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menu_items"))
    db.session.commit()
