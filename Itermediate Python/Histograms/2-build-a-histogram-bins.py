# You'll be making two plots here. The code in the script already includes plt.show() and plt.clf() calls;
# plt.show() displays a plot; plt.clf() cleans it up again so you can start afresh


# Build a histogram of life_exp, with 5 bins. Can you tell which bin contains the most observations?
# Build another histogram of life_exp, this time with 20 bins. Is this better?


from variables import life_exp
import matplotlib.pyplot as plt

# Build histogram with 5 bins
plt.hist(life_exp, edgecolor="red", bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, edgecolor="red", bins=20)

# Show and clean up again
plt.show()
plt.clf()