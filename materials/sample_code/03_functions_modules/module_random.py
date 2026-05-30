import random

# generate a random number and from a range of numbers

# Keywords: Do not name your Python files using the keywords
# such as random. You will not be able to import random and
# you will see an error "TypeError: 'module' object is
# not callable" when you try to call random.

prob = random.random()
print("\nThe generated random number is:", prob)


diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
print("\nThe dice throw gives:", diceThrow)

random.randrange(1, 7)
random.randrange(1, 7, 2)
random.rangint()