
def sqrt (n):
    oldguess = n / 2;
    for i in range (n):
        newguess = (1 / 2) * (oldguess + (n / oldguess))
        oldguess = newguess
    return newguess
n = 900
print (sqrt(n))

