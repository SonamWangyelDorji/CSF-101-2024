# Class definition (blueprint)
class Dog:
    def __init__(self, name, color, age): 
        self.name = name  
        self.color = color  
        self.age = age

    def bark(self):
        return f"{self.name} is {self.age} old and has {self.color} fur."

# Creating objects (instances)
a = Dog("Nima", "black", "1 year")
b = Dog("Dawa", "white", "2 years")
c = Dog("Bruno", "black and white", "2 years")

# Interacting with objects 
print(c.bark()) 
