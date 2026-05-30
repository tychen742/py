import re

txt = "The rain is raining in a inn in Spain"
abc = "** $1a , $bb cc ab abc acccc abCbcbc"
x1 = re.search("^The", txt)
x2 = re.search("ain$", txt)
# x=re.search("^T*n$", txt) ### note this will not work w/o a .
x3 = re.search("^T.*n$", txt)
x4 = re.search('rain', txt)
x5 = re.search('innn*', txt)
x6 = re.search("abcc+", abc)
x7 = re.findall("abc?", abc)
x8 = re.findall("abc{2}", abc)
x9 = re.findall("abc{2,5}", abc)  ### no space between 2, and 5
x10 = re.findall("a(bc)", abc)
x11 = re.findall("a(bc)*", abc)
x12 = re.findall("a(bc){2,5}", abc)
# x = re.findall("a(b|c)", abc)
x13 = re.findall("a([bc])", abc)  ### same as above but better
# x = re.findall("\d", abc)
# x = re.findall("\w", abc)
# x = re.findall("\s", abc)
# x = re.findall('.', abc)
# x = re.findall('\D', abc)
# x = re.findall('\W', abc)
# x = re.findall('\$\d', abc)
# x = re.findall('abc*', abc)
# x = re.findall('abc*', abc, flags=re.IGNORECASE)


#####
pattern = "h+o"          ### expresion
test_string = "hello world"
result = re.findall(pattern, test_string)
tt = re.findall(pattern, test_string)
if result:
    print('match', tt)
else:
    print("no match")


txt = "hello planet"

#Check if the string ends with 'planet':

# x = re.findall("planet$", txt)
# if x:
#   print("Yes, the string ends with 'planet'")
# else:
#   print("No match")
