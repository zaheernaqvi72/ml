import numpy as np

num_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Sum of all elements in the array
sum_array = np.sum(num_array)
print(f"Sum of Array: \n {sum_array}")

# Sum of Array along Axis 0
axis_sum_array = np.sum(num_array, axis=0)
print(f"Sum of Array along Axis 0: \n {axis_sum_array}")

# Cumulative Sum of Array
cum_sum_array = np.cumsum(num_array)
print(f"Cumulative Sum of Array: \n {cum_sum_array}")

