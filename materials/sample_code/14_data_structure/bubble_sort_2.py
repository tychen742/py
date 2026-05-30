def bubbleSort(alist):
    length = len(listNum)
    print("length: ", length)

    print("   ", listNum)

    for i in range(length, 0, -1):
        for index in range(0, i - 1, +1):
            # print(index, end="")

            if listNum[index] > listNum[index + 1]:
                temp = listNum[index]
                listNum[index] = listNum[index + 1]
                listNum[index + 1] = temp

                print("len", i, "compare", index, listNum)

            # print(index, listNum)


listNum = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(listNum)
