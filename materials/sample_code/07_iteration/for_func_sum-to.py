# a_list = [1, 2, 3, 4, 5, "haha"]
# # print(type(a_list))

# for thing in a_list:
#     print(thing, end=" ")

# print("\n")

# for x in range(10):
#     print(x, end=" ")
    
# print("\n")

# print(a_list)


def sum_to(bound):
    sum = 0
    for i in range(1, bound+1):
        sum = sum + i
        print(sum, end=" ")
    
    return sum

print(sum_to(100))
    