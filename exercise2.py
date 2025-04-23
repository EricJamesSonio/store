from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, code, author):
        self.title = title
        self.code = code
        self.author = author
        
    @abstractmethod
    def get_details(self):
        pass
    
class Book(LibraryItem):
    def get_details(self):
        return f"Title : {self.title}, Code : {self.code}, Author : {self.author}"
    
class Magazine(LibraryItem):
    def __init__(self, title, code, author, genre):
        super().__init__(title, code, author)
        self.genre = genre
        
    def get_details(self):
        return f"Title : {self.title}, Code : {self.code}, Author : {self.author}, Genre : {self.genre}"
    
class NewsPaper(LibraryItem):
    def __init__(self, title, code, author, date):
        super().__init__(title, code, author)
        self.date = date
        
    def get_details(self):
        return f"Title : {self.title}, Code : {self.code}, Author : {self.author}, Date : {self.date}"
    
class ResearchPaper(LibraryItem):
    def __init__(self, title, code, author, date):
        super().__init__(title, code, author)
        self.date = date
        
    def get_details(self):
        return f"Title : {self.title}, Code : {self.code}, Author : {self.author}, Date : {self.date}"

class Library:
    def __init__(self, name, location, owner):
        self.name = name
        self.location = location
        self.owner = owner
        self.items = []

    def add_item(self, item):
        self.items.append(item)  

    def find_item(self, barcode):
        for item in self.items:
            if barcode == item.barcode:
                return item
        return None
    
    def remove_item(self, barcode, quantity):
        target = self.find_item(barcode)
        if target and target.quantity > quantity:
            target.quantity =- quantity
        else:
            return "Item Doesnt Exist"
        
    def display(self):
        for item in self.items:
            print(item.get_details())
            

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_items = []
        
    def borrow_item(self, item):
        pass
    

