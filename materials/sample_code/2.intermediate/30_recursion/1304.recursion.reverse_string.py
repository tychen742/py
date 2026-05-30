# base
# change state toward base
# call function
def reverse(s, m, n):
    if n - m < 2:
        return s
    else:
        temp = s[m]
        print(temp)
        print(s[n])
        s = s[n:n + 1] + s[m + 1:n]
        print(s)
        s = s[m:m + 1] + temp
        print(s)
        m = m + 1
        n = n - 1
        return (reverse(s, m, n))


s = 'abcdef'
m = 0
n = len(s) - 1
print(reverse(s, m, n))
