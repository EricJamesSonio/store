from product import *
from inventory import Inventory

inv = Inventory()
d1 = Digital_Product("Gosurf50", 50, 5, 123, 50.0)
d2 = Digital_Product("Gosurf150", 150, 5, 124, 150.0)
d3 = Digital_Product("Gosurf250", 250, 5, 125, 250.0)
inv.add_item(d1)

p1 = Physical_Product("Pizza", 100, 2, 143, 2024-12-12, True)
print(inv.find_item(123))
print(inv.update_stock(123, 10))

print(d1.get_details())
print(p1.get_details())

inv.show_items()