def reverse(lst, m, n):
    # if not (m - n) < 1 :
    if (m >= len(lst) / 2):
        return lst
    else:

        temp = lst[m]
        lst[m] = lst[n]
        lst[n] = temp
        m = m + 1
        n = n - 1
        return reverse(lst, m, n)


lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
m = 0
n = len(lst) - 1
print(reverse(lst, m, n))

# VCS test
