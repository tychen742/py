### the assignment statement does not make a copy of a list
### 

## create the list
fruits = ['apple', 'banana', 'cherry']

# ## make a copy by assignment
# fruits_2 = fruits

# ## check the copies
# print(fruits)          ## ['apple', 'banana', 'cherry']
# print(fruits_2)        ## ['apple', 'banana', 'cherry']
# print(type(fruits))    ## list
# ## change the original copy 
# # fruits = ['apple', 'banana', 'cherry'].append('durian')  ## can't append
# fruits.append('durian')
# print(fruits)          ## ['apple', 'banana', 'cherry', 'durian']

# ## check the copies again
# print(fruits)          ## ['apple', 'banana', 'cherry', 'durian']
# print(fruits_2)        ## ['apple', 'banana', 'cherry', 'durian']
# ### when fruits changes, fruits_2 changes accordingly. 
# ### this behavior may not be what we want our list to have 


# ##### use the copy() method
# fruits_2 = fruits.copy()
# fruits.append('durian')
# print(fruits)          ## ['apple', 'banana', 'cherry', 'durian']
# print(fruits_2)        ## ['apple', 'banana', 'cherry']
# ### fruits_2 is a separate copy and does not reference to fruits anymore



##### use the list() method
fruits_2 = list(fruits)
fruits.append('durian')
print(fruits)          ## ['apple', 'banana', 'cherry', 'durian']
print(fruits_2)        ## ['apple', 'banana', 'cherry']
### fruits_2 is a separate copy and does not reference to fruits anymore



