def sumUntilEven(lst):
    # your code here
    sum = 0
    for num in lst:
        if num % 2 == 0:
            return sum  ### to break, just RETURN
        else:
            sum = sum + num
    return sum


lst = [1, 3, 5, 6]
print(sumUntilEven(lst))
