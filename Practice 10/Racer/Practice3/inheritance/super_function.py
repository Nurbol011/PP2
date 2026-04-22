class Animal:
    def __init__(self):
        print("Животное создано")

class Dog(Animal):
    def __init__(self):
        super().__init__()  # Вызываем логику родителя
        print("Собака создана")

dog = Dog()