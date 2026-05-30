import math

def findHypot (a, b):

    hypotenuse = math.sqrt (a**2 + b**2)
    return hypotenuse

def main ():
    result = findHypot(12, 5)
    print (result)
    print (type(result))

if __name__ == '__main__':
    main()