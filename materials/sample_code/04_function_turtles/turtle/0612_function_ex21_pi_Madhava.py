import math

def myPi (n):

    sum = 0

    for i in range(n):
        nominator = 1
        denominator = (pow(-1, i) ) * (i * 2 + 1)
        # denominator = ((-1) ** i ) * (i * 2 + 1)
        # print (denominator)
        # term = pow(3,  n)
        term = 3 ** i
        print (type(term))
        # term = pow(3,  i)
        print("term  =", term)

        value =  (nominator / (denominator * term))
        print ("value =", value)
        print(type(value))

        sum = value + sum
        print ("sum   =", sum)

        print()

    return sum

# print(type(myPi(5000)))   # was skipped?????????????
print ("pi = ", (math.sqrt(12)) * (myPi(5000)))


