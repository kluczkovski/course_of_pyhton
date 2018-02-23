class Animal():
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def talk(self):
        return "miauuu"

class Dog(Animal):
    def talk(self):
        return "au au au au"


animals = [Dog("Angus"), Cat("Hanna"),  Dog("Angie")]

for animal in animals:
    print(animal.name + ": " + animal.talk())