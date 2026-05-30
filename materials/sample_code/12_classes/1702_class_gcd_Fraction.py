##### helper function (gcd) and mutator method(simplify)
def gcd(m, n):
#    print("m =", m ,", n =", n)
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
#        print("m =", m, ", n =", n)

    return n

# print(gcd(1244, 166666))

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den
    def simply(self):
        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

fract = Fraction(30, 40)
print(fract)
fract.simply()
print(fract)