class Person:
    def __init__(self, gender, name):
        self.gender = gender
        self.name = name
    def display(self, value):
        print("You are a ", self.gender, ", and your name is ", self.name)
        print(value)
people = Person('Male', 'Alex')
people2 = Person('Female', "Jane")
people.display(100)
people2.display(1000)

