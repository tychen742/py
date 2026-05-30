origlist = [45, 76, 34, 55]
print(origlist * 3)  ### original list as element collection

newlist = [origlist] * 3  ### origlist as a List Element
print(newlist)

origlist[1] = 99
print(newlist)  ### mutable, still pointing to the same objects

# now how about this:
alist = [4, 2, 8, 6, 5]
blist = alist * 2  ### blist as a copy of the references in alist
blist[3] = 999  ### now the reference is changed in blist
print(alist)

# then compare with this:
alist = [4, 2, 8, 6, 5]
blist = [alist] * 2  ### blist refers to alist
alist[3] = 999  ### now the reference is changed in alist
print(blist)
