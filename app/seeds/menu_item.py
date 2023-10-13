from sqlalchemy import text
from ..models import db, MenuItem, MenuItemImg, environment, SCHEMA
from random import randint
from datetime import datetime
from faker import Faker
import random
# from ..menu_item_translators import entree_translator, dessert_translator, drink_translator, sides_translator
fake = Faker()
drink_translator = {
    "Cappuccino": f"react-app/src/assets/menu_item_images/drinks/cappuccino/img_{randint(1, 5)}.jpeg",
    "Gotham Red Wine": f"react-app/src/assets/menu_item_images/drinks/gotham_red_wine/img_{randint(1, 5)}.jpeg",
    "Margarita": f"react-app/src/assets/menu_item_images/drinks/margarita/img_{randint(1, 5)}.jpeg",
    "Redbull": f"react-app/src/assets/menu_item_images/drinks/redbull/img_{randint(1, 5)}.jpeg",
    "Seven and Seven":  f"react-app/src/assets/menu_item_images/drinks/seven_and_seven/img_{randint(1, 5)}.jpeg",
    "Sprite": f"react-app/src/assets/menu_item_images/drinks/sprite/img_{randint(1, 5)}.jpeg",
    "Gotham White Wine": f"react-app/src/assets/menu_item_images/drinks/gotham_white_wine/img_{randint(1, 5)}.jpeg",
    "Lemonade": f"react-app/src/assets/menu_item_images/drinks/lemonade/img_{randint(1, 5)}.jpeg",
    "Martini": f"react-app/src/assets/menu_item_images/drinks/martini/img_{randint(1, 5)}.jpeg",
    "Root Beer": f"react-app/src/assets/menu_item_images/drinks/root_beer/img_{randint(1, 5)}.jpeg",
    "Shirley Temple":  f"react-app/src/assets/menu_item_images/drinks/shirley_temple/img_{randint(1, 5)}.jpeg",
    "Coffee":  f"react-app/src/assets/menu_item_images/drinks/Coffee/img_{randint(1, 5)}.jpeg",
    "Gotham Beer": f"react-app/src/assets/menu_item_images/drinks/gotham_beer/img_{randint(1, 5)}.jpeg",
    "Long Island Iced Tea":  f"react-app/src/assets/menu_item_images/drinks/long_island_iced_tea/img_{randint(1, 5)}.jpeg",
    "Pepsi":  f"react-app/src/assets/menu_item_images/drinks/pepsi/img_{randint(1, 5)}.jpeg",
    "Rum and Coke":  f"react-app/src/assets/menu_item_images/drinks/rum_and_coke/img_{randint(1, 5)}.jpeg",
    "Smoothie": f"react-app/src/assets/menu_item_images/drinks/smoothie/img_{randint(1, 5)}.jpeg",
}
entree_translator = {
    "Buffalo Chicken Sandwich": f"react-app/src/assets/menu_item_images/entrees/buffalo_chicken_sandwich/img_{randint(1, 5)}.jpeg",
    "Chicken Tenders": f"react-app/src/assets/menu_item_images/entrees/chicken_tenders/img_{randint(1, 5)}.jpeg",
    "Lasagna": f"react-app/src/assets/menu_item_images/entrees/lasagna/img_{randint(1, 5)}.jpeg",
    "Philly Cheesesteak": f"react-app/src/assets/menu_item_images/entrees/philly_cheesesteak/img_{randint(1, 5)}.jpeg",
    "Spaghetti": f"react-app/src/assets/menu_item_images/entrees/spaghetti/img_{randint(1, 5)}.jpeg",
    "Chicken Fajita": f"react-app/src/assets/menu_item_images/entrees/chicken_fajita/img_{randint(1, 5)}.jpeg",
    "Fettuccine Alfredo": f"react-app/src/assets/menu_item_images/entrees/fettuccine_alfredo/img_{randint(1, 5)}.jpeg",
    "Gyro": f"react-app/src/assets/menu_item_images/entrees/gyro/img_{randint(1, 5)}.jpeg",
    "Lobster": f"react-app/src/assets/menu_item_images/entrees/lobster/img_{randint(1, 5)}.jpeg",
    "Steak": f"react-app/src/assets/menu_item_images/entrees/steak/img_{randint(1, 5)}.jpeg",
    "BBQ Ribs": f"react-app/src/assets/menu_item_images/entrees/bbq_ribs/img_{randint(1, 5)}.jpeg",
    "Chicken Parm": f"react-app/src/assets/menu_item_images/entrees/chicken_parmesean/img_{randint(1, 5)}.jpeg",
    "Fish & Chips": f"react-app/src/assets/menu_item_images/entrees/fish_and_chips/img_{randint(1, 5)}.jpeg",
    "Hamburger": f"react-app/src/assets/menu_item_images/entrees/hamburger/img_{randint(1, 5)}.jpeg",
    "Meatball Sandwich": f"react-app/src/assets/menu_item_images/entrees/meatball_sandwich/img_{randint(1, 5)}.jpeg",
    "Shish Kebab": f"react-app/src/assets/menu_item_images/entrees/shish_kebab/img_{randint(1, 5)}.jpeg",
    "Fish Tacos": f"react-app/src/assets/menu_item_images/entrees/fish_tacos/img_{randint(1, 5)}.jpeg",
    "Pizza": f"react-app/src/assets/menu_item_images/entrees/pizza/img_{randint(1, 5)}.jpeg"
}
dessert_translator = {
    'Blueberry tart': f"react-app/src/assets/menu_item_images/desserts/blueberry_tart/img_{randint(1, 5)}.jpeg",
    "Chocolate Chip Cookie": f"react-app/src/assets/menu_item_images/desserts/blueberry_tart/img_{randint(1, 5)}.jpeg",
    "Lava Cake": f"react-app/src/assets/menu_item_images/desserts/lava_cake/img_{randint(1, 5)}.jpeg",
    "Pumpkin pie": f"react-app/src/assets/menu_item_images/desserts/pumpkin_pie/img_{randint(1, 5)}.jpeg",
    'Carrot Cake': f"react-app/src/assets/menu_item_images/desserts/carrot_cake/img_{randint(1, 5)}.jpeg",
    "Chocolate Mousse": f"react-app/src/assets/menu_item_images/desserts/chocolate_mousse/img_{randint(1, 5)}.jpeg",
    "Milkshake": f"react-app/src/assets/menu_item_images/desserts/milkshake/img_{randint(1, 5)}.jpeg",
    "Strawberry Shortcake": f"react-app/src/assets/menu_item_images/desserts/strawberry_shortcake/img_{randint(1, 5)}.jpeg",
    'Apple Pie': f"react-app/src/assets/menu_item_images/desserts/apple_pie/img_{randint(1, 5)}.jpeg",
    "Cheesecake": f"react-app/src/assets/menu_item_images/desserts/cheesecake/img_{randint(1, 5)}.jpeg",
    "Cupcake": f"react-app/src/assets/menu_item_images/desserts/cupcake/img_{randint(1, 5)}.jpeg",
    "Peach Cobbler": f"react-app/src/assets/menu_item_images/desserts/peach_cobbler/img_{randint(1, 5)}.jpeg",
    "Tiramisu": f"react-app/src/assets/menu_item_images/desserts/tiramisu/img_{randint(1, 5)}.jpeg",
    "Banana Split": f"react-app/src/assets/menu_item_images/desserts/banana_split/img_{randint(1, 5)}.jpeg",
    "Chocolate Brownie": f"react-app/src/assets/menu_item_images/desserts/chocolate_brownie/img_{randint(1, 5)}.jpeg",
    "Flan": f"react-app/src/assets/menu_item_images/desserts/flan/img_{randint(1, 5)}.jpeg",
    "Pistachio Gelato": f"react-app/src/assets/menu_item_images/desserts/pistachio_gelato/img_{randint(1, 5)}.jpeg",
    "Vanilla IceCream": f"react-app/src/assets/menu_item_images/desserts/vanilla_icecream/img_{randint(1, 5)}.jpeg"
}
sides_translator = {
    "Chicken Wings": f"react-app/src/assets/menu_item_images/sides/chicken_wings/img_{randint(1, 5)}.jpeg",
    "Fried Rice": f"react-app/src/assets/menu_item_images/sides/fried_rice/img_{randint(1, 5)}.jpeg",
    "Green Beans": f"react-app/src/assets/menu_item_images/sides/green_beans/img_{randint(1, 5)}.jpeg",
    "Mozarella Sticks": f"react-app/src/assets/menu_item_images/sides/mozarella_sticks/img_{randint(1, 5)}.jpeg",
    "Roasted Veggies": f"react-app/src/assets/menu_item_images/sides/roasted_veggies/img_{randint(1, 5)}.jpeg",
    "Corn on the Cob": f"react-app/src/assets/menu_item_images/sides/corn_on_the_cob/img_{randint(1, 5)}.jpeg",
    "Fries": f"react-app/src/assets/menu_item_images/sides/fries/img_{randint(1, 5)}.jpeg",
    "Lo Mein": f"react-app/src/assets/menu_item_images/sides/lo_mein/img_{randint(1, 5)}.jpeg",
    "Nachos": f"react-app/src/assets/menu_item_images/sides/nachos/img_{randint(1, 5)}.jpeg",
    "Sweet Potato Fries": f"react-app/src/assets/menu_item_images/sides/sweet_potato_fries/img_{randint(1, 5)}.jpeg",
    "Baked Potato": f"react-app/src/assets/menu_item_images/sides/baked_potato/img_{randint(1, 5)}.jpeg",
    "Creamed Spinach": f"react-app/src/assets/menu_item_images/sides/creamed_spinach/img_{randint(1, 5)}.jpeg",
    "Garden Salad": f"react-app/src/assets/menu_item_images/sides/garden_salad/img_{randint(1, 5)}.jpeg",
    "Mac and Cheese": f"react-app/src/assets/menu_item_images/sides/mac_and_cheese/img_{randint(1, 5)}.jpeg",
    "Onion Rings": f"react-app/src/assets/menu_item_images/sides/onion_rings/img_{randint(1, 5)}.jpeg",
    "Tater Tots": f"react-app/src/assets/menu_item_images/sides/tater_tots/img_{randint(1, 5)}.jpeg",
    "Breadsticks": f"react-app/src/assets/menu_item_images/sides/breadsticks/img_{randint(1, 5)}.jpeg",
    "Edemame": f"react-app/src/assets/menu_item_images/sides/edemame/img_{randint(1, 5)}.jpeg",
    "Garlic Bread": f"react-app/src/assets/menu_item_images/sides/garlic_bread/img_{randint(1, 5)}.jpeg",
    "Mashed_Potatoes": f"react-app/src/assets/menu_item_images/sides/mashed_potatoes/img_{randint(1, 5)}.jpeg",
    "Roasted Cauliflower": f"react-app/src/assets/menu_item_images/sides/roasted_cauliflower/img_{randint(1, 5)}.jpeg"
}








villain_adj_dict = {
    "1_Alfred": ["loyal", "wise", "resourceful", "dedicated", "caring", "supportive", "knowledgeable", "discreet", "sophisticated", "dependable"],
    "2_Harley": ["manic", "unpredictable", "energetic", "devoted", "intelligent", "agile", "impulsive", "chaotic", "humorous", "enthusiastic"],
    "3_DickGrayson": ["agile", "resilient", "optimistic", "charismatic", "dedicated", "skilled", "athletic", "intelligent", "compassionate", "courageous"],
    "4_Joker": ["maniacal", "unpredictable", "intelligent", "cunning", "sadistic", "chaotic", "twisted", "anarchistic", "manipulative", "psychopathic"],
    "5_Catwoman": ["stealthy", "agile", "mysterious", "seductive", "intelligent", "resourceful", "independent", "adaptive", "calculating", "alluring"],
    "6_ThePenguin": ["scheming", "sophisticated", "intelligent", "manipulative", "ruthless", "resourceful", "calculating", "ambitious", "cunning", "eccentric"],
    "7_TheRiddler": ["intelligent", "obsessive", "complex", "enigmatic", "cunning", "manipulative", "calculating", "competitive", "puzzling", "cryptic"],
    "8_TwoFace": ["conflicted", "unpredictable", "vengeful", "bitter", "dualistic", "ruthless", "decisive", "disturbed", "resilient", "calculating"],
    "9_MrFreeze": ["cold", "driven", "intelligent", "melancholic", "stoic", "methodical", "isolated", "determined", "compassionate", "tragic"],
    "10_TheScarecrow": ["fearful", "intelligent", "manipulative", "cunning", "obsessive", "sadistic", "calculating", "chilling", "psychopathic", "menacing"],
    "11_RachelDawes": ["principled", "compassionate", "determined", "idealistic", "brave", "intelligent", "empathetic", "steadfast", "resilient", "courageous"],
    "12_LuciusFox": ["ingenious", "resourceful", "intelligent", "pragmatic", "loyal", "wise", "innovative", "ethical", "supportive", "confidential"],
    "13_BarbaraGordon": ["intelligent", "determined", "resourceful", "brave", "compassionate", "athletic", "inspirational", "adaptive", "analytical", "resilient"],
    "14_TimDrake": ["deductive", "intelligent", "resourceful", "disciplined", "analytical", "persistent", "adaptive", "strategic", "brave", "motivated"],
    "15_JasonTodd": ["rebellious", "impulsive", "skilled", "resilient", "vengeful", "intense", "determined", "brave", "conflicted", "aggressive"],
    "16_DamianWayne": ["disciplined", "confident", "skilled", "arrogant", "brave", "determined", "intelligent", "loyal", "stubborn", "focused"],
    "17_CassandraCain": ["silent", "observant", "lethal", "agile", "disciplined", "intuitive", "resilient", "adaptive", "compassionate", "fierce"],
    "19_everyone_else": ["mouth-watering", "delightful", "scrumptious", "appetizing", "delectable", "enticing", "irresistible", "tasty", "flavorful", "savoring", "tempting", "yummy", "divine", "palatable" "lip-smacking", "satisfying", "succulent", "indulgent", "inspirational"]
}








keysToVillains = ["1_penguin", "2_riddler", "3_ivy", "4_two_face", "5_scarecrow", "6_catwoman", "7_batman", "8_joker", "9_bane", "10_mr_freeze",
                  "11_clayface", "12_firefly", "13_mad_hatter", "14_talon", "15_zatanna", "16_bat_man", "17_mayor", "18_green_arrow", "19_everyone_else"]




entree_names = list(entree_translator.keys())
dessert_names = list(dessert_translator.keys())
drink_names = list(drink_translator.keys())
side_names = list(sides_translator.keys())
















def fake_price():
    num1 = randint(5, 30)
    num2 = randint(10, 99)
    return f"{num1}.{num2}"








def seed_menu_items():
    restaurant_counter = 0
    menu_item_img_counter = 1
    our_guy = None
    master_entrees = []
    master_drinks = []
    master_desserts = []
    master_sides = []
    master_menu_item_imgs = []
    restaurant_counter=0


    for i in range(0, 49):


        restaurant_counter += 1
        # Alfred
        if restaurant_counter <= 13:
            our_guy = "1_Alfred"
        # Harley
        elif restaurant_counter <= 15:
            our_guy = "2_Harley"
        # Nightwing
        elif restaurant_counter == 16:
            our_guy = "3_DickGrayson"
            # Joker
        elif restaurant_counter <= 19:
            our_guy = "4_Joker"
            # Catwoman
        elif restaurant_counter <= 22:
            our_guy = "5_Catwoman"
        elif restaurant_counter <= 25:
            our_guy = "6_ThePenguin"
            # Riddler
        elif restaurant_counter <= 28:
            our_guy = "7_TheRiddler"
            # Two face
        elif restaurant_counter <= 31:
            our_guy = "8_TwoFace"
            # mr freeze
        elif restaurant_counter <= 33:
            our_guy = "9_MrFreeze"
            # scarecrow
        elif restaurant_counter <= 35:
            our_guy = "10_TheScarecrow"
            # Rachel Dawes
        elif restaurant_counter <= 38:
            our_guy = "11_RachelDawes"
            # Lucious
        elif restaurant_counter <= 40:
            our_guy = "12_LuciusFox"
            # Oracle
        elif restaurant_counter <= 42:
            our_guy = "13_BarbaraGordon"
            # Tim
        elif restaurant_counter <= 44:
            our_guy = "14_TimDrake"
        elif restaurant_counter <= 46:
            our_guy = "15_JasonTodd"
        elif restaurant_counter <= 48:
            our_guy = "16_DamianWayne"
        else:
            our_guy = "17_CassandraCain"




        curr_adj_list = villain_adj_dict[our_guy]
        all_entrees = []
        all_desserts = []
        all_drinks = []
        all_sides = []
        all_menu_item_imgs = []








        for k in range(0, 3):
            entree_name_end = entree_names[randint(0, 12)]
            dessert_name_end = dessert_names[randint(0, 12)]
            drink_name_end = drink_names[randint(0, 14)]
            side_name_end = side_names[randint(0, 15)]








    ####create my entree.  chhange variable is 1
            changes1 = MenuItemImg(








            url=entree_translator[entree_name_end],
            preview=True if k == 0 else False
        )
            db.session.add(changes1)
            db.session.commit()










            currEntree = MenuItem(
            restaurant_id=restaurant_counter,
            menu_item_img_id=changes1.id,
            name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {entree_name_end}",
            description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {entree_name_end}s",
            price=float(fake_price()),
            type="entree",
            shopping_cart_id=restaurant_counter
        )
            db.session.add(currEntree)
            db.session.commit()
            currEntree.menu_item_img_id=changes1.id
            changes1.menu_item_id=currEntree.id
            db.session.commit()








        # create my side.   change variable is 2
            changes2 = MenuItemImg(
            url=sides_translator[side_name_end],
            preview=False
        )
            db.session.add(changes2)
            db.session.commit()
            currSide = MenuItem(
            restaurant_id=restaurant_counter,
            menu_item_img_id=changes2.id,
            name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {side_name_end}",
            description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {side_name_end}s",
            price=float(fake_price()),
            type="side",
            shopping_cart_id=restaurant_counter
        )
            db.session.add(currSide)
            db.session.commit()
            currSide.menu_item_img_id=changes2.id
            changes2.menu_item_id=currSide.id
            db.session.commit()








        # create dessert .  change variable is 3
            changes3 = MenuItemImg(
            url=dessert_translator[dessert_name_end],
            preview=False
        )
            db.session.add(changes3)
            db.session.commit()








            currDessert = MenuItem(
            restaurant_id=restaurant_counter,
            menu_item_img_id=changes3.id,
            name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {dessert_name_end}",
            description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {dessert_name_end}s",
            price=float(fake_price()),
            type="dessert",
            shopping_cart_id=restaurant_counter
        )
            db.session.add(currDessert)
            db.session.commit()
            currDessert.menu_item_img_id=changes3.id
            changes3.menu_item_id=currDessert.id
            db.session.commit()






        # create my drink.  change variable is 4
            changes4 = MenuItemImg(
            url=drink_translator[drink_name_end],
            preview=False
        )
            db.session.add(changes4)
            db.session.commit()
















            currDrink = MenuItem(
            restaurant_id=restaurant_counter,
            menu_item_img_id=changes4.id,
            name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {drink_name_end}",
            description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {drink_name_end}s",
            price=float(fake_price()),
            type="drink",
            shopping_cart_id=restaurant_counter
        )
            db.session.add(currDrink)
            db.session.commit()
            currDrink.menu_item_img_id=changes4.id
            changes4.menu_item_id=currDrink.id
            db.session.commit()






















def undo_menu_items():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.menu_items RESTART IDENTITY CASCADE;")


        db.session.execute(
            f"TRUNCATE table {SCHEMA}.menu_item_imgs RESTART IDENTITY CASCADE;")


    else:
        db.session.execute(text("DELETE FROM menu_items"))
        db.session.execute(text("DELETE FROM menu_item_imgs"))




    db.session.commit()
