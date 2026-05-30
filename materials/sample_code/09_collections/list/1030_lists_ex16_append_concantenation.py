myList = []
myList.append(76)
myList.append(92.3)
myList.append("hello")
myList.append(True)
myList.append(4)
myList.append(76)
print(myList)

# someList = []
# myList = someList
# print (myList)
myList = []
print(myList)
myList = myList + [76]
myList = myList + [92.3]
myList = myList + ["hello"]
myList = myList + [True]
myList = myList + [4]
myList = myList + [76]
print(myList)

"""
Starting with the list in Exercise 2, write Python statements to do the following:

Append “apple” and 76 to the list.
Insert the value “cat” at position 3.
Insert the value 99 at the start of the list.
Find the index of “hello”.
Count the number of 76s in the list.
Remove the first occurrence of 76 from the list.
Remove True from the list using pop and index.
Save & RunShow FeedbackShow/Hide CodeShow CodeLensCode Coach """

myList.append("apple")
myList.append(76)
myList.insert(3, "cat")  ### INSERT must have index
myList.insert(0, 99)

print(myList)
print(myList.index("hello"))  ### INDEX can be used the other way around. ^^ Friendly language design
print(myList.count(76))  ### COUNT
# print (myList.pop())          ### pop is for the last one
print(myList.remove(76))
print(myList)
# print (myList.pop[4])         ### attempting, but ...
print(myList.pop(4))  ### pop is a method, so use ( )
print(myList)
print(myList.insert(4, True))  ### return None, so don't assign it to the list itself??????
print(myList)

### Can't pop a value. pop must use Index. pop (TRUE) == pop(1), pop(FALSE) == pop(0)

print(myList.insert(4, True))  ### return NONE
print(myList.pop(4))  ### return the VALUE popped

# delete True with pop AND index


# myList[4] = []             ##### index is an attribute, so use [], as vs. methods like pop(
myList[4] = myList[4:4]
print(myList)
