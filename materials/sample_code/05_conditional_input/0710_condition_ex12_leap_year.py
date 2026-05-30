
def isLeapYear (year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False

result = isLeapYear(200)
print (result)