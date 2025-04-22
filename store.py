
class Store:
    def __init__(self, name, location, inventory, cart):
        self.name = name
        self.location = location
        self.inventory = inventory
        self.cart = cart
        
    def add_product(self,product):
        return self.inventory.add_item(product)
    
    def show_products(self):
        return self.inventory.show_items()
    
    def process_add_cart(self, barcode, quantity):
        item = self.inventory.find_item(barcode)
        if item and item.quantity >= quantity:
            self.cart.add(item, quantity)
            self.inventory.update_stock(barcode, -quantity)
            return f"Item {item.name} Quantity : {quantity} added to cart! "
        else:
            return "Product Not Available"
            
    def find_item_inventory(self, barcode):
        item = self.inventory.find_item(barcode)
        if item:
            return f"Item {item.name} Exist!"
        else:
            return f"Item does'nt Exist!"
            

class Cart:
    def __init__(self):
        self.items = []
        
    def add(self, item, quantity):
        for cart_item in self.items:
            if cart_item['item'].barcode == item.barcode:
                cart_item['quantity'] += quantity
                return 
        self.items.append({'item': item, 'quantity': quantity})
        
    def show_cart(self):
        print("< -- CART ITEMS -- >")
        for entry in self.items:
            item = entry['item']
            quantity = entry['quantity']
            print(f"{item.name} x{quantity} - ₱{item.price * quantity:.2f}")

    def remove(self, barcode, quantity):
        for cart_item in self.items:
            item = cart_item['item']
            if item.barcode == barcode:
                if cart_item['quantity'] == quantity:
                    self.items.remove(cart_item)
                    print(f"Removed all of {item.name} from cart.")
                elif cart_item['quantity'] > quantity:
                    cart_item['quantity'] -= quantity
                    print(f"Removed {quantity} from {item.name} in cart.")
                else:
                    print(f"Cannot remove {quantity}. Only {cart_item['quantity']} in cart.")
                return
        print("Item not found in cart.")
    

                

            
            
            
        
        