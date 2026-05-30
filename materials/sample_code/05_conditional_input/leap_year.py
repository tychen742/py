##### turn the leap year algorithm to flow chart then code
#                           [No] --> Not Leap
# START --> <divisible by 4>
#                                                        [No] --> Leap      
#                           [Yes] --> <divisable by 100>
#                                                        [Yes] --> <divisable by 400>
#

# leap year: the year has 366 days
# rule 1: the year is evenly divisible by 4
# rule 2: if #1 and the year is NOT evenly divisible by 100
# rule 3: if #2, if the year is evenly divisible by 400 ==> leap year

year = int(input("Please enter a year: "))

if year % 4 == 0:
    
    if year % 100 == 0:
    
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year.")
                    
    else:
        print(f"{year} is a leap year")
        
                
else:
    print(f"{year} is not a leap year.")

# print(f"You entered {year}")