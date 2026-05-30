import re
from banas_regex02 import findPat2

f = open('randomcharacters.txt' )

strToSearch = ''

for line in f:
    strToSearch += line
    
print(strToSearch)


patFinder2 = re.compile('b3b2c', re.IGNORECASE)
findPat2 = re.search(patFinder2, strToSearch)

if (findPat2): 
    print(findPat2.group()) # group() : find all matching subgroups
    print('WHAT! Pat2')
else:
    print("Nothing Found.")
    

patFinder3 = re.compile('.*', re.IGNORECASE) # . : anything but a newline; w : repetition
findPat3 = re.search(patFinder3, strToSearch)
print(findPat3.group())