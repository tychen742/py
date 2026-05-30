
def sum_list_len(lst):
    sum = 0
#    print(len(lst))
    for ele in range(0, len(lst)):
        sum = sum + lst[ele]
    return sum

list = [ 1, 3, 5 ]
print(sum_list_len(list))


def sum_list(lst):
    sum = 0
    for element in lst:
        sum = sum + element
    return sum

list2 = [ 1, 3, 5 ]
print(sum_list(list2))

def recur_sum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + recur_sum(numlist[1:])

list3 = [1, 3, 5 ]
print(recur_sum(list3))