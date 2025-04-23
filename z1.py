from abc import ABC, abstractmethod
from typing import List, Optional

class Course(ABC):
    def __init__(self, course_id, name, units : int):
        self.course_id = course_id
        self.name = name
        self.units = units

    @abstractmethod
    def get_details(self):
        pass

class BSBA(Course):
    def __init__(self, course_id, name, units):
        super().__init__(course_id, name, units)   

    def get_details(self):
        return f"Name : {self.name}, Course Id : {self.course_id}, Units : {self.units}"
    
class BSA(Course):
    def __init__(self, course_id, name, units):
        super().__init__(course_id, name, units)   

    def get_details(self):
        return f"Name : {self.name}, Course Id : {self.course_id}, Units : {self.units}"
    
class BSCA(Course):
    def __init__(self, course_id, name, units):
        super().__init__(course_id, name, units)   

    def get_details(self):
        return f"Name : {self.name}, Course Id : {self.course_id}, Units : {self.units}"
    
class Student:
    def __init__(self, student_id ,name, registered_course : List['Course']):
        self.student_id = student_id
        self.name = name
        self.registered_course = registered_course
        
    def __repr__(self):
        return f"Name : {self.name}, Id : {self.student_id}"
    
    def register(self, course : Course):
        if course in self.registered_course:
            print("Course Already Exist")
        else:
            self.registered_course.append(course)
            
    def get_course(self, id):
        for course in self.registered_course:
            if id == course.course_id:
                return course
        return None
            
        
        
        
        
    
class University:
    def __init__(self, name, student : List['Student'], course : List['Course']):
        self.name = name
        self.student =student
        self.course = course
        
    def add_student(self, student : 'Student'):
        self.student.append(student)
        
    def add_course(self, course : Course):
        self.course.append(course)
        
    def find_student(self, id):
        for stud in self.student:
            if id == stud.student_id:
                print(f"Student Found!", repr(stud))
                return stud
            
        return "Student Does'nt Exist"
    
    def find_course(self, id):
        for cor in self.course:
            if id == cor.course_id:
                print("Found Course!", cor.get_details())
                return cor
            

    

        
         