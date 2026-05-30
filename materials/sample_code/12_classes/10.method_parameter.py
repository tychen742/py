class Person:
    def __init__(self, gender, name):
        self.gender = gender
        self.name = name

    def display(self, value):
        print("You are a ", self.gender, ", and your name is ", self.name)
        print(value)


# ### create an object (instance of the class)
# ### arguments are passed to the constructor
# ### constructor is a special method that is called when an object is created
# ### constructor is used to initialize the object
# ### constructor is called when the object is created
person1 = Person('Male', 'Alex')

# ### create another object (instance of the class)
person2 = Person('Female', "Jane")

# ### call the display method of the object with own parameter
# ### display method is a normal instance method of the class
person1.display(100)
person2.display(1000)
