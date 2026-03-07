class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def move(self):
        print(f"{self.brand} is moving at {self.speed} kmph")
class Car(Vehicle):
    def __init__(self, brand, speed, feultype):
        super().__init__(brand, speed)
        self.feultype = feultype
    def honk(self):
        print(f"{self.brand} goes beep beep")
class ElectricCar(Car):
    def move(self):
        print(f"{self.brand} is moving silently at {self.speed} kmph")

car1 = ElectricCar("Tesla", 150, "Electric")
car1.move()
car1.honk()