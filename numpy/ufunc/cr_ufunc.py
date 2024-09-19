import numpy as np

# Define a simple function
def mysum (a, b):
    return a + b
# Create a ufunc from the function
mysum_ufunc = np.frompyfunc(mysum, 2, 1)
# Use the ufunc just like a regular function and pass arrays as arguments
print(mysum_ufunc([1, 2, 3, 4], [5, 6, 7, 8]))

print(type(mysum_ufunc))