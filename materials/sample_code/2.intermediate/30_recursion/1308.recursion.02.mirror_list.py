def reverse(lst, m, n):
    # if lst[m] == lst[n]:
    if not abs(m - n) > 1:
        return lst
    else:

        temp = lst[m]
        lst[m] = lst[n]
        lst[n] = temp
        m = m + 1
        n = n - 1
        return reverse(lst, m, n)


lst = ['a', 'b', 'c', 'd', 'e', 'f']
m = 0
n = len(lst) - 1
print(reverse(lst, m, n))

# VCS test
