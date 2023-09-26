from ..models import db, MenuItem,MenuItemImg, environment, SCHEMA
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
"Cappuccino":f"/menu_item_images/drinks/cappuccino/img ({randint(1, 5)}).jpeg",
"Gotham Red Wine": f"/menu_item_images/drinks/gotham_red_wine/img ({randint(1, 5)}).jpeg",
"Margarita": f"/menu_item_images/drinks/margarita/img ({randint(1, 5)}).jpeg",
"Redbull": f"/menu_item_images/drinks/redbull/img ({randint(1, 5)}).jpeg",
"Seven and Seven":  f"/menu_item_images/drinks/seven_and_seven/img ({randint(1, 5)}).jpeg",
"Sprite": f"/menu_item_images/drinks/sprite/img ({randint(1, 5)}).jpeg",
"Gotham White Wine": f"/menu_item_images/drinks/gotham_white_wine/img ({randint(1, 5)}).jpeg",
"Lemonade": f"/menu_item_images/drinks/lemonade/img ({randint(1, 5)}).jpeg",
"Martini": f"/menu_item_images/drinks/martini/img ({randint(1, 5)}).jpeg",
"Root Beer": f"/menu_item_images/drinks/root_beer/img ({randint(1, 5)}).jpeg",
"Shirley Temple":  f"/menu_item_images/drinks/shirley_temple/img ({randint(1, 5)}).jpeg",
"Coffee":  f"/menu_item_images/drinks/Coffee/img ({randint(1, 5)}).jpeg",
"Gotham Beer": f"/menu_item_images/drinks/gotham_beer/img ({randint(1, 5)}).jpeg",
"Long Island Iced Tea":  f"/menu_item_images/drinks/long_island_iced_tea/img ({randint(1, 5)}).jpeg",
"Pepsi":  f"/menu_item_images/drinks/pepsi/img ({randint(1, 5)}).jpeg",
"Rum and Coke":  f"/menu_item_images/drinks/rum_and_coke/img ({randint(1, 5)}).jpeg",
"Smoothie": f"/menu_item_images/drinks/smoothie/img ({randint(1, 5)}).jpeg",
}


entree_translator= {
    "Buffalo Chicken Sandwich": f"/menu_item_images/entrees/buffalo_chicken_sandwich/img ({randint(1, 5)}).jpeg",
    "Chicken Tenders": f"/menu_item_images/entrees/chicken_tenders/img ({randint(1, 5)}).jpeg",
    "Lasagna": f"/menu_item_images/entrees/lasagna/img ({randint(1, 5)}).jpeg",
    "Philly Cheesesteak": f"/menu_item_images/entrees/philly_cheesesteak/img ({randint(1, 5)}).jpeg",
    "Spaghetti": f"/menu_item_images/entrees/spaghetti/img ({randint(1, 5)}).jpeg",
    "Chicken Fajita": f"/menu_item_images/entrees/chicken_fajita/img ({randint(1, 5)}).jpeg",
    "Fettuccine Alfredo": f"/menu_item_images/entrees/fettuccine_alfredo/img ({randint(1, 5)}).jpeg",
    "Gyro": f"/menu_item_images/entrees/gyro/img ({randint(1, 5)}).jpeg",
    "Lobster": f"/menu_item_images/entrees/lobster/img ({randint(1, 5)}).jpeg",
    "Steak": f"/menu_item_images/entrees/steak/img ({randint(1, 5)}).jpeg",
    "BBQ Ribs": f"/menu_item_images/entrees/bbq_ribs/img ({randint(1, 5)}).jpeg",
    "Chicken Parm": f"/menu_item_images/entrees/chicken_parmesean/img ({randint(1, 5)}).jpeg",
    "Fish & Chips": f"/menu_item_images/entrees/fish_and_chips/img ({randint(1, 5)}).jpeg",
    "Hamburger": f"/menu_item_images/entrees/hamburger/img ({randint(1, 5)}).jpeg",
    "Meatball Sandwich": f"/menu_item_images/entrees/meatball_sandwich/img ({randint(1, 5)}).jpeg",
    "Shish Kebab": f"/menu_item_images/entrees/shish_kebab/img ({randint(1, 5)}).jpeg",
    "Fish Tacos" : f"/menu_item_images/entrees/fish_tacos/img ({randint(1, 5)}).jpeg",
    "Pizza" : f"/menu_item_images/entrees/pizza/img ({randint(1, 5)}).jpeg"
}


dessert_translator= {
    'Blueberry tart': f"/menu_item_images/desserts/blueberry_tart/img ({randint(1, 5)}).jpeg",
    "Chocolate Chip Cookie": f"/menu_item_images/desserts/blueberry_tart/img ({randint(1, 5)}).jpeg",
    "Lava Cake": f"/menu_item_images/desserts/lava_cake/img ({randint(1, 5)}).jpeg",
    "Pumpkin pie": f"/menu_item_images/desserts/pumpkin_pie/img ({randint(1, 5)}).jpeg",
    'Carrot Cake': f"/menu_item_images/desserts/carrot_cake/img ({randint(1, 5)}).jpeg",
    "Chocolate Mousse": f"/menu_item_images/desserts/chocolate_mousse/img ({randint(1, 5)}).jpeg",
    "Milkshake": f"/menu_item_images/desserts/milkshake/img ({randint(1, 5)}).jpeg",
    "Strawberry Shortcake": f"/menu_item_images/desserts/strawberry_shortcake/img ({randint(1, 5)}).jpeg",
    'Apple Pie': f"/menu_item_images/desserts/apple_pie/img ({randint(1, 5)}).jpeg",
    "Cheesecake": f"/menu_item_images/desserts/cheesecake/img ({randint(1, 5)}).jpeg",
    "Cupcake": f"/menu_item_images/desserts/cupcake/img ({randint(1, 5)}).jpeg",
    "Peach Cobbler": f"/menu_item_images/desserts/peach_cobbler/img ({randint(1, 5)}).jpeg",
    "Tiramisu": f"/menu_item_images/desserts/tiramisu/img ({randint(1, 5)}).jpeg",
    "Banana Split": f"/menu_item_images/desserts/banana_split/img ({randint(1, 5)}).jpeg",
    "Chocolate Brownie": f"/menu_item_images/desserts/chocolate_brownie/img ({randint(1, 5)}).jpeg",
    "Flan": f"/menu_item_images/desserts/flan/img ({randint(1, 5)}).jpeg",
    "Pistachio Gelato": f"/menu_item_images/desserts/pistachio_gelato/img ({randint(1, 5)}).jpeg",
    "Vanilla IceCream": f"/menu_item_images/desserts/vanilla_icecream/img ({randint(1, 5)}).jpeg"
}


sides_translator= {
"Chicken Wings": f"/menu_item_images/sides/chicken_wings/img ({randint(1, 5)}).jpeg",
"Fried Rice": f"/menu_item_images/sides/fried_rice/img ({randint(1, 5)}).jpeg",
"Green Beans": f"/menu_item_images/sides/green_beans/img ({randint(1, 5)}).jpeg",
"Mozarella Sticks": f"/menu_item_images/sides/mozarella_sticks/img ({randint(1, 5)}).jpeg",
"Roasted Veggies": f"/menu_item_images/sides/roasted_veggies/img ({randint(1, 5)}).jpeg",
"Corn on the Cob": f"/menu_item_images/sides/corn_on_the_cob/img ({randint(1, 5)}).jpeg",
"Fries": f"/menu_item_images/sides/fries/img ({randint(1, 5)}).jpeg",
"Lo Mein": f"/menu_item_images/sides/lo_mein/img ({randint(1, 5)}).jpeg",
"Nachos": f"/menu_item_images/sides/nachos/img ({randint(1, 5)}).jpeg",
"Sweet Potato Fries": f"/menu_item_images/sides/sweet_potato_fries/img ({randint(1, 5)}).jpeg",
"Baked Potato": f"/menu_item_images/sides/baked_potato/img ({randint(1, 5)}).jpeg",
"Creamed Spinach": f"/menu_item_images/sides/creamed_spinach/img ({randint(1, 5)}).jpeg",
"Garden Salad": f"/menu_item_images/sides/garden_salad/img ({randint(1, 5)}).jpeg",
"Mac and Cheese": f"/menu_item_images/sides/mac_and_cheese/img ({randint(1, 5)}).jpeg",
"Onion Rings": f"/menu_item_images/sides/onion_rings/img ({randint(1, 5)}).jpeg",
"Tater Tots": f"/menu_item_images/sides/tater_tots/img ({randint(1, 5)}).jpeg",
"Breadsticks": f"/menu_item_images/sides/breadsticks/img ({randint(1, 5)}).jpeg",
"Edemame": f"/menu_item_images/sides/edemame/img ({randint(1, 5)}).jpeg",
"Garlic Bread": f"/menu_item_images/sides/garlic_bread/img ({randint(1, 5)}).jpeg",
"Mashed_Potatoes": f"/menu_item_images/sides/mashed_potatoes/img ({randint(1, 5)}).jpeg",
"Roasted Cauliflower": f"/menu_item_images/sides/roasted_cauliflower/img ({randint(1, 5)}).jpeg"
}


villain_adj_dict = {
    "1_penguin": ["scheming", "waddling", "umbrella-toting", "calculating", "icy"],
    "2_riddler": ["enigmatic", "puzzling", "question-asking", "clever", "green-suited"],
    "3_ivy": ["seductive", "poisonous", "nature-loving", "manipulative", "vibrant"],
    "4_two_face": ["dual-personality", "coin-flipping", "disfigured", "ambivalent", "harvey-dent"],
    "5_scarecrow": ["fear-inducing", "terrifying", "sinister", "psychological", "straw-hat"],
    "6_catwoman": ["cat-like", "thief", "feline", "independent", "whip-wielding"],
    "7_batman": ["mysterious", "vigilante", "cape-wearing", "dark", "justice-seeking"],
    "8_joker": ["chaotic", "maniacal", "laughter-loving", "twisted", "purple-suited"],
    "9_bane": ["muscle-bound", "venom-injecting", "intelligent", "merciless", "masked"],
    "10_mr_freeze": ["cryogenic", "cold-hearted", "ice-obsessed", "tragic", "cryosuit-wearing"],
    "11_clayface": ["shape-shifting", "malleable", "actor", "melting", "mud-like"],
    "12_firefly": ["pyromaniac", "fire-starting", "winged", "arsonist", "flame-obsessed"],
    "13_mad_hatter": ["mad", "hat-wearing", "tea-obsessed", "eccentric", "mind-controlling"],
    "14_talon": ["lethal", "assassin", "feathered", "loyal", "Court-of-Owls"],
    "15_zatanna": ["magician", "spell-casting", "charming", "mystical", "top-hat-wearing"],
    "16_bat_man": ["bat-themed", "wealthy", "genius", "inventor", "gadget-equipped"],
    "17_mayor": ["politician", "corrupt", "powerful", "manipulative", "Gotham's leader"],
    "18_green_arrow": ["archer", "vigilante", "emerald-clad", "skilled", "arrow-shooting"],
    "19_everyone_else": ["mouth-watering", "delightful", "scrumptious", "appetizing", "delectable", "enticing", "irresistible", "tasty", "flavorful", "savoring", "tempting", "yummy", "divine", "palatable" "lip-smacking", "satisfying", "succulent", "indulgent", "inspirational"]
            }


keysToVillains=["1_penguin","2_riddler","3_ivy","4_two_face","5_scarecrow","6_catwoman","7_batman","8_joker","9_bane","10_mr_freeze","11_clayface","12_firefly","13_mad_hatter","14_talon","15_zatanna","16_bat_man","17_mayor","18_green_arrow","19_everyone_else"]




def fake_price():
    num1= randint(5,30)
    num2= randint(10,99)
    return f"{num1}.{num2}"


#START SEEDER*************************************
def seed_menu_items():
    counter=1
    our_guy=None
    master_entrees=[]
    master_drinks=[]
    master_desserts=[]
    master_sides=[]
    master_menu_item_imgs=[]




    for i in range(0,50):
        entree_name_end = Entree_List[randint(0,17)]
        dessert_name_end= dessert_list[randint(0,17)]
        drink_name_end= drink_list[randint(0,16)]
        side_name_end= sides_list[randint(0,20)]
        if counter<=18:
            our_guy=keysToVillains[counter-1]
        else:
            our_guy=keysToVillains[18]




        curr_adj_list = villain_adj_dict[our_guy]
        all_entrees=[]
        all_desserts=[]
        all_drinks=[]
        all_sides=[]
        all_menu_item_imgs=[]
        for k in range(0,11):


            #add ENTREE and picture for it***************************
            currEntree=MenuItem(
            restaurant_id=counter,
            menu_item_img_id=counter,
            name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {entree_name_end}",
            description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {entree_name_end}s",
            price=float(fake_price()),
            type="entree",
            shopping_cart_id=counter,


        )
            db.session.add(currEntree)
            db.session.commit()
            all_menu_item_imgs.append(MenuItemImg(
                menu_item_id=currEntree.id,
                url=entree_translator[entree_name_end],
                preview= True if k==0 else False
            )),




            #add SIDE and picture for it****************************
            currSide=MenuItem(
                restaurant_id=counter,
                menu_item_img_id=counter,
                name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {side_name_end}", description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]}{dessert_name_end}s",
                price=float(fake_price()),
                type="side",
                shopping_cart_id=counter)
            db.session.add(currSide)
            db.session.commit()


            all_menu_item_imgs.append(MenuItemImg(
                menu_item_id=currSide.id,
                url=sides_translator[side_name_end],
                preview= False))




            #add DESSERT and picture for it************************
            currDessert=MenuItem(
                restaurant_id=counter,
                menu_item_img_id=counter,
                name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {dessert_name_end}", description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {dessert_name_end}s",
                price=float(fake_price()),
                type="dessert")
            db.session.add(currDessert)
            db.session.commit()


            all_menu_item_imgs.append(MenuItemImg(
                menu_item_id=currDessert.id,
                url=dessert_translator[dessert_name_end],
                preview= False))


            #add DRINK and picture for it*********************
            currDrink=MenuItem(
                restaurant_id=counter,
                menu_item_img_id=counter,
                name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {drink_name_end}",
                description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {entree_name_end}s",
                price=float(fake_price()),
                type="drink")
            db.session.add(currDrink)
            db.session.commit()


            all_menu_item_imgs.append(MenuItemImg(
                menu_item_id=currDrink.id,
                url=drink_translator[drink_name_end],
                preview= False))


        master_menu_item_imgs.append(all_menu_item_imgs)
        counter+=1


    for array5 in master_menu_item_imgs:
        db.session.add_all(array5)
    db.session.commit()


def undo_menu_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menu_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menu_items"))
    db.session.commit()



