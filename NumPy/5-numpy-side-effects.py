import numpy as np

# Have a look at this line of code:

code = np.array([True, 1, 2]) + np.array([3, 4, False])

# Can you tell which code chunk builds the exact same Python object?

a = np.array([True, 1, 2, 3, 4, False])
b = np.array([4, 3, 0]) + np.array([0, 2, 2])
c = np.array([1, 1, 2]) + np.array([3, 4, -1])
d = np.array([0, 1, 2, 3, 4, 5])

print(f"code {code} \n")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

print("\nNote that True is converted to 1 and False is converted to 0")