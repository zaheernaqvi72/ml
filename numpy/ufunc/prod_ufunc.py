import numpy as np

data_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Product of all elements in the array
prod_array = np.prod(data_array)
print(f"Product of Array: \n {prod_array}")

axis_prod_array = np.prod(data_array, axis=0)
print(f"Product of Array along Axis 0: \n {axis_prod_array}")

cumulative_prod_array = np.cumprod(data_array)
print(f"Cumulative Product of Array: \n {cumulative_prod_array}")