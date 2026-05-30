class Math:
    def __init__(self, x, y):           # ### class constructor
        self.x = x
        self.y = y

    @staticmethod
    def add(x, y):
        return x + y

    def subtract(self, a, b):
        x = self.x
        y = self.y
        print(f"self.x: {self.x}")
        return (a - b)

    def multiply(self, a, b):
        # x = self.x
        # y = self.y
        # print(f"self.x: {self.x}")
        return (a * b)
    
    def divide(self):
        return (self.x / self.y)
    
# static method
# belongs to the class and not to the instance
# does not require an instance of the class to be called
# called on the class itself or on an instance of the class
# does not require self as the first parameter
print(Math.add(2, 3))

# create an instance of the class passing the parameters
math = Math(2, 3)  # Create a new Math object
print(math.add(2, 3))  # This will work


# This works because subtract is a method of the instance
print(math.subtract(11, 3))
# math.subtract(2, 3) # This will raise an error because subtract is not a static method
# math = Math(2, 3) # Create a new Math object

print(math.multiply(11, 3)) # This will raise an error because multiply is not a static method

print(math.divide())