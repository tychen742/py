# this example is from w3schools: https://www.w3schools.com/python/python_polymorphism.asp
# ### 1/3 function polymorphism
x = "Hello World!"
print(len(x))

mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisdict))


# ### 2/3 class polymorphism: using the same method names in different classes
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

print("\n########## \n########## class inheritance polymorphism\
      \n########## Observe the move() ")

# ### 3/3 inheritance class polymorphism: using the same method names in different CHILD classes


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("A vehicle moves!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    # print(x.brand)
    # print(x.model)
    # x.move()
    print("inheritance polymorphism:", x.brand, x.model, end=" ")
    x.move()
