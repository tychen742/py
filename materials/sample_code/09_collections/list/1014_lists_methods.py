### what are methods? 1) ~ function; 2) under class
##### These methods can be very useful. For example, you have a set of
##### customer purchase records and you can read the data, put them into []
##### to make it a list and sort, count to find out the Min/Max
##### and occurrence, which are the basic analyses of customer analytics
##### The basic methods allow you to explore the data.
##### For commercial use, you would write them as programs to generate #'s
##### As part of the analytics team, you would observe and find patterns.



##### Mutable Sequence Types operation https://docs.python.org/3/library/stdtypes.html#iterator-types
mylist = []
mylist.append(5)  ### append adds element to the END of the List
mylist.append(27)
mylist.append(3)
mylist.append(3)
mylist.append(12)
mylist.append(12)
print('mylist:', mylist)

lastitem = mylist.pop()  ### pop w/o parameter will Remove and RETURN the last element
print('last item poped:', lastitem)
print('mylist after pop:', mylist)  ### "Lists are MUTABLE"

lastitem = mylist.pop(0)  ### pop with parameter
print('poped position 0:', mylist)

### APPEND and POP works on the end of the list.


### INSERT and REMOVE
mylist.insert(1, 12)  ### insert  # takes two arguments
print('insert 12 into position 1:', mylist)

mylist.remove(12)  ### remove the FIRST occurrence of the element
print('remove 12 from mylist:', mylist)

### count for frequency     ############### !!!!!!!
print('count 12:', mylist.count(12))
print('count 3:', mylist.count(3))  ### count

### index for position
print('index of 27:', mylist.index(27))  ### index

### ordering: sort, RETURN NONE
mylist.sort()  ### sort
# mylist = mylist.sort()        ##### DON't do this
another_list = mylist.sort()  ##### can do this
print('sort mylist:', mylist)

### ordering: reverse, RETURN NONE
mylist.reverse()  ### reverse

print('reverse mylst:', mylist)

### Sequence Types: Common Sequence Operators
### https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
max_mylist = max(mylist)  ### max
print('max:', max_mylist)
min_mylist = min(mylist)  ### min
print('min:', min_mylist)
# print (min_mylist[0])     # syntax error
print('mylist:', mylist)
print('the 0 position of mylist:', mylist[0])  ### index

alist = [4, 2, 8, 6, 5]
alist = alist.pop(0)
print(alist)
