# create a class called person, wth 3 attributes, name, age, and gender
# then create a constructor method and method and object
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        print(f"Your name is {self.name}, the age {self.age}, and gender {self.gender}")

#instance of the class /object
P1=Person(name="Ernest", age=18, gender="Male")
P1.display()