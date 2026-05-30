class Fraction:

    # a_random_int = 8
    # str repr: https://www.digitalocean.com/community/tutorials/python-str-repr-functions

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def show(self):
        print(self.numerator, "/", self.denominator)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


a_fraction = Fraction(3, 10)

print(a_fraction)

a_fraction.show()
