from app.models import db, MenuItem, environment, SCHEMA
from sqlalchemy.sql import text




    # Restaurant 1
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
# Restaurant 2
r2_entrees = [
    MenuItem(restaurant_id=2, menu_id=2, name="Sushi Platter", description="Assorted fresh sushi", price=20.99, type="entree", picture="path/to/picture41"),
    MenuItem(restaurant_id=2, menu_id=2, name="Teriyaki Chicken", description="Grilled chicken with teriyaki sauce", price=16.99, type="entree", picture="path/to/picture42"),
    MenuItem(restaurant_id=2, menu_id=2, name="Tempura Udon", description="Thick noodles with tempura shrimp", price=14.99, type="entree", picture="path/to/picture43"),
    MenuItem(restaurant_id=2, menu_id=2, name="Katsu Curry", description="Breaded pork with curry sauce", price=15.99, type="entree", picture="path/to/picture44"),
    MenuItem(restaurant_id=2, menu_id=2, name="Gyoza", description="Pan-fried dumplings", price=7.99, type="entree", picture="path/to/picture45"),
    MenuItem(restaurant_id=2, menu_id=2, name="Tonkotsu Ramen", description="Pork broth noodles with chashu", price=14.49, type="entree", picture="path/to/picture46"),
    MenuItem(restaurant_id=2, menu_id=2, name="Ebi Fry", description="Breaded fried shrimp", price=8.99, type="entree", picture="path/to/picture47"),
    MenuItem(restaurant_id=2, menu_id=2, name="Yakitori", description="Grilled chicken skewers", price=9.49, type="entree", picture="path/to/picture48"),
    MenuItem(restaurant_id=2, menu_id=2, name="Chirashi Bowl", description="Assorted sashimi over rice", price=18.49, type="entree", picture="path/to/picture49"),
    MenuItem(restaurant_id=2, menu_id=2, name="Okonomiyaki", description="Savory Japanese pancake", price=12.79, type="entree", picture="path/to/picture50"),
]
r2_drinks = [
    MenuItem(restaurant_id=2, menu_id=2, name="Green Tea", description="Refreshing and warm", price=3.99, type="drink", picture="path/to/picture51"),
    MenuItem(restaurant_id=2, menu_id=2, name="Sake", description="Japanese rice wine", price=7.99, type="drink", picture="path/to/picture52"),
    MenuItem(restaurant_id=2, menu_id=2, name="Asahi Beer", description="Crisp and cold", price=6.49, type="drink", picture="path/to/picture53"),
    MenuItem(restaurant_id=2, menu_id=2, name="Plum Wine", description="Sweet and tangy", price=7.49, type="drink", picture="path/to/picture54"),
    MenuItem(restaurant_id=2, menu_id=2, name="Matcha Latte", description="Creamy green tea drink", price=5.99, type="drink", picture="path/to/picture55"),
    MenuItem(restaurant_id=2, menu_id=2, name="Ginger Ale", description="Sparkling and spicy", price=4.49, type="drink", picture="path/to/picture56"),
    MenuItem(restaurant_id=2, menu_id=2, name="Lychee Martini", description="Sweet and fragrant cocktail", price=8.99, type="drink", picture="path/to/picture57"),
    MenuItem(restaurant_id=2, menu_id=2, name="Oolong Tea", description="Semi-fermented tea", price=3.49, type="drink", picture="path/to/picture58"),
    MenuItem(restaurant_id=2, menu_id=2, name="Cold Brew Coffee", description="Smooth and rich coffee", price=4.99, type="drink", picture="path/to/picture59"),
    MenuItem(restaurant_id=2, menu_id=2, name="Iced Matcha", description="Refreshing green tea drink", price=5.49, type="drink", picture="path/to/picture60"),
]
r2_sides = [
    MenuItem(restaurant_id=2, menu_id=2, name="Miso Soup", description="Warm and flavorful", price=2.99, type="side", picture="path/to/picture61"),
    MenuItem(restaurant_id=2, menu_id=2, name="Edamame", description="Salted soybeans", price=3.99, type="side", picture="path/to/picture62"),
    MenuItem(restaurant_id=2, menu_id=2, name="Cucumber Salad", description="Marinated cucumber slices", price=4.49, type="side", picture="path/to/picture63"),
    MenuItem(restaurant_id=2, menu_id=2, name="Seaweed Salad", description="Savory and tangy seaweed", price=5.49, type="side", picture="path/to/picture64"),
    MenuItem(restaurant_id=2, menu_id=2, name="Pickled Radish", description="Sweet and tangy radish slices", price=3.49, type="side", picture="path/to/picture65"),
    MenuItem(restaurant_id=2, menu_id=2, name="Rice", description="Steamed white rice", price=1.99, type="side", picture="path/to/picture66"),
    MenuItem(restaurant_id=2, menu_id=2, name="Tempura Vegetables", description="Battered and fried veggies", price=5.99, type="side", picture="path/to/picture67"),
    MenuItem(restaurant_id=2, menu_id=2, name="Sashimi", description="Assorted raw fish slices", price=10.99, type="side", picture="path/to/picture68"),
    MenuItem(restaurant_id=2, menu_id=2, name="Spring Rolls", description="Crispy rolls with vegetables", price=4.49, type="side", picture="path/to/picture69"),
    MenuItem(restaurant_id=2, menu_id=2, name="Kimchi", description="Spicy fermented cabbage", price=4.99, type="side", picture="path/to/picture70"),
]
r2_desserts = [
    MenuItem(restaurant_id=2, menu_id=2, name="Mochi Ice Cream", description="Sweet rice cake with ice cream", price=5.49, type="dessert", picture="path/to/picture71"),
    MenuItem(restaurant_id=2, menu_id=2, name="Matcha Cake", description="Green tea flavored cake", price=6.49, type="dessert", picture="path/to/picture72"),
    MenuItem(restaurant_id=2, menu_id=2, name="Red Bean Bun", description="Sweet red bean filling", price=3.99, type="dessert", picture="path/to/picture73"),
    MenuItem(restaurant_id=2, menu_id=2, name="Dorayaki", description="Red bean pancake sandwich", price=4.49, type="dessert", picture="path/to/picture74"),
    MenuItem(restaurant_id=2, menu_id=2, name="Tempura Ice Cream", description="Fried ice cream", price=6.99, type="dessert", picture="path/to/picture75"),
    MenuItem(restaurant_id=2, menu_id=2, name="Green Tea Pudding", description="Creamy matcha dessert", price=5.79, type="dessert", picture="path/to/picture76"),
    MenuItem(restaurant_id=2, menu_id=2, name="Sesame Balls", description="Sweet rice balls with sesame", price=4.99, type="dessert", picture="path/to/picture77"),
    MenuItem(restaurant_id=2, menu_id=2, name="Mango Sticky Rice", description="Sweet rice with ripe mango", price=6.49, type="dessert", picture="path/to/picture78"),
    MenuItem(restaurant_id=2, menu_id=2, name="Jelly Fruit Cubes", description="Fruity gelatin dessert", price=4.79, type="dessert", picture="path/to/picture79"),
    MenuItem(restaurant_id=2, menu_id=2, name="Chocolate Dipped Strawberries", description="Rich and sweet treat", price=6.49, type="dessert", picture="path/to/picture80"),
]
    # Restaurant 3
r3_entrees = [
    MenuItem(restaurant_id=3, menu_id=3, name="BBQ Ribs", description="Tender ribs with smoky BBQ sauce", price=20.99, type="entree", picture="path/to/picture81"),
    MenuItem(restaurant_id=3, menu_id=3, name="Grilled Salmon", description="Fresh salmon with lemon butter", price=18.99, type="entree", picture="path/to/picture82"),
    MenuItem(restaurant_id=3, menu_id=3, name="Steak Frites", description="Juicy steak with french fries", price=22.99, type="entree", picture="path/to/picture83"),
    MenuItem(restaurant_id=3, menu_id=3, name="Chicken Pot Pie", description="Creamy chicken with a flaky crust", price=15.99, type="entree", picture="path/to/picture84"),
    MenuItem(restaurant_id=3, menu_id=3, name="Lobster Roll", description="Fresh lobster in a buttered roll", price=19.99, type="entree", picture="path/to/picture85"),
    MenuItem(restaurant_id=3, menu_id=3, name="Beef Tacos", description="Spicy beef with fresh toppings", price=12.99, type="entree", picture="path/to/picture86"),
    MenuItem(restaurant_id=3, menu_id=3, name="Veggie Burger", description="Plant-based patty with all the fixings", price=13.99, type="entree", picture="path/to/picture87"),
    MenuItem(restaurant_id=3, menu_id=3, name="Caesar Salad", description="Crispy romaine with creamy dressing", price=11.99, type="entree", picture="path/to/picture88"),
    MenuItem(restaurant_id=3, menu_id=3, name="Shrimp Scampi", description="Garlic shrimp with linguini", price=17.99, type="entree", picture="path/to/picture89"),
    MenuItem(restaurant_id=3, menu_id=3, name="Meatball Sub", description="Juicy meatballs in a toasted bun", price=14.99, type="entree", picture="path/to/picture90"),
]
r3_drinks = [
    MenuItem(restaurant_id=3, menu_id=3, name="Craft Beer", description="Local artisanal brews", price=6.99, type="drink", picture="path/to/picture91"),
    MenuItem(restaurant_id=3, menu_id=3, name="Red Wine", description="Rich and robust", price=7.99, type="drink", picture="path/to/picture92"),
    MenuItem(restaurant_id=3, menu_id=3, name="Mojito", description="Refreshing mint and lime", price=8.49, type="drink", picture="path/to/picture93"),
    MenuItem(restaurant_id=3, menu_id=3, name="Bloody Mary", description="Spicy and tangy", price=7.49, type="drink", picture="path/to/picture94"),
    MenuItem(restaurant_id=3, menu_id=3, name="Iced Tea", description="Cold brewed tea with lemon", price=3.99, type="drink", picture="path/to/picture95"),
    MenuItem(restaurant_id=3, menu_id=3, name="Root Beer Float", description="Classic soda and ice cream drink", price=5.49, type="drink", picture="path/to/picture96"),
    MenuItem(restaurant_id=3, menu_id=3, name="Whiskey Sour", description="Whiskey with a hint of citrus", price=9.49, type="drink", picture="path/to/picture97"),
    MenuItem(restaurant_id=3, menu_id=3, name="White Russian", description="Creamy coffee-flavored cocktail", price=8.99, type="drink", picture="path/to/picture98"),
    MenuItem(restaurant_id=3, menu_id=3, name="Sparkling Water", description="Bubbly and refreshing", price=2.99, type="drink", picture="path/to/picture99"),
    MenuItem(restaurant_id=3, menu_id=3, name="Lemonade", description="Sweet and tangy", price=3.49, type="drink", picture="path/to/picture100"),
]
r3_sides = [
    MenuItem(restaurant_id=3, menu_id=3, name="Baked Potato", description="Fluffy potato with toppings", price=3.99, type="side", picture="path/to/picture101"),
    MenuItem(restaurant_id=3, menu_id=3, name="Coleslaw", description="Creamy slaw with crisp veggies", price=2.99, type="side", picture="path/to/picture102"),
    MenuItem(restaurant_id=3, menu_id=3, name="Brussels Sprouts", description="Roasted with bacon", price=4.99, type="side", picture="path/to/picture103"),
    MenuItem(restaurant_id=3, menu_id=3, name="Mac & Cheese", description="Creamy and cheesy", price=5.49, type="side", picture="path/to/picture104"),
    MenuItem(restaurant_id=3, menu_id=3, name="Onion Rings", description="Crispy and golden", price=4.99, type="side", picture="path/to/picture105"),
    MenuItem(restaurant_id=3, menu_id=3, name="Cornbread", description="Sweet and buttery", price=3.49, type="side", picture="path/to/picture106"),
    MenuItem(restaurant_id=3, menu_id=3, name="Sweet Potato Fries", description="Sweet and crispy", price=4.49, type="side", picture="path/to/picture107"),
    MenuItem(restaurant_id=3, menu_id=3, name="Buttered Vegetables", description="Seasonal veggies", price=4.99, type="side", picture="path/to/picture108"),
    MenuItem(restaurant_id=3, menu_id=3, name="Mashed Potatoes", description="Creamy with gravy", price=4.49, type="side", picture="path/to/picture109"),
    MenuItem(restaurant_id=3, menu_id=3, name="Corn on the Cob", description="Buttered and grilled", price=3.99, type="side", picture="path/to/picture110"),
]
r3_desserts = [
    MenuItem(restaurant_id=3, menu_id=3, name="Brownie Sundae", description="Warm brownie with ice cream", price=6.49, type="dessert", picture="path/to/picture111"),
    MenuItem(restaurant_id=3, menu_id=3, name="Apple Pie", description="Flaky crust with spiced apples", price=5.99, type="dessert", picture="path/to/picture112"),
    MenuItem(restaurant_id=3, menu_id=3, name="Creme Brulee", description="Creamy with a caramelized top", price=6.99, type="dessert", picture="path/to/picture113"),
    MenuItem(restaurant_id=3, menu_id=3, name="Chocolate Fondue", description="Melted chocolate with dippables", price=7.99, type="dessert", picture="path/to/picture114"),
    MenuItem(restaurant_id=3, menu_id=3, name="Lemon Tart", description="Tangy and sweet", price=5.49, type="dessert", picture="path/to/picture115"),
    MenuItem(restaurant_id=3, menu_id=3, name="Tiramisu", description="Coffee-soaked layers with mascarpone", price=6.79, type="dessert", picture="path/to/picture116"),
    MenuItem(restaurant_id=3, menu_id=3, name="Pavlova", description="Meringue with fresh berries", price=5.99, type="dessert", picture="path/to/picture117"),
    MenuItem(restaurant_id=3, menu_id=3, name="Molten Chocolate Cake", description="Gooey chocolate center", price=6.49, type="dessert", picture="path/to/picture118"),
    MenuItem(restaurant_id=3, menu_id=3, name="Pecan Pie", description="Sweet and nutty", price=5.79, type="dessert", picture="path/to/picture119"),
    MenuItem(restaurant_id=3, menu_id=3, name="Banana Split", description="Classic ice cream dessert", price=6.49, type="dessert", picture="path/to/picture120"),
]
# Restaurant 4
r4_entrees = [
    MenuItem(restaurant_id=4, menu_id=4, name="Tuna Steak", description="Grilled to perfection with sesame crust", price=21.99, type="entree", picture="path/to/picture121"),
    MenuItem(restaurant_id=4, menu_id=4, name="Beef Stir Fry", description="Tender beef with fresh vegetables", price=19.99, type="entree", picture="path/to/picture122"),
    MenuItem(restaurant_id=4, menu_id=4, name="Tempura Udon", description="Noodles with tempura prawns", price=18.99, type="entree", picture="path/to/picture123"),
    MenuItem(restaurant_id=4, menu_id=4, name="Pork Ramen", description="Rich broth with tender pork", price=17.99, type="entree", picture="path/to/picture124"),
    MenuItem(restaurant_id=4, menu_id=4, name="Sushi Platter", description="Assorted sushi rolls", price=24.99, type="entree", picture="path/to/picture125"),
    MenuItem(restaurant_id=4, menu_id=4, name="Bento Box", description="A little bit of everything", price=22.99, type="entree", picture="path/to/picture126"),
    MenuItem(restaurant_id=4, menu_id=4, name="Salmon Teriyaki", description="Grilled salmon with teriyaki glaze", price=20.99, type="entree", picture="path/to/picture127"),
    MenuItem(restaurant_id=4, menu_id=4, name="Katsu Curry", description="Breaded meat with curry sauce", price=16.99, type="entree", picture="path/to/picture128"),
    MenuItem(restaurant_id=4, menu_id=4, name="Ebi Fry", description="Fried prawn with tangy sauce", price=19.49, type="entree", picture="path/to/picture129"),
    MenuItem(restaurant_id=4, menu_id=4, name="Yakisoba", description="Stir-fried noodles with vegetables", price=15.99, type="entree", picture="path/to/picture130"),
]
r4_drinks = [
    MenuItem(restaurant_id=4, menu_id=4, name="Green Tea", description="Refreshing and calming", price=3.49, type="drink", picture="path/to/picture131"),
    MenuItem(restaurant_id=4, menu_id=4, name="Sake", description="Japanese rice wine", price=7.99, type="drink", picture="path/to/picture132"),
    MenuItem(restaurant_id=4, menu_id=4, name="Matcha Latte", description="Rich green tea with milk", price=4.99, type="drink", picture="path/to/picture133"),
    MenuItem(restaurant_id=4, menu_id=4, name="Ume Plum Wine", description="Sweet and tangy", price=6.49, type="drink", picture="path/to/picture134"),
    MenuItem(restaurant_id=4, menu_id=4, name="Wasabi Bloody Mary", description="Spicy cocktail with a kick", price=8.99, type="drink", picture="path/to/picture135"),
    MenuItem(restaurant_id=4, menu_id=4, name="Lychee Martini", description="Fruity cocktail with vodka", price=7.99, type="drink", picture="path/to/picture136"),
    MenuItem(restaurant_id=4, menu_id=4, name="Mango Bubble Tea", description="Sweet mango with tapioca pearls", price=5.49, type="drink", picture="path/to/picture137"),
    MenuItem(restaurant_id=4, menu_id=4, name="Hojicha Roasted Tea", description="Roasty and smooth", price=3.99, type="drink", picture="path/to/picture138"),
    MenuItem(restaurant_id=4, menu_id=4, name="Yuzu Lemonade", description="Citrusy and refreshing", price=4.49, type="drink", picture="path/to/picture139"),
    MenuItem(restaurant_id=4, menu_id=4, name="Mochaccino", description="Chocolate coffee with mochi bits", price=5.29, type="drink", picture="path/to/picture140"),
]
r4_sides = [
    MenuItem(restaurant_id=4, menu_id=4, name="Spring Rolls", description="Crispy and delicious", price=4.49, type="side", picture="path/to/picture141"),
    MenuItem(restaurant_id=4, menu_id=4, name="Edamame", description="Salty and healthy", price=3.49, type="side", picture="path/to/picture142"),
    MenuItem(restaurant_id=4, menu_id=4, name="Miso Soup", description="Warm and soothing", price=2.99, type="side", picture="path/to/picture143"),
    MenuItem(restaurant_id=4, menu_id=4, name="Gyoza", description="Pan-fried dumplings", price=5.49, type="side", picture="path/to/picture144"),
    MenuItem(restaurant_id=4, menu_id=4, name="Seaweed Salad", description="Healthy and tasty", price=4.99, type="side", picture="path/to/picture145"),
    MenuItem(restaurant_id=4, menu_id=4, name="Shrimp Tempura", description="Crispy fried shrimps", price=6.99, type="side", picture="path/to/picture146"),
    MenuItem(restaurant_id=4, menu_id=4, name="Takoyaki", description="Octopus balls with mayo and bonito", price=5.99, type="side", picture="path/to/picture147"),
    MenuItem(restaurant_id=4, menu_id=4, name="Rice", description="Steamed white rice", price=2.49, type="side", picture="path/to/picture148"),
    MenuItem(restaurant_id=4, menu_id=4, name="Kimchi", description="Spicy Korean cabbage", price=3.99, type="side", picture="path/to/picture149"),
    MenuItem(restaurant_id=4, menu_id=4, name="Chuka Salad", description="Chinese style salad with sesame dressing", price=4.79, type="side", picture="path/to/picture150"),
]
r4_desserts = [
    MenuItem(restaurant_id=4, menu_id=4, name="Green Tea Ice Cream", description="Creamy and flavorful", price=5.99, type="dessert", picture="path/to/picture151"),
    MenuItem(restaurant_id=4, menu_id=4, name="Mochi", description="Sweet rice cakes", price=4.99, type="dessert", picture="path/to/picture152"),
    MenuItem(restaurant_id=4, menu_id=4, name="Red Bean Cake", description="Sweet and chewy", price=4.49, type="dessert", picture="path/to/picture153"),
    MenuItem(restaurant_id=4, menu_id=4, name="Sesame Balls", description="Crispy and filled with sweet paste", price=4.79, type="dessert", picture="path/to/picture154"),
    MenuItem(restaurant_id=4, menu_id=4, name="Matcha Cheesecake", description="Rich and creamy with green tea flavor", price=6.49, type="dessert", picture="path/to/picture155"),
    MenuItem(restaurant_id=4, menu_id=4, name="Tempura Banana", description="Fried banana with honey drizzle", price=5.49, type="dessert", picture="path/to/picture156"),
    MenuItem(restaurant_id=4, menu_id=4, name="Yuzu Sorbet", description="Citrusy and refreshing", price=4.99, type="dessert", picture="path/to/picture157"),
    MenuItem(restaurant_id=4, menu_id=4, name="Sake Jelly", description="Jelly with a hint of rice wine", price=5.29, type="dessert", picture="path/to/picture158"),
    MenuItem(restaurant_id=4, menu_id=4, name="Kanten", description="Japanese agar dessert with fruit", price=4.69, type="dessert", picture="path/to/picture159"),
    MenuItem(restaurant_id=4, menu_id=4, name="Wasabi Brownies", description="Spicy twist on a classic", price=5.79, type="dessert", picture="path/to/picture160"),
]
# Restaurant 5
r5_entrees = [
    MenuItem(restaurant_id=5, menu_id=5, name="Gyro Wrap", description="Savory meat in a soft pita", price=10.99, type="entree", picture="path/to/picture161"),
    MenuItem(restaurant_id=5, menu_id=5, name="Spanakopita", description="Spinach pie with flaky crust", price=8.99, type="entree", picture="path/to/picture162"),
    MenuItem(restaurant_id=5, menu_id=5, name="Souvlaki", description="Grilled meat skewers", price=11.99, type="entree", picture="path/to/picture163"),
    MenuItem(restaurant_id=5, menu_id=5, name="Moussaka", description="Layered eggplant, meat, and béchamel", price=14.99, type="entree", picture="path/to/picture164"),
    MenuItem(restaurant_id=5, menu_id=5, name="Pastitsio", description="Greek lasagna with meat and pasta", price=13.99, type="entree", picture="path/to/picture165"),
    MenuItem(restaurant_id=5, menu_id=5, name="Lamb Kleftiko", description="Roasted lamb with herbs", price=16.99, type="entree", picture="path/to/picture166"),
    MenuItem(restaurant_id=5, menu_id=5, name="Dolmades", description="Rice stuffed grape leaves", price=9.99, type="entree", picture="path/to/picture167"),
    MenuItem(restaurant_id=5, menu_id=5, name="Tiropita", description="Cheese-filled pastry", price=8.49, type="entree", picture="path/to/picture168"),
    MenuItem(restaurant_id=5, menu_id=5, name="Taramasalata", description="Fish roe dip with olive oil", price=7.99, type="entree", picture="path/to/picture169"),
    MenuItem(restaurant_id=5, menu_id=5, name="Horiatiki", description="Classic Greek salad", price=9.49, type="entree", picture="path/to/picture170"),
]
r5_drinks = [
    MenuItem(restaurant_id=5, menu_id=5, name="Greek Coffee", description="Strong and flavorful", price=2.99, type="drink", picture="path/to/picture171"),
    MenuItem(restaurant_id=5, menu_id=5, name="Ouzo", description="Anise-flavored liqueur", price=6.99, type="drink", picture="path/to/picture172"),
    MenuItem(restaurant_id=5, menu_id=5, name="Retsina", description="Pine-resinated white wine", price=5.49, type="drink", picture="path/to/picture173"),
    MenuItem(restaurant_id=5, menu_id=5, name="Mastiha", description="Liqueur with mastic flavor", price=7.49, type="drink", picture="path/to/picture174"),
    MenuItem(restaurant_id=5, menu_id=5, name="Tzatziki Smoothie", description="Yogurt drink with cucumber and mint", price=4.99, type="drink", picture="path/to/picture175"),
    MenuItem(restaurant_id=5, menu_id=5, name="Metaxa", description="Greek brandy", price=7.99, type="drink", picture="path/to/picture176"),
    MenuItem(restaurant_id=5, menu_id=5, name="Athens Spritz", description="Refreshing cocktail with Ouzo", price=8.49, type="drink", picture="path/to/picture177"),
    MenuItem(restaurant_id=5, menu_id=5, name="Lemonada", description="Fresh Greek lemonade", price=3.49, type="drink", picture="path/to/picture178"),
    MenuItem(restaurant_id=5, menu_id=5, name="Chamomile Tea", description="Soothing herbal tea", price=2.99, type="drink", picture="path/to/picture179"),
    MenuItem(restaurant_id=5, menu_id=5, name="Orange Cinnamon Punch", description="Citrusy and warm", price=4.99, type="drink", picture="path/to/picture180"),
]
r5_sides = [
    MenuItem(restaurant_id=5, menu_id=5, name="Pita Bread", description="Soft and fluffy", price=1.99, type="side", picture="path/to/picture181"),
    MenuItem(restaurant_id=5, menu_id=5, name="Tzatziki", description="Yogurt cucumber dip", price=3.99, type="side", picture="path/to/picture182"),
    MenuItem(restaurant_id=5, menu_id=5, name="Fasolada", description="White bean soup", price=4.49, type="side", picture="path/to/picture183"),
    MenuItem(restaurant_id=5, menu_id=5, name="Greek Olives", description="Mixed olives with herbs", price=3.49, type="side", picture="path/to/picture184"),
    MenuItem(restaurant_id=5, menu_id=5, name="Spanakorizo", description="Spinach rice", price=4.99, type="side", picture="path/to/picture185"),
    MenuItem(restaurant_id=5, menu_id=5, name="Briam", description="Roasted vegetables in tomato sauce", price=4.79, type="side", picture="path/to/picture186"),
    MenuItem(restaurant_id=5, menu_id=5, name="Skordalia", description="Garlic almond dip", price=3.99, type="side", picture="path/to/picture187"),
    MenuItem(restaurant_id=5, menu_id=5, name="Kolokithokeftedes", description="Zucchini fritters", price=5.29, type="side", picture="path/to/picture188"),
    MenuItem(restaurant_id=5, menu_id=5, name="Loukaniko", description="Greek sausage", price=5.99, type="side", picture="path/to/picture189"),
    MenuItem(restaurant_id=5, menu_id=5, name="Revithia", description="Chickpea stew", price=4.49, type="side", picture="path/to/picture190"),
]
r5_desserts = [
    MenuItem(restaurant_id=5, menu_id=5, name="Baklava", description="Nut-filled pastry with syrup", price=5.99, type="dessert", picture="path/to/picture191"),
    MenuItem(restaurant_id=5, menu_id=5, name="Loukoumades", description="Honey-soaked dough balls", price=5.49, type="dessert", picture="path/to/picture192"),
    MenuItem(restaurant_id=5, menu_id=5, name="Galaktoboureko", description="Custard pie with syrup", price=5.79, type="dessert", picture="path/to/picture193"),
    MenuItem(restaurant_id=5, menu_id=5, name="Rizogalo", description="Rice pudding with cinnamon", price=4.99, type="dessert", picture="path/to/picture194"),
    MenuItem(restaurant_id=5, menu_id=5, name="Koulourakia", description="Twisted butter cookies", price=4.49, type="dessert", picture="path/to/picture195"),
    MenuItem(restaurant_id=5, menu_id=5, name="Kataifi", description="Shredded pastry with nuts and syrup", price=5.69, type="dessert", picture="path/to/picture196"),
    MenuItem(restaurant_id=5, menu_id=5, name="Amygdalota", description="Almond cookies", price=4.79, type="dessert", picture="path/to/picture197"),
    MenuItem(restaurant_id=5, menu_id=5, name="Ekmek Kataifi", description="Pastry with custard and cream", price=6.29, type="dessert", picture="path/to/picture198"),
    MenuItem(restaurant_id=5, menu_id=5, name="Melomakarona", description="Honey cookies with walnuts", price=5.49, type="dessert", picture="path/to/picture199"),
    MenuItem(restaurant_id=5, menu_id=5, name="Diples", description="Fried dough with honey and nuts", price=5.89, type="dessert", picture="path/to/picture200"),
]
# Restaurant 6
r6_entrees = [
    MenuItem(restaurant_id=6, menu_id=6, name="Vegan Burger", description="Plant-based patty with vegan cheese", price=11.99, type="entree", picture="path/to/picture201"),
    MenuItem(restaurant_id=6, menu_id=6, name="Lentil Soup", description="Rich and hearty lentil-based soup", price=9.99, type="entree", picture="path/to/picture202"),
    MenuItem(restaurant_id=6, menu_id=6, name="Mushroom Risotto", description="Creamy risotto with wild mushrooms", price=12.99, type="entree", picture="path/to/picture203"),
    MenuItem(restaurant_id=6, menu_id=6, name="Vegan Tacos", description="Filled with beans, vegan cheese, and salsa", price=10.49, type="entree", picture="path/to/picture204"),
    MenuItem(restaurant_id=6, menu_id=6, name="Falafel Wrap", description="Crispy falafel with tahini sauce", price=9.49, type="entree", picture="path/to/picture205"),
    MenuItem(restaurant_id=6, menu_id=6, name="Vegan Pizza", description="With vegan cheese and assorted veggies", price=14.99, type="entree", picture="path/to/picture206"),
    MenuItem(restaurant_id=6, menu_id=6, name="Thai Green Curry", description="Coconut-based curry with tofu", price=13.99, type="entree", picture="path/to/picture207"),
    MenuItem(restaurant_id=6, menu_id=6, name="Seitan Stir Fry", description="Seitan pieces with veggies in teriyaki sauce", price=12.49, type="entree", picture="path/to/picture208"),
    MenuItem(restaurant_id=6, menu_id=6, name="Quinoa Salad", description="Refreshing salad with veggies and quinoa", price=9.99, type="entree", picture="path/to/picture209"),
    MenuItem(restaurant_id=6, menu_id=6, name="Tempeh Sandwich", description="Grilled tempeh with vegan mayo", price=10.99, type="entree", picture="path/to/picture210"),
]
r6_drinks = [
    MenuItem(restaurant_id=6, menu_id=6, name="Green Smoothie", description="Spinach, kale, and banana blend", price=5.99, type="drink", picture="path/to/picture211"),
    MenuItem(restaurant_id=6, menu_id=6, name="Almond Latte", description="Rich coffee with almond milk", price=4.49, type="drink", picture="path/to/picture212"),
    MenuItem(restaurant_id=6, menu_id=6, name="Herbal Tea", description="Soothing blend of herbs", price=2.99, type="drink", picture="path/to/picture213"),
    MenuItem(restaurant_id=6, menu_id=6, name="Vegan Shake", description="Made with soy milk and vegan protein", price=6.99, type="drink", picture="path/to/picture214"),
    MenuItem(restaurant_id=6, menu_id=6, name="Detox Juice", description="Green apple, celery, and cucumber", price=5.49, type="drink", picture="path/to/picture215"),
    MenuItem(restaurant_id=6, menu_id=6, name="Ginger Lemonade", description="Tangy and spicy lemonade", price=4.49, type="drink", picture="path/to/picture216"),
    MenuItem(restaurant_id=6, menu_id=6, name="Turmeric Latte", description="Golden milk with a hint of pepper", price=4.99, type="drink", picture="path/to/picture217"),
    MenuItem(restaurant_id=6, menu_id=6, name="Berry Bliss", description="Mixed berry smoothie", price=5.79, type="drink", picture="path/to/picture218"),
    MenuItem(restaurant_id=6, menu_id=6, name="Cold Brew", description="Strong and chilled coffee", price=3.99, type="drink", picture="path/to/picture219"),
    MenuItem(restaurant_id=6, menu_id=6, name="Kombucha", description="Fermented tea with a fizz", price=4.79, type="drink", picture="path/to/picture220"),
]
r6_sides = [
    MenuItem(restaurant_id=6, menu_id=6, name="Vegan Slaw", description="Tangy and crunchy", price=3.49, type="side", picture="path/to/picture221"),
    MenuItem(restaurant_id=6, menu_id=6, name="Sweet Potato Fries", description="Baked and lightly salted", price=4.99, type="side", picture="path/to/picture222"),
    MenuItem(restaurant_id=6, menu_id=6, name="Edamame", description="Steamed soybeans with a pinch of salt", price=3.99, type="side", picture="path/to/picture223"),
    MenuItem(restaurant_id=6, menu_id=6, name="Hummus and Pita", description="Creamy chickpea dip with bread", price=4.49, type="side", picture="path/to/picture224"),
    MenuItem(restaurant_id=6, menu_id=6, name="Roasted Veggies", description="Seasonal veggies roasted to perfection", price=4.79, type="side", picture="path/to/picture225"),
    MenuItem(restaurant_id=6, menu_id=6, name="Guacamole", description="Avocado dip with lime and cilantro", price=4.99, type="side", picture="path/to/picture226"),
    MenuItem(restaurant_id=6, menu_id=6, name="Kale Chips", description="Crispy baked kale with sea salt", price=3.79, type="side", picture="path/to/picture227"),
    MenuItem(restaurant_id=6, menu_id=6, name="Polenta Fries", description="Crispy outside, soft inside", price=4.49, type="side", picture="path/to/picture228"),
    MenuItem(restaurant_id=6, menu_id=6, name="Vegan Nachos", description="With vegan cheese and jalapenos", price=5.99, type="side", picture="path/to/picture229"),
    MenuItem(restaurant_id=6, menu_id=6, name="Chia Pudding", description="Chia seeds soaked in almond milk", price=4.99, type="side", picture="path/to/picture230"),
]
r6_desserts = [
    MenuItem(restaurant_id=6, menu_id=6, name="Vegan Cheesecake", description="Cashew-based creamy delight", price=5.99, type="dessert", picture="path/to/picture231"),
    MenuItem(restaurant_id=6, menu_id=6, name="Avocado Chocolate Mousse", description="Rich and creamy", price=5.49, type="dessert", picture="path/to/picture232"),
    MenuItem(restaurant_id=6, menu_id=6, name="Vegan Brownie", description="Chocolatey and moist", price=5.79, type="dessert", picture="path/to/picture233"),
    MenuItem(restaurant_id=6, menu_id=6, name="Mango Sorbet", description="Refreshing mango treat", price=4.99, type="dessert", picture="path/to/picture234"),
    MenuItem(restaurant_id=6, menu_id=6, name="Berry Parfait", description="Layers of berry compote and vegan yogurt", price=4.49, type="dessert", picture="path/to/picture235"),
    MenuItem(restaurant_id=6, menu_id=6, name="Almond Joy Bites", description="Almond, coconut, and chocolate", price=5.69, type="dessert", picture="path/to/picture236"),
    MenuItem(restaurant_id=6, menu_id=6, name="Vegan Gelato", description="Creamy and dairy-free", price=4.79, type="dessert", picture="path/to/picture237"),
    MenuItem(restaurant_id=6, menu_id=6, name="Peanut Butter Cups", description="Vegan chocolate and peanut butter", price=5.29, type="dessert", picture="path/to/picture238"),
    MenuItem(restaurant_id=6, menu_id=6, name="Fruit Tart", description="Seasonal fruits on a crisp base", price=5.49, type="dessert", picture="path/to/picture239"),
    MenuItem(restaurant_id=6, menu_id=6, name="Banana Bread", description="Moist and nutty", price=4.89, type="dessert", picture="path/to/picture240"),
]
# Restaurant 7
r7_entrees = [
    MenuItem(restaurant_id=7, menu_id=7, name="Butter Chicken", description="Rich tomato gravy with tender chicken pieces", price=13.99, type="entree", picture="path/to/picture241"),
    MenuItem(restaurant_id=7, menu_id=7, name="Lamb Rogan Josh", description="Aromatic curry with succulent lamb chunks", price=15.99, type="entree", picture="path/to/picture242"),
    MenuItem(restaurant_id=7, menu_id=7, name="Paneer Tikka Masala", description="Grilled paneer in spiced gravy", price=12.99, type="entree", picture="path/to/picture243"),
    MenuItem(restaurant_id=7, menu_id=7, name="Chana Masala", description="Spiced chickpea curry", price=11.49, type="entree", picture="path/to/picture244"),
    MenuItem(restaurant_id=7, menu_id=7, name="Beef Vindaloo", description="Hot and tangy beef curry", price=14.49, type="entree", picture="path/to/picture245"),
    MenuItem(restaurant_id=7, menu_id=7, name="Chicken Biryani", description="Fragrant rice with spiced chicken", price=13.99, type="entree", picture="path/to/picture246"),
    MenuItem(restaurant_id=7, menu_id=7, name="Vegetable Korma", description="Mixed veggies in creamy sauce", price=12.99, type="entree", picture="path/to/picture247"),
    MenuItem(restaurant_id=7, menu_id=7, name="Goan Fish Curry", description="Fish in tangy coconut gravy", price=14.49, type="entree", picture="path/to/picture248"),
    MenuItem(restaurant_id=7, menu_id=7, name="Daal Makhani", description="Rich lentil curry", price=10.99, type="entree", picture="path/to/picture249"),
    MenuItem(restaurant_id=7, menu_id=7, name="Egg Curry", description="Boiled eggs in spiced tomato gravy", price=11.99, type="entree", picture="path/to/picture250"),
]
r7_drinks = [
    MenuItem(restaurant_id=7, menu_id=7, name="Masala Chai", description="Spiced tea with milk", price=2.99, type="drink", picture="path/to/picture251"),
    MenuItem(restaurant_id=7, menu_id=7, name="Mango Lassi", description="Yogurt-based mango drink", price=4.49, type="drink", picture="path/to/picture252"),
    MenuItem(restaurant_id=7, menu_id=7, name="Salted Lassi", description="Yogurt drink with a pinch of salt", price=3.99, type="drink", picture="path/to/picture253"),
    MenuItem(restaurant_id=7, menu_id=7, name="Rose Sherbet", description="Refreshing rose-flavored drink", price=4.49, type="drink", picture="path/to/picture254"),
    MenuItem(restaurant_id=7, menu_id=7, name="Soda Shikanji", description="Lemon soda with spices", price=3.49, type="drink", picture="path/to/picture255"),
    MenuItem(restaurant_id=7, menu_id=7, name="Rooh Afza", description="Herbal drink with a hint of rose", price=3.99, type="drink", picture="path/to/picture256"),
    MenuItem(restaurant_id=7, menu_id=7, name="Tamarind Drink", description="Sweet and tangy", price=4.29, type="drink", picture="path/to/picture257"),
    MenuItem(restaurant_id=7, menu_id=7, name="Cardamom Coffee", description="Coffee with a hint of cardamom", price=3.79, type="drink", picture="path/to/picture258"),
    MenuItem(restaurant_id=7, menu_id=7, name="Coconut Water", description="Refreshing and hydrating", price=2.99, type="drink", picture="path/to/picture259"),
    MenuItem(restaurant_id=7, menu_id=7, name="Pomegranate Juice", description="Freshly squeezed pomegranate", price=4.99, type="drink", picture="path/to/picture260"),
]
r7_sides = [
    MenuItem(restaurant_id=7, menu_id=7, name="Samosa", description="Fried pastry with potato filling", price=3.49, type="side", picture="path/to/picture261"),
    MenuItem(restaurant_id=7, menu_id=7, name="Naan Bread", description="Soft and fluffy bread", price=2.99, type="side", picture="path/to/picture262"),
    MenuItem(restaurant_id=7, menu_id=7, name="Basmati Rice", description="Fragrant long-grain rice", price=2.49, type="side", picture="path/to/picture263"),
    MenuItem(restaurant_id=7, menu_id=7, name="Tandoori Roti", description="Whole wheat bread", price=2.49, type="side", picture="path/to/picture264"),
    MenuItem(restaurant_id=7, menu_id=7, name="Onion Bhaji", description="Fried onion fritters", price=3.79, type="side", picture="path/to/picture265"),
    MenuItem(restaurant_id=7, menu_id=7, name="Cucumber Raita", description="Yogurt with cucumber and spices", price=2.99, type="side", picture="path/to/picture266"),
    MenuItem(restaurant_id=7, menu_id=7, name="Mango Pickle", description="Tangy and spicy", price=2.49, type="side", picture="path/to/picture267"),
    MenuItem(restaurant_id=7, menu_id=7, name="Papadum", description="Crispy lentil crackers", price=2.79, type="side", picture="path/to/picture268"),
    MenuItem(restaurant_id=7, menu_id=7, name="Garlic Naan", description="Naan bread with garlic flavor", price=3.49, type="side", picture="path/to/picture269"),
    MenuItem(restaurant_id=7, menu_id=7, name="Mint Chutney", description="Mint-based dipping sauce", price=1.99, type="side", picture="path/to/picture270"),
]
r7_desserts = [
    MenuItem(restaurant_id=7, menu_id=7, name="Gulab Jamun", description="Milk-based sweet balls in syrup", price=4.49, type="dessert", picture="path/to/picture271"),
    MenuItem(restaurant_id=7, menu_id=7, name="Ras Malai", description="Milk cake in creamy sauce", price=4.99, type="dessert", picture="path/to/picture272"),
    MenuItem(restaurant_id=7, menu_id=7, name="Kheer", description="Rice pudding with nuts", price=4.29, type="dessert", picture="path/to/picture273"),
    MenuItem(restaurant_id=7, menu_id=7, name="Carrot Halwa", description="Sweet carrot dessert", price=4.49, type="dessert", picture="path/to/picture274"),
    MenuItem(restaurant_id=7, menu_id=7, name="Kulfi", description="Indian ice cream", price=4.79, type="dessert", picture="path/to/picture275"),
    MenuItem(restaurant_id=7, menu_id=7, name="Besan Ladoo", description="Chickpea flour and sugar balls", price=4.49, type="dessert", picture="path/to/picture276"),
    MenuItem(restaurant_id=7, menu_id=7, name="Barfi", description="Milk-based fudge", price=4.29, type="dessert", picture="path/to/picture277"),
    MenuItem(restaurant_id=7, menu_id=7, name="Shahi Tukda", description="Bread pudding with nuts", price=4.79, type="dessert", picture="path/to/picture278"),
    MenuItem(restaurant_id=7, menu_id=7, name="Jalebi", description="Swirls of sweet syrup", price=4.49, type="dessert", picture="path/to/picture279"),
    MenuItem(restaurant_id=7, menu_id=7, name="Coconut Ladoo", description="Sweet coconut balls", price=4.69, type="dessert", picture="path/to/picture280"),
]
# Restaurant 8
r8_entrees = [
    MenuItem(restaurant_id=8, menu_id=8, name="Shrimp Har Gow", description="Steamed shrimp dumplings", price=6.99, type="entree", picture="path/to/picture281"),
    MenuItem(restaurant_id=8, menu_id=8, name="Pork Siu Mai", description="Steamed pork and shrimp dumplings", price=6.49, type="entree", picture="path/to/picture282"),
    MenuItem(restaurant_id=8, menu_id=8, name="BBQ Pork Buns", description="Fluffy buns with sweet pork filling", price=6.79, type="entree", picture="path/to/picture283"),
    MenuItem(restaurant_id=8, menu_id=8, name="Steamed Chicken Feet", description="In black bean sauce", price=5.99, type="entree", picture="path/to/picture284"),
    MenuItem(restaurant_id=8, menu_id=8, name="Rice Noodle Roll", description="With shrimp or beef", price=6.49, type="entree", picture="path/to/picture285"),
    MenuItem(restaurant_id=8, menu_id=8, name="Sticky Rice in Lotus Leaf", description="Rice with meat filling", price=6.99, type="entree", picture="path/to/picture286"),
    MenuItem(restaurant_id=8, menu_id=8, name="Steamed Spare Ribs", description="In garlic and black bean sauce", price=6.79, type="entree", picture="path/to/picture287"),
    MenuItem(restaurant_id=8, menu_id=8, name="Duck Web with Abalone", description="Luxurious dim sum item", price=7.49, type="entree", picture="path/to/picture288"),
    MenuItem(restaurant_id=8, menu_id=8, name="Custard Buns", description="Sweet buns with custard filling", price=5.99, type="entree", picture="path/to/picture289"),
    MenuItem(restaurant_id=8, menu_id=8, name="Tofu Skin Roll", description="Stuffed with veggies and meat", price=6.49, type="entree", picture="path/to/picture290"),
]
r8_drinks = [
    MenuItem(restaurant_id=8, menu_id=8, name="Jasmine Tea", description="Fragrant floral tea", price=2.99, type="drink", picture="path/to/picture291"),
    MenuItem(restaurant_id=8, menu_id=8, name="Oolong Tea", description="Semi-oxidized Chinese tea", price=3.49, type="drink", picture="path/to/picture292"),
    MenuItem(restaurant_id=8, menu_id=8, name="Chrysanthemum Tea", description="Soothing herbal tea", price=3.29, type="drink", picture="path/to/picture293"),
    MenuItem(restaurant_id=8, menu_id=8, name="Pu-erh Tea", description="Aged fermented tea", price=3.79, type="drink", picture="path/to/picture294"),
    MenuItem(restaurant_id=8, menu_id=8, name="Lychee Black Tea", description="Black tea with lychee flavor", price=3.49, type="drink", picture="path/to/picture295"),
    MenuItem(restaurant_id=8, menu_id=8, name="Lemon Iced Tea", description="Refreshing black tea with lemon", price=3.29, type="drink", picture="path/to/picture296"),
    MenuItem(restaurant_id=8, menu_id=8, name="Mango Slush", description="Iced mango drink", price=3.99, type="drink", picture="path/to/picture297"),
    MenuItem(restaurant_id=8, menu_id=8, name="Honeydew Bubble Tea", description="With tapioca pearls", price=4.49, type="drink", picture="path/to/picture298"),
    MenuItem(restaurant_id=8, menu_id=8, name="Coconut Juice", description="Sweet coconut drink", price=3.99, type="drink", picture="path/to/picture299"),
    MenuItem(restaurant_id=8, menu_id=8, name="Passionfruit Green Tea", description="Tangy and refreshing", price=3.79, type="drink", picture="path/to/picture300"),
]
r8_sides = [
    MenuItem(restaurant_id=8, menu_id=8, name="Spring Rolls", description="Crispy rolls with veggie filling", price=4.99, type="side", picture="path/to/picture301"),
    MenuItem(restaurant_id=8, menu_id=8, name="Fried Wonton", description="Crispy wonton with meat filling", price=5.49, type="side", picture="path/to/picture302"),
    MenuItem(restaurant_id=8, menu_id=8, name="Salt and Pepper Squid", description="Fried squid with spices", price=6.79, type="side", picture="path/to/picture303"),
    MenuItem(restaurant_id=8, menu_id=8, name="Fried Tofu", description="Golden brown tofu cubes", price=4.99, type="side", picture="path/to/picture304"),
    MenuItem(restaurant_id=8, menu_id=8, name="Stuffed Eggplant", description="With shrimp and black bean sauce", price=5.99, type="side", picture="path/to/picture305"),
    MenuItem(restaurant_id=8, menu_id=8, name="Garlic Green Beans", description="Stir-fried with garlic", price=4.79, type="side", picture="path/to/picture306"),
    MenuItem(restaurant_id=8, menu_id=8, name="Pan-fried Radish Cake", description="Crispy on the outside, soft inside", price=5.49, type="side", picture="path/to/picture307"),
    MenuItem(restaurant_id=8, menu_id=8, name="Stuffed Chili Peppers", description="With shrimp paste", price=5.99, type="side", picture="path/to/picture308"),
    MenuItem(restaurant_id=8, menu_id=8, name="Sweet Soy Sauce Noodles", description="With scallions and bean sprouts", price=5.29, type="side", picture="path/to/picture309"),
    MenuItem(restaurant_id=8, menu_id=8, name="Turnip Cake", description="Steamed and pan-fried", price=5.49, type="side", picture="path/to/picture310"),
]
r8_desserts = [
    MenuItem(restaurant_id=8, menu_id=8, name="Egg Tart", description="Creamy egg custard in flaky crust", price=4.49, type="dessert", picture="path/to/picture311"),
    MenuItem(restaurant_id=8, menu_id=8, name="Mango Pudding", description="Smooth mango-flavored dessert", price=4.29, type="dessert", picture="path/to/picture312"),
    MenuItem(restaurant_id=8, menu_id=8, name="Red Bean Soup", description="Sweet soup with lotus seeds", price=3.99, type="dessert", picture="path/to/picture313"),
    MenuItem(restaurant_id=8, menu_id=8, name="Black Sesame Roll", description="Sweet sesame jelly roll", price=4.29, type="dessert", picture="path/to/picture314"),
    MenuItem(restaurant_id=8, menu_id=8, name="Durian Pastry", description="With rich durian filling", price=4.99, type="dessert", picture="path/to/picture315"),
    MenuItem(restaurant_id=8, menu_id=8, name="Almond Jelly", description="With fruit cocktail", price=3.99, type="dessert", picture="path/to/picture316"),
    MenuItem(restaurant_id=8, menu_id=8, name="Coconut Pudding", description="Smooth coconut-flavored dessert", price=4.29, type="dessert", picture="path/to/picture317"),
    MenuItem(restaurant_id=8, menu_id=8, name="Sweet Rice Ball", description="Stuffed with sesame or red bean", price=4.49, type="dessert", picture="path/to/picture318"),
    MenuItem(restaurant_id=8, menu_id=8, name="Steamed Egg Cake", description="Soft and fluffy cake", price=4.29, type="dessert", picture="path/to/picture319"),
    MenuItem(restaurant_id=8, menu_id=8, name="Osmanthus Jelly", description="With wolfberries", price=4.49, type="dessert", picture="path/to/picture320"),
]
# Restaurant 9
r9_entrees = [
    MenuItem(restaurant_id=8, menu_id=8, name="Moussaka", description="Layered eggplant, potato, and spiced meat", price=16.99, type="entree", picture="path/to/picture321"),
    MenuItem(restaurant_id=8, menu_id=8, name="Spanakopita", description="Spinach pie with feta cheese", price=12.99, type="entree", picture="path/to/picture322"),
    MenuItem(restaurant_id=8, menu_id=8, name="Gyro Plate", description="Sliced rotisserie meat with tzatziki", price=13.99, type="entree", picture="path/to/picture323"),
    MenuItem(restaurant_id=8, menu_id=8, name="Stuffed Grape Leaves", description="Rice and herb-stuffed leaves", price=11.99, type="entree", picture="path/to/picture324"),
    MenuItem(restaurant_id=8, menu_id=8, name="Pastitsio", description="Greek lasagna with béchamel sauce", price=14.99, type="entree", picture="path/to/picture325"),
    MenuItem(restaurant_id=8, menu_id=8, name="Lamb Souvlaki", description="Grilled lamb skewers", price=15.99, type="entree", picture="path/to/picture326"),
    MenuItem(restaurant_id=8, menu_id=8, name="Baked Feta", description="Feta cheese in tomato sauce", price=9.99, type="entree", picture="path/to/picture327"),
    MenuItem(restaurant_id=8, menu_id=8, name="Greek Salad", description="Olives, tomatoes, cucumber, and feta", price=10.99, type="entree", picture="path/to/picture328"),
    MenuItem(restaurant_id=8, menu_id=8, name="Chicken Kebab", description="Marinated chicken skewers", price=13.99, type="entree", picture="path/to/picture329"),
    MenuItem(restaurant_id=8, menu_id=8, name="Grilled Octopus", description="With olive oil and oregano", price=17.99, type="entree", picture="path/to/picture330"),
]
r9_drinks = [
    MenuItem(restaurant_id=8, menu_id=8, name="Greek Coffee", description="Strong brewed coffee", price=3.49, type="drink", picture="path/to/picture331"),
    MenuItem(restaurant_id=8, menu_id=8, name="Ouzo", description="Anise-flavored liquor", price=5.99, type="drink", picture="path/to/picture332"),
    MenuItem(restaurant_id=8, menu_id=8, name="Retsina", description="Pine-resinated wine", price=5.49, type="drink", picture="path/to/picture333"),
    MenuItem(restaurant_id=8, menu_id=8, name="Mythos Beer", description="Popular Greek beer", price=4.99, type="drink", picture="path/to/picture334"),
    MenuItem(restaurant_id=8, menu_id=8, name="Tetmosol Lemonade", description="Refreshing lemonade", price=3.99, type="drink", picture="path/to/picture335"),
    MenuItem(restaurant_id=8, menu_id=8, name="Mastiha Liqueur", description="From the island of Chios", price=6.99, type="drink", picture="path/to/picture336"),
    MenuItem(restaurant_id=8, menu_id=8, name="Aegean Spritz", description="Bubbly cocktail with Mastiha", price=7.99, type="drink", picture="path/to/picture337"),
    MenuItem(restaurant_id=8, menu_id=8, name="Rose Wine", description="Crisp and aromatic", price=5.49, type="drink", picture="path/to/picture338"),
    MenuItem(restaurant_id=8, menu_id=8, name="Iced Tea", description="Chilled herbal tea", price=3.49, type="drink", picture="path/to/picture339"),
    MenuItem(restaurant_id=8, menu_id=8, name="Frappe", description="Greek iced coffee", price=4.29, type="drink", picture="path/to/picture340"),
]
r9_sides = [
    MenuItem(restaurant_id=8, menu_id=8, name="Tzatziki", description="Yogurt, cucumber, and garlic dip", price=4.99, type="side", picture="path/to/picture341"),
    MenuItem(restaurant_id=8, menu_id=8, name="Olives & Feta", description="Marinated in olive oil", price=5.49, type="side", picture="path/to/picture342"),
    MenuItem(restaurant_id=8, menu_id=8, name="Roasted Vegetables", description="With Greek herbs", price=5.29, type="side", picture="path/to/picture343"),
    MenuItem(restaurant_id=8, menu_id=8, name="Pita Bread", description="Warm and soft", price=3.99, type="side", picture="path/to/picture344"),
    MenuItem(restaurant_id=8, menu_id=8, name="Fava Dip", description="Yellow split pea puree", price=4.99, type="side", picture="path/to/picture345"),
    MenuItem(restaurant_id=8, menu_id=8, name="Horiatiki Salad", description="Classic Greek salad", price=5.99, type="side", picture="path/to/picture346"),
    MenuItem(restaurant_id=8, menu_id=8, name="Hummus", description="Creamy chickpea dip", price=4.99, type="side", picture="path/to/picture347"),
    MenuItem(restaurant_id=8, menu_id=8, name="Dolmadakia", description="Stuffed grape leaves", price=5.49, type="side", picture="path/to/picture348"),
    MenuItem(restaurant_id=8, menu_id=8, name="Gigantes Beans", description="In tomato sauce", price=5.29, type="side", picture="path/to/picture349"),
    MenuItem(restaurant_id=8, menu_id=8, name="Baked Eggplant", description="With tomato and feta", price=5.49, type="side", picture="path/to/picture350"),
]
r9_desserts = [
    MenuItem(restaurant_id=8, menu_id=8, name="Baklava", description="Layered pastry with nuts and honey", price=4.99, type="dessert", picture="path/to/picture351"),
    MenuItem(restaurant_id=8, menu_id=8, name="Loukoumades", description="Honey-soaked doughnuts", price=4.79, type="dessert", picture="path/to/picture352"),
    MenuItem(restaurant_id=8, menu_id=8, name="Galaktoboureko", description="Custard-filled pastry", price=4.49, type="dessert", picture="path/to/picture353"),
    MenuItem(restaurant_id=8, menu_id=8, name="Kourabiedes", description="Buttery almond cookies", price=4.29, type="dessert", picture="path/to/picture354"),
    MenuItem(restaurant_id=8, menu_id=8, name="Rizogalo", description="Greek rice pudding", price=4.49, type="dessert", picture="path/to/picture355"),
    MenuItem(restaurant_id=8, menu_id=8, name="Tavuk Göğsü", description="Chicken breast pudding", price=5.49, type="dessert", picture="path/to/picture356"),
    MenuItem(restaurant_id=8, menu_id=8, name="Melomakarona", description="Spiced cookies with syrup", price=4.29, type="dessert", picture="path/to/picture357"),
    MenuItem(restaurant_id=8, menu_id=8, name="Ekmek Kataifi", description="Shredded pastry with custard", price=4.79, type="dessert", picture="path/to/picture358"),
    MenuItem(restaurant_id=8, menu_id=8, name="Halva", description="Sweet semolina pudding", price=4.29, type="dessert", picture="path/to/picture359"),
    MenuItem(restaurant_id=8, menu_id=8, name="Yogurt with Honey", description="Thick yogurt with walnuts", price=4.49, type="dessert", picture="path/to/picture360"),
]
#Rstaurant 10
r10_entrees = [
    MenuItem(restaurant_id=10, menu_id=10, name="Dark Knight Burger", description="Gotham's finest beef patty", price=14.99, type="entree", picture="path/to/dark_knight_burger"),
    MenuItem(restaurant_id=10, menu_id=10, name="Batarang Steak", description="Sizzling steak with a side of justice", price=19.99, type="entree", picture="path/to/batarang_steak"),
    MenuItem(restaurant_id=10, menu_id=10, name="Gotham City Pizza", description="Loaded with crime-fighting toppings", price=16.99, type="entree", picture="path/to/gotham_pizza"),
    MenuItem(restaurant_id=10, menu_id=10, name="Batwing BBQ Ribs", description="Fall-off-the-bone ribs", price=18.99, type="entree", picture="path/to/batwing_ribs"),
    MenuItem(restaurant_id=10, menu_id=10, name="Bat-Salad", description="Fresh greens with a heroic twist", price=10.99, type="entree", picture="path/to/bat_salad"),
    MenuItem(restaurant_id=10, menu_id=10, name="Arkham Asparagus", description="Grilled asparagus spears", price=8.99, type="entree", picture="path/to/arkham_asparagus"),
    MenuItem(restaurant_id=10, menu_id=10, name="Catwoman's Pasta", description="Penne pasta with a mysterious sauce", price=12.99, type="entree", picture="path/to/catwoman_pasta"),
    MenuItem(restaurant_id=10, menu_id=10, name="Joker's Jackfruit Tacos", description="Vegan tacos with a twist", price=13.99, type="entree", picture="path/to/jokers_tacos"),
    MenuItem(restaurant_id=10, menu_id=10, name="Penguin's Poutine", description="A Canadian delicacy with a villainous touch", price=15.99, type="entree", picture="path/to/penguins_poutine"),
    MenuItem(restaurant_id=10, menu_id=10, name="Harley's Hot Wings", description="Spicy wings with a hint of chaos", price=11.99, type="entree", picture="path/to/harleys_wings"),
]
r10_drinks = [
    MenuItem(restaurant_id=10, menu_id=10, name="Batmobile Brew", description="Dark and bold coffee", price=3.99, type="drink", picture="path/to/batmobile_brew"),
    MenuItem(restaurant_id=10, menu_id=10, name="Gotham Goblet", description="Mysterious red wine", price=7.99, type="drink", picture="path/to/gotham_goblet"),
    MenuItem(restaurant_id=10, menu_id=10, name="Bat-Signal Smoothie", description="Healthy and heroic", price=5.99, type="drink", picture="path/to/bat_signal_smoothie"),
    MenuItem(restaurant_id=10, menu_id=10, name="Justice Juice", description="Blended fruit goodness", price=4.99, type="drink", picture="path/to/justice_juice"),
    MenuItem(restaurant_id=10, menu_id=10, name="Vigilante Vodka", description="For the daring", price=8.99, type="drink", picture="path/to/vigilante_vodka"),
    MenuItem(restaurant_id=10, menu_id=10, name="Batcave Brew", description="Craft beer from the depths", price=6.99, type="drink", picture="path/to/batcave_brew"),
    MenuItem(restaurant_id=10, menu_id=10, name="Batwoman's Brew", description="A coffee with a feminine kick", price=4.79, type="drink", picture="path/to/batwomans_brew"),
    MenuItem(restaurant_id=10, menu_id=10, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
    MenuItem(restaurant_id=10, menu_id=10, name="Alfred's Elixir", description="A refined drink for the butler in you", price=6.49, type="drink", picture="path/to/alfreds_elixir"),
    MenuItem(restaurant_id=10, menu_id=10, name="Justice Juice", description="A heroic concoction", price=6.49, type="drink", picture="path/to/justice_juice"),
]
r10_sides = [
    MenuItem(restaurant_id=10, menu_id=10, name="Wayne Manor Fries", description="Crispy and golden", price=4.99, type="side", picture="path/to/wayne_fries"),
    MenuItem(restaurant_id=10, menu_id=10, name="Joker's Slaw", description="Colorful coleslaw", price=3.99, type="side", picture="path/to/joker_slaw"),
    MenuItem(restaurant_id=10, menu_id=10, name="Two-Face Taters", description="Mashed with a twist", price=5.99, type="side", picture="path/to/two_face_taters"),
    MenuItem(restaurant_id=10, menu_id=10, name="Bat-Broccoli", description="Steamed to perfection", price=4.49, type="side", picture="path/to/bat_broccoli"),
    MenuItem(restaurant_id=10, menu_id=10, name="Gotham Greens", description="Sautéed spinach and kale", price=5.49, type="side", picture="path/to/gotham_greens"),
    MenuItem(restaurant_id=10, menu_id=10, name="Riddler's Riddles", description="Crispy riddle-themed snacks", price=4.99, type="side", picture="path/to/riddlers_riddles"),
    MenuItem(restaurant_id=10, menu_id=10, name="Batgirl's Bruschetta", description="A bite-sized hero", price=4.99, type="side", picture="path/to/batgirls_bruschetta"),
    MenuItem(restaurant_id=10, menu_id=10, name="Bane's Broccoli Rabe", description="A side that'll break your back", price=5.99, type="side", picture="path/to/banes_broccoli_rabe"),
    MenuItem(restaurant_id=10, menu_id=10, name="Penguin's Potato Wedges", description="Crispy and villainous", price=4.99, type="side", picture="path/to/penguins_wedges"),
    MenuItem(restaurant_id=10, menu_id=10, name="Harvey's Hash Browns", description="Two-Face-approved potatoes", price=5.49, type="side", picture="path/to/harveys_hash_browns"),
]
r10_desserts = [
    MenuItem(restaurant_id=10, menu_id=10, name="Dark Knight Delight", description="Decadent chocolate cake", price=7.99, type="dessert", picture="path/to/dark_knight_cake"),
    MenuItem(restaurant_id=10, menu_id=10, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=10, menu_id=10, name="Robin's Apple Pie", description="A classic favorite", price=6.49, type="dessert", picture="path/to/robin_pie"),
    MenuItem(restaurant_id=10, menu_id=10, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=10, menu_id=10, name="Riddler's Pudding", description="A puzzling treat", price=5.99, type="dessert", picture="path/to/riddler_pudding"),
    MenuItem(restaurant_id=10, menu_id=10, name="Catwoman's Cannoli", description="Crunchy pastry with a hidden agenda", price=7.49, type="dessert", picture="path/to/catwomans_cannoli"),
    MenuItem(restaurant_id=10, menu_id=10, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=6.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=10, menu_id=10, name="Penguin's Profiteroles", description="Cream puffs with a chilly twist", price=7.99, type="dessert", picture="path/to/penguins_profiteroles"),
    MenuItem(restaurant_id=10, menu_id=10, name="Batgirl's Brownie", description="A chocolatey vigilante", price=7.49, type="dessert", picture="path/to/batgirls_brownie"),
    MenuItem(restaurant_id=10, menu_id=10, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
]
# Restaurant 11
r11_entrees = [
    MenuItem(restaurant_id=11, menu_id=11, name="Batcave Burger", description="Secret recipe beef patty", price=15.99, type="entree", picture="path/to/batcave_burger"),
    MenuItem(restaurant_id=11, menu_id=11, name="Joker's Pizza", description="Wild and unpredictable toppings", price=17.99, type="entree", picture="path/to/jokers_pizza"),
    MenuItem(restaurant_id=11, menu_id=11, name="Harley Quinn's Spaghetti", description="Twisted pasta with a side of mayhem", price=13.99, type="entree", picture="path/to/harley_spaghetti"),
    MenuItem(restaurant_id=11, menu_id=11, name="Riddler's Ribs", description="A riddle in every bite", price=18.99, type="entree", picture="path/to/riddler_ribs"),
    MenuItem(restaurant_id=11, menu_id=11, name="Penguin's Pastrami", description="Smoked to villainous perfection", price=16.99, type="entree", picture="path/to/penguin_pastrami"),
    MenuItem(restaurant_id=11, menu_id=11, name="Catwoman's Crepe", description="Thin and stealthy", price=14.99, type="entree", picture="path/to/catwoman_crepe"),
    MenuItem(restaurant_id=11, menu_id=11, name="Bane's Burrito", description="A hearty and powerful meal", price=19.99, type="entree", picture="path/to/banes_burrito"),
    MenuItem(restaurant_id=11, menu_id=11, name="Poison Ivy's Salad", description="A green delight with a hint of danger", price=11.99, type="entree", picture="path/to/poison_ivy_salad"),
    MenuItem(restaurant_id=11, menu_id=11, name="Mad Hatter's Mac 'n' Cheese", description="A whimsical comfort food", price=12.99, type="entree", picture="path/to/mad_hatters_mac"),
    MenuItem(restaurant_id=11, menu_id=11, name="Scarecrow's Stir-Fry", description="Fearfully flavorful", price=16.49, type="entree", picture="path/to/scarecrow_stirfry"),
]
r11_drinks = [
    MenuItem(restaurant_id=11, menu_id=11, name="Gotham Gazette Coffee", description="News-worthy caffeine", price=4.49, type="drink", picture="path/to/gotham_coffee"),
    MenuItem(restaurant_id=11, menu_id=11, name="Penguin's Pinot", description="A fine and fancy wine", price=9.99, type="drink", picture="path/to/penguin_pinot"),
    MenuItem(restaurant_id=11, menu_id=11, name="Bane's Brew", description="A powerful energy drink", price=5.99, type="drink", picture="path/to/banes_brew"),
    MenuItem(restaurant_id=11, menu_id=11, name="Joker's Julep", description="A twist of madness in a glass", price=6.99, type="drink", picture="path/to/jokers_julep"),
    MenuItem(restaurant_id=11, menu_id=11, name="Riddler's Refreshment", description="A puzzling thirst quencher", price=4.99, type="drink", picture="path/to/riddlers_refreshment"),
    MenuItem(restaurant_id=11, menu_id=11, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=11, menu_id=11, name="Two-Face's Tea", description="A dual-flavored delight", price=3.99, type="drink", picture="path/to/two_faces_tea"),
    MenuItem(restaurant_id=11, menu_id=11, name="Penguin's Punch", description="Chilled and villainous", price=5.99, type="drink", picture="path/to/penguins_punch"),
    MenuItem(restaurant_id=11, menu_id=11, name="Harley's Hot Chocolate", description="Sweet with a touch of insanity", price=4.49, type="drink", picture="path/to/harleys_hot_chocolate"),
    MenuItem(restaurant_id=11, menu_id=11, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
]
r11_sides = [
    MenuItem(restaurant_id=11, menu_id=11, name="Gotham Grits", description="Creamy and comforting", price=5.49, type="side", picture="path/to/gotham_grits"),
    MenuItem(restaurant_id=11, menu_id=11, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=11, menu_id=11, name="Poison Ivy's Potato Salad", description="Potato salad with a botanical twist", price=5.99, type="side", picture="path/to/poison_ivy_potatosalad"),
    MenuItem(restaurant_id=11, menu_id=11, name="Mad Hatter's Mushrooms", description="A whimsical side of sautéed mushrooms", price=4.99, type="side", picture="path/to/mad_hatters_mushrooms"),
    MenuItem(restaurant_id=11, menu_id=11, name="Riddler's Rice", description="A side that'll leave you guessing", price=5.29, type="side", picture="path/to/riddlers_rice"),
    MenuItem(restaurant_id=11, menu_id=11, name="Harley's Hash Browns", description="Crispy potatoes with a hint of chaos", price=4.49, type="side", picture="path/to/harleys_hashbrowns"),
    MenuItem(restaurant_id=11, menu_id=11, name="Joker's Jalapeño Poppers", description="Fiery and unpredictable", price=5.49, type="side", picture="path/to/jokers_poppers"),
    MenuItem(restaurant_id=11, menu_id=11, name="Penguin's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/penguins_polenta"),
    MenuItem(restaurant_id=11, menu_id=11, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=11, menu_id=11, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
]
r11_desserts = [
    MenuItem(restaurant_id=11, menu_id=11, name="Arkham Apple Pie", description="Madly good", price=7.49, type="dessert", picture="path/to/arkham_pie"),
    MenuItem(restaurant_id=11, menu_id=11, name="Two-Face Tiramisu", description="A dessert with a twist", price=6.99, type="dessert", picture="path/to/two_face_tiramisu"),
    MenuItem(restaurant_id=11, menu_id=11, name="Riddler's Raspberry Tart", description="A tart to perplex your taste buds", price=7.99, type="dessert", picture="path/to/riddlers_tart"),
    MenuItem(restaurant_id=11, menu_id=11, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=11, menu_id=11, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=11, menu_id=11, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=11, menu_id=11, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=6.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=11, menu_id=11, name="Harley's Hot Fudge Sundae", description="A dangerously delightful sundae", price=7.99, type="dessert", picture="path/to/harleys_sundae"),
    MenuItem(restaurant_id=11, menu_id=11, name="Penguin's Profiteroles", description="Cream puffs with a chilly twist", price=7.99, type="dessert", picture="path/to/penguins_profiteroles"),
    MenuItem(restaurant_id=11, menu_id=11, name="Mad Hatter's Muffin", description="A whimsical muffin to finish your meal", price=4.99, type="dessert", picture="path/to/mad_hatters_muffin"),
]
# Restaurant 12
r12_entrees = [
    MenuItem(restaurant_id=12, menu_id=12, name="Gotham Grilled Cheese", description="Melted goodness on toasted bat-bread", price=13.99, type="entree", picture="path/to/gotham_grilled_cheese"),
    MenuItem(restaurant_id=12, menu_id=12, name="Batwing Beef Tacos", description="Savory beef in bat-tortillas", price=16.99, type="entree", picture="path/to/batwing_tacos"),
    MenuItem(restaurant_id=12, menu_id=12, name="Penguin's Pizza", description="Toppings that'll flip you", price=14.99, type="entree", picture="path/to/penguins_pizza"),
    MenuItem(restaurant_id=12, menu_id=12, name="Joker's Jambalaya", description="A wild mix of flavors", price=15.99, type="entree", picture="path/to/jokers_jambalaya"),
    MenuItem(restaurant_id=12, menu_id=12, name="Riddler's Ravioli", description="Pasta filled with enigma", price=17.99, type="entree", picture="path/to/riddlers_ravioli"),
    MenuItem(restaurant_id=12, menu_id=12, name="Harley's Hot Dogs", description="A playful twist on a classic", price=12.99, type="entree", picture="path/to/harleys_hotdogs"),
    MenuItem(restaurant_id=12, menu_id=12, name="Two-Face Tofu Stir-Fry", description="A dual-flavored delight for vegetarians", price=14.49, type="entree", picture="path/to/two_face_stirfry"),
    MenuItem(restaurant_id=12, menu_id=12, name="Catwoman's Calzone", description="Stuffed with stealthy ingredients", price=16.49, type="entree", picture="path/to/catwomans_calzone"),
    MenuItem(restaurant_id=12, menu_id=12, name="Bane's BBQ Brisket", description="Smoked to villainous perfection", price=19.99, type="entree", picture="path/to/banes_brisket"),
    MenuItem(restaurant_id=12, menu_id=12, name="Poison Ivy's Pasta Salad", description="A green delight with a touch of nature", price=12.99, type="entree", picture="path/to/poison_ivy_pasta"),
]
r12_drinks = [
    MenuItem(restaurant_id=12, menu_id=12, name="Batwing Brew", description="Dark and bold coffee", price=3.99, type="drink", picture="path/to/batwing_brew"),
    MenuItem(restaurant_id=12, menu_id=12, name="Gotham Goblet", description="Mysterious red wine", price=7.99, type="drink", picture="path/to/gotham_goblet"),
    MenuItem(restaurant_id=12, menu_id=12, name="Bat-Signal Smoothie", description="Healthy and heroic", price=5.99, type="drink", picture="path/to/bat_signal_smoothie"),
    MenuItem(restaurant_id=12, menu_id=12, name="Justice Juice", description="Blended fruit goodness", price=4.99, type="drink", picture="path/to/justice_juice"),
    MenuItem(restaurant_id=12, menu_id=12, name="Vigilante Vodka", description="For the daring", price=8.99, type="drink", picture="path/to/vigilante_vodka"),
    MenuItem(restaurant_id=12, menu_id=12, name="Batcave Brew", description="Craft beer from the depths", price=6.99, type="drink", picture="path/to/batcave_brew"),
    MenuItem(restaurant_id=12, menu_id=12, name="Bat-Brewed Tea", description="A unique blend from Batman's collection", price=4.49, type="drink", picture="path/to/bat_brewed_tea"),
    MenuItem(restaurant_id=12, menu_id=12, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
    MenuItem(restaurant_id=12, menu_id=12, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=12, menu_id=12, name="Two-Face's Tea", description="A dual-flavored delight", price=3.99, type="drink", picture="path/to/two_faces_tea"),
]
r12_sides = [
    MenuItem(restaurant_id=12, menu_id=12, name="Wayne Manor Fries", description="Crispy and golden", price=4.99, type="side", picture="path/to/wayne_fries"),
    MenuItem(restaurant_id=12, menu_id=12, name="Joker's Slaw", description="Colorful coleslaw", price=3.99, type="side", picture="path/to/joker_slaw"),
    MenuItem(restaurant_id=12, menu_id=12, name="Two-Face Taters", description="Mashed with a twist", price=5.99, type="side", picture="path/to/two_face_taters"),
    MenuItem(restaurant_id=12, menu_id=12, name="Bat-Broccoli", description="Steamed to perfection", price=4.49, type="side", picture="path/to/bat_broccoli"),
    MenuItem(restaurant_id=12, menu_id=12, name="Gotham Greens", description="Sautéed spinach and kale", price=5.49, type="side", picture="path/to/gotham_greens"),
    MenuItem(restaurant_id=12, menu_id=12, name="Penguin's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/penguins_polenta"),
    MenuItem(restaurant_id=12, menu_id=12, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=12, menu_id=12, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=12, menu_id=12, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_pilaf"),
    MenuItem(restaurant_id=12, menu_id=12, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
]
r12_desserts = [
    MenuItem(restaurant_id=12, menu_id=12, name="Dark Knight Delight", description="Decadent chocolate cake", price=7.99, type="dessert", picture="path/to/dark_knight_cake"),
    MenuItem(restaurant_id=12, menu_id=12, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=12, menu_id=12, name="Robin's Apple Pie", description="A classic favorite", price=6.49, type="dessert", picture="path/to/robin_pie"),
    MenuItem(restaurant_id=12, menu_id=12, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=12, menu_id=12, name="Riddler's Raspberry Tart", description="A tart to perplex your taste buds", price=7.99, type="dessert", picture="path/to/riddlers_tart"),
    MenuItem(restaurant_id=12, menu_id=12, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=12, menu_id=12, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=12, menu_id=12, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=12, menu_id=12, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=6.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=12, menu_id=12, name="Harley's Hot Fudge Sundae", description="A dangerously delightful sundae", price=7.99, type="dessert", picture="path/to/harleys_sundae"),
]
# Restaurant 13
r13_entrees = [
    MenuItem(restaurant_id=13, menu_id=13, name="Batmobile Burger", description="High-speed beef patty", price=15.99, type="entree", picture="path/to/batmobile_burger"),
    MenuItem(restaurant_id=13, menu_id=13, name="Penguin's Poutine", description="A villainous twist on a classic", price=17.99, type="entree", picture="path/to/penguins_poutine"),
    MenuItem(restaurant_id=13, menu_id=13, name="Robin's Risotto", description="Sidekick-approved dish", price=13.99, type="entree", picture="path/to/robins_risotto"),
    MenuItem(restaurant_id=13, menu_id=13, name="Poison Ivy's Salad", description="Fresh and dangerously good", price=11.99, type="entree", picture="path/to/poison_ivys_salad"),
    MenuItem(restaurant_id=13, menu_id=13, name="Harley's Hot Dogs", description="A playful twist on a classic", price=12.99, type="entree", picture="path/to/harleys_hotdogs"),
    MenuItem(restaurant_id=13, menu_id=13, name="Riddler's Ravioli", description="Pasta filled with enigma", price=17.99, type="entree", picture="path/to/riddlers_ravioli"),
    MenuItem(restaurant_id=13, menu_id=13, name="Catwoman's Calzone", description="Stuffed with stealthy ingredients", price=16.49, type="entree", picture="path/to/catwomans_calzone"),
    MenuItem(restaurant_id=13, menu_id=13, name="Bane's BBQ Brisket", description="Smoked to villainous perfection", price=19.99, type="entree", picture="path/to/banes_brisket"),
    MenuItem(restaurant_id=13, menu_id=13, name="Two-Face Tofu Stir-Fry", description="A dual-flavored delight for vegetarians", price=14.49, type="entree", picture="path/to/two_face_stirfry"),
    MenuItem(restaurant_id=13, menu_id=13, name="Gotham Grilled Cheese", description="Melted goodness on toasted bat-bread", price=13.99, type="entree", picture="path/to/gotham_grilled_cheese"),
]
r13_drinks = [
    MenuItem(restaurant_id=13, menu_id=13, name="Gotham Gazette Coffee", description="News-worthy caffeine", price=4.49, type="drink", picture="path/to/gotham_coffee"),
    MenuItem(restaurant_id=13, menu_id=13, name="Joker's Juice", description="A laughably good drink", price=5.99, type="drink", picture="path/to/jokers_juice"),
    MenuItem(restaurant_id=13, menu_id=13, name="Catwoman's Cabernet", description="A wine that purrs", price=9.99, type="drink", picture="path/to/catwomans_cabernet"),
    MenuItem(restaurant_id=13, menu_id=13, name="Penguin's Pinot", description="A fine and fancy wine", price=9.99, type="drink", picture="path/to/penguin_pinot"),
    MenuItem(restaurant_id=13, menu_id=13, name="Vigilante Vodka", description="For the daring", price=8.99, type="drink", picture="path/to/vigilante_vodka"),
    MenuItem(restaurant_id=13, menu_id=13, name="Batcave Brew", description="Craft beer from the depths", price=6.99, type="drink", picture="path/to/batcave_brew"),
    MenuItem(restaurant_id=13, menu_id=13, name="Bat-Brewed Tea", description="A unique blend from Batman's collection", price=4.49, type="drink", picture="path/to/bat_brewed_tea"),
    MenuItem(restaurant_id=13, menu_id=13, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
    MenuItem(restaurant_id=13, menu_id=13, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=13, menu_id=13, name="Riddler's Refreshment", description="A drink that poses questions", price=4.99, type="drink", picture="path/to/riddlers_refreshment"),
]
r13_sides = [
    MenuItem(restaurant_id=13, menu_id=13, name="Gotham Grits", description="Creamy and comforting", price=5.49, type="side", picture="path/to/gotham_grits"),
    MenuItem(restaurant_id=13, menu_id=13, name="Riddler's Rice", description="A side dish full of questions", price=4.99, type="side", picture="path/to/riddler_rice"),
    MenuItem(restaurant_id=13, menu_id=13, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hashbrowns"),
    MenuItem(restaurant_id=13, menu_id=13, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=13, menu_id=13, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=13, menu_id=13, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=13, menu_id=13, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_pilaf"),
    MenuItem(restaurant_id=13, menu_id=13, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
    MenuItem(restaurant_id=13, menu_id=13, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_salad"),
    MenuItem(restaurant_id=13, menu_id=13, name="Two-Face Taters", description="Mashed with a twist", price=5.99, type="side", picture="path/to/two_face_taters"),
]
r13_desserts = [
    MenuItem(restaurant_id=13, menu_id=13, name="Arkham Apple Pie", description="Madly good", price=7.49, type="dessert", picture="path/to/arkham_pie"),
    MenuItem(restaurant_id=13, menu_id=13, name="Two-Face Tiramisu", description="A dessert with a twist", price=6.99, type="dessert", picture="path/to/two_face_tiramisu"),
    MenuItem(restaurant_id=13, menu_id=13, name="Catwoman's Chocolate Cake", description="Rich and decadent", price=8.49, type="dessert", picture="path/to/catwomans_cake"),
    MenuItem(restaurant_id=13, menu_id=13, name="Penguin's Parfait", description="Chilled and calculating", price=7.99, type="dessert", picture="path/to/penguins_parfait"),
    MenuItem(restaurant_id=13, menu_id=13, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_brownie"),
    MenuItem(restaurant_id=13, menu_id=13, name="Riddler's Raspberry Tart", description="A tart to perplex your taste buds", price=7.99, type="dessert", picture="path/to/riddlers_tart"),
    MenuItem(restaurant_id=13, menu_id=13, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=13, menu_id=13, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=13, menu_id=13, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=13, menu_id=13, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=6.99, type="dessert", picture="path/to/Poison_Ivy_Parfait"),
]
# Restaurant 14
r14_entrees = [
    MenuItem(restaurant_id=14, menu_id=14, name="Batcave Burger", description="Secret recipe beef patty", price=15.99, type="entree", picture="path/to/batcave_burger"),
    MenuItem(restaurant_id=14, menu_id=14, name="Joker's Pizza", description="Wild and unpredictable toppings", price=17.99, type="entree", picture="path/to/jokers_pizza"),
    MenuItem(restaurant_id=14, menu_id=14, name="Harley Quinn's Spaghetti", description="Twisted pasta with a side of mayhem", price=13.99, type="entree", picture="path/to/harley_spaghetti"),
    MenuItem(restaurant_id=14, menu_id=14, name="Riddler's Ribs", description="A riddle in every bite", price=18.99, type="entree", picture="path/to/riddler_ribs"),
    MenuItem(restaurant_id=14, menu_id=14, name="Catwoman's Carbonara", description="Seductively creamy pasta", price=16.99, type="entree", picture="path/to/catwoman_carbonara"),
    MenuItem(restaurant_id=14, menu_id=14, name="Mr. Freeze's Filet Mignon", description="Ice-cold perfection", price=22.99, type="entree", picture="path/to/mr_freeze_filet"),
    MenuItem(restaurant_id=14, menu_id=14, name="Bane's BBQ Brisket", description="Smoked to villainous perfection", price=19.99, type="entree", picture="path/to/banes_brisket"),
    MenuItem(restaurant_id=14, menu_id=14, name="Penguin's Pepperoni Pasta", description="Pasta with a sinister twist", price=15.99, type="entree", picture="path/to/penguins_pasta"),
    MenuItem(restaurant_id=14, menu_id=14, name="Poison Ivy's Pappardelle", description="Freshly picked herb-infused pasta", price=16.99, type="entree", picture="path/to/poison_ivys_pappardelle"),
    MenuItem(restaurant_id=14, menu_id=14, name="Two-Face Tofu Stir-Fry", description="A dual-flavored delight for vegetarians", price=14.49, type="entree", picture="path/to/two_face_stirfry"),
]
r14_drinks = [
    MenuItem(restaurant_id=14, menu_id=14, name="Gotham Gazette Coffee", description="News-worthy caffeine", price=4.49, type="drink", picture="path/to/gotham_coffee"),
    MenuItem(restaurant_id=14, menu_id=14, name="Penguin's Pinot", description="A fine and fancy wine", price=9.99, type="drink", picture="path/to/penguin_pinot"),
    MenuItem(restaurant_id=14, menu_id=14, name="Bane's Brew", description="A powerful energy drink", price=5.99, type="drink", picture="path/to/banes_brew"),
    MenuItem(restaurant_id=14, menu_id=14, name="Joker's Julep", description="A laughably good drink", price=6.49, type="drink", picture="path/to/jokers_julep"),
    MenuItem(restaurant_id=14, menu_id=14, name="Harley's Hot Chocolate", description="Mischievously creamy", price=5.99, type="drink", picture="path/to/harleys_hot_chocolate"),
    MenuItem(restaurant_id=14, menu_id=14, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=14, menu_id=14, name="Riddler's Raspberry Soda", description="A fizzy enigma", price=4.99, type="drink", picture="path/to/riddlers_raspberry_soda"),
    MenuItem(restaurant_id=14, menu_id=14, name="Penguin's Pale Ale", description="A brew as cold as ice", price=6.99, type="drink", picture="path/to/penguins_pale_ale"),
    MenuItem(restaurant_id=14, menu_id=14, name="Two-Face Tea", description="A dual-flavored tea", price=4.99, type="drink", picture="path/to/two_face_tea"),
    MenuItem(restaurant_id=14, menu_id=14, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
]
r14_sides = [
    MenuItem(restaurant_id=14, menu_id=14, name="Gotham Grits", description="Creamy and comforting", price=5.49, type="side", picture="path/to/gotham_grits"),
    MenuItem(restaurant_id=14, menu_id=14, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=14, menu_id=14, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hashbrowns"),
    MenuItem(restaurant_id=14, menu_id=14, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=14, menu_id=14, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=14, menu_id=14, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=14, menu_id=14, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_pilaf"),
    MenuItem(restaurant_id=14, menu_id=14, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
    MenuItem(restaurant_id=14, menu_id=14, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_salad"),
    MenuItem(restaurant_id=14, menu_id=14, name="Two-Face Taters", description="Mashed with a twist", price=5.99, type="side", picture="path/to/two_face_taters"),
]
r14_desserts = [
    MenuItem(restaurant_id=14, menu_id=14, name="Arkham Apple Pie", description="Madly good", price=7.49, type="dessert", picture="path/to/arkham_pie"),
    MenuItem(restaurant_id=14, menu_id=14, name="Two-Face Tiramisu", description="A dessert with a twist", price=6.99, type="dessert", picture="path/to/two_face_tiramisu"),
    MenuItem(restaurant_id=14, menu_id=14, name="Catwoman's Chocolate Cake", description="Rich and decadent", price=8.49, type="dessert", picture="path/to/catwomans_cake"),
    MenuItem(restaurant_id=14, menu_id=14, name="Penguin's Parfait", description="Chilled and calculating", price=7.99, type="dessert", picture="path/to/penguins_parfait"),
    MenuItem(restaurant_id=14, menu_id=14, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_brownie"),
    MenuItem(restaurant_id=14, menu_id=14, name="Riddler's Raspberry Tart", description="A tart to perplex your taste buds", price=7.99, type="dessert", picture="path/to/riddlers_tart"),
    MenuItem(restaurant_id=14, menu_id=14, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=14, menu_id=14, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=14, menu_id=14, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=14, menu_id=14, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
]
# Restaurant 15
r15_entrees = [
    MenuItem(restaurant_id=15, menu_id=15, name="Dark Knight Burger", description="The hero Gotham deserves", price=15.99, type="entree", picture="path/to/dark_knight_burger"),
    MenuItem(restaurant_id=15, menu_id=15, name="Penguin's Pizza", description="Toppings as unpredictable as the villain", price=17.99, type="entree", picture="path/to/penguins_pizza"),
    MenuItem(restaurant_id=15, menu_id=15, name="Robin's Ravioli", description="A sidekick-approved pasta dish", price=13.99, type="entree", picture="path/to/robins_ravioli"),
    MenuItem(restaurant_id=15, menu_id=15, name="Poison Ivy's Greens", description="Fresh greens with a touch of danger", price=11.99, type="entree", picture="path/to/poison_ivys_greens"),
    MenuItem(restaurant_id=15, menu_id=15, name="Riddler's Roast Chicken", description="A meal full of riddles", price=16.99, type="entree", picture="path/to/riddlers_roast"),
    MenuItem(restaurant_id=15, menu_id=15, name="Two-Face T-Bone Steak", description="A dual-flavored steak", price=19.99, type="entree", picture="path/to/two_face_steak"),
    MenuItem(restaurant_id=15, menu_id=15, name="Catwoman's Carbonara", description="Seductively creamy pasta", price=16.99, type="entree", picture="path/to/catwomans_carbonara"),
    MenuItem(restaurant_id=15, menu_id=15, name="Mr. Freeze's Filet Mignon", description="Cold and perfectly cooked", price=22.99, type="entree", picture="path/to/mr_freeze_fillet"),
    MenuItem(restaurant_id=15, menu_id=15, name="Bane's BBQ Brisket", description="Smoked to villainous perfection", price=19.99, type="entree", picture="path/to/banes_brisket"),
    MenuItem(restaurant_id=15, menu_id=15, name="Harley's Hotdog", description="A mischievous twist on a classic", price=12.99, type="entree", picture="path/to/harleys_hotdog"),
]
r15_drinks = [
    MenuItem(restaurant_id=15, menu_id=15, name="Gotham Gazette Coffee", description="News-worthy caffeine", price=4.49, type="drink", picture="path/to/gotham_coffee"),
    MenuItem(restaurant_id=15, menu_id=15, name="Penguin's Pinot", description="A fine and fancy wine", price=9.99, type="drink", picture="path/to/penguin_pinot"),
    MenuItem(restaurant_id=15, menu_id=15, name="Bane's Brew", description="A powerful energy drink", price=5.99, type="drink", picture="path/to/banes_brew"),
    MenuItem(restaurant_id=15, menu_id=15, name="Joker's Julep", description="A laughably good drink", price=6.49, type="drink", picture="path/to/jokers_julep"),
    MenuItem(restaurant_id=15, menu_id=15, name="Harley's Hot Chocolate", description="Mischievously creamy", price=5.99, type="drink", picture="path/to/harleys_hot_chocolate"),
    MenuItem(restaurant_id=15, menu_id=15, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=15, menu_id=15, name="Riddler's Raspberry Soda", description="A fizzy enigma", price=4.99, type="drink", picture="path/to/riddlers_raspberry_soda"),
    MenuItem(restaurant_id=15, menu_id=15, name="Penguin's Pale Ale", description="A brew as cold as ice", price=6.99, type="drink", picture="path/to/penguins_pale_ale"),
    MenuItem(restaurant_id=15, menu_id=15, name="Two-Face Tea", description="A dual-flavored tea", price=4.99, type="drink", picture="path/to/two_face_tea"),
    MenuItem(restaurant_id=15, menu_id=15, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
]
r15_sides = [
    MenuItem(restaurant_id=15, menu_id=15, name="Gotham Grits", description="Creamy and comforting", price=5.49, type="side", picture="path/to/gotham_grits"),
    MenuItem(restaurant_id=15, menu_id=15, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=15, menu_id=15, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hashbrowns"),
    MenuItem(restaurant_id=15, menu_id=15, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=15, menu_id=15, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=15, menu_id=15, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=15, menu_id=15, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_pilaf"),
    MenuItem(restaurant_id=15, menu_id=15, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
    MenuItem(restaurant_id=15, menu_id=15, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_salad"),
    MenuItem(restaurant_id=15, menu_id=15, name="Two-Face Taters", description="Mashed with a twist", price=5.99, type="side", picture="path/to/two_face_taters"),
]
r15_desserts = [
    MenuItem(restaurant_id=15, menu_id=15, name="Batman's Brownie", description="The hero's favorite treat", price=7.49, type="dessert", picture="path/to/batmans_brownie"),
    MenuItem(restaurant_id=15, menu_id=15, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=15, menu_id=15, name="Alfred's Apple Pie", description="A classic in Wayne Manor", price=6.49, type="dessert", picture="path/to/alfreds_pie"),
    MenuItem(restaurant_id=15, menu_id=15, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=15, menu_id=15, name="Riddler's Riddle Cake", description="A cake that leaves you guessing", price=7.99, type="dessert", picture="path/to/riddlers_cake"),
    MenuItem(restaurant_id=15, menu_id=15, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=15, menu_id=15, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=15, menu_id=15, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=15, menu_id=15, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=15, menu_id=15, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_brownie"),
]
# Restaurant 16
r16_entrees = [
    MenuItem(restaurant_id=16, menu_id=16, name="Gotham Burger", description="A taste of the city's hero", price=14.99, type="entree", picture="path/to/gotham_burger"),
    MenuItem(restaurant_id=16, menu_id=16, name="Joker's Delight", description="Wild and unpredictable flavors", price=17.99, type="entree", picture="path/to/jokers_delight"),
    MenuItem(restaurant_id=16, menu_id=16, name="Batwing Pasta", description="Pasta with a heroic twist", price=13.99, type="entree", picture="path/to/batwing_pasta"),
    MenuItem(restaurant_id=16, menu_id=16, name="Riddler's Ribs", description="A riddle in every bite", price=18.99, type="entree", picture="path/to/riddlers_ribs"),
    MenuItem(restaurant_id=16, menu_id=16, name="Two-Face Tacos", description="Tacos with a dual flavor", price=15.99, type="entree", picture="path/to/two_face_tacos"),
    MenuItem(restaurant_id=16, menu_id=16, name="Catwoman's Carbonara", description="Seductively creamy pasta", price=16.99, type="entree", picture="path/to/catwomans_carbonara"),
    MenuItem(restaurant_id=16, menu_id=16, name="Mr. Freeze's Filet Mignon", description="Cold and perfectly cooked", price=22.99, type="entree", picture="path/to/mr_freezes_fillet"),
    MenuItem(restaurant_id=16, menu_id=16, name="Bane's BBQ Brisket", description="Smoked to villainous perfection", price=19.99, type="entree", picture="path/to/banes_bbq"),
    MenuItem(restaurant_id=16, menu_id=16, name="Harley's Hotdog", description="A mischievous twist on a classic", price=12.99, type="entree", picture="path/to/harleys_hotdog"),
    MenuItem(restaurant_id=16, menu_id=16, name="Penguin's Pizza", description="Toppings as unpredictable as the villain", price=17.99, type="entree", picture="path/to/penguins_pizza"),
]
r16_drinks = [
    MenuItem(restaurant_id=16, menu_id=16, name="Gotham Gazette Coffee", description="News-worthy caffeine", price=4.49, type="drink", picture="path/to/gotham_coffee"),
    MenuItem(restaurant_id=16, menu_id=16, name="Penguin's Pinot", description="A fine and fancy wine", price=9.99, type="drink", picture="path/to/penguin_pinot"),
    MenuItem(restaurant_id=16, menu_id=16, name="Bane's Brew", description="A powerful energy drink", price=5.99, type="drink", picture="path/to/banes_brew"),
    MenuItem(restaurant_id=16, menu_id=16, name="Joker's Julep", description="A laughably good drink", price=6.49, type="drink", picture="path/to/jokers_julep"),
    MenuItem(restaurant_id=16, menu_id=16, name="Harley's Hot Chocolate", description="Mischievously creamy", price=5.99, type="drink", picture="path/to/harleys_hot_chocolate"),
    MenuItem(restaurant_id=16, menu_id=16, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=16, menu_id=16, name="Riddler's Raspberry Soda", description="A fizzy enigma", price=4.99, type="drink", picture="path/to/riddlers_raspberry_soda"),
    MenuItem(restaurant_id=16, menu_id=16, name="Penguin's Pale Ale", description="A brew as cold as ice", price=6.99, type="drink", picture="path/to/penguins_pale_ale"),
    MenuItem(restaurant_id=16, menu_id=16, name="Two-Face Tea", description="A dual-flavored tea", price=4.99, type="drink", picture="path/to/two_face_tea"),
    MenuItem(restaurant_id=16, menu_id=16, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
]
r16_sides = [
    MenuItem(restaurant_id=16, menu_id=16, name="Gotham Grits", description="Creamy and comforting", price=5.49, type="side", picture="path/to/gotham_grits"),
    MenuItem(restaurant_id=16, menu_id=16, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=16, menu_id=16, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hashbrowns"),
    MenuItem(restaurant_id=16, menu_id=16, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=16, menu_id=16, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=16, menu_id=16, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=16, menu_id=16, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_pilaf"),
    MenuItem(restaurant_id=16, menu_id=16, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
    MenuItem(restaurant_id=16, menu_id=16, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_salad"),
    MenuItem(restaurant_id=16, menu_id=16, name="Two-Face Taters", description="Mashed with a twist", price=5.99, type="side", picture="path/to/two_face_taters"),
]
r16_desserts = [
    MenuItem(restaurant_id=16, menu_id=16, name="Batman's Brownie", description="The hero's favorite treat", price=7.49, type="dessert", picture="path/to/batmans_brownie"),
    MenuItem(restaurant_id=16, menu_id=16, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=16, menu_id=16, name="Alfred's Apple Pie", description="A classic in Wayne Manor", price=6.49, type="dessert", picture="path/to/alfreds_pie"),
    MenuItem(restaurant_id=16, menu_id=16, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=16, menu_id=16, name="Riddler's Riddle Cake", description="A cake that leaves you guessing", price=7.99, type="dessert", picture="path/to/riddlers_cake"),
    MenuItem(restaurant_id=16, menu_id=16, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=16, menu_id=16, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=16, menu_id=16, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=16, menu_id=16, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=16, menu_id=16, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_brownie"),
]
# Restaurant 17
r17_entrees = [
    MenuItem(restaurant_id=17, menu_id=17, name="Gotham Burger", description="A taste of the city's hero", price=14.99, type="entree", picture="path/to/gotham_burger"),
    MenuItem(restaurant_id=17, menu_id=17, name="Joker's Delight", description="Wild and unpredictable flavors", price=17.99, type="entree", picture="path/to/jokers_delight"),
    MenuItem(restaurant_id=17, menu_id=17, name="Batwing Pasta", description="Pasta with a heroic twist", price=13.99, type="entree", picture="path/to/batwing_pasta"),
    MenuItem(restaurant_id=17, menu_id=17, name="Riddler's Ribs", description="A riddle in every bite", price=18.99, type="entree", picture="path/to/riddlers_ribs"),
    MenuItem(restaurant_id=17, menu_id=17, name="Two-Face Tacos", description="Tacos with a dual flavor", price=15.99, type="entree", picture="path/to/two_face_tacos"),
    MenuItem(restaurant_id=17, menu_id=17, name="Catwoman's Carbonara", description="Seductively creamy pasta", price=16.99, type="entree", picture="path/to/catwomans_carbonara"),
    MenuItem(restaurant_id=17, menu_id=17, name="Mr. Freeze's Filet Mignon", description="Cold and perfectly cooked", price=22.99, type="entree", picture="path/to/mr_freezes_fillet"),
    MenuItem(restaurant_id=17, menu_id=17, name="Bane's BBQ Brisket", description="Smoked to villainous perfection", price=19.99, type="entree", picture="path/to/banes_bbq"),
    MenuItem(restaurant_id=17, menu_id=17, name="Harley's Hotdog", description="A mischievous twist on a classic", price=12.99, type="entree", picture="path/to/harleys_hotdog"),
    MenuItem(restaurant_id=17, menu_id=17, name="Penguin's Pizza", description="Toppings as unpredictable as the villain", price=17.99, type="entree", picture="path/to/penguins_pizza"),
]
r17_drinks = [
    MenuItem(restaurant_id=17, menu_id=17, name="Gotham Gazette Coffee", description="News-worthy caffeine", price=4.49, type="drink", picture="path/to/gotham_coffee"),
    MenuItem(restaurant_id=17, menu_id=17, name="Penguin's Pinot", description="A fine and fancy wine", price=9.99, type="drink", picture="path/to/penguin_pinot"),
    MenuItem(restaurant_id=17, menu_id=17, name="Bane's Brew", description="A powerful energy drink", price=5.99, type="drink", picture="path/to/banes_brew"),
    MenuItem(restaurant_id=17, menu_id=17, name="Joker's Julep", description="A laughably good drink", price=6.49, type="drink", picture="path/to/jokers_julep"),
    MenuItem(restaurant_id=17, menu_id=17, name="Harley's Hot Chocolate", description="Mischievously creamy", price=5.99, type="drink", picture="path/to/harleys_hot_chocolate"),
    MenuItem(restaurant_id=17, menu_id=17, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=17, menu_id=17, name="Riddler's Raspberry Soda", description="A fizzy enigma", price=4.99, type="drink", picture="path/to/riddlers_raspberry_soda"),
    MenuItem(restaurant_id=17, menu_id=17, name="Penguin's Pale Ale", description="A brew as cold as ice", price=6.99, type="drink", picture="path/to/penguins_pale_ale"),
    MenuItem(restaurant_id=17, menu_id=17, name="Two-Face Tea", description="A dual-flavored tea", price=4.99, type="drink", picture="path/to/two_face_tea"),
    MenuItem(restaurant_id=17, menu_id=17, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
]
r17_sides = [
    MenuItem(restaurant_id=17, menu_id=17, name="Gotham Grits", description="Creamy and comforting", price=5.49, type="side", picture="path/to/gotham_grits"),
    MenuItem(restaurant_id=17, menu_id=17, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=17, menu_id=17, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hashbrowns"),
    MenuItem(restaurant_id=17, menu_id=17, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=17, menu_id=17, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=17, menu_id=17, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=17, menu_id=17, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_pilaf"),
    MenuItem(restaurant_id=17, menu_id=17, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
    MenuItem(restaurant_id=17, menu_id=17, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_salad"),
    MenuItem(restaurant_id=17, menu_id=17, name="Joker's Jalapeño Poppers", description="A spicy surprise", price=5.99, type="side", picture="path/to/jokers_poppers"),
]
r17_desserts = [
    MenuItem(restaurant_id=17, menu_id=17, name="Batman's Brownie", description="The hero's favorite treat", price=7.49, type="dessert", picture="path/to/batmans_brownie"),
    MenuItem(restaurant_id=17, menu_id=17, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=17, menu_id=17, name="Alfred's Apple Pie", description="A classic in Wayne Manor", price=6.49, type="dessert", picture="path/to/alfreds_pie"),
    MenuItem(restaurant_id=17, menu_id=17, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=17, menu_id=17, name="Riddler's Riddle Cake", description="A cake that leaves you guessing", price=7.99, type="dessert", picture="path/to/riddlers_cake"),
    MenuItem(restaurant_id=17, menu_id=17, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=17, menu_id=17, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=17, menu_id=17, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=17, menu_id=17, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=17, menu_id=17, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_brownie"),
]
# Restaurant 18
r18_entrees = [
    MenuItem(restaurant_id=18, menu_id=18, name="Gotham Burger", description="A taste of the city's hero", price=14.99, type="entree", picture="path/to/gotham_burger"),
    MenuItem(restaurant_id=18, menu_id=18, name="Joker's Delight", description="Wild and unpredictable flavors", price=17.99, type="entree", picture="path/to/jokers_delight"),
    MenuItem(restaurant_id=18, menu_id=18, name="Batwing Pasta", description="Pasta with a heroic twist", price=13.99, type="entree", picture="path/to/batwing_pasta"),
    MenuItem(restaurant_id=18, menu_id=18, name="Riddler's Ribs", description="A riddle in every bite", price=18.99, type="entree", picture="path/to/riddlers_ribs"),
    MenuItem(restaurant_id=18, menu_id=18, name="Two-Face Tacos", description="Tacos with a dual flavor", price=15.99, type="entree", picture="path/to/two_face_tacos"),
    MenuItem(restaurant_id=18, menu_id=18, name="Catwoman's Carbonara", description="Seductively creamy pasta", price=16.99, type="entree", picture="path/to/catwomans_carbonara"),
    MenuItem(restaurant_id=18, menu_id=18, name="Mr. Freeze's Filet Mignon", description="Cold and perfectly cooked", price=22.99, type="entree", picture="path/to/mr_freezes_fillet"),
    MenuItem(restaurant_id=18, menu_id=18, name="Bane's BBQ Brisket", description="Smoked to villainous perfection", price=19.99, type="entree", picture="path/to/banes_bbq"),
    MenuItem(restaurant_id=18, menu_id=18, name="Harley's Hotdog", description="A mischievous twist on a classic", price=12.99, type="entree", picture="path/to/harleys_hotdog"),
    MenuItem(restaurant_id=18, menu_id=18, name="Penguin's Pizza", description="Toppings as unpredictable as the villain", price=17.99, type="entree", picture="path/to/penguins_pizza"),
]
r18_drinks = [
    MenuItem(restaurant_id=18, menu_id=18, name="Gotham Gazette Coffee", description="News-worthy caffeine", price=4.49, type="drink", picture="path/to/gotham_coffee"),
    MenuItem(restaurant_id=18, menu_id=18, name="Penguin's Pinot", description="A fine and fancy wine", price=9.99, type="drink", picture="path/to/penguin_pinot"),
    MenuItem(restaurant_id=18, menu_id=18, name="Bane's Brew", description="A powerful energy drink", price=5.99, type="drink", picture="path/to/banes_brew"),
    MenuItem(restaurant_id=18, menu_id=18, name="Joker's Julep", description="A laughably good drink", price=6.49, type="drink", picture="path/to/jokers_julep"),
    MenuItem(restaurant_id=18, menu_id=18, name="Harley's Hot Chocolate", description="Mischievously creamy", price=5.99, type="drink", picture="path/to/harleys_hot_chocolate"),
    MenuItem(restaurant_id=18, menu_id=18, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=18, menu_id=18, name="Riddler's Raspberry Soda", description="A fizzy enigma", price=4.99, type="drink", picture="path/to/riddlers_raspberry_soda"),
    MenuItem(restaurant_id=18, menu_id=18, name="Penguin's Pale Ale", description="A brew as cold as ice", price=6.99, type="drink", picture="path/to/penguins_pale_ale"),
    MenuItem(restaurant_id=18, menu_id=18, name="Two-Face Tea", description="A dual-flavored tea", price=4.99, type="drink", picture="path/to/two_face_tea"),
    MenuItem(restaurant_id=18, menu_id=18, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
]
r18_sides = [
    MenuItem(restaurant_id=18, menu_id=18, name="Gotham Grits", description="Creamy and comforting", price=5.49, type="side", picture="path/to/gotham_grits"),
    MenuItem(restaurant_id=18, menu_id=18, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=18, menu_id=18, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hashbrowns"),
    MenuItem(restaurant_id=18, menu_id=18, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=18, menu_id=18, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=18, menu_id=18, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=18, menu_id=18, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_pilaf"),
    MenuItem(restaurant_id=18, menu_id=18, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
    MenuItem(restaurant_id=18, menu_id=18, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_salad"),
    MenuItem(restaurant_id=18, menu_id=18, name="Two-Face Taters", description="Mashed with a dual twist", price=5.99, type="side", picture="path/to/two_face_taters"),
]
r18_desserts = [
    MenuItem(restaurant_id=18, menu_id=18, name="Batman's Brownie", description="The hero's favorite treat", price=7.49, type="dessert", picture="path/to/batmans_brownie"),
    MenuItem(restaurant_id=18, menu_id=18, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=18, menu_id=18, name="Alfred's Apple Pie", description="A classic in Wayne Manor", price=6.49, type="dessert", picture="path/to/alfreds_pie"),
    MenuItem(restaurant_id=18, menu_id=18, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=18, menu_id=18, name="Riddler's Riddle Cake", description="A cake that leaves you guessing", price=7.99, type="dessert", picture="path/to/riddlers_cake"),
    MenuItem(restaurant_id=18, menu_id=18, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=18, menu_id=18, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=18, menu_id=18, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=18, menu_id=18, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=18, menu_id=18, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_brownie"),
]
# Restaurant 19
r19_entrees = [
    MenuItem(restaurant_id=19, menu_id=19, name="Batcave Burger", description="A taste of justice in every bite", price=14.99, type="entree", picture="path/to/batcave_burger"),
    MenuItem(restaurant_id=19, menu_id=19, name="Joker's Pizza", description="Wild and unpredictable toppings", price=17.99, type="entree", picture="path/to/jokers_pizza"),
    MenuItem(restaurant_id=19, menu_id=19, name="Harley Quinn's Spaghetti", description="Twisted pasta with a side of mayhem", price=13.99, type="entree", picture="path/to/harley_spaghetti"),
    MenuItem(restaurant_id=19, menu_id=19, name="Riddler's Ribs", description="A riddle in every bite", price=18.99, type="entree", picture="path/to/riddler_ribs"),
    MenuItem(restaurant_id=19, menu_id=19, name="Two-Face Tacos", description="Tacos with a dual flavor", price=15.99, type="entree", picture="path/to/two_face_tacos"),
    MenuItem(restaurant_id=19, menu_id=19, name="Catwoman's Carbonara", description="Seductively creamy pasta", price=16.99, type="entree", picture="path/to/catwomans_carbonara"),
    MenuItem(restaurant_id=19, menu_id=19, name="Mr. Freeze's Filet Mignon", description="Cold and perfectly cooked", price=22.99, type="entree", picture="path/to/mr_freezes_fillet"),
    MenuItem(restaurant_id=19, menu_id=19, name="Bane's BBQ Brisket", description="Smoked to villainous perfection", price=19.99, type="entree", picture="path/to/banes_bbq"),
    MenuItem(restaurant_id=19, menu_id=19, name="Harley's Hotdog", description="A mischievous twist on a classic", price=12.99, type="entree", picture="path/to/harleys_hotdog"),
    MenuItem(restaurant_id=19, menu_id=19, name="Penguin's Pizza", description="Toppings as unpredictable as the villain", price=17.99, type="entree", picture="path/to/penguins_pizza"),
]
r19_drinks = [
    MenuItem(restaurant_id=19, menu_id=19, name="Gotham Gazette Coffee", description="News-worthy caffeine", price=4.49, type="drink", picture="path/to/gotham_coffee"),
    MenuItem(restaurant_id=19, menu_id=19, name="Penguin's Pinot", description="A fine and fancy wine", price=9.99, type="drink", picture="path/to/penguin_pinot"),
    MenuItem(restaurant_id=19, menu_id=19, name="Bane's Brew", description="A powerful energy drink", price=5.99, type="drink", picture="path/to/banes_brew"),
    MenuItem(restaurant_id=19, menu_id=19, name="Joker's Julep", description="A laughably good drink", price=6.49, type="drink", picture="path/to/jokers_julep"),
    MenuItem(restaurant_id=19, menu_id=19, name="Harley's Hot Chocolate", description="Mischievously creamy", price=5.99, type="drink", picture="path/to/harleys_hot_chocolate"),
    MenuItem(restaurant_id=19, menu_id=19, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=19, menu_id=19, name="Riddler's Raspberry Soda", description="A fizzy enigma", price=4.99, type="drink", picture="path/to/riddlers_raspberry_soda"),
    MenuItem(restaurant_id=19, menu_id=19, name="Penguin's Pale Ale", description="A brew as cold as ice", price=6.99, type="drink", picture="path/to/penguins_pale_ale"),
    MenuItem(restaurant_id=19, menu_id=19, name="Two-Face Tea", description="A dual-flavored tea", price=4.99, type="drink", picture="path/to/two_face_tea"),
    MenuItem(restaurant_id=19, menu_id=19, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
]
r19_sides = [
    MenuItem(restaurant_id=19, menu_id=19, name="Gotham Grits", description="Creamy and comforting", price=5.49, type="side", picture="path/to/gotham_grits"),
    MenuItem(restaurant_id=19, menu_id=19, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=19, menu_id=19, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hashbrowns"),
    MenuItem(restaurant_id=19, menu_id=19, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=19, menu_id=19, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=19, menu_id=19, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=19, menu_id=19, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_pilaf"),
    MenuItem(restaurant_id=19, menu_id=19, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
    MenuItem(restaurant_id=19, menu_id=19, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_salad"),
    MenuItem(restaurant_id=19, menu_id=19, name="Joker's Jalapeño Poppers", description="Spicy and whimsical", price=5.99, type="side", picture="path/to/jokers_poppers"),
]
r19_desserts = [
    MenuItem(restaurant_id=19, menu_id=19, name="Batman's Brownie", description="The hero's favorite treat", price=7.49, type="dessert", picture="path/to/batmans_brownie"),
    MenuItem(restaurant_id=19, menu_id=19, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=19, menu_id=19, name="Alfred's Apple Pie", description="A classic in Wayne Manor", price=6.49, type="dessert", picture="path/to/alfreds_pie"),
    MenuItem(restaurant_id=19, menu_id=19, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=19, menu_id=19, name="Riddler's Riddle Cake", description="A cake that leaves you guessing", price=7.99, type="dessert", picture="path/to/riddlers_cake"),
    MenuItem(restaurant_id=19, menu_id=19, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=19, menu_id=19, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=19, menu_id=19, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=19, menu_id=19, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=19, menu_id=19, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_brownie"),
]
# Restaurant 20
r20_entrees = [
    MenuItem(restaurant_id=20, menu_id=20, name="Gotham Grilled Cheese", description="A cheesy delight", price=12.99, type="entree", picture="path/to/gotham_grilled_cheese"),
    MenuItem(restaurant_id=20, menu_id=20, name="Penguin's Pesto Pasta", description="A villainous twist on pesto", price=16.99, type="entree", picture="path/to/penguins_pesto_pasta"),
    MenuItem(restaurant_id=20, menu_id=20, name="Batwing Buffalo Wings", description="Spicy wings for heroes", price=14.99, type="entree", picture="path/to/batwing_buffalo_wings"),
    MenuItem(restaurant_id=20, menu_id=20, name="Riddler's Ramen", description="A noodle puzzle", price=13.99, type="entree", picture="path/to/riddlers_ramen"),
    MenuItem(restaurant_id=20, menu_id=20, name="Two-Face Tacos", description="Tacos with a dual flavor", price=15.99, type="entree", picture="path/to/two_face_tacos"),
    MenuItem(restaurant_id=20, menu_id=20, name="Catwoman's Carbonara", description="Seductively creamy pasta", price=16.99, type="entree", picture="path/to/catwomans_carbonara"),
    MenuItem(restaurant_id=20, menu_id=20, name="Mr. Freeze's Filet Mignon", description="Cold and perfectly cooked", price=22.99, type="entree", picture="path/to/mr_freezes_fillet"),
    MenuItem(restaurant_id=20, menu_id=20, name="Bane's BBQ Brisket", description="Smoked to villainous perfection", price=19.99, type="entree", picture="path/to/banes_bbq"),
    MenuItem(restaurant_id=20, menu_id=20, name="Harley's Hotdog", description="A mischievous twist on a classic", price=12.99, type="entree", picture="path/to/harleys_hotdog"),
    MenuItem(restaurant_id=20, menu_id=20, name="Penguin's Pizza", description="Toppings as unpredictable as the villain", price=17.99, type="entree", picture="path/to/penguins_pizza"),
]
r20_drinks = [
    MenuItem(restaurant_id=20, menu_id=20, name="Gotham Gazette Coffee", description="News-worthy caffeine", price=4.49, type="drink", picture="path/to/gotham_coffee"),
    MenuItem(restaurant_id=20, menu_id=20, name="Penguin's Pinot", description="A fine and fancy wine", price=9.99, type="drink", picture="path/to/penguin_pinot"),
    MenuItem(restaurant_id=20, menu_id=20, name="Bane's Brew", description="A powerful energy drink", price=5.99, type="drink", picture="path/to/banes_brew"),
    MenuItem(restaurant_id=20, menu_id=20, name="Joker's Julep", description="A laughably good drink", price=6.49, type="drink", picture="path/to/jokers_julep"),
    MenuItem(restaurant_id=20, menu_id=20, name="Harley's Hot Chocolate", description="Mischievously creamy", price=5.99, type="drink", picture="path/to/harleys_hot_chocolate"),
    MenuItem(restaurant_id=20, menu_id=20, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=20, menu_id=20, name="Riddler's Raspberry Soda", description="A fizzy enigma", price=4.99, type="drink", picture="path/to/riddlers_raspberry_soda"),
    MenuItem(restaurant_id=20, menu_id=20, name="Penguin's Pale Ale", description="A brew as cold as ice", price=6.99, type="drink", picture="path/to/penguins_pale_ale"),
    MenuItem(restaurant_id=20, menu_id=20, name="Two-Face Tea", description="A dual-flavored tea", price=4.99, type="drink", picture="path/to/two_face_tea"),
    MenuItem(restaurant_id=20, menu_id=20, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
]
r20_sides = [
    MenuItem(restaurant_id=20, menu_id=20, name="Gotham Grits", description="Creamy and comforting", price=5.49, type="side", picture="path/to/gotham_grits"),
    MenuItem(restaurant_id=20, menu_id=20, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=20, menu_id=20, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hashbrowns"),
    MenuItem(restaurant_id=20, menu_id=20, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=20, menu_id=20, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=20, menu_id=20, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=20, menu_id=20, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_pilaf"),
    MenuItem(restaurant_id=20, menu_id=20, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
    MenuItem(restaurant_id=20, menu_id=20, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_salad"),
    MenuItem(restaurant_id=20, menu_id=20, name="Two-Face Taters", description="Mashed with a dual personality", price=5.99, type="side", picture="path/to/two_face_taters"),
]
r20_desserts = [
    MenuItem(restaurant_id=20, menu_id=20, name="Batman's Brownie", description="The hero's favorite treat", price=7.49, type="dessert", picture="path/to/batmans_brownie"),
    MenuItem(restaurant_id=20, menu_id=20, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=20, menu_id=20, name="Alfred's Apple Pie", description="A classic in Wayne Manor", price=6.49, type="dessert", picture="path/to/alfreds_pie"),
    MenuItem(restaurant_id=20, menu_id=20, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=20, menu_id=20, name="Riddler's Riddle Cake", description="A cake that leaves you guessing", price=7.99, type="dessert", picture="path/to/riddlers_cake"),
    MenuItem(restaurant_id=20, menu_id=20, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=20, menu_id=20, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=20, menu_id=20, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=20, menu_id=20, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=20, menu_id=20, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_brownie"),
]

# Restaurant 21 - The Dark Knight Diner
r21_entrees = [
    MenuItem(restaurant_id=21, menu_id=21, name="Batman's Bat-Burger", description="A burger fit for a hero", price=12.99, type="entree", picture="path/to/batmans_burger"),
    MenuItem(restaurant_id=21, menu_id=21, name="Robin's Ribs", description="Tender ribs that even Batman approves", price=16.99, type="entree", picture="path/to/robins_ribs"),
    MenuItem(restaurant_id=21, menu_id=21, name="Batgirl's BBQ Chicken", description="Saucy and satisfying", price=14.99, type="entree", picture="path/to/batgirls_bbq_chicken"),
    MenuItem(restaurant_id=21, menu_id=21, name="Gotham Gourmet Pizza", description="A pizza with all the toppings", price=13.99, type="entree", picture="path/to/gotham_gourmet_pizza"),
    MenuItem(restaurant_id=21, menu_id=21, name="Justice League Lasagna", description="Layers of flavor", price=15.99, type="entree", picture="path/to/justice_league_lasagna"),
    MenuItem(restaurant_id=21, menu_id=21, name="Arkham Asylum Alfredo", description="Creamy pasta from the asylum's kitchen", price=16.99, type="entree", picture="path/to/arkham_asylum_alfredo"),
    MenuItem(restaurant_id=21, menu_id=21, name="Bat-Wing Wontons", description="Crispy wontons with a heroic twist", price=12.99, type="entree", picture="path/to/batwing_wontons"),
    MenuItem(restaurant_id=21, menu_id=21, name="The Joker's Jambalaya", description="A chaotic mix of flavors", price=18.99, type="entree", picture="path/to/jokers_jambalaya"),
    MenuItem(restaurant_id=21, menu_id=21, name="Penguin's Pasta Primavera", description="A villainous veggie delight", price=14.99, type="entree", picture="path/to/penguins_pasta_primavera"),
    MenuItem(restaurant_id=21, menu_id=21, name="Riddler's Ramen", description="A noodle puzzle", price=13.99, type="entree", picture="path/to/riddlers_ramen"),
]

# Restaurant 21 - The Dark Knight Diner - Drinks
r21_drinks = [
    MenuItem(restaurant_id=21, menu_id=21, name="Bat-Signal Smoothie", description="A fruity hero's delight", price=4.49, type="drink", picture="path/to/bat_signal_smoothie"),
    MenuItem(restaurant_id=21, menu_id=21, name="Wonder Woman's Watermelon Cooler", description="Refreshing and powerful", price=5.99, type="drink", picture="path/to/wonder_womans_cooler"),
    MenuItem(restaurant_id=21, menu_id=21, name="Green Lantern Green Tea", description="Light up your day", price=3.99, type="drink", picture="path/to/green_lantern_green_tea"),
    MenuItem(restaurant_id=21, menu_id=21, name="Aquaman's Oceanic Elixir", description="Tastes like the sea", price=6.49, type="drink", picture="path/to/aquamans_elixir"),
    MenuItem(restaurant_id=21, menu_id=21, name="Flash's Flashade", description="Quick and refreshing", price=4.99, type="drink", picture="path/to/flashs_flashade"),
    MenuItem(restaurant_id=21, menu_id=21, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=21, menu_id=21, name="The Batmobile Brew", description="Fueled for action", price=4.99, type="drink", picture="path/to/batmobile_brew"),
    MenuItem(restaurant_id=21, menu_id=21, name="Bane's Bubbly Soda", description="A powerful fizz", price=4.99, type="drink", picture="path/to/banes_bubbly_soda"),
    MenuItem(restaurant_id=21, menu_id=21, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
    MenuItem(restaurant_id=21, menu_id=21, name="Superman's Super Smoothie", description="A drink that lifts you up", price=5.99, type="drink", picture="path/to/supermans_smoothie"),
]

# Restaurant 21 - The Dark Knight Diner - Sides
r21_sides = [
    MenuItem(restaurant_id=21, menu_id=21, name="Bat-Fries", description="Crispy and seasoned to perfection", price=5.49, type="side", picture="path/to/bat_fries"),
    MenuItem(restaurant_id=21, menu_id=21, name="Wonder Woman's Spinach Salad", description="A salad fit for an Amazon", price=4.49, type="side", picture="path/to/wonder_womans_salad"),
    MenuItem(restaurant_id=21, menu_id=21, name="Green Lantern Guacamole", description="A green and powerful dip", price=4.99, type="side", picture="path/to/green_lantern_guacamole"),
    MenuItem(restaurant_id=21, menu_id=21, name="Aquaman's Seaweed Snack", description="A taste of the ocean", price=4.99, type="side", picture="path/to/aquamans_seaweed_snack"),
    MenuItem(restaurant_id=21, menu_id=21, name="Flash's French Fries", description="Quick and crispy", price=4.49, type="side", picture="path/to/flashs_french_fries"),
    MenuItem(restaurant_id=21, menu_id=21, name="Catwoman's Coleslaw", description="Seductively delicious", price=5.49, type="side", picture="path/to/catwomans_coleslaw"),
    MenuItem(restaurant_id=21, menu_id=21, name="Bat-Wing Nachos", description="Loaded with heroics", price=6.49, type="side", picture="path/to/batwing_nachos"),
    MenuItem(restaurant_id=21, menu_id=21, name="The Joker's Jalapeño Poppers", description="A spicy surprise", price=5.99, type="side", picture="path/to/jokers_jalapeno_poppers"),
    MenuItem(restaurant_id=21, menu_id=21, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_potato_salad"),
    MenuItem(restaurant_id=21, menu_id=21, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_rice_pilaf"),
]

# Restaurant 21 - The Dark Knight Diner - Desserts
r21_desserts = [
    MenuItem(restaurant_id=21, menu_id=21, name="Batman's Brownie", description="The hero's favorite treat", price=7.49, type="dessert", picture="path/to/batmans_brownie"),
    MenuItem(restaurant_id=21, menu_id=21, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=21, menu_id=21, name="Alfred's Apple Pie", description="A classic in Wayne Manor", price=6.49, type="dessert", picture="path/to/alfreds_apple_pie"),
    MenuItem(restaurant_id=21, menu_id=21, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=21, menu_id=21, name="Riddler's Riddle Cake", description="A cake that leaves you guessing", price=7.99, type="dessert", picture="path/to/riddlers_riddle_cake"),
    MenuItem(restaurant_id=21, menu_id=21, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=21, menu_id=21, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_chocolate_mousse"),
    MenuItem(restaurant_id=21, menu_id=21, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=21, menu_id=21, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=21, menu_id=21, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_haunted_brownie"),
]

# Restaurant 22 - Wayne Manor Fine Dining
r22_entrees = [
    MenuItem(restaurant_id=22, menu_id=22, name="Bruce Wayne's Steak", description="A billionaire's favorite", price=39.99, type="entree", picture="path/to/bruce_waynes_steak"),
    MenuItem(restaurant_id=22, menu_id=22, name="Alfred's Roast Chicken", description="Cooked to perfection", price=29.99, type="entree", picture="path/to/alfreds_roast_chicken"),
    MenuItem(restaurant_id=22, menu_id=22, name="Gotham Lobster Thermidor", description="An extravagant seafood delight", price=45.99, type="entree", picture="path/to/gotham_lobster_thermidor"),
    MenuItem(restaurant_id=22, menu_id=22, name="Harvey Dent's Double Steak", description="Two cuts, twice the flavor", price=49.99, type="entree", picture="path/to/harvey_dents_double_steak"),
    MenuItem(restaurant_id=22, menu_id=22, name="Selina Kyle's Surf and Turf", description="A luxurious combination", price=42.99, type="entree", picture="path/to/selina_kyles_surf_and_turf"),
    MenuItem(restaurant_id=22, menu_id=22, name="Wayne Manor Wild Mushroom Risotto", description="A taste of the manor's garden", price=34.99, type="entree", picture="path/to/wayne_manor_risotto"),
    MenuItem(restaurant_id=22, menu_id=22, name="Riddler's Filet Mignon", description="A cut of mystery", price=38.99, type="entree", picture="path/to/riddlers_filet_mignon"),
    MenuItem(restaurant_id=22, menu_id=22, name="Penguin's Paella", description="A villainous seafood feast", price=46.99, type="entree", picture="path/to/penguins_paella"),
    MenuItem(restaurant_id=22, menu_id=22, name="Lucius Fox's Lamb Chops", description="Tech mogul's favorite", price=36.99, type="entree", picture="path/to/lucius_foxs_lamb_chops"),
    MenuItem(restaurant_id=22, menu_id=22, name="Damian Wayne's Duck Confit", description="A dish fit for the heir", price=37.99, type="entree", picture="path/to/damian_waynes_duck_confit"),
]

# Restaurant 22 - Wayne Manor Fine Dining - Drinks
r22_drinks = [
    MenuItem(restaurant_id=22, menu_id=22, name="Wayne Estate Merlot", description="A wine from the manor's vineyard", price=59.99, type="drink", picture="path/to/wayne_estate_merlot"),
    MenuItem(restaurant_id=22, menu_id=22, name="Lucius Fox's Old Fashioned", description="A classic cocktail with a high-tech twist", price=14.99, type="drink", picture="path/to/lucius_foxs_old_fashioned"),
    MenuItem(restaurant_id=22, menu_id=22, name="Selina Kyle's Sangria", description="A fruity delight", price=12.99, type="drink", picture="path/to/selina_kyles_sangria"),
    MenuItem(restaurant_id=22, menu_id=22, name="Gotham Gin and Tonic", description="A refreshing city favorite", price=11.99, type="drink", picture="path/to/gotham_gin_and_tonic"),
    MenuItem(restaurant_id=22, menu_id=22, name="Bruce Wayne's Bourbon", description="The billionaire's choice", price=17.99, type="drink", picture="path/to/bruce_waynes_bourbon"),
    MenuItem(restaurant_id=22, menu_id=22, name="Wayne Manor Chardonnay", description="An elegant white wine", price=54.99, type="drink", picture="path/to/wayne_manor_chardonnay"),
    MenuItem(restaurant_id=22, menu_id=22, name="Lucius Fox's Espresso Martini", description="A tech-infused coffee cocktail", price=16.99, type="drink", picture="path/to/lucius_foxs_espresso_martini"),
    MenuItem(restaurant_id=22, menu_id=22, name="Gotham Lemonade", description="A zesty and refreshing drink", price=5.99, type="drink", picture="path/to/gotham_lemonade"),
    MenuItem(restaurant_id=22, menu_id=22, name="Damian Wayne's Virgin Mojito", description="A non-alcoholic choice for the young heir", price=7.99, type="drink", picture="path/to/damian_waynes_virgin_mojito"),
    MenuItem(restaurant_id=22, menu_id=22, name="Wayne Manor Water", description="Pure and refreshing", price=2.99, type="drink", picture="path/to/wayne_manor_water"),
]

# Restaurant 22 - Wayne Manor Fine Dining - Sides
r22_sides = [
    MenuItem(restaurant_id=22, menu_id=22, name="Wayne Manor Mashed Potatoes", description="Creamy and buttery", price=8.99, type="side", picture="path/to/wayne_manor_mashed_potatoes"),
    MenuItem(restaurant_id=22, menu_id=22, name="Lucius Fox's Truffle Fries", description="Luxurious and flavorful", price=9.99, type="side", picture="path/to/lucius_foxs_truffle_fries"),
    MenuItem(restaurant_id=22, menu_id=22, name="Selina Kyle's Asparagus", description="Fresh and crisp", price=7.99, type="side", picture="path/to/selina_kyles_asparagus"),
    MenuItem(restaurant_id=22, menu_id=22, name="Gotham Garlic Bread", description="A classic side for any hero", price=5.99, type="side", picture="path/to/gotham_garlic_bread"),
    MenuItem(restaurant_id=22, menu_id=22, name="Bruce Wayne's Brussels Sprouts", description="Roasted to perfection", price=9.99, type="side", picture="path/to/bruce_waynes_brussels_sprouts"),
    MenuItem(restaurant_id=22, menu_id=22, name="Wayne Manor Caesar Salad", description="A timeless classic", price=8.99, type="side", picture="path/to/wayne_manor_caesar_salad"),
    MenuItem(restaurant_id=22, menu_id=22, name="Lucius Fox's Creamed Spinach", description="A rich and creamy side", price=7.99, type="side", picture="path/to/lucius_foxs_creamed_spinach"),
    MenuItem(restaurant_id=22, menu_id=22, name="Gotham Grilled Vegetables", description="Healthy and flavorful", price=8.99, type="side", picture="path/to/gotham_grilled_vegetables"),
    MenuItem(restaurant_id=22, menu_id=22, name="Damian Wayne's Mac and Cheese", description="A kid's favorite", price=7.99, type="side", picture="path/to/damian_waynes_mac_and_cheese"),
    MenuItem(restaurant_id=22, menu_id=22, name="Wayne Manor Wild Rice Pilaf", description="A manor specialty", price=8.99, type="side", picture="path/to/wayne_manor_rice_pilaf"),
]

# Restaurant 22 - Wayne Manor Fine Dining - Desserts
r22_desserts = [
    MenuItem(restaurant_id=22, menu_id=22, name="Wayne Manor Chocolate Fondue", description="Dip and indulge", price=12.99, type="dessert", picture="path/to/wayne_manor_chocolate_fondue"),
    MenuItem(restaurant_id=22, menu_id=22, name="Lucius Fox's Tiramisu", description="Elegant and coffee-infused", price=10.99, type="dessert", picture="path/to/lucius_foxs_tiramisu"),
    MenuItem(restaurant_id=22, menu_id=22, name="Selina Kyle's Black Forest Cake", description="A rich and dark delight", price=11.99, type="dessert", picture="path/to/selina_kyles_black_forest_cake"),
    MenuItem(restaurant_id=22, menu_id=22, name="Gotham Panna Cotta", description="Smooth and creamy", price=9.99, type="dessert", picture="path/to/gotham_panna_cotta"),
    MenuItem(restaurant_id=22, menu_id=22, name="Bruce Wayne's Biscuit Pudding", description="A classic dessert from the manor", price=11.99, type="dessert", picture="path/to/bruce_waynes_biscuit_pudding"),
    MenuItem(restaurant_id=22, menu_id=22, name="Wayne Manor White Chocolate Mousse", description="Luxurious and white as snow", price=12.99, type="dessert", picture="path/to/wayne_manor_white_chocolate_mousse"),
    MenuItem(restaurant_id=22, menu_id=22, name="Lucius Fox's Creme Brulee", description="A perfectly torched delight", price=10.99, type="dessert", picture="path/to/lucius_foxs_creme_brulee"),
    MenuItem(restaurant_id=22, menu_id=22, name="Gotham Berry Tart", description="Fresh berries in a buttery crust", price=11.99, type="dessert", picture="path/to/gotham_berry_tart"),
    MenuItem(restaurant_id=22, menu_id=22, name="Damian Wayne's Ice Cream Sundae", description="A young hero's favorite", price=9.99, type="dessert", picture="path/to/damian_waynes_ice_cream_sundae"),
    MenuItem(restaurant_id=22, menu_id=22, name="Wayne Manor Affogato", description="Espresso meets ice cream", price=10.99, type="dessert", picture="path/to/wayne_manor_affogato"),
]

# Restaurant 23
r23_entrees = [
    MenuItem(restaurant_id=23, menu_id=23, name="The Dark Knight Burger", description="A hero's delight", price=13.99, type="entree", picture="path/to/dark_knight_burger"),
    MenuItem(restaurant_id=23, menu_id=23, name="Gotham City Pizza", description="Pizza with Gotham flair", price=16.99, type="entree", picture="path/to/gotham_city_pizza"),
    MenuItem(restaurant_id=23, menu_id=23, name="Batwing BBQ Ribs", description="Smoky and succulent", price=18.99, type="entree", picture="path/to/batwing_bbq_ribs"),
    MenuItem(restaurant_id=23, menu_id=23, name="The Bat-Salad", description="A fresh and heroic salad", price=9.99, type="entree", picture="path/to/bat_salad"),
    MenuItem(restaurant_id=23, menu_id=23, name="Catwoman's Calzone", description="A cat-inspired delight", price=15.99, type="entree", picture="path/to/catwomans_calzone"),
    MenuItem(restaurant_id=23, menu_id=23, name="Bat-Spicy Pasta", description="A pasta with a kick", price=14.99, type="entree", picture="path/to/bat_spicy_pasta"),
    MenuItem(restaurant_id=23, menu_id=23, name="The Bat-Taco", description="A taco fit for a hero", price=12.99, type="entree", picture="path/to/bat_taco"),
    MenuItem(restaurant_id=23, menu_id=23, name="Joker's Jalapeño Burger", description="A burger with a twist", price=15.99, type="entree", picture="path/to/jokers_jalapeno_burger"),
    MenuItem(restaurant_id=23, menu_id=23, name="Penguin's Pepperoni Pasta", description="A villainous pasta", price=13.99, type="entree", picture="path/to/penguins_pepperoni_pasta"),
    MenuItem(restaurant_id=23, menu_id=23, name="Two-Face Tenders", description="Chicken tenders with a dual flavor", price=12.99, type="entree", picture="path/to/two_face_tenders"),
]

r23_drinks = [
    MenuItem(restaurant_id=23, menu_id=23, name="Bat-Juice", description="Energize like a hero", price=4.99, type="drink", picture="path/to/bat_juice"),
    MenuItem(restaurant_id=23, menu_id=23, name="Robin's Refresher", description="A sidekick's favorite", price=3.99, type="drink", picture="path/to/robins_refresher"),
    MenuItem(restaurant_id=23, menu_id=23, name="Batgirl's Blueberry Smoothie", description="A fruity delight", price=5.99, type="drink", picture="path/to/batgirls_smoothie"),
    MenuItem(restaurant_id=23, menu_id=23, name="Gotham Green Tea", description="Calm your inner hero", price=3.99, type="drink", picture="path/to/gotham_green_tea"),
    MenuItem(restaurant_id=23, menu_id=23, name="The Bat-Shake", description="Thick and chocolatey", price=5.99, type="drink", picture="path/to/bat_shake"),
    MenuItem(restaurant_id=23, menu_id=23, name="Bane's Brew", description="A powerful energy drink", price=5.99, type="drink", picture="path/to/banes_brew"),
    MenuItem(restaurant_id=23, menu_id=23, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
    MenuItem(restaurant_id=23, menu_id=23, name="Harley's Huckleberry Lemonade", description="Mischievously sweet", price=4.99, type="drink", picture="path/to/harleys_lemonade"),
    MenuItem(restaurant_id=23, menu_id=23, name="Riddler's Raspberry Soda", description="A fizzy enigma", price=4.99, type="drink", picture="path/to/riddlers_raspberry_soda"),
    MenuItem(restaurant_id=23, menu_id=23, name="Penguin's Pale Ale", description="A brew as cold as ice", price=6.99, type="drink", picture="path/to/penguins_pale_ale"),
]

r23_sides = [
    MenuItem(restaurant_id=23, menu_id=23, name="Gotham Garlic Fries", description="Crispy and flavorful", price=5.49, type="side", picture="path/to/gotham_garlic_fries"),
    MenuItem(restaurant_id=23, menu_id=23, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=23, menu_id=23, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hash_browns"),
    MenuItem(restaurant_id=23, menu_id=23, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=23, menu_id=23, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=23, menu_id=23, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=23, menu_id=23, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_rice_pilaf"),
    MenuItem(restaurant_id=23, menu_id=23, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
    MenuItem(restaurant_id=23, menu_id=23, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_potato_salad"),
    MenuItem(restaurant_id=23, menu_id=23, name="Two-Face Taters", description="Mashed with a dual personality", price=5.99, type="side", picture="path/to/two_face_taters"),
]

r23_desserts = [
    MenuItem(restaurant_id=23, menu_id=23, name="Batman's Brownie", description="The hero's favorite treat", price=7.49, type="dessert", picture="path/to/batmans_brownie"),
    MenuItem(restaurant_id=23, menu_id=23, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=23, menu_id=23, name="Alfred's Apple Pie", description="A classic in Wayne Manor", price=6.49, type="dessert", picture="path/to/alfreds_apple_pie"),
    MenuItem(restaurant_id=23, menu_id=23, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=23, menu_id=23, name="Riddler's Riddle Cake", description="A cake that leaves you guessing", price=7.99, type="dessert", picture="path/to/riddlers_riddle_cake"),
    MenuItem(restaurant_id=23, menu_id=23, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=23, menu_id=23, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_chocolate_mousse"),
    MenuItem(restaurant_id=23, menu_id=23, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=23, menu_id=23, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=23, menu_id=23, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_haunted_brownie"),
]

r23_menu = r23_entrees + r23_drinks + r23_sides + r23_desserts

r23_ = Restaurant(
    id=23,
    name="Gotham Grill",
    description="Where heroes and villains dine together",
    address="123 Batcave Road, Gotham City",
    phone_number="+1 987-654-3210",
    picture="path/to/gotham_grill_picture",
    menu=r23_menu,
)

# Restaurant 24
r24_entrees = [
    MenuItem(restaurant_id=24, menu_id=24, name="Batsignal Burger", description="Summon your appetite", price=13.99, type="entree", picture="path/to/batsignal_burger"),
    MenuItem(restaurant_id=24, menu_id=24, name="Wayne Manor Pizza", description="Pizza with manor elegance", price=16.99, type="entree", picture="path/to/wayne_manor_pizza"),
    MenuItem(restaurant_id=24, menu_id=24, name="Batmobile BBQ Ribs", description="Grilled to perfection", price=18.99, type="entree", picture="path/to/batmobile_bbq_ribs"),
    MenuItem(restaurant_id=24, menu_id=24, name="Gotham Garden Salad", description="Freshness from the city", price=9.99, type="entree", picture="path/to/gotham_garden_salad"),
    MenuItem(restaurant_id=24, menu_id=24, name="Riddler's Ricotta Calzone", description="A puzzling delight", price=15.99, type="entree", picture="path/to/riddlers_ricotta_calzone"),
    MenuItem(restaurant_id=24, menu_id=24, name="Bat-Spiced Pasta", description="Spices of the night", price=14.99, type="entree", picture="path/to/bat_spiced_pasta"),
    MenuItem(restaurant_id=24, menu_id=24, name="Gotham Taco", description="A taco for the city", price=12.99, type="entree", picture="path/to/gotham_taco"),
    MenuItem(restaurant_id=24, menu_id=24, name="Joker's Jackfruit Burger", description="A plant-based twist", price=15.99, type="entree", picture="path/to/jokers_jackfruit_burger"),
    MenuItem(restaurant_id=24, menu_id=24, name="Penguin's Penne Pasta", description="An icy pasta creation", price=13.99, type="entree", picture="path/to/penguins_penne_pasta"),
    MenuItem(restaurant_id=24, menu_id=24, name="Two-Face Fries", description="A duality of flavors", price=12.99, type="entree", picture="path/to/two_face_fries"),
]

r24_drinks = [
    MenuItem(restaurant_id=24, menu_id=24, name="Batbrew Coffee", description="Awaken your inner hero", price=4.99, type="drink", picture="path/to/batbrew_coffee"),
    MenuItem(restaurant_id=24, menu_id=24, name="Robin's Recovery Shake", description="Recharge like a sidekick", price=3.99, type="drink", picture="path/to/robins_recovery_shake"),
    MenuItem(restaurant_id=24, menu_id=24, name="Batgirl's Berry Blast", description="A fruity burst of energy", price=5.99, type="drink", picture="path/to/batgirls_berry_blast"),
    MenuItem(restaurant_id=24, menu_id=24, name="Gotham Green Smoothie", description="A healthy hero's choice", price=3.99, type="drink", picture="path/to/gotham_green_smoothie"),
    MenuItem(restaurant_id=24, menu_id=24, name="The Bat-Cream Soda", description="Creamy and nostalgic", price=5.99, type="drink", picture="path/to/bat_cream_soda"),
    MenuItem(restaurant_id=24, menu_id=24, name="Catwoman's Caffeine Kick", description="An espresso with a twist", price=5.99, type="drink", picture="path/to/catwomans_caffeine_kick"),
    MenuItem(restaurant_id=24, menu_id=24, name="Riddler's Riddle Refresher", description="A puzzling thirst quencher", price=4.99, type="drink", picture="path/to/riddlers_riddle_refresher"),
    MenuItem(restaurant_id=24, menu_id=24, name="Penguin's Pale Ale", description="A brew as cold as ice", price=6.99, type="drink", picture="path/to/penguins_pale_ale"),
    MenuItem(restaurant_id=24, menu_id=24, name="Two-Face Tea", description="A dual-flavored tea", price=4.99, type="drink", picture="path/to/two_face_tea"),
    MenuItem(restaurant_id=24, menu_id=24, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
]

r24_sides = [
    MenuItem(restaurant_id=24, menu_id=24, name="Bat-Taters", description="Crispy and heroic", price=5.49, type="side", picture="path/to/bat_taters"),
    MenuItem(restaurant_id=24, menu_id=24, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=24, menu_id=24, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hash_browns"),
    MenuItem(restaurant_id=24, menu_id=24, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=24, menu_id=24, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=24, menu_id=24, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=24, menu_id=24, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_rice_pilaf"),
    MenuItem(restaurant_id=24, menu_id=24, name="Two-Face Taters", description="Mashed with a dual personality", price=5.99, type="side", picture="path/to/two_face_taters"),
    MenuItem(restaurant_id=24, menu_id=24, name="Gotham Garlic Bread", description="A classic side for any hero", price=5.99, type="side", picture="path/to/gotham_garlic_bread"),
    MenuItem(restaurant_id=24, menu_id=24, name="Wayne Manor Wild Rice Pilaf", description="A manor specialty", price=8.99, type="side", picture="path/to/wayne_manor_rice_pilaf"),
]

r24_desserts = [
    MenuItem(restaurant_id=24, menu_id=24, name="Bat-Cake", description="A cake fit for a hero", price=7.49, type="dessert", picture="path/to/bat_cake"),
    MenuItem(restaurant_id=24, menu_id=24, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=24, menu_id=24, name="Wayne Manor Apple Pie", description="A classic from the manor", price=6.49, type="dessert", picture="path/to/wayne_manor_apple_pie"),
    MenuItem(restaurant_id=24, menu_id=24, name="Gotham Chocolate Mousse", description="Rich and decadent", price=8.49, type="dessert", picture="path/to/gotham_chocolate_mousse"),
    MenuItem(restaurant_id=24, menu_id=24, name="Riddler's Riddle Delight", description="A dessert that challenges", price=7.99, type="dessert", picture="path/to/riddlers_riddle_delight"),
    MenuItem(restaurant_id=24, menu_id=24, name="Joker's Gelato", description="Laughably delicious", price=5.49, type="dessert", picture="path/to/jokers_gelato"),
    MenuItem(restaurant_id=24, menu_id=24, name="Catwoman's Tiramisu", description="Elegance in every bite", price=8.49, type="dessert", picture="path/to/catwomans_tiramisu"),
    MenuItem(restaurant_id=24, menu_id=24, name="Bane's Brownie", description="A dessert with a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=24, menu_id=24, name="Poison Ivy's Parfait", description="A sweet treat with a hint of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=24, menu_id=24, name="Harley's Haunted Cupcake", description="A cupcake with a mischievous grin", price=6.56, type="dessert", picture="path/to/banes_brownie"),
]

r25_entrees = [
    MenuItem(restaurant_id=25, menu_id=25, name="Gotham Grilled Cheese", description="A cheesy delight", price=12.99, type="entree", picture="path/to/gotham_grilled_cheese"),
    MenuItem(restaurant_id=25, menu_id=25, name="Penguin's Pesto Pasta", description="A villainous twist on pesto", price=16.99, type="entree", picture="path/to/penguins_pesto_pasta"),
    MenuItem(restaurant_id=25, menu_id=25, name="Batwing Buffalo Wings", description="Spicy wings for heroes", price=14.99, type="entree", picture="path/to/batwing_buffalo_wings"),
    MenuItem(restaurant_id=25, menu_id=25, name="Riddler's Ramen", description="A noodle puzzle", price=13.99, type="entree", picture="path/to/riddlers_ramen"),
    MenuItem(restaurant_id=25, menu_id=25, name="Two-Face Tacos", description="Tacos with a dual flavor", price=15.99, type="entree", picture="path/to/two_face_tacos"),
    MenuItem(restaurant_id=25, menu_id=25, name="Catwoman's Carbonara", description="Seductively creamy pasta", price=16.99, type="entree", picture="path/to/catwomans_carbonara"),
    MenuItem(restaurant_id=25, menu_id=25, name="Mr. Freeze's Filet Mignon", description="Cold and perfectly cooked", price=22.99, type="entree", picture="path/to/mr_freezes_fillet"),
    MenuItem(restaurant_id=25, menu_id=25, name="Bane's BBQ Brisket", description="Smoked to villainous perfection", price=19.99, type="entree", picture="path/to/banes_bbq"),
    MenuItem(restaurant_id=25, menu_id=25, name="Harley's Hotdog", description="A mischievous twist on a classic", price=12.99, type="entree", picture="path/to/harleys_hotdog"),
    MenuItem(restaurant_id=25, menu_id=25, name="Penguin's Pizza", description="Toppings as unpredictable as the villain", price=17.99, type="entree", picture="path/to/penguins_pizza"),
]

r25_drinks = [
    MenuItem(restaurant_id=25, menu_id=25, name="Gotham Gazette Coffee", description="News-worthy caffeine", price=4.49, type="drink", picture="path/to/gotham_coffee"),
    MenuItem(restaurant_id=25, menu_id=25, name="Penguin's Pinot", description="A fine and fancy wine", price=9.99, type="drink", picture="path/to/penguin_pinot"),
    MenuItem(restaurant_id=25, menu_id=25, name="Bane's Brew", description="A powerful energy drink", price=5.99, type="drink", picture="path/to/banes_brew"),
    MenuItem(restaurant_id=25, menu_id=25, name="Joker's Julep", description="A laughably good drink", price=6.49, type="drink", picture="path/to/jokers_julep"),
    MenuItem(restaurant_id=25, menu_id=25, name="Harley's Hot Chocolate", description="Mischievously creamy", price=5.99, type="drink", picture="path/to/harleys_hot_chocolate"),
    MenuItem(restaurant_id=25, menu_id=25, name="Catwoman's Cappuccino", description="A smooth and stealthy brew", price=5.49, type="drink", picture="path/to/catwomans_cappuccino"),
    MenuItem(restaurant_id=25, menu_id=25, name="Riddler's Raspberry Soda", description="A fizzy enigma", price=4.99, type="drink", picture="path/to/riddlers_raspberry_soda"),
    MenuItem(restaurant_id=25, menu_id=25, name="Penguin's Pale Ale", description="A brew as cold as ice", price=6.99, type="drink", picture="path/to/penguins_pale_ale"),
    MenuItem(restaurant_id=25, menu_id=25, name="Two-Face Tea", description="A dual-flavored tea", price=4.99, type="drink", picture="path/to/two_face_tea"),
    MenuItem(restaurant_id=25, menu_id=25, name="Gotham Grog", description="A grog for night owls", price=5.29, type="drink", picture="path/to/gotham_grog"),
]

r25_sides = [
    MenuItem(restaurant_id=25, menu_id=25, name="Gotham Grits", description="Creamy and comforting", price=5.49, type="side", picture="path/to/gotham_grits"),
    MenuItem(restaurant_id=25, menu_id=25, name="Scarecrow's Slaw", description="Fearfully delicious", price=4.49, type="side", picture="path/to/scarecrow_slaw"),
    MenuItem(restaurant_id=25, menu_id=25, name="Harley's Hash Browns", description="Crispy and mischievous", price=4.99, type="side", picture="path/to/harleys_hashbrowns"),
    MenuItem(restaurant_id=25, menu_id=25, name="Poison Ivy's Polenta", description="Smooth and villainously rich", price=5.99, type="side", picture="path/to/poison_ivys_polenta"),
    MenuItem(restaurant_id=25, menu_id=25, name="Bane's Beans", description="Hearty and powerful baked beans", price=4.99, type="side", picture="path/to/banes_beans"),
    MenuItem(restaurant_id=25, menu_id=25, name="Catwoman's Carrots", description="Sliced carrots with a touch of elegance", price=4.49, type="side", picture="path/to/catwomans_carrots"),
    MenuItem(restaurant_id=25, menu_id=25, name="Riddler's Rice Pilaf", description="A side dish that poses questions", price=5.49, type="side", picture="path/to/riddlers_pilaf"),
    MenuItem(restaurant_id=25, menu_id=25, name="Harley's Hushpuppies", description="Fried to a crazy crunch", price=4.99, type="side", picture="path/to/harleys_hushpuppies"),
    MenuItem(restaurant_id=25, menu_id=25, name="Penguin's Potato Salad", description="Cold and calculating", price=5.49, type="side", picture="path/to/penguins_salad"),
    MenuItem(restaurant_id=25, menu_id=25, name="Two-Face Taters", description="Mashed with a dual personality", price=5.99, type="side", picture="path/to/two_face_taters"),
]

r25_desserts = [
    MenuItem(restaurant_id=25, menu_id=25, name="Batman's Brownie", description="The hero's favorite treat", price=7.49, type="dessert", picture="path/to/batmans_brownie"),
    MenuItem(restaurant_id=25, menu_id=25, name="Bat-Sundae", description="Ice cream with all the toppings", price=6.99, type="dessert", picture="path/to/bat_sundae"),
    MenuItem(restaurant_id=25, menu_id=25, name="Alfred's Apple Pie", description="A classic in Wayne Manor", price=6.49, type="dessert", picture="path/to/alfreds_pie"),
    MenuItem(restaurant_id=25, menu_id=25, name="Gotham Cheesecake", description="Creamy and indulgent", price=8.49, type="dessert", picture="path/to/gotham_cheesecake"),
    MenuItem(restaurant_id=25, menu_id=25, name="Riddler's Riddle Cake", description="A cake that leaves you guessing", price=7.99, type="dessert", picture="path/to/riddlers_cake"),
    MenuItem(restaurant_id=25, menu_id=25, name="Joker's Jello", description="Wobbly and whimsical", price=5.49, type="dessert", picture="path/to/jokers_jello"),
    MenuItem(restaurant_id=25, menu_id=25, name="Catwoman's Chocolate Mousse", description="Smooth and silky", price=8.49, type="dessert", picture="path/to/catwomans_mousse"),
    MenuItem(restaurant_id=25, menu_id=25, name="Bane's Brownie", description="A dessert that packs a punch", price=6.99, type="dessert", picture="path/to/banes_brownie"),
    MenuItem(restaurant_id=25, menu_id=25, name="Poison Ivy's Parfait", description="A sweet treat with a touch of nature", price=7.99, type="dessert", picture="path/to/poison_ivys_parfait"),
    MenuItem(restaurant_id=25, menu_id=25, name="Harley's Haunted Brownie", description="A brownie with a mischievous laugh", price=6.49, type="dessert", picture="path/to/harleys_brownie"),
]

# Restaurant 26
r26_entrees = [
    MenuItem(restaurant_id=26, menu_id=26, name="Justice League Burger", description="A burger fit for heroes", price=14.99, type="entree", picture="path/to/justice_league_burger"),
    MenuItem(restaurant_id=26, menu_id=26, name="Wonder Woman Wrap", description="Amazonian flavors in a wrap", price=16.99, type="entree", picture="path/to/wonder_woman_wrap"),
    MenuItem(restaurant_id=26, menu_id=26, name="Superman's Spaghetti", description="Spaghetti with superpowers", price=13.99, type="entree", picture="path/to/supermans_spaghetti"),
    MenuItem(restaurant_id=26, menu_id=26, name="The Flash's Fajitas", description="Fajitas in a flash", price=15.99, type="entree", picture="path/to/flashs_fajitas"),
    MenuItem(restaurant_id=26, menu_id=26, name="Aquaman's Sushi", description="Sushi from the depths", price=17.99, type="entree", picture="path/to/aquamans_sushi"),
    MenuItem(restaurant_id=26, menu_id=26, name="Green Lantern Grilled Chicken", description="Grilled to save the day", price=16.99, type="entree", picture="path/to/green_lantern_chicken"),
    MenuItem(restaurant_id=26, menu_id=26, name="Cyborg's Curry", description="High-tech curry experience", price=18.99, type="entree", picture="path/to/cyborgs_curry"),
    MenuItem(restaurant_id=26, menu_id=26, name="Batgirl's Burrito", description="A burrito with a sidekick", price=12.99, type="entree", picture="path/to/batgirls_burrito"),
    MenuItem(restaurant_id=26, menu_id=26, name="Martian Manhunter Meatloaf", description="Meatloaf from another world", price=19.99, type="entree", picture="path/to/martian_manhunter_meatloaf"),
    MenuItem(restaurant_id=26, menu_id=26, name="Green Arrow's Pizza", description="Pizza that hits the mark", price=17.99, type="entree", picture="path/to/green_arrows_pizza"),
]

r26_drinks = [
    MenuItem(restaurant_id=26, menu_id=26, name="Justice League Juice", description="A heroic blend of juices", price=5.49, type="drink", picture="path/to/justice_league_juice"),
    MenuItem(restaurant_id=26, menu_id=26, name="Wonder Woman's Wine", description="Divine and elegant wine", price=9.99, type="drink", picture="path/to/wonder_womans_wine"),
    MenuItem(restaurant_id=26, menu_id=26, name="Super Soda", description="A soda with super fizz", price=4.99, type="drink", picture="path/to/super_soda"),
    MenuItem(restaurant_id=26, menu_id=26, name="The Flash's Flashade", description="A lightning-fast lemonade", price=6.49, type="drink", picture="path/to/flashs_flashade"),
    MenuItem(restaurant_id=26, menu_id=26, name="Aquaman's Aqualyte", description="Hydrate like the king of the seas", price=5.99, type="drink", picture="path/to/aquamans_aqualyte"),
    MenuItem(restaurant_id=26, menu_id=26, name="Green Lantern Green Tea", description="Tea that ignites your willpower", price=5.49, type="drink", picture="path/to/green_lantern_tea"),
    MenuItem(restaurant_id=26, menu_id=26, name="Cyborg's Cyber Cola", description="Soda with a high-tech twist", price=4.99, type="drink", picture="path/to/cyborgs_cyber_cola"),
    MenuItem(restaurant_id=26, menu_id=26, name="Batgirl's Brew", description="A coffee with a sidekick", price=5.99, type="drink", picture="path/to/batgirls_brew"),
    MenuItem(restaurant_id=26, menu_id=26, name="Martian Manhunter Mojito", description="Mojito from another world", price=6.99, type="drink", picture="path/to/martian_manhunter_mojito"),
    MenuItem(restaurant_id=26, menu_id=26, name="Green Arrow's Gulp", description="A refreshing gulp for archers", price=5.29, type="drink", picture="path/to/green_arrows_gulp"),
]

r26_sides = [
    MenuItem(restaurant_id=26, menu_id=26, name="Justice League Fries", description="Fries with a heroic touch", price=5.49, type="side", picture="path/to/justice_league_fries"),
    MenuItem(restaurant_id=26, menu_id=26, name="Wonder Woman Wedges", description="Wedges fit for an Amazon", price=4.49, type="side", picture="path/to/wonder_woman_wedges"),
    MenuItem(restaurant_id=26, menu_id=26, name="Superman's Salad", description="A super salad", price=4.99, type="side", picture="path/to/supermans_salad"),
    MenuItem(restaurant_id=26, menu_id=26, name="The Flash's Fries", description="Fries in a flash", price=5.99, type="side", picture="path/to/flashs_fries"),
    MenuItem(restaurant_id=26, menu_id=26, name="Aquaman's Asparagus", description="Asparagus from the depths", price=4.99, type="side", picture="path/to/aquamans_asparagus"),
    MenuItem(restaurant_id=26, menu_id=26, name="Green Lantern Guacamole", description="Guacamole that ignites your willpower", price=4.49, type="side", picture="path/to/green_lantern_guacamole"),
    MenuItem(restaurant_id=26, menu_id=26, name="Cyborg's Coleslaw", description="High-tech coleslaw experience", price=5.49, type="side", picture="path/to/cyborgs_coleslaw"),
    MenuItem(restaurant_id=26, menu_id=26, name="Batgirl's Beans", description="Beans with a sidekick", price=4.99, type="side", picture="path/to/batgirls_beans"),
    MenuItem(restaurant_id=26, menu_id=26, name="Martian Manhunter Mash", description="Mashed potatoes from another world", price=5.49, type="side", picture="path/to/martian_manhunter_mash"),
    MenuItem(restaurant_id=26, menu_id=26, name="Green Arrow's Onion Rings", description="Onion rings that hit the mark", price=5.99, type="side", picture="path/to/green_arrows_onion_rings"),
]

r26_desserts = [
    MenuItem(restaurant_id=26, menu_id=26, name="Justice League Sundae", description="A heroic ice cream treat", price=7.49, type="dessert", picture="path/to/justice_league_sundae"),
    MenuItem(restaurant_id=26, menu_id=26, name="Wonder Woman Waffle", description="Amazonian waffle delight", price=6.99, type="dessert", picture="path/to/wonder_woman_waffle"),
    MenuItem(restaurant_id=26, menu_id=26, name="Superman's Sorbet", description="Super sorbet for super tastes", price=6.49, type="dessert", picture="path/to/supermans_sorbet"),
    MenuItem(restaurant_id=26, menu_id=26, name="The Flash's Flan", description="Flan in a flash", price=8.49, type="dessert", picture="path/to/flashs_flan"),
    MenuItem(restaurant_id=26, menu_id=26, name="Aquaman's Apple Pie", description="Pie from the depths", price=7.99, type="dessert", picture="path/to/aquamans_apple_pie"),
    MenuItem(restaurant_id=26, menu_id=26, name="Green Lantern Gelato", description="Gelato that ignites your willpower", price=5.49, type="dessert", picture="path/to/green_lantern_gelato"),
    MenuItem(restaurant_id=26, menu_id=26, name="Cyborg's Cheesecake", description="High-tech cheesecake experience", price=8.49, type="dessert", picture="path/to/cyborgs_cheesecake"),
    MenuItem(restaurant_id=26, menu_id=26, name="Batgirl's Brownie", description="A brownie with a sidekick", price=6.99, type="dessert", picture="path/to/batgirls_brownie"),
    MenuItem(restaurant_id=26, menu_id=26, name="Martian Manhunter Mousse", description="Mousse from another world", price=7.99, type="dessert", picture="path/to/martian_manhunter_mousse"),
    MenuItem(restaurant_id=26, menu_id=26, name="Green Arrow's Cake", description="Cake that hits the mark", price=6.49, type="dessert", picture="path/to/green_arrows_cake"),
]



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


def undo_menu_items():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.menu_items RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM menu_items"))
    db.session.commit()
