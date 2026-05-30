##### == or is in Python refer to obj reference (shallow)
##### in human world, equal means same values (deep)

def sameFraction(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())


class Fraction:
    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def getNum(self):
        return self.num
    def getDen(self):
        return self.den

fract1 = Fraction(3, 4)
print(fract1)

fract2 = Fraction(3, 4)
print(fract2)

print(fract1 == fract2)
print(fract1 is fract2)
print(sameFraction(fract1, fract2))