from typing import List
class Book:
    def __init__(self, title, author, isbn, number_of_pages , genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.number_of_pages = number_of_pages
        self.available = True
        self.genre = genre
        
    def get_details(self):
        return f"Title : {self.title}, Author : {self.author}, ISBN : {self.isbn}, Number of pages : {self.number_of_pages}, genre : {self.genre}"
    
class Member:
    def __init__(self, name, membership_id, borrowed_books : List['Book']):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = borrowed_books
        
    def borrow_book(self, book : Book):
        if book.available:
            self.borrowed_books.append(book)
        else:
            return f"Book Is not available!"
        
    def return_book(self, isbn):
        for book in self.borrowed_books:
            if isbn == book.isbn:
                return book
        return "Book Does'nt Exist"
        
        
class Library:
    def __init__(self, name, location, books : List['Book'], members : List[Member]):
        self.name = name
        self.location = location
        self.books = books
        self.members = members
        self.fantasy = []
        self.science = []
        self.history = []
        
    def add_book(self, book : Book):
        if book.available:
            self.books.append(book)
        
    def genre_look(self, genre):
        genre_books = [book for book in self.books if book.genre.lower() == genre.lower()]
        if not genre_books:
            return "Doesnt exist"
        return "\n".join(book.get_details() for book in genre_books)
    
            
        
            
    def find_book(self, isbn):
        for item in self.books:
            if isbn == item.isbn:
                return item
        return "Cannot Found"    
    
    def find_member(self, id):
        for member in self.members:
            if id == member.membership_id:
                return member
        return "Cannot Found"    

    def remove_book(self, isbn):
        target = self.find_book(isbn)
        if target:
            self.books.remove(target)
        else:
            return "Doesnt Exist"
        
    def add_member(self, member : Member):
        if member not in self.members:
            self.members.append(member)
        else:
            return "Member already exist"
        
    def remove_member(self, id):
        target = self.find_member(id)
        if target:
            self.members.remove(target)
        else:
            return "Member doesnt Exist"
            
            
        
        
if __name__ == "__main__":
    lib = Library("Chad", "Pandi", [], [])
    d1 = Book("sun", "shin", 123, 256, "fantasy")
    lib.add_book(d1)
    print(lib.genre_look("fantasy"))