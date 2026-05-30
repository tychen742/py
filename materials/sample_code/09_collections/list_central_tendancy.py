# #### central tendance header #####
print()
print("###################################################")
print("warming up")
print("###################################################")

# #### add_two parameters
def add_two(num1, num2):
    return num1 + num2

print("add two:         ", add_two(10, 5))


# #### add_multipe parameters
def add_multiple(*args):
    total = 0
    for num in args:
        total = total + num
    return total

total = add_multiple(1, 2, 3, 4, 5)
print("add multi values:", total)


# #### create list lst
lst = [1, 2, 3, 3, 4, 4, 4, 5]


# #### sum list elements using a for loop
def sum_list_for_loop(lst):
    total = 0
    for num in lst:
        total = total + num
    return total

total = sum_list_for_loop(lst)
print("sum lst for:     ", total)

# #### sum list elements using the list sum() function
def sum_list_total(l):
    # total = total(l)
    # return total
    return sum(l)

total = sum_list_total(lst)
print("sum lst sum():   ", total)

# #### central tendance header #####
print()
print("###################################################")
print("descriptive stats: 1/3 measures of central tendency")
print("###################################################")

# #### mean of data (lst)
# #### mean = (sum of data) / (# of data points)
def mean(l):
    total = sum(l)
    length = len(l)
    return total/length

print("mean of list:    ", mean(lst))

# median of data (lst)
# ##### If there is an odd number of data points, 
# ##### the median is the middle data point.
# ##### If there is an even number of data points, 
# ##### the median is the average of the middle two data points.
def median(l):
    lst.sort()
    index = len(lst)//2     ### floor division

    if (len(lst) % 2):      ### you can test if % == 0, means even
        return lst[index]
    else:
        return (lst[index] + lst[index + 1])/2

print ("median of lst:   ", median(lst))

# mode of data
# ##### The mode is the most commonly occurring data point in a dataset. 
# ##### There can be no mode, one mode, or multiple modes in a dataset.
# it's too complicated so I just use the statistics module from python
from statistics import mode
print("mode of lst:     ", mode(lst))


# #### variability header #####
print()
print("###################################################")
print("descriptive stats: 2/3 measures of variability")
print("###################################################")

# variance
def variance(l):
    the_mean = mean(l)
    total = 0
    for i in range(len(l)):
        total = total + l[i]** 2
    return total

print("variance of lst: ", variance(lst))


# standard deviation
def sd(l):
    return variance(l)/len(l)

print("std deviation:   ", sd(lst))


# #### frequency header #####
print()
print("###################################################")
print("descriptive stats: 3/3 measures of frequency distribution")
print("###################################################")

# frequency

def freq(lst):
    d = {}          ### declare a dictionary
    for i in lst:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1
    return d
print("frequency of lst: ", freq(lst))

if __name__== '__main__':
    print("hello, world")