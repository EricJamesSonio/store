from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self, total_amount):
        pass
    
class NoDiscount(Discount):
    def apply_discount(self, total_amount):
        return total_amount
    
class SeniorDiscount(Discount):
    def apply_discount(self, total_amount):
        return total_amount * 0.88
    
class PWDDiscount(Discount):
    def apply_discount(self, total_amount):
        return total_amount * 0.90
    

    
    