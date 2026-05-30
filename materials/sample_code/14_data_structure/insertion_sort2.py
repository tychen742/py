# my version is better than the thinkds version
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(0, alist)

for i in range(1, len(alist)):

    position = i
    current_value = alist[position]

    while position > 0 and alist[position - 1] > current_value:
        alist[position] = alist[position - 1]

        alist[position - 1] = current_value

        print("i", alist)
        position = position - 1

    print(i, alist)

print(alist)
