#!/usr/local/opt/python/bin/python3
##### learning: type conversion, round to decimal places, if statement, printf, clear if state ==> else

#  < 18.5: underweight
# >= 18.5 && < 25: normal weight
# >= 25 && < 30: overwight
# >=- 30 && < 35: obese
# >= 35: clinically obese

# bmi = kg/m^2
# bmi = weight(lb) / [height(in)^2 x 703]

##### input weight & hight
weight = float(input ("What is your weight in KG? "))
height = float(input ("What is your height in meter? "))

##### calculate BMI
# bmi = weight / (height * height)              ### original formula
bmi = round (weight / (height * height), 1)     ### with round/decimal
print (bmi)


##### translate to comment
if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}. You are normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}. You are overwight.")
elif bmi >=- 30 and bmi< 35: 
    print(f"Your BMI is {bmi}. You are obese.")
elif bmi >= 35: 
    print(f"Your BMI is {bmi}. You are clinically obese.")