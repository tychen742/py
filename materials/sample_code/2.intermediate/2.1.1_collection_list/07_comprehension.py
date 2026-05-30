#!/usr/local/bin/python3.12

##### create a new list with letter "a" in item/element names

# create the fruits list
fruits = ['apple', 'banana', 'cherry']

### 1. using conditional
# create/declare new empty list because I want to put the selected elements in it
new_list = []

# loop through elements and test with the "in" keyword
for fruit in fruits:                ### loop through the fruits one by one
    if "a" in fruit:                ### if "a" is in the fruit name
        new_list.append(fruit)      ### add the fruit to new_list

print(new_list)


### 2. using list comprehension
new_list = [x for x in fruits if "a" in x]
print(new_list)

### 3. with a conditional, get elements that are not "apple"
new_list = [ele for ele in fruits if ele != "apple"]
print(new_list)

# # with conditional omitted == loop
# new_list = [ ele for ele in fruits ]
# print(new_list)

# # with iterable, e.g., range()
# new_list = [ x for x in range(10)]
# print(new_list)

# ## with iterable adding condition
# new_list = [ x for x in range(10) if x < 5]
# print(new_list)

# ## expression
# # use an expression to change the value before adding to the new list
# new_list = [ ele.upper() for ele in fruits]
# print(new_list)

# # set all values 
# list_blue_burry = ['blue burry' for ele in fruits]
# print(list_blue_burry)

# # condition as expression
# new_list = [ ele if ele != "banana" else "oranage" for ele in fruits]
# print(new_list)

