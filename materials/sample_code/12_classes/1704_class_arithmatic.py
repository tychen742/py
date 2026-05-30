def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getDen(self):
        return self.den
    def getNum(self):
        return self.num

    def simplify(self):
        common = gcd(self.num, self.den)
        return str(self.num//common) + "/" + str(self.den//common)

    def add(self, q):
        newNum = self.num * q.den + self.den * q.num
        newDen = self.den * q.den
        common = gcd(newNum, newDen)
        return Fraction(newNum//common, newDen//common)

fract1 = Fraction(1, 3)
print(fract1)
print(fract1.simplify())

fract2 = Fraction(1, 4)
print(fract2)

print(gcd(fract1.den, fract2.den))

# print(gcd(2, 4))
addition = fract1.add(fract2)
print(addition)
##### there's got to be a better way: function calls class.method