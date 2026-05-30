
def grading (n):
    if n >= 90 and n <= 100:
        print ("A")
    elif n >= 80 and n < 90:
        print ("B")
    elif n >= 70 and n < 80:
        print ("C")
    elif n >= 60 and n < 70:
        print ("D")
    elif n >= 0 and n < 60:
        print ("F")
    else:
        print ("Your score must be between 0 and 100.")

grading (int(input("What is your grade?")))


# def grading(score):
#     if (100 >= score >= 90):
#         grade = "A"
#     elif (90 > score >= 80):
#         grade = "B"
#     elif (80 > score >= 70):
#         grade = "C"
#     elif (70 > score >= 60):
#         grade = "D"
#     elif (score < 60):
#         grade = "F"
#     else:
#         grade = "Scores must be between 0 and 100"
#     return grade


# print("score is 90, grade is:", grading(90))
# print("score is 85, grade is:", grading(85))
# print("score is 60, grade is:", grading(60))
# print("score is 50, grade is:", grading(50))
# print("score is 190, grade is:", grading(190))
