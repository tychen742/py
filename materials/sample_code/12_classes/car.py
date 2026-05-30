class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

my_car = Car("red", "Camry", 2019)
print(my_car.model)