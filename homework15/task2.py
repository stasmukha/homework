class Dog:
    age_factor = 7
    
    def __init__(self, age,):
        self.age = age
        
    def human_age(self):
        result = self.age * self.age_factor
        print(result)
    
dog = Dog(7)

dog.human_age()