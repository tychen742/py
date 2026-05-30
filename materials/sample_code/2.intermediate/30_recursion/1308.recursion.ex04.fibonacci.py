def fibonacci(start, step, n):
    num = []
    for i in range(n + 3):
        if i < 2:
            print('nothing')
        else:
            num[i] = num[i - 1] + num[i - 2]

    return num


step = 1
start = 0
num = 10
print(fibonacci(start, step, num))
