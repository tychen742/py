# range keyword
# range() is a built-in function that generates a sequence of numbers.
# It is commonly used in for loops to iterate over a sequence of numbers.
# The range() function can take up to three arguments:
# 1. start: The starting number of the sequence (inclusive). Default is 0.
# 2. stop: The ending number of the sequence (exclusive).
# 3. step: The difference between each number in the sequence. Default is 1.
# The range() function returns a range object, which is an immutable sequence type.
# The range object can be converted to a list or tuple using the list() or tuple() functions, respectively.
nums = range(5)             # 1 arg
print(nums)

for num in nums:
    print(num, end=" ")     # 0 to 4

print()                     

nums = range(5, 10)         # 2 args: Start, Stop
for num in nums:
    print(num, end=" ")     # 5 6 7 8 9

print()                  

nums = range(5, 10, 2)      # 3 args: Start, Stop, Step
for num in nums:
    print(num, end=" ")     # 5 7 9

print()                  
