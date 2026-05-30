def sum_recursion(sumList):
    if len(sumList) == 1:  # BASE CASE and STOP CLAUSE
        return sumList[0]
    else:
        return sumList[0] + sum_recursion(sumList[1:])
        # return sumList


int_list = [1, 3, 5, 7, 9]
print('Summation:', sum_recursion(int_list))


def factorial(num):
    if num <= 1:  # check to see if condition is met; base case & stop clause
        return num
    else:
        return num * factorial(num - 1)  # calling function itself


print('Factorial:', factorial(1))


def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]


print('Converted:', toStr(1453, 16))  # 1453


def base_conversion(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:  # base case
        return convertString[n]
    else:
        return base_conversion(n // base, base) + convertString[n % base]  # calling self


print('Conversed:', base_conversion(18, 16))
