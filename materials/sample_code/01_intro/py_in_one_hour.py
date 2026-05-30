# install python
# install vscode/PyCharm
# create project (virtual environment)
# print("hello world") at shell, jupyter notebook, & vscode
# save python file 

# 1. variables: declaration, assignment, re-assignment, data types, naming convention,
# 1. case-sensitive, comment
# data types: int, float,  str, boolean
# age = 20  # variable with value assignment
# print(age)

# 2. user input
# name = input("Please type your name: ")
# print("Hi, " + name)  # + for concatenation
# birth_year = input("Please enter your birth year: ")
# birth_year = int(birth_year)  # change type: type coercion using the int() function; also float(), bool(), str()
# age = 2023 - birth_year
# print(name, ", you are", age, "years old")  # use , to separate objects to be printed

# use float instead of int
# first = int(input("First: "))
# second = int(input("Second: "))
# print("The sum of", first, "and", second, "is", first + second) # or str() the sum here.

# 3. string object and its methods (e.g., upper(), lower(), find(), replace(), and the keyword "in" operator )
# course = "Python for Beginners"
# print(course.upper()) # does not change the course string object itself
# print(course.lower())
# print(course.find('y'))
# print(course.find('Y'))
# print(course.replace('for', "4"))
# print("Python" in course)

# 4. arithmatic operators ( +, -, *, /, // , % modulus, ** exponent, augmented assignment operator)
x = 10 + 2 * 10   # operator precedent; can be changed using parentheses
# x = x + 3
x += 3  # same as the line above
# print (x)
# print(10 // 3)

# 5. Comparison operators ( >, <, <=, >=, ==, != )
x = 3 != 2
# print(x)

# 6. logical operators (for conditions): and, or, not
# price = 100
# print(price < 200 and price > 90)
# print(price < 200 or price < 90)
# print(not price < 200)

# 7. if statement
# temperature = 100
# if temperature > 90:
#     # print('It's a hot day.') # apostrophe & single quote
#     print("It's a hot day.")    # note the indentation for code block
# elif temperature > 75:
#     print("It's a nice day.")
# elif temperature > 60 :
#     print("It's chilly.")
# else:
#     print("It's cold")
# print("End of story")

# exercise: convert lbs to kg
# factor = 0.453592
# weight = float(input("Enter your weight: \n"))
# unit = input("In (K)g or (L)bs: \n")
# if unit.upper() == "K":
#     weight_converted = weight / factor
#     print("Weight in Kg:", weight_converted)
# elif unit.upper() == "L":
#     weight_converted = weight * factor
#     print("Weight in lbs:", weight_converted)
# else:
#     print("Please enter K or L for unit")

# while loops
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# i = 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1

# list
names = [ "Aaron", "Ben", "Chris"]
print(names)
print(names[1])
print(names[-1])
