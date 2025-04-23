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

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_items = []
        
    def borrow_item(self, library : "Library", barcode ):
        library.lend_item(self, barcode)
    
    def back_item(self, barcode, library : "Library"):
        for item in self.borrowed_items:
            if barcode == item.barcode:
                self.borrowed_items.remove(item)
                library.add_item(item)
                print(f" ITem : {item.title} Back to the library")
                
    def display_borrowed_items(self):
        for item in self.borrowed_items:
            print(item.get_details())
            
        
class Library:
    def __init__(self, name, location, owner):
        self.name = name
        self.location = location
        self.owner = owner
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, barcode):
        for item in self.items:
            if barcode == item.barcode:  
                self.items.remove(item) 
                return f"Item {item.title} Remove!"
        return "Item doesnt exist"     
    
    def lend_item(self, student : Student, barcode):
        for item in self.items:
            if barcode == item.barcode:
                self.items.remove(item)
                student.borrowed_items.append(item)
                print(f"Item : {item.title} is Being Borrowed")
                return
        print("Item doesnt exist")
                

    def display(self):
        for item in self.items:
            print(item.get_details())
            

    
if __name__ == "__main__":
    student1 = Student("Eric", 789)
    library = Library("Library Store", "Bagong Bariio", "Eric")
     
    b1 = Book("Nothing", 234, "xander")
    m1 = Magazine("Club", 345, "Hand", "Style")
    
    library.add_item(b1)
    print(library.remove_item(234))
    library.display()