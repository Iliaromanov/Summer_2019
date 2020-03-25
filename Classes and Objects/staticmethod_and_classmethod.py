
# Class method is to access class variables without having any objects

# static method is to make functions not related to self within a class

class Dog:

    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod  # decorator
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod  # decorator
    def bark(n):
        for _ in range(n):
            print("Bark!")


bob = Dog("Bob")
bret = Dog("Bret")

print(Dog.num_dogs())  # Without class method would have to say bob.num_dogs() or bret.num_dogs()

Dog.bark(4) 
