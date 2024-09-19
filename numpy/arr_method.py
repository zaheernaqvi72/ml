import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()


from numpy import random

# Generate a random integer from 0 to 100
x = random.randint(100, size = (3, 5))
print(x)

# Generate a random float from 0 to 1
y = random.choice([3, 5, 7, 9], size = (3, 5))
print(y)

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

add = np.add(arr1, arr2)
print(add)

subt = np.subtract(arr1, arr2)
print(subt)

mult = np.multiply(arr1, arr2)
print(mult)

div = np.divide(arr1, arr2)
print(div)