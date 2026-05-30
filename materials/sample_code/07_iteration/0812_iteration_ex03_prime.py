# The question is erroneous to the answer.

def is_prime(n):
    # if ((n % 2 == 0) or (n % 3 == 0)):
    #     return False
    # else:
    #     return True

    # for i in range(2, n):
    #     print(i)
    #     if ((n % i) == 0):
    #         print(i, "dvisable")
    #         return False
    #
    #         # else:
    #         #     # print (i, "not divisable")
    #         #     return True
    # return True

    for i in range(2, n):
        while (n % i) == 0:
            return False
        else:
            print(i)
    return True


# n = 55071111111113
n = 17
result = is_prime(n)
print(result)
# print(n / 3)
