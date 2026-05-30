# input a number between 10 and -10

num = input("Enter a number between -10 and 10: \n")
print("You entered: ", num)

# detecting positive number
num = int(num)
if num < 0:
    print(num, " is a negative number.")
# elif num == 0:
#     print(num, " is 0.")
else:
    print(num, " is a positive number.")
# Thank you and bye
print("Thank you for using this software. Bye!")
