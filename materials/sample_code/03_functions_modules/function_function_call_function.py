
def square (x):
    x = x * x   # x is local variable in this function
    return x

def sum_of_squares (x, y, z):
    sum = square(x) + square(y) + square(z)     # x is local variable in this function
    return sum

result = sum_of_squares(1, 2, 3)
print(result)