def gcd(m, n):
    while m%n !=0 :
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

print(gcd(180, 160))

# m, n
# 12, 16
# m%n != 0
# oldm = 12
# oldn = 16
# m = oldn = 16
# n = oldm%oldn = 12%16 = 12
#
# m, n
# 16, 12
# m%n = 4
# oldm = 16
# oldn = 12
# m = oldn = 12
# n = oldm%oldn = 4
#
# m, n
# 12, 4
# m%n = 0
# break loop
# return n