# This example is to show scalability of OO programming.
# You can pass any number of keys and values into a dictionary held by a class.


class Example:
    def __init__(self, **kwargs):  # keyword argument; ** means dictionary; * : tuple
        self.variables = kwargs

    def set_vars(self, key, value):  # setter to set the values we need
        self.variables[key] = value

    def get_vars(self, key):
        return self.variables.get(key, None)


var = Example()
var.set_vars('name', 'Chen')

var = Example(Age=36, Location='US')
print(var.get_vars('name'))
print(var.get_vars('Location'))
print(var.get_vars('Age'))

var = Example(Age=38, Location='US')
print(var.get_vars('Age'))

var = Example(President='Trump')
print(var.get_vars('President'))
