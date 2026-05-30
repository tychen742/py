# https://python.plainenglish.io/these-python-data-structures-will-be-your-new-best-friends-45c770a6bf14
from collections import deque
from collections import namedtuple
from collections import Counter

#### deque
a = deque(maxlen=3)
a.append(1)
a.append(2)
a.append(3)
print(a)
a.append(4)
print(a)
a.appendleft(5)
print(a)
a.pop()
print(a)
a.popleft()
print("the deque is now: " , a)

##### Named Tuples
Point = namedtuple("Point", ["x", "y", "z"], defaults=[0,0])
p = Point(3, 4, 5)
print("printing the points:" , p.x, p.y, p.z)
print("default fields in named tuple: ", Point._fields_defaults)

##### Counter
c = Counter("aaabbbcccaaa")
print("this is counter c: ", c)
print("so many a's: ", c['a'])
print("so many z's: ", c['z'])
print("most common: ", c.most_common(1))
c.update("zzzz")
print("updated: ", c)
c.subtract("zzz")
print("subtracted: ", c)


##### Defaultdict
### regualr dict
toAdd = [("key1", 3), ("key2", 5), ("key3", 6), ("key2", 7)]
d = dict()
for key, val in toAdd:
    if key in d:
        d[key].append(val)
    else:
        d[key] = [val]
print("regular dict: ", d)

### defaultdict: faster
from collections import defaultdict
d = defaultdict(list)       ## list: a built-in function
for key, val in toAdd:
    d[key].append(val)
print("deaultdic: ", d)

### use setdefault method of dict()
d = dict()
for key, val in toAdd:
    d.setdefault(key, []).append(val)
print("setdefault: ", d)
