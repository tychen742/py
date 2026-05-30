a = "banana"  ### a is a variable, "banana" is an object
b = "banana"  ### b is a variable, "banana" is an object

print(a == b)
print(a is b)
### (is: object test) is will return True if two variables point to the same object,
### (==: value test) == if the objects referred to by the variables are equal
print(id(a))  ### a points (REFER) to OBJECT 4302994600
print(id(b))  ### b also points (REFER) to OBJECT 4302994600

### a and b have the same REFERENCE, which is the String Object "banana".
### Strings are immutable, so Python make the two variables that refer to
### the same string (in memory) refer to the same object instead of creating
### another reference

##### But, Lists are mutable!!
a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)  ### return False because List is Collection of References to
### objects, a and b each has a Collection
print(a == b)
### Integers are immutable, so Python makes a and b share the integer objects.
