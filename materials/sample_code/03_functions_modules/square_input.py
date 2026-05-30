# some changes here.

def Square(x, p):
    # power = p  # nonsensical, don't mix global with local
    y = x ** p
    return y  # ^^ always return

base = int (input ("Please enter the base:"))
power = int (input ("Please enter the power:"))

result = Square(base, power)
print ("The result is:", result)