class Mom:
    def eyes(self):
        print("Зеленые глаза")

class Dad:
    def hair(self):
        print("Темные волосы")

class Child(Mom, Dad):
    pass

baby = Child()
baby.eyes()
baby.hair()