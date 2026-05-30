def selection_sort(list):
    for length_each_pass in range(len(list) - 1, 0, -1):

        index_max = 0
        for i in range(1, length_each_pass + 1):

            if list[index_max] < list[i]:
                index_max = i

        # switch
        temp_max = list[index_max]
        list[index_max] = list[length_each_pass]
        list[length_each_pass] = temp_max
        # end of switch

        print(list)


listA = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(listA, "original")
selection_sort(listA)
