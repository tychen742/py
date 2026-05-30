# n-1 passes to sort
# in each pass, select the largest to temp and save it to the end of the list

lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(len(lista), ": length of original list")  # this is n
print(" ", lista)

# how many passes
for index in range(len(lista) - 1, 0, -1):  # comparison: n-1 times, until 0, decrementing 1
    print(index, end=" ")

    # how many to compare & swap in each pass
    tempMaxPosition = 0
    for location in range(1, index + 1):
        # print(" ", lista) # we don't swap until the end, so no changes here

        # compare to find the largest one, but don't swap until end of pass
        if lista[location] > lista[tempMaxPosition]:
            tempMaxPosition = location  # we want this

    # temp = lista[location] # the last value in list is index,
    # swap at the end of the pass
    temp = lista[index]  # the last value in list
    lista[index] = lista[tempMaxPosition]
    lista[tempMaxPosition] = temp

    print(lista, "end of round:", index)
