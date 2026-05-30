

def TimesSelf (x):
    running_total = 0   # This is the accumulator, starts with 0.
    for counter in range(x):
        running_total = running_total + x   # accumulating
        print(running_total)
    return running_total

result = TimesSelf (10)

print ("The result is:", result)