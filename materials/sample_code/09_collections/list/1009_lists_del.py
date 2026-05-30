### del

a = ['one', 'two', 'three']
del a[1]
# del a[10]       ### out of range
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[0 - 2]  ### use a SLICE as an Index for del
print(alist)

blist = ['a', 'b', 'c', 'd', 'e', 'f']
del blist[6:9]  ### NOT out of range
print(blist)
