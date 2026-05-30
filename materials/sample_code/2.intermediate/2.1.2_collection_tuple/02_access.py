fruits = ("apple", "banana", "cherry")

# ## 0 indexing
print(fruits[0])


# ## negative indexing
print(fruits[-1])


# ## index range
print(fruits[0:1])      ### 1 excluded


# ## index range
print(fruits[:1])
print(fruits[1:])
print(fruits[-3:-1])    ### ('apple', 'banana') with -3 excluded


# ## the in keyword
if ("apple") in fruits:
    print("Apple is in the fruits tuple.")

