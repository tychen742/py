class Vehicle:
    wheels = 4

    def __init__(self):
        print("vehicle")

    def calcvelocity(self, x):
        return 3 * x + 10


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.speed = 10


exampleCar = Car()
print(exampleCar.speed)
print(exampleCar.calcvelocity(20))
print(exampleCar.wheels)
