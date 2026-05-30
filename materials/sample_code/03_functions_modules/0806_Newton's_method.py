def newtonsMethod(n, howMany):
    approx = 1 / 2 * n

    for i in range(howMany):
        betterApprox = 1 / 2 * (approx + n / approx)
        while betterApprox != approx:
            approx = betterApprox

    return approx


n = 9
howMany = 0
result = 0

while result != n ** (1 / 2):
    result = newtonsMethod(n, howMany)
    print(howMany, result)
    howMany = howMany + 1
print(howMany, "times to converge")


# while result != n**(1/2):
#     print(result)
#     newtonsMethod(100, howMany)
#     howMany = howMany - 1
