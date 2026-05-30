# ### function recursion
def recursion(k):
    if (k > 0):
        result = k + recursion(k-1)
        print(result)
    else:
        result = 0
    return result
recursion(10)