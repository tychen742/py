#  harmonic series
#  Sigma(1, infinite) of ( 1 / n**p), p = 1


def p_series(j, p, n):
    total = 0
    for i in range(n):
        total = 1 / (j ** p) + total
        # print("sum = ", sum)
        j = j + 1
        # print(i, ": total + ", 1/j**p, "=", total)
    return total


result = p_series(1, 1, 100000000)

print("sum = ", result)
