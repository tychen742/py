
# ##### when txt is not defined
# an exception will hapen because txt is not defined
# with try, the program keeps executing and
# except will handle the error.

# ##### when txt is defined, the except block will not run
# txt = "This is a test"

# try:
#     print(txt)
# except:
#     print("An exception occurred")


# # ##### nested try

# ### deal with open error
# try:
#   f = open("demo.txt")
# except:
#   print("I have no idea.")


import os
# print("===================================================================")
# print(os.listdir())
# print("===================================================================")
# os.chdir("33_try_except")
# print(os.getcwd())
# print(os.listdir())

try:
    f = open("./33_try_except/demo.txt", "a")
    # print(os.getcwd())
    # f.write("Lorum Ipsum\n")
    try:
        # print(os.getcwd())
        # f = open("demo.txt", "a")
        f.write("Lorum Ipsum\n")
        # with f.open('demo.txt', 'r') as f:
        #     print(f)
    except:
        print("Something went wrong while WRITING to the file")
    finally:
        f.close()
except:
    print("Something went wrong when OPENING the file")

# with open("./33_try_except/demo.txt", "a") as f:
#     f.write("something\n")



