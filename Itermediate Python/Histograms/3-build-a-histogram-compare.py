# Build a histogram of life_exp with 15 bins.
# Build a histogram of life_exp1950, also with 15 bins. Is there a big difference with the histogram for the 2007 data?

from variables import life_exp, life_exp1950
import matplotlib.pyplot as plt

# Histogram of life_exp, 15 bins
plt.hist(life_exp, edgecolor="red", bins=15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, edgecolor="red", bins=15)

# Show and clear plot again
plt.show()
plt.clf()
