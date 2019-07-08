class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Yo nigga im {self.name} and I'm {self.age}")

    def talk(self):
        print(f"{self.name} says:  'Bark!'")


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)  # 'Dog' is the super class, and this basically copies lines 3 & 4
        self.color = color

    def talk(self):
        print(f"{self.name} says: 'Meaow!'")  # Every method in child class overrides the parent class methods


# opa = Dog('Opa', 16)

# dundas = Cat('Dundas', 5, 'purple')

# opa.speak()
# opa.talk()

# dundas.speak()
# dundas.talk()


'''
class Dog():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def talk(self):
        print(f"Yo nigga im {self.name}")
'''


class Vehicle:
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fill_up_tank(self):
        self.gas = 100

    def empty_tank(self):
        self.gas = 0

    def gas_left(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print("Beeep!")

class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print("Honk!")
