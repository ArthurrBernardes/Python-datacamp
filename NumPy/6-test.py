# BEFORE WE START

# Python lists and numpy arrays sometimes behave differently. Luckily, there are still certainties in this world.
# For example, subsetting (using the square bracket notation on lists or arrays) works exactly the same.
# To see this for yourself, try the following lines of code:

# x = ["a", "b", "c"]
# x[1]
#
# np_x = np.array(x)
# np_x[1]

import numpy as np
x = ["a", "b", "c"]
x[1]
print(x[1])

np_x = np.array(x)
np_x[1]
print(np_x[1])

# Both come up as "b"