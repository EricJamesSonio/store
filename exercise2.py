from abc import ABC, abstractmethod

# === Base Library Item ===
class LibraryItem(ABC):
    def __init__(self, title, code, author):
        self.title = title
        self.code = code
        self.author = author
        
    @abstractmethod
    def get_details(self):
        pass

# === Subclasses ===
class Book(LibraryItem):
    def get_details(self):
        return f"Title: {self.title}, Code: {self.code}, Author: {self.author}"

class Magazine(LibraryItem):
    def __init__(self, title, code, author, genre):
        super().__init__(title, code, author)
        self.genre = genre
        
    def get_details(self):
        return f"Title: {self.title}, Code: {self.code}, Author: {self.author}, Genre: {self.genre}"

class NewsPaper(LibraryItem):
    def __init__(self, title, code, author, date):
        super().__init__(title, code, author)
        self.date = date
        
    def get_details(self):
        return f"Title: {self.title}, Code: {self.code}, Author: {self.author}, Date: {self.date}"

class ResearchPaper(LibraryItem):
    def __init__(self, title, code, author, date):
        super().__init__(title, code, author)
        self.date = date
        
    def get_details(self):
        return f"Title: {self.title}, Code: {self.code}, Author: {self.author}, Date: {self.date}"

# === Library Class ===
class Library:
    def __init__(self, name, location, owner):
        self.name = name
        self.location = location
        self.owner = owner
        self.items = []  # List of dictionaries with 'item' and 'quantity'

    def add_item(self, item, quantity=1):
        for entry in self.items:
            if entry['item'].code == item.code:
                entry['quantity'] += quantity
                return
        self.items.append({'item': item, 'quantity': quantity})

    def find_item(self, barcode):
        for item in self.items:
            if item['item'].code == barcode:
                return item
        return None

    def remove_item(self, barcode, quantity):
        target = self.find_item(barcode)
        if target:
            if target['quantity'] > quantity:
                target['quantity'] -= quantity
            elif target['quantity'] == quantity:
                self.items.remove(target)
            else:
                return "Not enough stock!"
        else:
            return "Item doesn't exist"

    def display(self):
        for entry in self.items:
            print(entry['item'].get_details(), f"Quantity: {entry['quantity']}")

    def lend_item(self, student: "Student", barcode):
        target = self.find_item(barcode)
        if target and target['quantity'] > 1:
            target['quantity'] -= 1
        elif target and target['quantity'] == 1:
            self.items.remove(target)
        else:
            return "Item doesn't exist or not enough in stock"

        # Add to student's borrowed_items
        for entry in student.borrowed_items:
            if entry['item'].code == barcode:
                entry['quantity'] += 1
                return

        student.borrowed_items.append({'item': target['item'], 'quantity': 1})

# === Student Class ===
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_items = []  # List of dictionaries with 'item' and 'quantity'

    def borrow_item(self, barcode, library: 'Library'):
        library.lend_item(self, barcode)

    def display_borrowed(self):
        if not self.borrowed_items:
            print(f"{self.name} has not borrowed any items.")
        else:
            print(f"{self.name} borrowed:")
            for entry in self.borrowed_items:
                print(entry['item'].get_details(), f"Quantity: {entry['quantity']}")
