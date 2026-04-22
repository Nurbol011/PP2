class Animal:
    def sound(self):
        print("...")

class Dog(Animal):
    def sound(self):
        print("Гав!")

dog = Dog()
dog.sound()  # Выведет "Гав!"