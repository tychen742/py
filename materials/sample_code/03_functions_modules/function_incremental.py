import math

def distance (x1, y1, x2, y2):      #01: Function ( + parameter Input) for calculating distance
    dist_temp = (x2 - x1)**2 + (y2-y1)**2
    dist = math.sqrt(dist_temp)
    return dist                                   #02: Output

result = distance (1, 2, 4, 6)                  #03: Arguments

print (result)                                  #02: Output printed