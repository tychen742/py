##### using for loop
def sum_to(bound):
    sum = 0
    for i in range(1, bound + 1):
        sum = sum + i
    return sum
print(sum_to(4))
print(sum_to(100))

##### using while loop
def sumto(bound):
    a = 0
    sum = 0
    while a <= bound:
        sum = sum + a
    #    print(a)
        a = a + 1
    return sum
#    print("The sum is: ", sum)
print(sumto(4))
print(sumto(100))





