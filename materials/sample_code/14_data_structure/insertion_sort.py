lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(0, lista)

for index in range(1, len(lista)):

    # print(i, listA[i])
    position = index
    current_value = lista[index]

    # here is the sorted sub-list
    while position > 0 and lista[position - 1] > current_value:
        # compare all elements in the sublist to current_value one by one
        # replace if > current_value

        # temp = lista[index]
        # lista[index] = lista[index - 1]
        # lista[index - 1] = temp

        lista[position] = lista[position - 1]
        print("i", lista)

        position = position - 1


    # after
    lista[position] = current_value

    print(index, lista)
