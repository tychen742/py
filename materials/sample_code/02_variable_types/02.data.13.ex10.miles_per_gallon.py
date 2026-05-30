# MPG: Calculating Miles per Gallon

# Write a program that will compute MPG for a car. Prompt the user to
# enter the number of miles driven and the number of gallons used.
# Print a nice message with the answer.


miles = input("Please input the miles driven: ")
gallon = input("Please input number of gallon used: ")

# mpg = miles/gallon    # This will give you a str/str error. Note that INPUT == string
# miles = float(miles)
miles = int(miles)
# gallon = float(gallon)
gallon = int(gallon)
mpg = miles / gallon  # int/int == float

# print("The MPG for a car running " + miles + " using " + gallon + " is: ", mpg)
# Can't convert float to str implicitly: Pyton will try for you, but failed
# Can't convert object to str implicitly either.

print("The MPG for a car running ", miles, " using ", gallon, " is: ", mpg)
