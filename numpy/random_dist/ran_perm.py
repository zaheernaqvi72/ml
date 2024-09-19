import numpy as np

original = np.array([1, 2, 3, 4, 5])

# Shuffle the array by using numpy.random.shuffle(), it modifies the original array
np.random.shuffle(original)

print(f"Original array: {original}")

# Permute the array by using numpy.random.permutation() it does not modify the original array
permuted = np.random.permutation(original)

print(f"Permuted array: {permuted}")

print(f"Original array: {original}")


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Permute the elements in the 3D array along the first axis (rows)
permuted_rows = np.random.permutation(arr3d)

# Permute the elements in the 3D array along the second axis (columns)
permuted_columns = np.random.permutation(arr3d.T).T

print(f"Original 3D array: {arr3d}")
print(f"Permuted rows: {permuted_rows}")
print(f"Permuted columns: {permuted_columns}")
