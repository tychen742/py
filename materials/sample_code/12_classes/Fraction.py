class Fraction:

    # a_random_int = 8

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def show(self):
        print(self.numerator, "/", self.denominator)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


another_fraction = Fraction(3, 10)

print(another_fraction)

another_fraction.show()
