# Free of financial burdens?  Check this out!!

P = 10000
n = 12
r = 0.05

t = float(input("Please enter the number of year(s): "))
# t = 15

# amount = P ((1 + (r/n))**(n*t))   # This will produce error because P is considered a function
amount = P * ((1 + (r / n)) ** (n * t))  # This will work. Programming language is not tolerant with ambiguity.

print(amount)
