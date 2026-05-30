def newtonsMethod(n, howMany):
    approx = 1 / 2 * n
    betterApprox = 1 / 2 * (approx + n / approx)
    print(betterApprox)

    while betterApprox != approx:
        approx = betterApprox
        betterApprox = 1 / 2 * (approx + n / approx)
        print(betterApprox, end=" ")
        howMany = howMany + 1
        print(howMany)
    return approx, howMany


n = 10
howMany = 1
# result = 0

# while result != n ** (1 / 2):
result = newtonsMethod(n, howMany)
print(result)
#     howMany = howMany + 1

# print(howMany, "times to converge")
