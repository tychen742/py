class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog("Fido")

d.add_trick("Play Dead")

print(d.tricks)
print(d.name)