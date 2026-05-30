

# match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong"

status = int(input("Please enter status 400, 404, or 418:\n"))

if status == 400:
    print("Bad request!")
elif status == 404:
    print("Not found")
elif status == 418:
    print("I'm a teapot")
else:
    print("Something's wrong")