from abc import ABC,abstractmethod
class LibraryItem(ABC):
    def __init__(self, title, barcode, author):
        self.title = title
        self.barcode = barcode
        self.author = author
        
    @abstractmethod
    def get_details(self):
        pass
    
class Book(LibraryItem):
    def get_details(self):
        return f"Title : {self.title} , Barcode : {self.barcode}, Author : {self.author}"

class Magazine(LibraryItem):
    def __init__(self, title, barcode, author, genre):
        super().__init__(title, barcode, author)
        self.genre = genre
        
    def get_details(self):
        return f"Title : {self.title}, Barcode : {self.barcode}, Author : {self.author}, Genre : {self.genre}"
    
class Newspaper(LibraryItem):
    def __init__(self, title, barcode, author, date):
        super().__init__(title, barcode, author)
        self.date = date
        
    def get_details(self):
        return f"Title : {self.title}, Barcode : {self.barcode}, Author : {self.author}, Date : {self.date}"
    
class Researchpaper(LibraryItem):
    def __init__(self, title, barcode, author, topic):
        super().__init__(title, barcode, author)
        self.topic = topic
        
    def get_details(self):
        return f"Title : {self.title}, Barcode : {self.barcode}, Author : {self.author}, Topic : {self.topic}"

class Library:
    def __init__(self, name, location, owner):
        self.name = name
        self.location = location
        self.owner = owner
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def display(self):
        for item in self.items:
            print(item.get_details())
        




class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_items = []
        

    

    

if __name__ == "__main__":
    student1 = Student("Eric", 789)
    library = Library("Library Store", "Bagong Bariio", "Eric")
    
    b1 = Book("Nothing", 234, "xander")
    m1 = Magazine("Club", 345, "Hand", "Style")
    
    library.add_item(b1)
    library.display()