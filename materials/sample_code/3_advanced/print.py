# ##### the *-operator
# https://stackoverflow.com/questions/2921847/what-do-double-star-asterisk-and-star-asterisk-mean-in-a-function-call
# https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists


# test
# ### TODO: generate a random list
arr = [5, 7, 9, 1, 11, 101, 55]
print(arr, "(regular print list)")     # ### print using regular print


arr.sort()              # ### sort and change the list
print(arr, "(regular print list)")     # ### print using regular print
print(*arr, "(the *operator)")             # ### print using the * operator


for ele in arr:         # ### print using a for loop
    print(ele, end=" ")     # ### end replace the new line 
    # print(ele, sep=" ")   # ### sep will give unexpected results

print()
print(*arr, "(the 'sep' option)", sep=" ")    # ### print using the sep parameter
