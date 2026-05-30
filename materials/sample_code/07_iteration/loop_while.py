# i = 0
# while i < 10:
# # while True:
#     print(i, end=" ")
#     # not missing
#     i = i + 1
# else:
#     print("Something")
    
    

def sum_to (bound):
    
    sum = 0
    i = 1
    
    while ( i < bound + 1):
        
        sum = sum + i
        print(sum, end=" ")
        i = i + 1
        
    return sum

print(sum_to(100))