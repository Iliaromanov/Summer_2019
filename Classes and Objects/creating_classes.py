class Snake(objetcs):  # '(objects)' is not necessary
    def __init__(self, name):  
        self.name = name

    def talk(self):  # Method
        print(f"Yo dawgs im {self.name}")

    def change_name(self, new_name):  # Method
        self.name = new_name


bartholamule = Snake("Barhtolamule")

opa = Snake('Opa')

opa.change_name('Dundas')

if __name__ == "__main__":
    bartholamule.talk()
    opa.talk()
