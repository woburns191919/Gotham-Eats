from ..models import db, MenuItem, environment, SCHEMA
from sqlalchemy.sql import text
from random import randint, random
from faker import Faker




'''
*******************this section is just for reference.  example of complete
seeder file:

r1_entrees = [
    MenuItem(restaurant_id=1, menu_id=1, name="Chicken Alfredo", description="Creamy chicken pasta", price=15.99, type="entree", picture="path/to/picture1"),
    MenuItem(restaurant_id=1, menu_id=1, name="Beef Lasagna", description="Layered beef and cheese", price=16.99, type="entree", picture="path/to/picture2"),
    MenuItem(restaurant_id=1, menu_id=1, name="Grilled Salmon", description="Salmon with a lemon herb glaze", price=18.99, type="entree", picture="path/to/picture3"),
    MenuItem(restaurant_id=1, menu_id=1, name="Steak Frites", description="Juicy steak with French fries", price=22.99, type="entree", picture="path/to/picture4"),
    MenuItem(restaurant_id=1, menu_id=1, name="Pork Chop", description="Grilled pork chop with apple sauce", price=20.99, type="entree", picture="path/to/picture5"),
    MenuItem(restaurant_id=1, menu_id=1, name="Lamb Curry", description="Spicy and flavorful lamb curry", price=17.99, type="entree", picture="path/to/picture6"),
    MenuItem(restaurant_id=1, menu_id=1, name="Vegetable Stir-Fry", description="Assorted vegetables in a savory sauce", price=14.99, type="entree", picture="path/to/picture7"),
    MenuItem(restaurant_id=1, menu_id=1, name="Spaghetti Carbonara", description="Creamy pasta with bacon and cheese", price=15.49, type="entree", picture="path/to/picture8"),
    MenuItem(restaurant_id=1, menu_id=1, name="Chicken Tikka Masala", description="Chicken in a creamy tomato sauce", price=16.49, type="entree", picture="path/to/picture9"),
    MenuItem(restaurant_id=1, menu_id=1, name="Beef Stew", description="Hearty beef stew with vegetables", price=16.79, type="entree", picture="path/to/picture10"),
]
r1_drinks = [
    MenuItem(restaurant_id=1, menu_id=1, name="Mango Smoothie", description="Refreshing mango blend", price=5.99, type="drink", picture="path/to/picture11"),
    MenuItem(restaurant_id=1, menu_id=1, name="Iced Latte", description="Chilled coffee with milk", price=4.99, type="drink", picture="path/to/picture12"),
    MenuItem(restaurant_id=1, menu_id=1, name="Green Tea", description="Warm and soothing", price=3.49, type="drink", picture="path/to/picture13"),
    MenuItem(restaurant_id=1, menu_id=1, name="Lemonade", description="Sweet and tangy", price=4.49, type="drink", picture="path/to/picture14"),
    MenuItem(restaurant_id=1, menu_id=1, name="Red Wine", description="Rich and full-bodied", price=7.99, type="drink", picture="path/to/picture15"),
    MenuItem(restaurant_id=1, menu_id=1, name="Craft Beer", description="Local brew", price=6.49, type="drink", picture="path/to/picture16"),
    MenuItem(restaurant_id=1, menu_id=1, name="Espresso", description="Strong and aromatic", price=3.99, type="drink", picture="path/to/picture17"),
    MenuItem(restaurant_id=1, menu_id=1, name="Champagne", description="Bubbly and crisp", price=9.99, type="drink", picture="path/to/picture18"),
    MenuItem(restaurant_id=1, menu_id=1, name="Bloody Mary", description="Spicy and invigorating", price=7.99, type="drink", picture="path/to/picture19"),
    MenuItem(restaurant_id=1, menu_id=1, name="Mojito", description="Minty and refreshing", price=6.99, type="drink", picture="path/to/picture20"),
]
r1_sides = [
    MenuItem(restaurant_id=1, menu_id=1, name="French Fries", description="Golden and crispy", price=3.99, type="side", picture="path/to/picture21"),
    MenuItem(restaurant_id=1, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="path/to/picture22"),
    MenuItem(restaurant_id=1, menu_id=1, name="Onion Rings", description="Crispy and delicious", price=4.49, type="side", picture="path/to/picture23"),
    MenuItem(restaurant_id=1, menu_id=1, name="Mashed Potatoes", description="Creamy and buttery", price=3.49, type="side", picture="path/to/picture24"),
    MenuItem(restaurant_id=1, menu_id=1, name="Coleslaw", description="Crunchy and tangy", price=2.49, type="side", picture="path/to/picture25"),
    MenuItem(restaurant_id=1, menu_id=1, name="Green Beans", description="Sauteed with garlic", price=2.99, type="side", picture="path/to/picture26"),
    MenuItem(restaurant_id=1, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="path/to/picture27"),
    MenuItem(restaurant_id=1, menu_id=1, name="Bread Rolls", description="Soft and warm", price=2.49, type="side", picture="path/to/picture28"),
    MenuItem(restaurant_id=1, menu_id=1, name="Garden Salad", description="Fresh and light", price=3.99, type="side", picture="path/to/picture29"),
    MenuItem(restaurant_id=1, menu_id=1, name="Rice Pilaf", description="Fluffy and aromatic", price=3.49, type="side", picture="path/to/picture30"),
]
r1_desserts = [
    MenuItem(restaurant_id=1, menu_id=1, name="Chocolate Mousse", description="Rich and creamy dessert", price=6.99, type="dessert", picture="path/to/picture31"),
    MenuItem(restaurant_id=1, menu_id=1, name="Cheesecake", description="Smooth and sweet cheesecake", price=7.99, type="dessert", picture="path/to/picture32"),
    MenuItem(restaurant_id=1, menu_id=1, name="Panna Cotta", description="Silky and light", price=6.49, type="dessert", picture="path/to/picture33"),
    MenuItem(restaurant_id=1, menu_id=1, name="Brownie Sundae", description="Warm brownie with ice cream", price=6.99, type="dessert", picture="path/to/picture34"),
    MenuItem(restaurant_id=1, menu_id=1, name="Apple Pie", description="Spiced apple filling with flaky crust", price=5.99, type="dessert", picture="path/to/picture35"),
    MenuItem(restaurant_id=1, menu_id=1, name="Lemon Tart", description="Tangy and sweet", price=5.49, type="dessert", picture="path/to/picture36"),
    MenuItem(restaurant_id=1, menu_id=1, name="Tiramisu", description="Layered coffee-soaked dessert", price=7.49, type="dessert", picture="path/to/picture37"),
    MenuItem(restaurant_id=1, menu_id=1, name="Gelato", description="Rich and creamy Italian ice cream", price=5.99, type="dessert", picture="path/to/picture38"),
    MenuItem(restaurant_id=1, menu_id=1, name="Creme Brulee", description="Crunchy caramel top with creamy custard", price=6.79, type="dessert", picture="path/to/picture39"),
    MenuItem(restaurant_id=1, menu_id=1, name="Chocolate Cake", description="Decadent and moist", price=6.49, type="dessert", picture="path/to/picture40"),
]

**************************************************
'''
'''
entree randomizer.  step 1:  randomly pick entree from list
'''
filename_entree_list=["buffalo_chicken_sandwich", "chicken_tenders", "fish_tacos", "lasagna", "philly_cheesesteak",  "spaghetti", "chicken_fajita", "fettuccine_alfredo", "gyro", "lobster", "pizza", "steak", "bbq_ribs", "chicken_parmesan", "fish_and_chips", "hamburger", "meatball_sandwich", "shish_kebab"]

Entree_List=['Buffalo Chicken Sandwich', 'Chicken Tenders', 'Fish Tacos', "Lasagna", "Philly Cheesesteak", "Spaghetti", 'Chicken Fajita',"Fettuccine Alfredo", "Gyro", "Lobster", "Pizza", "Steak", "BBQ Ribs", "Chicken Parm", "Fish & Chips", "Hamburger", "Meatball Sandwich", "Shish Kebab"]
dessert_list=['blueberry_tart',     "chocolate_chip_cookie",  "lava_cake",         "pumpkin_pie", 'carrot_cake',      "chocolate_mousse",       "milkshake",         "strawberry_shortcake", 'apple_pie',     "cheesecake",         "cupcake",                "peach_cobbler",     "tiramisu", "banana_split",  "chocolate_brownie",  "flan", "pistachio_gelato",  "vanilla_icecream"]

#step 2:   from the entree list picked, get the image url and randomly assign 1-5.  we make an object with key and path values as translator.



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

def fakePrice():
    az= 5
    zy=30
    rand_num = random.uniform(az,zy)
    return rand_num
# ouradj=ourobject[counter.string()]

# if counter < 19
# selected villain =

# hop in after iteration 19

def seed_menu_items():
    counter=0
    all_entrees=[]
    for i in range(0,50):

        entree_name_end = Entree_List[randint(0,17)]
        dessert_name_end= dessert_list[randint(0,17)]

        fake_price = 2.99

        chosen_villain = { chosen_villain for chosen_villain, adjective in villain_adj_dict.items() }
        villain_list = list(chosen_villain)
        our_set = set(villain_list)
        rand_villain_no_duplicates = list(our_set)
        rand_villian = rand_villain_no_duplicates[randint(0, 17)]

        # chosen_villain = { chosen_villain for chosen_villain, adjective in villain_adj_dict.items() }
        # villain_list = list(chosen_villain)

        # rand_villian = villain_list[randint(0, 17)]
        r_var = rand_villian.split('_')
        villain_number = r_var[0]

        curr_adj_list = villain_adj_dict[rand_villian]

        currnew=MenuItem(
            restaurant_id=int(villain_number),
            menu_id=int(villain_number),
            name=f"{curr_adj_list[randint(0, len(curr_adj_list)-1)]} {entree_name_end}",
            description=f"{villain_adj_dict['19_everyone_else'][randint(0, 17)]} {entree_name_end}s",
            price=fake_price,
            type="entree",
            picture=entree_translator[entree_name_end]
        )
        all_entrees.append(currnew)
        counter+=1

    db.session.add_all(all_entrees)
    db.session.commit()





# finished_var = MenuItem(
#       restaurant_id=villain_number, menu_id=villain_number, name="Pork Chop", description="Grilled pork chop with apple sauce", price=20.99, type="entree", picture="path/to/picture5"
#       )





#grab the path using translator[ourpickedentree]

#construct r1 entree look up top for format

# ownersOfRestaurant= {"1": penguin, "2":riddler, "3": Ivy, 4: Two-Face, 5: Scarecrow, 6:Catwoman, 7: Batman, 8: Joker, 9: Bane,
# 10: mr freeze, 11: Clayface, 12: Firefly,13: mad hatter, 14: Talon, 15: Zatanna, 16: Batman, 18: GreenArrow}

#if we want also make a table of adjectives for each character.  construct name of entree  make it spicy

#insert entree and make sure filepath correct.






'''
#************THESE ARE ALL OF THE SIDES THEYH ARE DONE EXCEPT WE missing r17
r1_sides = [
    MenuItem(restaurant_id=1, menu_id=1, name="Bane's Baked Potato", description="Loaded with toppings", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (3).jpeg"),
    MenuItem(restaurant_id=1, menu_id=1, name="Joker's Breadsticks", description="Twisted and delicious", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (2).jpeg"),
    MenuItem(restaurant_id=1, menu_id=1, name="Penguin's Chicken Wings", description="Served with a cold twist", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (4).jpeg"),
    MenuItem(restaurant_id=1, menu_id=1, name="Two-Face's Corn on the Cob", description="Half-charred, half-sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (1).jpeg"),
    MenuItem(restaurant_id=1, menu_id=1, name="Riddler's Edamame", description="A mysterious snack", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (5).jpeg"),
    MenuItem(restaurant_id=1, menu_id=1, name="Scarecrow's Fried Rice", description="Fearfully flavorful", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (3).jpeg"),
    MenuItem(restaurant_id=1, menu_id=1, name="Joker's Fries", description="Chaos in every bite", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (2).jpeg"),
    MenuItem(restaurant_id=1, menu_id=1, name="Garlic Bread", description="Toasty and sinister", price=3.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=1, menu_id=1, name="Green Goblin's Green Beans", description="Sauteed with a villainous twist", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (1).jpeg"),
    MenuItem(restaurant_id=1, menu_id=1, name="Mad Hatter's Lo Mein", description="Madly delicious", price=5.49, type="side", picture="/menu_item_images/sides/lo_mein/img (5).jpeg")
]


r2_sides = [
    MenuItem(restaurant_id=2, menu_id=1, name="Selina's Mac and Cheese", description="Purrfectly cheesy", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (2).jpeg"),
    MenuItem(restaurant_id=2, menu_id=1, name="Ivy's Mashed Potatoes", description="Eco-friendly and creamy", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (4).jpeg"),
    MenuItem(restaurant_id=2, menu_id=1, name="Riddler's Mozarella Sticks", description="Riddled with flavor", price=3.99, type="side", picture="/menu_item_images/sides/mozarella_sticks/img (1).jpeg"),
    MenuItem(restaurant_id=2, menu_id=1, name="Harley's Nachos", description="A crazy twist on a classic", price=5.49, type="side", picture="/menu_item_images/sides/nachos/img (3).jpeg"),
    MenuItem(restaurant_id=2, menu_id=1, name="Oswald's Onion Rings", description="Crispy and Cobblepot-approved", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (2).jpeg"),
    MenuItem(restaurant_id=2, menu_id=1, name="Penguin's Roasted Cauliflower", description="A sinister side dish", price=3.49, type="side", picture="/menu_item_images/sides/roasted_califlower/img (5).jpeg"),
    MenuItem(restaurant_id=2, menu_id=1, name="Riddler's Roasted Veggies", description="A riddle for your taste buds", price=4.99, type="side", picture="/menu_item_images/sides/roasted_veggies/img (3).jpeg"),
    MenuItem(restaurant_id=2, menu_id=1, name="Harley's Sweet Potato Fries", description="A sweet and chaotic delight", price=3.99, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (4).jpeg"),
    MenuItem(restaurant_id=2, menu_id=1, name="Joker's Tater Tots", description="A twist of madness", price=2.99, type="side", picture="/menu_item_images/sides/tater_tots/img (1).jpeg"),
    MenuItem(restaurant_id=2, menu_id=1, name="Catwoman's Breadsticks", description="Stolen and savory", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (5).jpeg")
]



r3_sides = [
    MenuItem(restaurant_id=3, menu_id=1, name="Enchanted Baked Potato", description="Vibrantly delicious", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (1).jpeg"),
    MenuItem(restaurant_id=3, menu_id=1, name="Verdant Breadsticks", description="Green and crunchy", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (2).jpeg"),
    MenuItem(restaurant_id=3, menu_id=1, name="Thorny Chicken Wings", description="Crispy and plant-based", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (3).jpeg"),
    MenuItem(restaurant_id=3, menu_id=1, name="Overgrown Corn on the Cob", description="Wild and flavorful", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (4).jpeg"),
    MenuItem(restaurant_id=3, menu_id=1, name="Leafy Edamame", description="Green goodness", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (5).jpeg"),
    MenuItem(restaurant_id=3, menu_id=1, name="Foliage Fried Rice", description="Savory and plant-based", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (1).jpeg"),
    MenuItem(restaurant_id=3, menu_id=1, name="Vine-Covered Fries", description="Crunchy and tantalizing", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (2).jpeg"),
    MenuItem(restaurant_id=3, menu_id=1, name="Garlic Bread", description="Toasty and herb-infused", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=3, menu_id=1, name="Green Bean Medley", description="Sauteed with garden herbs", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (4).jpeg"),
    MenuItem(restaurant_id=3, menu_id=1, name="Moss-Covered Mac and Cheese", description="Cheesy and comforting", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (5).jpeg"),
]


r4_sides = [
    MenuItem(restaurant_id=4, menu_id=1, name="Good Side Baked Potato", description="Pure and comforting", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (1).jpeg"),
    MenuItem(restaurant_id=4, menu_id=1, name="Bad Side Baked Potato", description="Sinfully delicious", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (2).jpeg"),
    MenuItem(restaurant_id=4, menu_id=1, name="Double-Dealing Breadsticks", description="A twist in every bite", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (3).jpeg"),
    MenuItem(restaurant_id=4, menu_id=1, name="Coinflip Chicken Wings", description="50/50 flavor sensation", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (4).jpeg"),
    MenuItem(restaurant_id=4, menu_id=1, name="Jekyll and Hyde Corn on the Cob", description="Two flavors, one cob", price=4.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (5).jpeg"),
    MenuItem(restaurant_id=4, menu_id=1, name="Double-Edged Edamame", description="A surprise in every pod", price=3.99, type="side", picture="/menu_item_images/sides/edamame/img (1).jpeg"),
    MenuItem(restaurant_id=4, menu_id=1, name="Dual Personality Fried Rice", description="Twisting taste sensations", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=4, menu_id=1, name="Double-Dose Fries", description="Two flavors, one plate", price=4.99, type="side", picture="/menu_item_images/sides/fries/img (3).jpeg"),
    MenuItem(restaurant_id=4, menu_id=1, name="Guilt and Glory Garlic Bread", description="A choice to make", price=3.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=4, menu_id=1, name="Two-Face's Trickster Mac and Cheese", description="A dual-cheese experience", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (5).jpeg"),
]



r5_sides = [
    MenuItem(restaurant_id=5, menu_id=1, name="Fear-Inducing Baked Potato", description="Terrifyingly tasty", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (3).jpeg"),
    MenuItem(restaurant_id=5, menu_id=1, name="Nightmare Breadsticks", description="Hauntingly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (4).jpeg"),
    MenuItem(restaurant_id=5, menu_id=1, name="Toxin-Tainted Chicken Wings", description="Poisonously delicious", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (5).jpeg"),
    MenuItem(restaurant_id=5, menu_id=1, name="Venomous Corn on the Cob", description="Venom-infused flavor", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (1).jpeg"),
    MenuItem(restaurant_id=5, menu_id=1, name="Dreadful Edamame", description="Fearfully good", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (2).jpeg"),
    MenuItem(restaurant_id=5, menu_id=1, name="Psychotic Fried Rice", description="Insanely flavorful", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (3).jpeg"),
    MenuItem(restaurant_id=5, menu_id=1, name="Scary Fries", description="Fear-inducing crunch", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (4).jpeg"),
    MenuItem(restaurant_id=5, menu_id=1, name="Fearful Garlic Bread", description="Toasted to haunt your taste buds", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (5).jpeg"),
    MenuItem(restaurant_id=5, menu_id=1, name="Eerie Green Beans", description="Ghoulishly garlicky", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (1).jpeg"),
    MenuItem(restaurant_id=5, menu_id=1, name="Phantom Mac and Cheese", description="Cheese to haunt your dreams", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (2).jpeg"),
]


r6_sides = [
    MenuItem(restaurant_id=6, menu_id=1, name="Sleek Baked Potato", description="Cat-approved flavor", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (4).jpeg"),
    MenuItem(restaurant_id=6, menu_id=1, name="Cat's Meow Breadsticks", description="Purr-fectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (5).jpeg"),
    MenuItem(restaurant_id=6, menu_id=1, name="Catnip Chicken Wings", description="Irresistibly good", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (1).jpeg"),
    MenuItem(restaurant_id=6, menu_id=1, name="Sneaky Corn on the Cob", description="Quietly flavorful", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (2).jpeg"),
    MenuItem(restaurant_id=6, menu_id=1, name="Paw-some Edamame", description="Paw-licking good", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (3).jpeg"),
    MenuItem(restaurant_id=6, menu_id=1, name="Whisker-twitching Fried Rice", description="Cat-approved taste", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (4).jpeg"),
    MenuItem(restaurant_id=6, menu_id=1, name="Feline Fries", description="Crunchy delight", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (5).jpeg"),
    MenuItem(restaurant_id=6, menu_id=1, name="Purr-fect Garlic Bread", description="Toasty and irresistible", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (1).jpeg"),
    MenuItem(restaurant_id=6, menu_id=1, name="Catnap Green Beans", description="Sleepily sauteed", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (2).jpeg"),
    MenuItem(restaurant_id=6, menu_id=1, name="Stealthy Mac and Cheese", description="Silently cheesy", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (3).jpeg"),
]


r7_sides = [
    MenuItem(restaurant_id=7, menu_id=1, name="Bat-tastic Baked Potato", description="Heroically tasty", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (5).jpeg"),
    MenuItem(restaurant_id=7, menu_id=1, name="Dark Knight Breadsticks", description="Gotham's crunch", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (1).jpeg"),
    MenuItem(restaurant_id=7, menu_id=1, name="Batwing Chicken Wings", description="Caped and delicious", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (2).jpeg"),
    MenuItem(restaurant_id=7, menu_id=1, name="Gotham Corn on the Cob", description="Heroic flavor", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (3).jpeg"),
    MenuItem(restaurant_id=7, menu_id=1, name="Batarang Edamame", description="Gotham's favorite", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (4).jpeg"),
    MenuItem(restaurant_id=7, menu_id=1, name="Justice Fried Rice", description="Served with justice", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (5).jpeg"),
    MenuItem(restaurant_id=7, menu_id=1, name="Bat Fries", description="Crunching for justice", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (1).jpeg"),
    MenuItem(restaurant_id=7, menu_id=1, name="Bat Signal Garlic Bread", description="Heroic toasts", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (2).jpeg"),
    MenuItem(restaurant_id=7, menu_id=1, name="Gotham Green Beans", description="Heroic sauteed greens", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (3).jpeg"),
    MenuItem(restaurant_id=7, menu_id=1, name="Caped Crusader Mac and Cheese", description="Cheesy heroism", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (4).jpeg"),
]


r8_sides = [
    MenuItem(restaurant_id=8, menu_id=1, name="Joker's Jestful Baked Potato", description="Laughably delicious", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (1).jpeg"),
    MenuItem(restaurant_id=8, menu_id=1, name="Riddler's Riddling Breadsticks", description="Puzzle-packed crunch", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (2).jpeg"),
    MenuItem(restaurant_id=8, menu_id=1, name="Harley's Hilarious Chicken Wings", description="Madly good", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (3).jpeg"),
    MenuItem(restaurant_id=8, menu_id=1, name="Two-Face's Double-Dealing Corn on the Cob", description="Two flavors, one cob", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (4).jpeg"),
    MenuItem(restaurant_id=8, menu_id=1, name="Penguin's Peculiar Edamame", description="Fishy yet tasty", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (5).jpeg"),
    MenuItem(restaurant_id=8, menu_id=1, name="Catwoman's Cackling Fried Rice", description="Cat-themed flavor", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (1).jpeg"),
    MenuItem(restaurant_id=8, menu_id=1, name="Riddler's Ridiculous Fries", description="Puzzle-shaped crunch", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (2).jpeg"),
    MenuItem(restaurant_id=8, menu_id=1, name="Harley's Hysterical Garlic Bread", description="Madly toasty", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=8, menu_id=1, name="Two-Face's Coinflip Green Beans", description="Two-sided sautee", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (4).jpeg"),
    MenuItem(restaurant_id=8, menu_id=1, name="Penguin's Prankster Mac and Cheese", description="Cheesy antics", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (5).jpeg"),
]

r9_sides = [
    MenuItem(restaurant_id=9, menu_id=1, name="Bane's Powerhouse Baked Potato", description="Strength in flavor", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (2).jpeg"),
    MenuItem(restaurant_id=9, menu_id=1, name="Riddler's Riddling Breadsticks", description="Puzzle-packed crunch", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (3).jpeg"),
    MenuItem(restaurant_id=9, menu_id=1, name="Bane's Muscular Chicken Wings", description="Muscle-bound taste", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (4).jpeg"),
    MenuItem(restaurant_id=9, menu_id=1, name="Two-Face's Double-Dealing Corn on the Cob", description="Two flavors, one cob", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (5).jpeg"),
    MenuItem(restaurant_id=9, menu_id=1, name="Penguin's Peculiar Edamame", description="Fishy yet tasty", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (1).jpeg"),
    MenuItem(restaurant_id=9, menu_id=1, name="Catwoman's Cackling Fried Rice", description="Cat-themed flavor", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=9, menu_id=1, name="Riddler's Ridiculous Fries", description="Puzzle-shaped crunch", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (3).jpeg"),
    MenuItem(restaurant_id=9, menu_id=1, name="Harley's Hysterical Garlic Bread", description="Madly toasty", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=9, menu_id=1, name="Two-Face's Coinflip Green Beans", description="Two-sided sautee", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (5).jpeg"),
    MenuItem(restaurant_id=9, menu_id=1, name="Penguin's Prankster Mac and Cheese", description="Cheesy antics", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (1).jpeg"),
]


r10_sides = [
    MenuItem(restaurant_id=10, menu_id=1, name="Frozen Baked Potato", description="Icy yet flavorful", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (3).jpeg"),
    MenuItem(restaurant_id=10, menu_id=1, name="Chilled Breadsticks", description="Frozen crunch", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (4).jpeg"),
    MenuItem(restaurant_id=10, menu_id=1, name="Arctic Chicken Wings", description="Cold and delicious", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (5).jpeg"),
    MenuItem(restaurant_id=10, menu_id=1, name="Frozen Corn on the Cob", description="Chilled flavor sensation", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (1).jpeg"),
    MenuItem(restaurant_id=10, menu_id=1, name="Icy Edamame", description="Frozen delight", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (2).jpeg"),
    MenuItem(restaurant_id=10, menu_id=1, name="Chilled Fried Rice", description="Frozen to perfection", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (3).jpeg"),
    MenuItem(restaurant_id=10, menu_id=1, name="Frosty Fries", description="Cold and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (4).jpeg"),
    MenuItem(restaurant_id=10, menu_id=1, name="Frozen Garlic Bread", description="Chilled to thrill", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (5).jpeg"),
    MenuItem(restaurant_id=10, menu_id=1, name="Chilled Green Beans", description="Icy sauteed greens", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (1).jpeg"),
    MenuItem(restaurant_id=10, menu_id=1, name="Ice-Cold Mac and Cheese", description="Cheesy and icy", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (2).jpeg"),
]



r11_sides = [
    MenuItem(restaurant_id=11, menu_id=1, name="Morphing Baked Potato", description="Ever-changing flavors", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (3).jpeg"),
    MenuItem(restaurant_id=11, menu_id=1, name="Shape-Shifting Breadsticks", description="Twisting textures", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (4).jpeg"),
    MenuItem(restaurant_id=11, menu_id=1, name="Clay Wings", description="Adaptive and tasty", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (5).jpeg"),
    MenuItem(restaurant_id=11, menu_id=1, name="Malleable Corn on the Cob", description="Customized flavors", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (1).jpeg"),
    MenuItem(restaurant_id=11, menu_id=1, name="Shapeshifter's Edamame", description="Changing with every bite", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (2).jpeg"),
    MenuItem(restaurant_id=11, menu_id=1, name="Adaptive Fried Rice", description="Always a surprise", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (3).jpeg"),
    MenuItem(restaurant_id=11, menu_id=1, name="Morphed Fries", description="Shifting textures", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (4).jpeg"),
    MenuItem(restaurant_id=11, menu_id=1, name="Shapeshifter's Garlic Bread", description="Flavors in flux", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (5).jpeg"),
    MenuItem(restaurant_id=11, menu_id=1, name="Clay Bean Blend", description="Always adapting", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (1).jpeg"),
    MenuItem(restaurant_id=11, menu_id=1, name="Adaptive Mac and Cheese", description="Ever-changing cheese", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (2).jpeg"),
]


r12_sides = [
    MenuItem(restaurant_id=12, menu_id=1, name="Blazing Baked Potato", description="Fire-touched delight", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (2).jpeg"),
    MenuItem(restaurant_id=12, menu_id=1, name="Inferno Breadsticks", description="Scorching and savory", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (3).jpeg"),
    MenuItem(restaurant_id=12, menu_id=1, name="Fire Wings", description="Spicy and sizzling", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (4).jpeg"),
    MenuItem(restaurant_id=12, menu_id=1, name="Flaming Corn on the Cob", description="Burnin' with flavor", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (5).jpeg"),
    MenuItem(restaurant_id=12, menu_id=1, name="Scorching Edamame", description="Hot and tasty", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (1).jpeg"),
    MenuItem(restaurant_id=12, menu_id=1, name="Fire-Roasted Fried Rice", description="Blazing with spices", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=12, menu_id=1, name="Inferno Fries", description="Heat and crunch", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (3).jpeg"),
    MenuItem(restaurant_id=12, menu_id=1, name="Flame-Grilled Garlic Bread", description="Toasty and fiery", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=12, menu_id=1, name="Scalding Green Bean Medley", description="Sauteed with fire", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (5).jpeg"),
    MenuItem(restaurant_id=12, menu_id=1, name="Blazing Mac and Cheese", description="Hot and cheesy", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (1).jpeg"),
]


r13_sides = [
    MenuItem(restaurant_id=13, menu_id=1, name="Tea-Infused Baked Potato", description="Wonderfully whimsical", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (3).jpeg"),
    MenuItem(restaurant_id=13, menu_id=1, name="Hat-Topped Breadsticks", description="A touch of magic", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (4).jpeg"),
    MenuItem(restaurant_id=13, menu_id=1, name="Mad Winged Wonders", description="Delightfully delirious", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (5).jpeg"),
    MenuItem(restaurant_id=13, menu_id=1, name="Whimsical Corn on the Cob", description="A playful twist", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (1).jpeg"),
    MenuItem(restaurant_id=13, menu_id=1, name="Magic-Infused Edamame", description="Enchantingly delicious", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (2).jpeg"),
    MenuItem(restaurant_id=13, menu_id=1, name="Wonderland Fried Rice", description="Magical mix of flavors", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (3).jpeg"),
    MenuItem(restaurant_id=13, menu_id=1, name="Illusionist's Fries", description="Deceptively delightful", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (4).jpeg"),
    MenuItem(restaurant_id=13, menu_id=1, name="Mysterious Garlic Bread", description="A taste of the unknown", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (5).jpeg"),
    MenuItem(restaurant_id=13, menu_id=1, name="Enchanted Green Bean Medley", description="Sauteed with magic", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (1).jpeg"),
    MenuItem(restaurant_id=13, menu_id=1, name="Whimsy Mac and Cheese", description="Playfully cheesy", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (2).jpeg"),
]


r14_sides = [
    MenuItem(restaurant_id=14, menu_id=1, name="Assassin's Baked Potato", description="Lethally delicious", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (1).jpeg"),
    MenuItem(restaurant_id=14, menu_id=1, name="Talon's Breadsticks", description="Sharp and savory", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (2).jpeg"),
    MenuItem(restaurant_id=14, menu_id=1, name="Silent Wing Blades", description="Stealthy and flavorful", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (3).jpeg"),
    MenuItem(restaurant_id=14, menu_id=1, name="Shadowy Corn on the Cob", description="Dark and delectable", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (4).jpeg"),
    MenuItem(restaurant_id=14, menu_id=1, name="Talon's Talons", description="Dangerously addictive", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (5).jpeg"),
    MenuItem(restaurant_id=14, menu_id=1, name="Assassin's Fried Rice", description="Deadly mix of flavors", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (1).jpeg"),
    MenuItem(restaurant_id=14, menu_id=1, name="Shadow Fries", description="Dark and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (2).jpeg"),
    MenuItem(restaurant_id=14, menu_id=1, name="Silent Garlic Bread", description="Whispers of flavor", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=14, menu_id=1, name="Shadowy Green Bean Medley", description="Sauteed in secrecy", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (4).jpeg"),
    MenuItem(restaurant_id=14, menu_id=1, name="Talon's Stealth Mac and Cheese", description="Silently cheesy", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (5).jpeg"),
]


r15_sides = [
    MenuItem(restaurant_id=15, menu_id=1, name="Enchanted Baked Potato", description="Mystically delicious", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (2).jpeg"),
    MenuItem(restaurant_id=15, menu_id=1, name="Magic Wand Breadsticks", description="Spellbindingly savory", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (3).jpeg"),
    MenuItem(restaurant_id=15, menu_id=1, name="Mystic Chicken Wings", description="Magical and flavorful", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (4).jpeg"),
    MenuItem(restaurant_id=15, menu_id=1, name="Wizard's Corn on the Cob", description="Enchanting flavors", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (5).jpeg"),
    MenuItem(restaurant_id=15, menu_id=1, name="Sorcerer's Edamame", description="Spellbound goodness", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (1).jpeg"),
    MenuItem(restaurant_id=15, menu_id=1, name="Magical Fried Rice", description="Otherworldly mix of flavors", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=15, menu_id=1, name="Wizard's Fries", description="Magical and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (3).jpeg"),
    MenuItem(restaurant_id=15, menu_id=1, name="Enchanted Garlic Bread", description="Toasty and bewitched", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=15, menu_id=1, name="Sorceress Green Bean Medley", description="Sauteed with magic herbs", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (5).jpeg"),
    MenuItem(restaurant_id=15, menu_id=1, name="Wizard's Mac and Cheese", description="Magically cheesy", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (1).jpeg"),
]

r16_sides = [
    MenuItem(restaurant_id=16, menu_id=1, name="Bat-Tato Wedges", description="Heroic and flavorful", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (1).jpeg"),
    MenuItem(restaurant_id=16, menu_id=1, name="Batwing Breadsticks", description="Crunchy and dark", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (2).jpeg"),
    MenuItem(restaurant_id=16, menu_id=1, name="Gotham Guardian Wings", description="Heroically spiced", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (3).jpeg"),
    MenuItem(restaurant_id=16, menu_id=1, name="Bat-Cob", description="Dark and flavorful", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (4).jpeg"),
    MenuItem(restaurant_id=16, menu_id=1, name="Dark Edamame", description="Broodingly delicious", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (5).jpeg"),
    MenuItem(restaurant_id=16, menu_id=1, name="Nocturnal Fried Rice", description="Nighttime mix of flavors", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (1).jpeg"),
    MenuItem(restaurant_id=16, menu_id=1, name="Gotham Fries", description="Crunchy and dark", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (2).jpeg"),
    MenuItem(restaurant_id=16, menu_id=1, name="Bat-Garlic Bread", description="Toasty and heroic", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=16, menu_id=1, name="Nightfall Green Beans", description="Sauteed in the moonlight", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (4).jpeg"),
    MenuItem(restaurant_id=16, menu_id=1, name="Bat-Mac and Cheese", description="Dark and cheesy", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (5).jpeg"),
]


r17_sides = []

r18_sides = [
    MenuItem(restaurant_id=18, menu_id=1, name="Arrowhead Baked Potato", description="Healthy and hearty", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (2).jpeg"),
    MenuItem(restaurant_id=18, menu_id=1, name="Quiver Breadsticks", description="Arrow-straight and savory", price=3.99, type="side", picture="/menu_item_images/sides/breadsticks/img (3).jpeg"),
    MenuItem(restaurant_id=18, menu_id=1, name="Archery Wings", description="Targeted flavor", price=5.49, type="side", picture="/menu_item_images/sides/chicken_wings/img (4).jpeg"),
    MenuItem(restaurant_id=18, menu_id=1, name="Arrow Corn on the Cob", description="Bullseye flavors", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (5).jpeg"),
    MenuItem(restaurant_id=18, menu_id=1, name="Green Edamame", description="Healthy goodness", price=4.49, type="side", picture="/menu_item_images/sides/edamame/img (1).jpeg"),
    MenuItem(restaurant_id=18, menu_id=1, name="Arrow Shot Fried Rice", description="Straight to the taste", price=5.99, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=18, menu_id=1, name="Archer's Fries", description="Straight and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (3).jpeg"),
    MenuItem(restaurant_id=18, menu_id=1, name="Quiver Garlic Bread", description="Toasty and precise", price=4.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=18, menu_id=1, name="Healthy Green Bean Medley", description="Sauteed with natural herbs", price=4.99, type="side", picture="/menu_item_images/sides/green_beans/img (5).jpeg"),
    MenuItem(restaurant_id=18, menu_id=1, name="Arrowhead Mac and Cheese", description="Healthy and cheesy", price=5.49, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (1).jpeg"),
]


r19_sides = [
    MenuItem(restaurant_id=19, menu_id=1, name="French Fries", description="Classic and crispy", price=2.99, type="side", picture="/menu_item_images/sides/fries/img (1).jpeg"),
    MenuItem(restaurant_id=19, menu_id=1, name="Onion Rings", description="Crispy and flavorful", price=3.49, type="side", picture="/menu_item_images/sides/onion_rings/img (2).jpeg"),
    MenuItem(restaurant_id=19, menu_id=1, name="Garlic Bread", description="Toasty and savory", price=2.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=19, menu_id=1, name="Green Beans", description="Fresh and healthy", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (4).jpeg"),
    MenuItem(restaurant_id=19, menu_id=1, name="Mashed Potatoes", description="Creamy and rich", price=3.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=19, menu_id=1, name="Bread Rolls", description="Soft and warm", price=2.99, type="side", picture="/menu_item_images/sides/breadsticks/img (1).jpeg"),
    MenuItem(restaurant_id=19, menu_id=1, name="Coleslaw", description="Crunchy and tangy", price=2.49, type="side", picture="/menu_item_images/sides/coleslaw/img (2).jpeg"),
    MenuItem(restaurant_id=19, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (3).jpeg"),
    MenuItem(restaurant_id=19, menu_id=1, name="Roasted Veggies", description="Flavorful and wholesome", price=4.49, type="side", picture="/menu_item_images/sides/roasted_veggies/img (4).jpeg"),
    MenuItem(restaurant_id=19, menu_id=1, name="Tater Tots", description="Crispy and addictive", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (5).jpeg"),
]


r20_sides = [
    MenuItem(restaurant_id=20, menu_id=1, name="French Fries", description="Classic and crispy", price=2.99, type="side", picture="/menu_item_images/sides/fries/img (1).jpeg"),
    MenuItem(restaurant_id=20, menu_id=1, name="Onion Rings", description="Crispy and flavorful", price=3.49, type="side", picture="/menu_item_images/sides/onion_rings/img (2).jpeg"),
    MenuItem(restaurant_id=20, menu_id=1, name="Garlic Bread", description="Toasty and savory", price=2.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=20, menu_id=1, name="Green Beans", description="Fresh and healthy", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (4).jpeg"),
    MenuItem(restaurant_id=20, menu_id=1, name="Mashed Potatoes", description="Creamy and rich", price=3.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=20, menu_id=1, name="Bread Rolls", description="Soft and warm", price=2.99, type="side", picture="/menu_item_images/sides/breadsticks/img (1).jpeg"),
    MenuItem(restaurant_id=20, menu_id=1, name="Coleslaw", description="Crunchy and tangy", price=2.49, type="side", picture="/menu_item_images/sides/coleslaw/img (2).jpeg"),
    MenuItem(restaurant_id=20, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (3).jpeg"),
    MenuItem(restaurant_id=20, menu_id=1, name="Roasted Veggies", description="Flavorful and wholesome", price=4.49, type="side", picture="/menu_item_images/sides/roasted_veggies/img (4).jpeg"),
    MenuItem(restaurant_id=20, menu_id=1, name="Tater Tots", description="Crispy and addictive", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (5).jpeg"),
]

r21_sides = [
    MenuItem(restaurant_id=21, menu_id=1, name="Delicious French Fries", description="Crispy and delightful", price=2.99, type="side", picture="/menu_item_images/sides/fries/img (1).jpeg"),
    MenuItem(restaurant_id=21, menu_id=1, name="Savory Onion Rings", description="Crispy and mouthwatering", price=3.49, type="side", picture="/menu_item_images/sides/onion_rings/img (2).jpeg"),
    MenuItem(restaurant_id=21, menu_id=1, name="Toasty Garlic Bread", description="Warm and comforting", price=2.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=21, menu_id=1, name="Fresh Green Beans", description="Healthy and flavorful", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (4).jpeg"),
    MenuItem(restaurant_id=21, menu_id=1, name="Creamy Mashed Potatoes", description="Rich and creamy", price=3.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=21, menu_id=1, name="Warm Bread Rolls", description="Soft and comforting", price=2.99, type="side", picture="/menu_item_images/sides/breadsticks/img (1).jpeg"),
    MenuItem(restaurant_id=21, menu_id=1, name="Tangy Coleslaw", description="Crunchy and tangy", price=2.49, type="side", picture="/menu_item_images/sides/coleslaw/img (2).jpeg"),
    MenuItem(restaurant_id=21, menu_id=1, name="Cheesy Mac and Cheese", description="Cheesy and indulgent", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (3).jpeg"),
    MenuItem(restaurant_id=21, menu_id=1, name="Roasted Veggies", description="Flavorful and wholesome", price=4.49, type="side", picture="/menu_item_images/sides/roasted_veggies/img (4).jpeg"),
    MenuItem(restaurant_id=21, menu_id=1, name="Crispy Tater Tots", description="Irresistibly crispy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (5).jpeg"),
]


r22_sides = [
    MenuItem(restaurant_id=22, menu_id=1, name="Classic French Fries", description="All-time favorite", price=2.99, type="side", picture="/menu_item_images/sides/fries/img (1).jpeg"),
    MenuItem(restaurant_id=22, menu_id=1, name="Golden Onion Rings", description="Crispy and golden", price=3.49, type="side", picture="/menu_item_images/sides/onion_rings/img (2).jpeg"),
    MenuItem(restaurant_id=22, menu_id=1, name="Buttery Garlic Bread", description="Buttery and aromatic", price=2.49, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=22, menu_id=1, name="Seasoned Green Beans", description="Delicately seasoned", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (4).jpeg"),
    MenuItem(restaurant_id=22, menu_id=1, name="Creamy Mashed Potatoes", description="Homestyle goodness", price=3.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=22, menu_id=1, name="Soft Bread Rolls", description="Warm and soft", price=2.99, type="side", picture="/menu_item_images/sides/breadsticks/img (1).jpeg"),
    MenuItem(restaurant_id=22, menu_id=1, name="Zesty Coleslaw", description="Zesty and crunchy", price=2.49, type="side", picture="/menu_item_images/sides/coleslaw/img (2).jpeg"),
    MenuItem(restaurant_id=22, menu_id=1, name="Ultimate Mac and Cheese", description="Ultimate cheesiness", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (3).jpeg"),
    MenuItem(restaurant_id=22, menu_id=1, name="Roasted Veggie Platter", description="Colorful and roasted", price=4.49, type="side", picture="/menu_item_images/sides/roasted_veggies/img (4).jpeg"),
    MenuItem(restaurant_id=22, menu_id=1, name="Crispy Tater Tots", description="Crispy perfection", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (5).jpeg"),
]

r23_sides = [
    MenuItem(restaurant_id=23, menu_id=1, name="Green Beans", description="Buttery and tender", price=6.99, type="side", picture="/menu_item_images/sides/green_beans/img (1).jpeg"),
    MenuItem(restaurant_id=23, menu_id=1, name="Roasted Veggies", description="Colorful and flavorful", price=7.49, type="side", picture="/menu_item_images/sides/roasted_veggies/img (2).jpeg"),
    MenuItem(restaurant_id=23, menu_id=1, name="Sweet Potato Fries", description="Crispy and sweet", price=5.99, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (3).jpeg"),
    MenuItem(restaurant_id=23, menu_id=1, name="Tater Tots", description="Golden and crunchy", price=4.99, type="side", picture="/menu_item_images/sides/tater_tots/img (4).jpeg"),
    MenuItem(restaurant_id=23, menu_id=1, name="Corn on the Cob", description="Buttered and seasoned", price=6.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (5).jpeg"),
    MenuItem(restaurant_id=23, menu_id=1, name="Mozzarella Sticks", description="Cheesy and delightful", price=5.99, type="side", picture="/menu_item_images/sides/mozarella_sticks/img (1).jpeg"),
    MenuItem(restaurant_id=23, menu_id=1, name="Fried Rice", description="Savory and satisfying", price=7.49, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=23, menu_id=1, name="Nachos", description="Loaded and crunchy", price=6.99, type="side", picture="/menu_item_images/sides/nachos/img (3).jpeg"),
    MenuItem(restaurant_id=23, menu_id=1, name="Baked Potato", description="Loaded and hearty", price=7.49, type="side", picture="/menu_item_images/sides/baked_potato/img (4).jpeg"),
    MenuItem(restaurant_id=23, menu_id=1, name="Garlic Bread", description="Toasty and aromatic", price=5.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (5).jpeg"),
]


r24_sides = [
    MenuItem(restaurant_id=24, menu_id=1, name="French Fries", description="Golden and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (1).jpeg"),
    MenuItem(restaurant_id=24, menu_id=1, name="Onion Rings", description="Crispy and savory", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (2).jpeg"),
    MenuItem(restaurant_id=24, menu_id=1, name="Mashed Potatoes", description="Creamy and buttery", price=3.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (1).jpeg"),
    MenuItem(restaurant_id=24, menu_id=1, name="Green Beans", description="Fresh and flavorful", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (2).jpeg"),
    MenuItem(restaurant_id=24, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (3).jpeg"),
    MenuItem(restaurant_id=24, menu_id=1, name="Bread Rolls", description="Soft and warm", price=2.49, type="side", picture="/menu_item_images/sides/breadsticks/img (3).jpeg"),
    MenuItem(restaurant_id=24, menu_id=1, name="Garden Salad", description="Fresh and healthy", price=3.99, type="side", picture="/menu_item_images/sides/salad/img (4).jpeg"),
    MenuItem(restaurant_id=24, menu_id=1, name="Sweet Potato Fries", description="Sweet and crispy", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (4).jpeg"),
    MenuItem(restaurant_id=24, menu_id=1, name="Tater Tots", description="Crunchy and satisfying", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (4).jpeg"),
]




r25_sides = [
    MenuItem(restaurant_id=25, menu_id=1, name="Sizzling Steak", description="Juicy and mouthwatering", price=14.99, type="side", picture="/menu_item_images/sides/steak/img (1).jpeg"),
    MenuItem(restaurant_id=25, menu_id=1, name="Crispy Chicken Tenders", description="Crispy and delicious", price=9.99, type="side", picture="/menu_item_images/sides/chicken_tenders/img (2).jpeg"),
    MenuItem(restaurant_id=25, menu_id=1, name="Fresh Garden Salad", description="Fresh and healthy", price=7.99, type="side", picture="/menu_item_images/sides/garden_salad/img (3).jpeg"),
    MenuItem(restaurant_id=25, menu_id=1, name="Homestyle Mashed Potatoes", description="Comforting and homestyle", price=6.99, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (4).jpeg"),
    MenuItem(restaurant_id=25, menu_id=1, name="Seasoned Broccoli", description="Flavorfully seasoned", price=5.99, type="side", picture="/menu_item_images/sides/broccoli/img (5).jpeg"),
    MenuItem(restaurant_id=25, menu_id=1, name="Classic French Fries", description="Classic and crispy", price=4.99, type="side", picture="/menu_item_images/sides/fries/img (1).jpeg"),
    MenuItem(restaurant_id=25, menu_id=1, name="Buttered Corn on the Cob", description="Buttery and sweet", price=3.99, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (2).jpeg"),
    MenuItem(restaurant_id=25, menu_id=1, name="Warm Dinner Rolls", description="Warm and soft", price=2.99, type="side", picture="/menu_item_images/sides/dinner_rolls/img (3).jpeg"),
    MenuItem(restaurant_id=25, menu_id=1, name="Creamy Coleslaw", description="Creamy and crunchy", price=3.49, type="side", picture="/menu_item_images/sides/coleslaw/img (4).jpeg"),
    MenuItem(restaurant_id=25, menu_id=1, name="Sweet Potato Fries", description="Sweet and savory", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (5).jpeg"),
]


r26_sides = [
    MenuItem(restaurant_id=26, menu_id=1, name="Grilled Salmon", description="Grilled to perfection", price=16.99, type="side", picture="/menu_item_images/sides/salmon/img (1).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Crispy Calamari", description="Crispy and tender", price=12.99, type="side", picture="/menu_item_images/sides/calamari/img (2).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Caesar Salad", description="Classic and flavorful", price=8.99, type="side", picture="/menu_item_images/sides/caesar_salad/img (3).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Garlic Buttered Asparagus", description="Buttery and aromatic", price=7.99, type="side", picture="/menu_item_images/sides/asparagus/img (4).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Loaded Baked Potatoes", description="Loaded with toppings", price=6.99, type="side", picture="/menu_item_images/sides/baked_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Crispy French Fries", description="Crispy and seasoned", price=5.99, type="side", picture="/menu_item_images/sides/fries/img (1).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Savory Stuffing", description="Savory and comforting", price=4.99, type="side", picture="/menu_item_images/sides/stuffing/img (2).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Buttered Corn", description="Buttery and sweet", price=3.99, type="side", picture="/menu_item_images/sides/corn/img (3).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Soft Dinner Rolls", description="Soft and fluffy", price=2.99, type="side", picture="/menu_item_images/sides/rolls/img (4).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Fresh Fruit Salad", description="Fresh and colorful", price=4.49, type="side", picture="/menu_item_images/sides/fruit_salad/img (5).jpeg"),
]


r27_sides = [
    MenuItem(restaurant_id=27, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Broccoli", description="Melted cheddar goodness", price=4.99, type="side", picture="/menu_item_images/sides/broccoli/img (1).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Onion Rings", description="Golden and satisfying", price=3.99, type="side", picture="/menu_item_images/sides/onion_rings/img (3).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (4).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Roasted Vegetables", description="Tender and colorful", price=5.99, type="side", picture="/menu_item_images/sides/roasted_veggies/img (1).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (2).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/salad/img (3).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (4).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (5).jpeg"),
]


r28_sides = [
    MenuItem(restaurant_id=28, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (5).jpeg"),
    MenuItem(restaurant_id=28, menu_id=1, name="Sweet Potato Fries", description="Crispy and delightful", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (1).jpeg"),
    MenuItem(restaurant_id=28, menu_id=1, name="Green Beans", description="Sautéed to perfection", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (2).jpeg"),
    MenuItem(restaurant_id=28, menu_id=1, name="Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (3).jpeg"),
    MenuItem(restaurant_id=28, menu_id=1, name="Lo Mein", description="Savory noodle delight", price=5.49, type="side", picture="/menu_item_images/sides/lo_mein/img (4).jpeg"),
    MenuItem(restaurant_id=28, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (5).jpeg"),
    MenuItem(restaurant_id=28, menu_id=1, name="French Fries", description="Golden and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (1).jpeg"),
    MenuItem(restaurant_id=28, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (2).jpeg"),
    MenuItem(restaurant_id=28, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (3).jpeg"),
    MenuItem(restaurant_id=28, menu_id=1, name="Onion Rings", description="Golden and satisfying", price=3.99, type="side", picture="/menu_item_images/sides/onion_rings/img (4).jpeg"),
]

r29_sides = [
    MenuItem(restaurant_id=29, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=29, menu_id=1, name="French Fries", description="Golden and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (2).jpeg"),
    MenuItem(restaurant_id=29, menu_id=1, name="Onion Rings", description="Crispy and delicious", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (1).jpeg"),
    MenuItem(restaurant_id=29, menu_id=1, name="Mashed Potatoes", description="Creamy and buttery", price=3.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=29, menu_id=1, name="Coleslaw", description="Crunchy and tangy", price=2.49, type="side", picture="/menu_item_images/sides/coleslaw/img (4).jpeg"),
    MenuItem(restaurant_id=29, menu_id=1, name="Green Beans", description="Sauteed with garlic", price=2.99, type="side", picture="/menu_item_images/sides/green_beans/img (3).jpeg"),
    MenuItem(restaurant_id=29, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (2).jpeg"),
    MenuItem(restaurant_id=29, menu_id=1, name="Bread Rolls", description="Soft and warm", price=2.49, type="side", picture="/menu_item_images/sides/bread_rolls/img (1).jpeg"),
    MenuItem(restaurant_id=29, menu_id=1, name="Garden Salad", description="Fresh and light", price=3.99, type="side", picture="/menu_item_images/sides/garden_salad/img (5).jpeg"),
    MenuItem(restaurant_id=29, menu_id=1, name="Rice Pilaf", description="Fluffy and aromatic", price=3.49, type="side", picture="/menu_item_images/sides/rice_pilaf/img (4).jpeg"),
]


r30_sides = [
    MenuItem(restaurant_id=30, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (3).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (2).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Sweet Potato Fries", description="Crispy and delightful", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (1).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Green Beans", description="Sautéed to perfection", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (5).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (4).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (3).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Crispy Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (2).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/salad/img (1).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Cheesy Broccoli", description="Melted cheddar goodness", price=4.99, type="side", picture="/menu_item_images/sides/broccoli/img (5).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (4).jpeg"),
]


r31_sides = [
    MenuItem(restaurant_id=31, menu_id=1, name="Onion Rings", description="Crispy and delicious", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (5).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="French Fries", description="Golden and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (4).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Roasted Vegetables", description="Tender and colorful", price=5.99, type="side", picture="/menu_item_images/sides/roasted_veggies/img (3).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Creamy Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (2).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (1).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (5).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (3).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (1).jpeg"),
]


r32_sides = [
    MenuItem(restaurant_id=32, menu_id=1, name="Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (5).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Sweet Potato Fries", description="Crispy and delightful", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (4).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Green Beans", description="Sautéed to perfection", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (3).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Garlic Parmesan Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (2).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (1).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Crispy Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (5).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (4).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (3).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (2).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (1).jpeg"),
]


r33_sides = [
    MenuItem(restaurant_id=33, menu_id=1, name="Coleslaw", description="Crunchy and tangy", price=2.49, type="side", picture="/menu_item_images/sides/coleslaw/img (5).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (4).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Bread Rolls", description="Soft and warm", price=2.49, type="side", picture="/menu_item_images/sides/bread_rolls/img (3).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Garden Salad", description="Fresh and light", price=3.99, type="side", picture="/menu_item_images/sides/garden_salad/img (2).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Roasted Cauliflower", description="Tender and flavorful", price=4.49, type="side", picture="/menu_item_images/sides/roasted_cauliflower/img (1).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Sweet Potato Fries", description="Crispy and delightful", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (5).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Lo Mein", description="Savory noodle delight", price=5.49, type="side", picture="/menu_item_images/sides/lo_mein/img (4).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (3).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (2).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Cheesy Broccoli", description="Melted cheddar goodness", price=4.99, type="side", picture="/menu_item_images/sides/broccoli/img (1).jpeg"),
]

r34_sides = [
    MenuItem(restaurant_id=34, menu_id=1, name="French Fries", description="Golden and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (5).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Onion Rings", description="Crispy and delicious", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (4).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (2).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (1).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (5).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Sweet Potato Fries", description="Crispy and delightful", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (4).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (3).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Green Beans", description="Sautéed to perfection", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (2).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (1).jpeg"),
]


r35_sides = [
    MenuItem(restaurant_id=35, menu_id=1, name="Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (5).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Crispy Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (4).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (3).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (2).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Roasted Vegetables", description="Tender and colorful", price=5.99, type="side", picture="/menu_item_images/sides/roasted_veggies/img (1).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Creamy Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Tasty Corn on the Cob", description="Naturally sweet", price=3.99, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (4).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Buttered Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (3).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Cheesy Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (2).jpeg"),
]


r36_sides = [
    MenuItem(restaurant_id=36, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (5).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Crispy Onion Rings", description="Crispy and delicious", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (4).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Buttery Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (3).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Savory Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (2).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Roasted Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (1).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Tasty Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (5).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (4).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (3).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Creamed Spinach", description="Rich and creamy", price=4.29, type="side", picture="/menu_item_images/sides/creamed_spinach/img (2).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (1).jpeg"),
]

r37_sides = [
    MenuItem(restaurant_id=37, menu_id=1, name="Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (5).jpeg"),
    MenuItem(restaurant_id=37, menu_id=1, name="Crispy Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (4).jpeg"),
    MenuItem(restaurant_id=37, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (3).jpeg"),
    MenuItem(restaurant_id=37, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (2).jpeg"),
    MenuItem(restaurant_id=37, menu_id=1, name="Roasted Vegetables", description="Tender and colorful", price=5.99, type="side", picture="/menu_item_images/sides/roasted_veggies/img (1).jpeg"),
    MenuItem(restaurant_id=37, menu_id=1, name="Creamy Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=37, menu_id=1, name="Tasty Corn on the Cob", description="Naturally sweet", price=3.99, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (4).jpeg"),
    MenuItem(restaurant_id=37, menu_id=1, name="Buttered Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=37, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (3).jpeg"),
    MenuItem(restaurant_id=37, menu_id=1, name="Cheesy Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (2).jpeg"),
]

r38_sides = [
    MenuItem(restaurant_id=38, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (5).jpeg"),
    MenuItem(restaurant_id=38, menu_id=1, name="Crispy Onion Rings", description="Crispy and delicious", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (4).jpeg"),
    MenuItem(restaurant_id=38, menu_id=1, name="Buttery Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (3).jpeg"),
    MenuItem(restaurant_id=38, menu_id=1, name="Savory Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (2).jpeg"),
    MenuItem(restaurant_id=38, menu_id=1, name="Roasted Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (1).jpeg"),
    MenuItem(restaurant_id=38, menu_id=1, name="Tasty Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (5).jpeg"),
    MenuItem(restaurant_id=38, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (4).jpeg"),
    MenuItem(restaurant_id=38, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (3).jpeg"),
    MenuItem(restaurant_id=38, menu_id=1, name="Creamed Spinach", description="Rich and creamy", price=4.29, type="side", picture="/menu_item_images/sides/creamed_spinach/img (2).jpeg"),
    MenuItem(restaurant_id=38, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (1).jpeg"),
]


r39_sides = [
    MenuItem(restaurant_id=39, menu_id=1, name="Crispy Onion Rings", description="Crispy and delicious", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (5).jpeg"),
    MenuItem(restaurant_id=39, menu_id=1, name="Buttery Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (4).jpeg"),
    MenuItem(restaurant_id=39, menu_id=1, name="Savory Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (3).jpeg"),
    MenuItem(restaurant_id=39, menu_id=1, name="Roasted Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (2).jpeg"),
    MenuItem(restaurant_id=39, menu_id=1, name="Tasty Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (1).jpeg"),
    MenuItem(restaurant_id=39, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (5).jpeg"),
    MenuItem(restaurant_id=39, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (4).jpeg"),
    MenuItem(restaurant_id=39, menu_id=1, name="Creamed Spinach", description="Rich and creamy", price=4.29, type="side", picture="/menu_item_images/sides/creamed_spinach/img (3).jpeg"),
    MenuItem(restaurant_id=39, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=39, menu_id=1, name="Cheesy Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (5).jpeg"),
]


r40_sides = [
    MenuItem(restaurant_id=40, menu_id=1, name="Roasted Vegetables", description="Tender and colorful", price=5.99, type="side", picture="/menu_item_images/sides/roasted_veggies/img (5).jpeg"),
    MenuItem(restaurant_id=40, menu_id=1, name="Creamy Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (4).jpeg"),
    MenuItem(restaurant_id=40, menu_id=1, name="Tasty Corn on the Cob", description="Naturally sweet", price=3.99, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (3).jpeg"),
    MenuItem(restaurant_id=40, menu_id=1, name="Buttered Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (2).jpeg"),
    MenuItem(restaurant_id=40, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (5).jpeg"),
    MenuItem(restaurant_id=40, menu_id=1, name="Cheesy Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (4).jpeg"),
    MenuItem(restaurant_id=40, menu_id=1, name="Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (3).jpeg"),
    MenuItem(restaurant_id=40, menu_id=1, name="Crispy Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (2).jpeg"),
    MenuItem(restaurant_id=40, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (1).jpeg"),
    MenuItem(restaurant_id=40, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (5).jpeg"),
]


r41_sides = [
    MenuItem(restaurant_id=41, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (1).jpeg"),
    MenuItem(restaurant_id=41, menu_id=1, name="Creamed Spinach", description="Rich and creamy", price=4.29, type="side", picture="/menu_item_images/sides/creamed_spinach/img (5).jpeg"),
    MenuItem(restaurant_id=41, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (4).jpeg"),
    MenuItem(restaurant_id=41, menu_id=1, name="Cheesy Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (3).jpeg"),
    MenuItem(restaurant_id=41, menu_id=1, name="Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (2).jpeg"),
    MenuItem(restaurant_id=41, menu_id=1, name="Crispy Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (1).jpeg"),
    MenuItem(restaurant_id=41, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (5).jpeg"),
    MenuItem(restaurant_id=41, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (4).jpeg"),
    MenuItem(restaurant_id=41, menu_id=1, name="Roasted Vegetables", description="Tender and colorful", price=5.99, type="side", picture="/menu_item_images/sides/roasted_veggies/img (3).jpeg"),
    MenuItem(restaurant_id=41, menu_id=1, name="Creamy Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (1).jpeg"),
]

r42_sides = [
    MenuItem(restaurant_id=30, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (3).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (2).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Sweet Potato Fries", description="Crispy and delightful", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (1).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Green Beans", description="Sautéed to perfection", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (5).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (4).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (3).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Crispy Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (2).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/salad/img (1).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Cheesy Broccoli", description="Melted cheddar goodness", price=4.99, type="side", picture="/menu_item_images/sides/broccoli/img (5).jpeg"),
    MenuItem(restaurant_id=30, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (4).jpeg"),
]


r43_sides = [
    MenuItem(restaurant_id=31, menu_id=1, name="Onion Rings", description="Crispy and delicious", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (5).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="French Fries", description="Golden and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (4).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Roasted Vegetables", description="Tender and colorful", price=5.99, type="side", picture="/menu_item_images/sides/roasted_veggies/img (3).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Creamy Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (2).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (1).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (5).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (3).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=31, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (1).jpeg"),
]


r44_sides = [
    MenuItem(restaurant_id=32, menu_id=1, name="Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (5).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Sweet Potato Fries", description="Crispy and delightful", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (4).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Green Beans", description="Sautéed to perfection", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (3).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Garlic Parmesan Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (2).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (1).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Crispy Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (5).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (4).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (3).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (2).jpeg"),
    MenuItem(restaurant_id=32, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (1).jpeg"),
]


r45_sides = [
    MenuItem(restaurant_id=33, menu_id=1, name="Coleslaw", description="Crunchy and tangy", price=2.49, type="side", picture="/menu_item_images/sides/coleslaw/img (5).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (4).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Bread Rolls", description="Soft and warm", price=2.49, type="side", picture="/menu_item_images/sides/bread_rolls/img (3).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Garden Salad", description="Fresh and light", price=3.99, type="side", picture="/menu_item_images/sides/garden_salad/img (2).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Roasted Cauliflower", description="Tender and flavorful", price=4.49, type="side", picture="/menu_item_images/sides/roasted_cauliflower/img (1).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Sweet Potato Fries", description="Crispy and delightful", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (5).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Lo Mein", description="Savory noodle delight", price=5.49, type="side", picture="/menu_item_images/sides/lo_mein/img (4).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (3).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (2).jpeg"),
    MenuItem(restaurant_id=33, menu_id=1, name="Cheesy Broccoli", description="Melted cheddar goodness", price=4.99, type="side", picture="/menu_item_images/sides/broccoli/img (1).jpeg"),
]


r46_sides = [
    MenuItem(restaurant_id=34, menu_id=1, name="French Fries", description="Golden and crispy", price=3.99, type="side", picture="/menu_item_images/sides/fries/img (5).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Onion Rings", description="Crispy and delicious", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (4).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (3).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (2).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (1).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (5).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Sweet Potato Fries", description="Crispy and delightful", price=4.49, type="side", picture="/menu_item_images/sides/sweet_potato_fries/img (4).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (3).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Green Beans", description="Sautéed to perfection", price=3.99, type="side", picture="/menu_item_images/sides/green_beans/img (2).jpeg"),
    MenuItem(restaurant_id=34, menu_id=1, name="Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (1).jpeg"),
]


r47_sides = [
    MenuItem(restaurant_id=35, menu_id=1, name="Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (5).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Crispy Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (4).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (3).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (2).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Roasted Vegetables", description="Tender and colorful", price=5.99, type="side", picture="/menu_item_images/sides/roasted_veggies/img (1).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Creamy Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Tasty Corn on the Cob", description="Naturally sweet", price=3.99, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (4).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Buttered Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (4).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (3).jpeg"),
    MenuItem(restaurant_id=35, menu_id=1, name="Cheesy Mac and Cheese", description="Cheesy and comforting", price=4.99, type="side", picture="/menu_item_images/sides/mac_and_cheese/img (2).jpeg"),
]


r48_sides = [
    MenuItem(restaurant_id=36, menu_id=1, name="Garlic Bread", description="Toasty and buttery", price=2.99, type="side", picture="/menu_item_images/sides/garlic_bread/img (5).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Crispy Onion Rings", description="Crispy and delicious", price=4.49, type="side", picture="/menu_item_images/sides/onion_rings/img (4).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Buttery Baked Potato", description="Buttery and satisfying", price=4.99, type="side", picture="/menu_item_images/sides/baked_potato/img (3).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Savory Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (2).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Roasted Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (1).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Tasty Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (5).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Fresh Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/garden_salad/img (4).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Zesty Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (3).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Creamed Spinach", description="Rich and creamy", price=4.29, type="side", picture="/menu_item_images/sides/creamed_spinach/img (2).jpeg"),
    MenuItem(restaurant_id=36, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (1).jpeg"),
]

r49_sides = [
    MenuItem(restaurant_id=26, menu_id=1, name="Grilled Salmon", description="Grilled to perfection", price=16.99, type="side", picture="/menu_item_images/sides/salmon/img (1).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Crispy Calamari", description="Crispy and tender", price=12.99, type="side", picture="/menu_item_images/sides/calamari/img (2).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Caesar Salad", description="Classic and flavorful", price=8.99, type="side", picture="/menu_item_images/sides/caesar_salad/img (3).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Garlic Buttered Asparagus", description="Buttery and aromatic", price=7.99, type="side", picture="/menu_item_images/sides/asparagus/img (4).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Loaded Baked Potatoes", description="Loaded with toppings", price=6.99, type="side", picture="/menu_item_images/sides/baked_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Crispy French Fries", description="Crispy and seasoned", price=5.99, type="side", picture="/menu_item_images/sides/fries/img (1).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Savory Stuffing", description="Savory and comforting", price=4.99, type="side", picture="/menu_item_images/sides/stuffing/img (2).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Buttered Corn", description="Buttery and sweet", price=3.99, type="side", picture="/menu_item_images/sides/corn/img (3).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Soft Dinner Rolls", description="Soft and fluffy", price=2.99, type="side", picture="/menu_item_images/sides/rolls/img (4).jpeg"),
    MenuItem(restaurant_id=26, menu_id=1, name="Fresh Fruit Salad", description="Fresh and colorful", price=4.49, type="side", picture="/menu_item_images/sides/fruit_salad/img (5).jpeg"),
]

r50_sides = [
    MenuItem(restaurant_id=27, menu_id=1, name="Fried Rice", description="Flavorful rice medley", price=5.49, type="side", picture="/menu_item_images/sides/fried_rice/img (2).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Broccoli", description="Melted cheddar goodness", price=4.99, type="side", picture="/menu_item_images/sides/broccoli/img (1).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Onion Rings", description="Golden and satisfying", price=3.99, type="side", picture="/menu_item_images/sides/onion_rings/img (3).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Breadsticks", description="Irresistibly aromatic", price=4.99, type="side", picture="/menu_item_images/sides/breadsticks/img (4).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Mashed Potatoes", description="Buttery and smooth", price=4.49, type="side", picture="/menu_item_images/sides/mashed_potatoes/img (5).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Roasted Vegetables", description="Tender and colorful", price=5.99, type="side", picture="/menu_item_images/sides/roasted_veggies/img (1).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Tater Tots", description="Perfectly crunchy", price=3.99, type="side", picture="/menu_item_images/sides/tater_tots/img (2).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Garden Salad", description="Crisp and refreshing", price=4.99, type="side", picture="/menu_item_images/sides/salad/img (3).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Corn on the Cob", description="Naturally sweet", price=3.49, type="side", picture="/menu_item_images/sides/corn_on_the_cob/img (4).jpeg"),
    MenuItem(restaurant_id=27, menu_id=1, name="Nachos", description="Loaded with flavor", price=4.79, type="side", picture="/menu_item_images/sides/nachos/img (5).jpeg"),
]
'''


'''  ********OUR ACTUAL SEED MENU.   WE WILL COMMBINE ALL ARAYS THEN
ADD TO DATABASE AND COMMIT THEM.
def seed_menu_items():

    menu_items = r1_entrees + r1_drinks + r1_sides + r1_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r2_entrees + r2_drinks + r2_sides + r2_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r3_entrees + r3_drinks + r3_sides + r3_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r4_entrees + r4_drinks + r4_sides + r4_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r5_entrees + r5_drinks + r5_sides + r5_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r6_entrees + r6_drinks + r6_sides + r6_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r7_entrees + r7_drinks + r7_sides + r7_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r8_entrees + r8_drinks + r8_sides + r8_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r9_entrees + r9_drinks + r9_sides + r9_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r10_entrees + r10_drinks + r10_sides + r10_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r11_entrees + r11_drinks + r11_sides + r11_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r12_entrees + r12_drinks + r12_sides + r12_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r13_entrees + r13_drinks + r13_sides + r13_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r14_entrees + r14_drinks + r14_sides + r14_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r15_entrees + r15_drinks + r15_sides + r15_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r16_entrees + r16_drinks + r16_sides + r16_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r17_entrees + r17_drinks + r17_sides + r17_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r18_entrees + r18_drinks + r18_sides + r18_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r19_entrees + r19_drinks + r19_sides + r19_desserts
    db.session.add_all(menu_items)
    db.session.commit()

    menu_items = r20_entrees + r20_drinks + r20_sides + r20_desserts
    db.session.add_all(menu_items)
    db.session.commit()

'''
def undo_menu_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menu_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menu_items"))
    db.session.commit()
