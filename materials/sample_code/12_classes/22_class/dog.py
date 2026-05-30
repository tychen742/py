class Dog:

    def __init__(self, name):           # ### clas constructor
        self.name = name
        self.tricks = []

    def add_trick(self, trick):         
        self.tricks.append(trick)

d = Dog("Fido") # Create a new Dog object
# d = Dog()  # Create a new Dog object: parameter name is required

d.add_trick("Play Dead")
d.add_trick("Retrieve Stick")
d.add_trick("Jump")

print(d.tricks)
print(d.name)