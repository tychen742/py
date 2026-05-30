class Math:

    def add(a, b):
        return a + b

    def subtract( a, b):
        return (a - b)

    def multiply(a, b):
        return (a * b)
    
    def divide(a, b):
        return (a / b)
    


# create an instance of the class passing the parameters
math = Math()  # Create a new Math object
print(math.add(2, 3))  # This will work


# This works because subtract is a method of the instance
print(math.subtract(11, 3))
# math.subtract(2, 3) # This will raise an error because subtract is not a static method
# math = Math(2, 3) # Create a new Math object

print(math.multiply(11, 3)) # This will raise an error because multiply is not a static method

print(math.divide())