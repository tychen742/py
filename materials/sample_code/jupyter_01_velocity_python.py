# ### To make a barchart, we need x's and y's

# ### 1/4. import packages/libraries
import numpy as np
import matplotlib.pyplot as plt
from emoji import emojize 

# ### 2/4. create empty lists for x & y
x = []
y = []

# ### 3/4. adding values to x[] & y[]
for i in np.arange(0, 3.1, 0.5):    # 0.5 increment
    x.append(i)
    y.append(64 - (16 * (i-1)**2))  # the formula

# ### to test, print out the lists
# print(x)
# print(y)

# ### 4/4. set up, draw, and show the barchart
plt.title("Time and height")
plt.xlabel("Time")
plt.ylabel("Height")
plt.bar(x, y, color='orange', width=0.25)   # draw
plt.show()                                  # show
