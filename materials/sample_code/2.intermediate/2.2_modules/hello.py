### a variable 
sky_color = "blue"

### a function that RETURNS
def hello(name):
    return(f'Hi, {name}')  

# hello("T.Y. Chen")

### a class
class Person:
    def __init__(self, name, age):
        self.age = int(age)
        self.name = name

    def greet (self):
        print(f"{self.name} is", self.age, "years old.")
        
