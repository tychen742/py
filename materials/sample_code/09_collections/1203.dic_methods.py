# keys(), values(), items()
fruits = {'apples': 100, 'bananas': 200, 'cherries': 300}
print(fruits)

for aKey in fruits.keys():  # keys() method takes no parameter
    print(aKey, "has inventory value of: ", fruits[aKey])

# dict to list conversion ==> only keys are kept
print(list(fruits))

# omit the keys() method
for aKey in fruits:
    print(aKey, "has inventory value of: ", fruits[aKey])

# values
print(fruits.values())

# items
print(fruits.items())

# iteration through a dict with two local variables
for (k, v) in fruits.items():
    print("There are", v, k)

# with one AND skip the items() method
for (k) in fruits:
    print("There are", fruits[k], k)

# in and not in operators
print('apples' in fruits)
print('cantaloupes' in fruits)

if 'bananas' not in fruits:
    print("No bananas!")
else:
    print("There are", fruits['bananas'], "bananas.")

# get
print(fruits.get('apples'))
print(fruits.get("cantaloupes"))
print(fruits.get("cantaloupes", 0))
