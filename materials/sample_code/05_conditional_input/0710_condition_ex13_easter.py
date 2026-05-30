def calcEaster (year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dateOfEaster = 22 + d + e

    specialYear = [1954, 1981, 2049, 2076]
    for i in  (specialYear):
        if year == specialYear:
            dateOfEaster = dateOfEaster - 7
    if dateOfEaster <= 31:
        return ("March ", dateOfEaster)
    elif dateOfEaster > 31:
        return ("April ", (dateOfEaster - 31))
    else:
        return ("Something is wrong.")

    # return dateOfEaster

def main ():
    print()
    year = int(input("Please enter a year: "))
    if (1900 <= year <= 2099):
        result = calcEaster(year)
        print ("The date of Easter is ", result)
    else:
        print ("Please enter a year between 1900 and 2099")

if __name__ == '__main__':
    main()