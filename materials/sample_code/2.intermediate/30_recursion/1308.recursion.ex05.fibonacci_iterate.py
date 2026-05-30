def fibo(start, step, n):
    sumup = 0
    for i in range(n):
        sumup = sumup + i * step
        print(sumup)
    return sumup


print(fibo(0, 1, 10))
