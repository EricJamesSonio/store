class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, product):
        self.items.append(product)
        return f"Product : {product.name} succesfully addded to Inventory!"
    
    def remove_item(self, barcode):
        for item in self.items:
            if barcode == item.barcode:
                self.items.remove(item)
                return f"Item {item.name} is remove from the Inventory!"
            
    def show_items(self):
        if not self.items:
            return f"Empty Inventory!"
        else:
            for item in self.items:
                print(" - ", item.get_details())
                
    def find_item(self, barcode):
        for item in self.items:
            if barcode == item.barcode:
                return item
        return None

    def update_stock(self, barcode, quantity):
        product = self.find_item(barcode)
        if product:
            product.quantity += quantity
            return f"Added {quantity} to {product.name}"
        else:
            return f"Item does not exist"
        

                
                