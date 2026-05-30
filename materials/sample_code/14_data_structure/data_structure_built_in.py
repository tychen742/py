##### built-in DS: set, tuple, list, dict
##### differing points among DS: mutability & order


##### list (array in other lanuages)
## ordered, mutable, nestable (can contain other data structure elements)
## can only manipulate the rightmost element; optimized for scientific data
a_list = ["1", '3', 5]
print("type of a_list: ", type(a_list))
a_list.pop()
print("popped: ", a_list)
for i in range (len(a_list)):
    print(a_list[i])

##### tutple: immutable list
## odered, immutable, automatic scale
# a_tuple = 2, 4, 6     ### parentheses are optional
a_tuple = (2, 4, 6)
print("type of a_tuple: ", type(a_tuple))

##### set
## un-ordered (un-indexed, no sequence), mutable
## good for: memebership tests
a_set = {"aaa", "bbb", "ccc"}
print("type of a_set: ", type(a_set))

##### dictionary: similar to hashmap or hash table
## key-value pair collection
## keys are unique and immutable