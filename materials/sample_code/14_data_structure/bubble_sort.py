listA = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def bubble_sort(list):
    numTotal = 1
    for num_pass in range(len(list) - 1, 0, -1):
        for i in range(num_pass):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
            print(numTotal, list, i)
            numTotal += 1
    print(list, "final", numTotal)


bubble_sort(listA)

