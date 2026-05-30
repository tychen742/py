def myPi (n):
    # denominator = ( 1)
    sum = 0
    # x = 0
    for i in range(n):
        # denominator = (pow(-1, i) ) * (i * 2 + 1)
        denominator = ((-1) ** i ) * (i * 2 + 1)
        nominator = 1
        # print (denominator)
        value =  (nominator / denominator)
        # y = x
        print(value)
        sum = value + sum
        # print ("denominator =", denominator)
        # denominator = - denominator

        # print ("pi =", sum)

    return sum


print("Leibniz pi = ", 4 * myPi(1000))



# Write a function called myPi that will return an approximation of PI (3.14159...).
# Use the Leibniz approximation at https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
