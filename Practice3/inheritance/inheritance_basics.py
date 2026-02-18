class Animal:
    def breathe(self):
        print("Дышу")

class Dog(Animal):
    pass

dog = Dog()
dog.breathe()  # Собака умеет дышать, потому что она Animal