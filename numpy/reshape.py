import numpy as np

original_array = np.array([1,2,3,4,5,6])

# default it'll be row major reshaping
reshapedarray = np.reshape(original_array, (2, 3))

rowmajor = np.reshape(original_array, (2, 3), order='C')

# column major reshaping
columnmajor = np.reshape(original_array, (2, 3), order='F')

print(f"Original array: \n{original_array}")
print(f"Reshaped array: \n{reshapedarray}")

print(f"Row major reshaped array: \n{rowmajor}")
print(f"Column major reshaped array: \n{columnmajor}")

