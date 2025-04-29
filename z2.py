from typing import List, Optional

class Book:
    used_isbn = set()
    def __init__(self, title, author, isbn, available_copies = True):
        if isbn in Book.used_isbn:
            raise ValueError(f"Hey {isbn} already been used!")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies
        Book.used_isbn.add(isbn)
        
        
    def __repr__(self):
        return f"Title : {self.title}, Author : {self.author}, Isbn : {self.isbn}, Available_copies : {self.available_copies}"
    
class Student:
    
    borrowed_count = 0
    
    def __init__(self, student_id, name, borrowed_books : list['Book']):
        self.student_id = student_id
        self.name = name
        self.borrowed_books = borrowed_books
        
    def __repr__(self):
        book = ', '.join([str(book) for book in self.borrowed_books])
        return f"Name : {self.name}, Id : {self.student_id}, Borrowed_Books : [{book}]"
    
    def borrow_book(self, book : Book, library : 'Library'):
        if Student.borrowed_count == 3:
            return "Maximum Borrowed Books"
        else:
            if book in library.books:
                if book.available_copies == True:
                    self.borrowed_books.append(book)
                    book.available_copies == False
                    Student.borrowed_count += 1
                    return f"Book : {book.title} is borrowed by {self.name}"
                else:
                    return "Not Available"
            
            else:
                return "Doesnt exist"
        
    def return_book(self, book : Book, library : 'Library'):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.add_book(book)
        else:
            return "Book Doesnt exist"
            
    def show_borrowed(self):
        for item in self.borrowed_books:
            print(f"Item : {item.__repr__()}")
            
     
class Library:
    def __init__(self, books : List['Book'], student : List['Student']):
        self.books = books
        self.registered_student = student
        
    def add_book(self, item : Book):
        if item in self.books:
            item['quantity'] += 1
            item.available_copies == True
        else:
            self.books.append(item)
            
    def register_student(self, student : Student):
        if student in self.register_student:
            return "Already in the List"
        else:
            self.registered_student.append(student)
            return f"Student : {student.name} Is Registered"
        
    def available_books(self):
        for book in self.books:
            print(book.__repr__())
            
    def display_registered_student(self):
        for stud in self.registered_student:
            print(stud.__repr__())
            

        
        
            


            
        
        
        
