
import datetime
from datetime import datetime
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]

product_ids = []

while True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items:")
    if product_id == "DONE":
        print("THANKS ALL DONE HERE")
        break
    else:
        print("THE PRODUCT IDENTIFIER IS: " + str(product_id))
        product_ids.append(product_id)

today = datetime.now()
currentdate = str(today.year) +"-"+ str(today.month) +"-"+ str(today.day)
currenthour  = today.hour
currentminute = today.minute
currentsecond = today.second


print("-------------------------------")
print("Whole Foods Overpriced Groceries")
print("-------------------------------")
print("http://www.wholefoodsmarket.com")
print("Phone: 1.123.456.7890")
print("CHECKOUT TIME:", str(currentdate), str(currenthour) + ":" + str(currentminute)
+ ":" + str(currentsecond))
print("-------------------------------")
print("Shopping Cart Items:")
def get_product_id(product_id):
    return [product["name"] for product in products if product["id"]==product_id]
def get_product_price(product_id):
    return [product["price"] for product in products if product["id"]==product_id]
for product_id in product_ids:
    matching_id = get_product_id(product_id)
    matching_price = get_product_price(product_id)
    print("+",str(matching_id), str(matching_price))
print("-------------------------------")
product_price=[]
for product in products:
    for product_id in product_ids:
        if product["id"] == product_id:
            product_price.append(product["price"])
subtotal=sum(product_price)
tax = subtotal*.08875
total = tax+subtotal
print("Subtotal ",subtotal)
print("Plus NYC Sales Tax (8.875%): ", tax)
print("Total: ",total)
print("-------------------------------")
print("Don't come back you're wasting your money")









# def get_products(department_name):
#   return [product for product in products if product["department"] == department_name]

# print "There Are".upper(),len(departments),"Departments:".upper()
# for dep in departments:
#     matching_products= get_products(dep)
#     print("+" + dep.title() + "(" + str(len(matching_products))+ " " + "Products)")
#
# print(product_ids)
