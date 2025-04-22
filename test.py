from product import *
from inventory import *
from store import *

cart = Cart()
inv = Inventory()
alfamart = Store("Alfamart", "Bagong Barrio, Pandi", inv, cart)

# Add digital products
d1 = Digital_Product("Gosurf50", 50, 5, 123, 50.0)
d2 = Digital_Product("Gosurf150", 150, 5, 124, 150.0)
d3 = Digital_Product("Gosurf250", 250, 5, 125, 250.0)

inv.add_item(d1)
inv.add_item(d2)
inv.add_item(d3)

# Add physical product
p1 = Physical_Product("Pizza", 100, 2, 143, "2024-12-12", True)
inv.add_item(p1)

# Show all items
inv.show_items()

# Try updating stock
print(inv.update_stock(123, 10))

# Try adding item to cart
print(alfamart.process_add_cart(123, 2))  # Adds Gosurf50
print(alfamart.process_add_cart(143, 1))  # Adds Pizza

# Show cart
cart.show_cart()
