# Area of circle

pi = 3.14159

# r = 5
r = input("Please input the radius (r) of the circle: ")  # Note that input values are type string
# The above line will get you error because r is assigned a STRING TYPE VALUE
r = float(r)
# Now r is updated by reassignment (that's one way to manipulate variables)

area = pi * r ** 2

print(area)

# Note you will get an answer of something like "31415.899999999998".  WHY???

# Extra credit question for today!!!
