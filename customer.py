from discount import *
from store import *

class Customer:
    def __init__(self, customer_id, name, discount_strategy):
        self.customer_id = customer_id
        self.name = name
        self.discount_strategy = discount_strategy
        self.cart = Cart()

    def add_to_cart(self, item, quantity):
        self.cart.add(item, quantity)

    def view_cart(self):
        self.cart.show_cart()

    def checkout(self):
        total = self.cart.calculate_total()
        return self.discount_strategy.apply_discount(total)

