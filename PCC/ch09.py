class Mammal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
