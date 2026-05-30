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

# print(time_it(3))


info = sys.path
print(info)         ### ['/Users/tcn85/workspace/python_code', 
                    ### '/Library/Frameworks/Python.framework/Versions/3.12/lib/python312.zip', 
                    ### '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12', 
                    ### '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload', 
                    ### '/Users/tcn85/workspace/python/.venv/lib/python3.12/site-packages']

name = os.name
print(name)         ### posix

print(os.getcwd())  ### /Users/tcn85/workspace/python_code
                    ### depends on your terminal location