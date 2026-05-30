import random
print()

# print 10 random numbers
print ("Print 5 random numbers:")
for i in range (5):
    # print (random.random()) # do not directly print random.random()
    rand = random.random()
    print (rand)

print()

print("print 10 random numbers between 25 and 35")
for i in range (10):
    # print (int (25 + random.random()*11))
    print (25 + int(random.random()*11)) #

print()

print("print 10 random numbers between 25 and 35")
for i in range (10):
    # print (random.random(25, 36))
    # rand = random.random(25, 36)
    rand = random.randrange(25, 36)
    print (rand)
    # directly use the random function