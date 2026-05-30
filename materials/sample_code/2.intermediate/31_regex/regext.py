import re

string = "This is a string."
str = re.search("^This.*string", string)

if str:
    print("Match")
else:
    print("No match")