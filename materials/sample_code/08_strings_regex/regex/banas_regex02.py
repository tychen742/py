# |  = OR 

#'(Jennifer|Jen|Jenny)'
#### Search for either one 

# Also search for last names
#'(Jennifer|Jen|Jenny)\b\w+\b'
# or, 'Je(nnifer|nny|n){1,6}\s\w+\s'
# or, 'Je(nifery){1,6}\b\w+\b'
#### \b  = space proceeds or follows a whole word
#### \B  = when there's no space
#### \w  = any number of characters
#### \w+  = one or more characters


##### user brackets for repeating code ##### (to shorten your regex)
# '(Jennifer|Jen|Jenny)\b\w+\b' \1  == redo the (Jennifer|Jen|Jenny) part. So,
# '(Jennifer|Jen|Jenny)\b\w+\b\1' == '(Jennifer|Jen|Jenny)\b\w+\b\(Jennifer|Jen|Jenny)
# '(Jennifer|Jen|Jenny)(\b\w+)\b \2 means to repeat the second bracket. 

##### finding all sentences begin with a word "cat" #####
# '^Cat\s'  == only Cat, followed by a space, not cats or others. 
##### find entire sentences beginning with "Cat"
# '(^Cat\s.+$)'  == find characters Cat, followed by a space (\s), followed by 
# anything but a line break (.), followed by a series of characters (w+), and then 
# ($)  == end of sentence.  

import re

text_file = open('randomcharacters.txt')

strToSearch = ""

for line in text_file:
    strToSearch += line 
    
print(strToSearch)

patFinder1 = re.compile('Aa1B') # compile method to define what to search for 

findPat1 = re.search(patFinder1, strToSearch) 
# search method to search the regex defind.
# patFinder1: reference the regex
# strToSearch: reference the string
print(findPat1.group()) # group() : find all matching subgroups
print(findPat1.start())
print(findPat1.end())
print(findPat1.span())

findPat1 = re.findall(patFinder1, strToSearch)
for i in findPat1:
    print(i)

# split()     
splitFound = patFinder1.split(strToSearch)
print("result of the split method", splitFound)

# sub() == substitute
subFound = patFinder1.sub("REAL TEXT", strToSearch)
print(subFound)

patFinder2 = re.compile('a')
findPat2 = re.search(patFinder2, strToSearch)
print (findPat2.group())
print (findPat2.span())

p = re.compile('a-z')
for m in p.finditer('a1b2c3d4'):
    print m.start(), m.group()
    


