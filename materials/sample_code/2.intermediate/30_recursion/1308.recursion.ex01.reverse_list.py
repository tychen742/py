def reverseList(lst):
    lstTemp = []
    if len(lst) < 2:
        return lst
    else:
        if len(lst) % 2 == 0:
            lstTemp.insert(0, lst[len(lst) // 2 - 1])
            (lst[len(lst) // 2 - 1]) = lst[len(lst) // 2]
            lst[len(lst) // 2] = lstTemp[0]
            return reverseList(lst)


lst = [1, 2, 3, 4]
print(reverseList(lst))
