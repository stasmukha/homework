class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        
class Student(Person):
    def __init__(self, first_name, last_name, age, course):
        super().__init__(first_name, last_name, age)
        self.course = course
        
class Teacher(Person):
    def __init__(self, first_name, last_name, age, salary):
        super().__init__(first_name, last_name, age)
        self.salary = salary