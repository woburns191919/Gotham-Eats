
from sqlalchemy import text
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

from ..models import db, MenuItem,MenuItemImg,ShoppingCart, environment, SCHEMA
from sqlalchemy.sql import text
from random import randint, random
from faker import Faker







filename_entree_list=["buffalo_chicken_sandwich", "chicken_tenders", "fish_tacos", "lasagna", "philly_cheesesteak",  "spaghetti", "chicken_fajita", "fettuccine_alfredo", "gyro", "lobster", "pizza", "steak", "bbq_ribs", "chicken_parmesan", "fish_and_chips", "hamburger", "meatball_sandwich", "shish_kebab"]
















Entree_List=['Buffalo Chicken Sandwich', 'Chicken Tenders', 'Fish Tacos', "Lasagna", "Philly Cheesesteak", "Spaghetti", 'Chicken Fajita',"Fettuccine Alfredo", "Gyro", "Lobster", "Pizza", "Steak", "BBQ Ribs", "Chicken Parm", "Fish & Chips", "Hamburger", "Meatball Sandwich", "Shish Kebab"]
















filename_dessert_list=["blueberry_tart","chocolate_chip_cookie",  "lava_cake", "pumpkin_pie", "carrot_cake",  "chocolate_mousse","milkshake", "strawberry_shortcake", "apple_pie", "cheesecake",  "cupcake", "peach_cobbler", "tiramisu", "banana_split",  "chocolate_brownie",  "flan", "pistachio_gelato",  "vanilla_icecream"]
















dessert_list=["Blueberry tart","Chocolate Chip Cookie","Lava Cake","Pumpkin pie",'Carrot Cake',"Chocolate Mousse","Milkshake","Strawberry Shortcake",'Apple Pie',"Cheesecake","Cupcake","Peach Cobbler","Tiramisu","Banana Split","Chocolate Brownie","Flan","Pistachio Gelato","Vanilla IceCream"]
















filename_drink_list=["cappuccino","gotham_red_wine","margarita","redbull","seven_and_seven","sprite","gotham_white_wine","lemonade","martini","root_beer","shirley_temple","Coffee","gotham_beer","long_island_iced_tea","pepsi","rum_and_coke","smoothie"]
















drink_list=["Cappuccino", "Gotham Red Wine", "Margarita", "Redbull", "Seven and Seven", "Sprite", "Gotham White Wine", "Lemonade", "Martini", "Root Beer", "Shirley Temple", "Coffee", "Gotham Beer", "Long Island Iced Tea", "Pepsi", "Rum and Coke", "Smoothie"]
















filename_sides_list=["chicken_wings","fried_rice", "green_beans","mozarella_sticks", "roasted_veggies","corn_on_the_cob  fries", "lo_mein", "nachos", "sweet_potato_fries","baked_potato", "creamed_spinach", "garden_salad  mac_and_cheese","onion_rings","tater_tots",
"breadsticks", "edemame", "garlic_bread  mashed_potatoes",  "roasted_cauliflower"]
















sides_list=["Chicken Wings", "Fried Rice", "Green Beans", "Mozarella Sticks", "Roasted Veggies", "Corn on the Cob", "Fries", "Lo Mein", "Nachos", "Sweet Potato Fries", "Baked Potato", "Creamed Spinach", "Garden Salad", "Mac and Cheese", "Onion Rings", "Tater Tots", "Breadsticks", "Edemame", "Garlic Bread", "Mashed_Potatoes", "Roasted Cauliflower"]
















drink_translator={
"Cappuccino":f"/assets/menu_item_images/drinks/cappuccino/img_{randint(1, 5)}.jpeg",
"Gotham Red Wine": f"/assets/menu_item_images/drinks/gotham_red_wine/img_{randint(1, 5)}.jpeg",
"Margarita": f"/assets/menu_item_images/drinks/margarita/img_{randint(1, 5)}.jpeg",
"Redbull": f"/assets/menu_item_images/drinks/redbull/img_{randint(1, 5)}.jpeg",
"Seven and Seven":  f"/assets/menu_item_images/drinks/seven_and_seven/img_{randint(1, 5)}.jpeg",
"Sprite": f"/assets/menu_item_images/drinks/sprite/img_{randint(1, 5)}.jpeg",
"Gotham White Wine": f"/assets/menu_item_images/drinks/gotham_white_wine/img_{randint(1, 5)}.jpeg",
"Lemonade": f"/assets/menu_item_images/drinks/lemonade/img_{randint(1, 5)}.jpeg",
"Martini": f"/assets/menu_item_images/drinks/martini/img_{randint(1, 5)}.jpeg",
"Root Beer": f"/assets/menu_item_images/drinks/root_beer/img_{randint(1, 5)}.jpeg",
"Shirley Temple":  f"/assets/menu_item_images/drinks/shirley_temple/img_{randint(1, 5)}.jpeg",
"Coffee":  f"/assets/menu_item_images/drinks/Coffee/img_{randint(1, 5)}.jpeg",
"Gotham Beer": f"/assets/menu_item_images/drinks/gotham_beer/img_{randint(1, 5)}.jpeg",
"Long Island Iced Tea":  f"/assets/menu_item_images/drinks/long_island_iced_tea/img_{randint(1, 5)}.jpeg",
"Pepsi":  f"/assets/menu_item_images/drinks/pepsi/img_{randint(1, 5)}.jpeg",
"Rum and Coke":  f"/assets/menu_item_images/drinks/rum_and_coke/img_{randint(1, 5)}.jpeg",
"Smoothie": f"/assets/menu_item_images/drinks/smoothie/img_{randint(1, 5)}.jpeg",
}








drink_translator={
"Cappuccino":f"/assets/menu_item_images/drinks/cappuccino/img_{randint(1, 5)}.jpeg",
"Gotham Red Wine": f"/assets/menu_item_images/drinks/gotham_red_wine/img_{randint(1, 5)}.jpeg",
"Margarita": f"/assets/menu_item_images/drinks/margarita/img_{randint(1, 5)}.jpeg",
"Redbull": f"/assets/menu_item_images/drinks/redbull/img_{randint(1, 5)}.jpeg",
"Seven and Seven":  f"/assets/menu_item_images/drinks/seven_and_seven/img_{randint(1, 5)}.jpeg",
"Sprite": f"/assets/menu_item_images/drinks/sprite/img_{randint(1, 5)}.jpeg",
"Gotham White Wine": f"/assets/menu_item_images/drinks/gotham_white_wine/img_{randint(1, 5)}.jpeg",
"Lemonade": f"/assets/menu_item_images/drinks/lemonade/img_{randint(1, 5)}.jpeg",
"Martini": f"/assets/menu_item_images/drinks/martini/img_{randint(1, 5)}.jpeg",
"Root Beer": f"/assets/menu_item_images/drinks/root_beer/img_{randint(1, 5)}.jpeg",
"Shirley Temple":  f"/assets/menu_item_images/drinks/shirley_temple/img_{randint(1, 5)}.jpeg",
"Coffee":  f"/assets/menu_item_images/drinks/Coffee/img_{randint(1, 5)}.jpeg",
"Gotham Beer": f"/assets/menu_item_images/drinks/gotham_beer/img_{randint(1, 5)}.jpeg",
"Long Island Iced Tea":  f"/assets/menu_item_images/drinks/long_island_iced_tea/img_{randint(1, 5)}.jpeg",
"Pepsi":  f"/assets/menu_item_images/drinks/pepsi/img_{randint(1, 5)}.jpeg",
"Rum and Coke":  f"/assets/menu_item_images/drinks/rum_and_coke/img_{randint(1, 5)}.jpeg",
"Smoothie":     f"/assets/menu_item_images/drinks/smoothie/img_{randint(1, 5)}.jpeg",

















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


changes=7






keysToVillains=["1_penguin","2_riddler","3_ivy","4_two_face","5_scarecrow","6_catwoman","7_batman","8_joker","9_bane","10_mr_freeze","11_clayface","12_firefly","13_mad_hatter","14_talon","15_zatanna","16_bat_man","17_mayor","18_green_arrow","19_everyone_else"]

entree_names = list(entree_translator.keys())
dessert_names = list(dessert_translator.keys())
drink_names = list(drink_translator.keys())
side_names = list(sides_translator.keys())

















def fake_price():
    num1= randint(5,30)
    num2= randint(10,99)
    return f"{num1}.{num2}"


def seed_menu_items():
    restaurant_counter=1
    menu_item_img_counter=1
    our_guy=None
    master_entrees=[]
    master_drinks=[]
    master_desserts=[]
    master_sides=[]
    master_menu_item_imgs=[]


    for i in range(0,50):
        entree_name_end = entree_names[randint(0,17)]
        dessert_name_end= dessert_names[randint(0,17)]
        drink_name_end= drink_names[randint(0,16)]
        side_name_end= side_names[randint(0,20)]

        #Alfred
        if restaurant_counter<=13:
            our_guy="1_Alfred"
        #Harley
        elif restaurant_counter<=15:
            our_guy="2_Harley"
        #Nightwing
        elif restaurant_counter==16:
            our_guy="3_DickGrayson"
            #Joker
        elif restaurant_counter<=19:
            our_guy="4_Joker"
            #Catwoman
        elif restaurant_counter<=22:
            our_guy="5_Catwoman"
        elif restaurant_counter<=25:
            our_guy="6_ThePenguin"
            #Riddler
        elif restaurant_counter<=28:
            our_guy="7_TheRiddler"
            #Two face
        elif restaurant_counter<=31:
            our_guy="8_TwoFace"
            #mr freeze
        elif restaurant_counter<=33:
            our_guy="9_MrFreeze"
            #scarecrow
        elif restaurant_counter<=35:
            our_guy="10_TheScarecrow"
            #Rachel Dawes
        elif restaurant_counter<=38:
            our_guy="11_RachelDawes"
            #Lucious
        elif restaurant_counter<=40:
            our_guy="12_LuciusFox"
            #Oracle
        elif restaurant_counter<=42:
            our_guy="13_BarbaraGordon"
            #Tim
        elif restaurant_counter<=44:
            our_guy="14_TimDrake"
        elif restaurant_counter<=46:
            our_guy="15_JasonTodd"
        elif restaurant_counter<=48:
            our_guy="16_DamianWayne"

        else:
            our_guy="17_CassandraCain"


        curr_adj_list = villain_adj_dict[our_guy]
        all_entrees=[]
        all_desserts=[]
        all_drinks=[]
        all_sides=[]
        all_menu_item_imgs=[]
        for k in range(0,11):


            #add ENTREE and picture for it***************************
            currEntree=MenuItem(
            restaurant_id=restaurant_counter,
            menu_item_img_id=menu_item_img_counter,
            name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {entree_name_end}",
            description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {entree_name_end}s",
            price=float(fake_price()),
            type="entree",
            shopping_cart_id=restaurant_counter
        )
            db.session.add(currEntree)
            db.session.commit()


            menu_item_img_counter+=1


            changes2=MenuItemImg(
                menu_item_id=currEntree.id,
                url=entree_translator[entree_name_end],
                preview= True if k==0 else False
            )
            db.session.add(changes2)
            currEntree.menu_item_img_id=changes2.id
            db.session.commit()



    # user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    # menu_item_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("menu_items.id")))
    # quantity = db.Column(db.Integer, nullable=False)
    # created_at=db.Column(db.DateTime, default=datetime.now())
    # updated_at=db.Column(db.DateTime, default=datetime.now())

            #add SIDE and picture for it****************************
            currSide=MenuItem(
                restaurant_id=restaurant_counter,
                menu_item_img_id=menu_item_img_counter,
                name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {side_name_end}", description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]}{dessert_name_end}s",
                price=float(fake_price()),
                type="side",
                shopping_cart_id=restaurant_counter)
            db.session.add(currSide)
            db.session.commit()
            menu_item_img_counter+=1

            changes2=MenuItemImg(
                menu_item_id=currSide.id,
                url=sides_translator[side_name_end],
                preview= False)
            db.session.add(changes2)
            db.session.commit()

            currSide.menu_item_img_id=changes2.id

            #add DESSERT and picture for it************************
            currDessert=MenuItem(
                restaurant_id=restaurant_counter,
                menu_item_img_id=menu_item_img_counter,
                name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {dessert_name_end}", description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {dessert_name_end}s",
                price=float(fake_price()),
                type="dessert")
            db.session.add(currDessert)
            db.session.commit()
            menu_item_img_counter+=1


            changes2=MenuItemImg(
                menu_item_id=currDessert.id,
                url=dessert_translator[dessert_name_end],
                preview= False)
            db.session.add(changes2)
            db.session.commit()
            currDessert.menu_item_img_id=changes2.id

            #add DRINK and picture for it*********************
            currDrink=MenuItem(
                restaurant_id=restaurant_counter,
                menu_item_img_id=menu_item_img_counter,
                name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {drink_name_end}",
                description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {entree_name_end}s",
                price=float(fake_price()),
                type="drink")
            db.session.add(currDrink)
            db.session.commit()
            menu_item_img_counter+=1


            changes2=MenuItemImg(
                menu_item_id=currDrink.id,
                url=drink_translator[drink_name_end],
                preview= False)


            db.session.add(changes2)
            db.session.commit()
            currDrink.menu_item_img_id=changes2.id

        restaurant_counter+=1

def undo_menu_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menu_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menu_items"))
    db.session.commit()

