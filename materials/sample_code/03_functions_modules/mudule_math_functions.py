import math

# common modules used: Pi, Sqare Root,

# Pi
print ("pi = ", math.pi, "in Python. \n (Actually it depends on the capacity of your comptuer\n" )

pi_22_by_7 = 22/7
pi_355_by_113 = 355/113
pi_python = math.pi

print (pi_22_by_7)
print (pi_355_by_113)
print (pi_python)


# e
print ("e=", math.e, "\n")

# Take Square Root
# take_the_square_root_of_ = math.sqrt()  # note the math. namespace
square_root_of_9 = math.sqrt(9)
print(square_root_of_9)

# find the type of the variable square)root_of_9
print("The type of this sqaure root is:", type(square_root_of_9), "\n")
# Its class is float. ^^

# print(math.sin(math.radians(90)))

# sum & fsum
sum_1 = sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
print ("sum of 10 0.1 is: ", sum_1)
sum_2 = math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
print ("fsum of 10 0.1 is:", sum_2)

# sum is crappy
sum_test_2 = 0.1 + 0.1
print ("0.1 + 0.1 =", sum_test_2)
sum_test_3 = 0.1 + 0.1 + 0.1
print ("0.1 + 0.1 + 0.1 =", sum_test_3)
sum_test_4 = 0.1 + 0.1 + 0.1 + 0.1
print ("0.1 + 0.1 + 0.1 + 0.1 =", sum_test_4)
sum_test_5 = 0.1 + 0.1 + 0.1 + 0.1 + 0.1
print ("0.1 + 0.1 + 0.1 + 0.1 + 0.1 =", sum_test_5)

# Factorial
fact_10 = math.factorial(10)
print (fact_10)

# Power
# Square using Power
x = 10
power_of_something = math.pow(x, 2)
print (power_of_something)

# Hypotenuse + Power + SQRT
# x ^2 = y^2 + z^2
#x = 5
y = 3
z = 4

y2 = math.pow(y, 2)
z2 = math.pow(z, 2)
x = math.sqrt(y2 + z2)
print ("the hypotenuse x =", x)

hypotenuse = math.hypot(y, z)
print ("the hypotenuse x =", hypotenuse)

# print (math.sqrt(hypotenuse))


