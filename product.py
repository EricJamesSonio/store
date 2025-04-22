from abc import ABC,abstractmethod
from datetime import date

class Product(ABC):
    def __init__(self, name, price , quantity, barcode):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.barcode = barcode
        
    @abstractmethod
    def get_details(self):
        pass
    
class Digital_Product(Product):
    def __init__(self, name, price, quantity, barcode, size_mb : float):
        super().__init__(name, price, quantity, barcode)
        self.size_mb = size_mb
        
    def get_details(self):
        return f"[Digital Product] Name : {self.name}, Price : {self.price}, Quantity : {self.quantity}, Barcode : {self.barcode}, Size : {self.size_mb}"
        
    
class Physical_Product(Product):
    def __init__(self, name, price, quantity, barcode, expiration_date : date, fda_approve : bool):
        super().__init__(name, price, quantity, barcode)
        self.expiration_date = expiration_date
        self.fda_approve = fda_approve
        
    def get_details(self):
        return f"[Physical Product] Name : {self.name}, Price : {self.price}, Quantity : {self.quantity}, Barcode : {self.barcode}, Exp : {self.expiration_date}, Fda_Approve : {self.fda_approve}"
    


    
