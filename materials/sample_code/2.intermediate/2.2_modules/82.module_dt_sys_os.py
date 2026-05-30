import datetime
import sys
import os

# now = datetime.datetime.now()
# print(now)


def addition():
    i = 0
    while i < 100000:
        i += 1


def time_it(i):
    for run in range(i):
        time_start = datetime.datetime.now()
        addition()
        time_end = datetime.datetime.now()
        print(time_end - time_start)

print(time_it(3))


info = sys.path
print(info)

name = os.name
print(name)
