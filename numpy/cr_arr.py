import numpy as np

arr_1_d = np.array([1, 2, 3, 4, 5])
arr_2_d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3_d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(f"1D array: {arr_1_d}")
print(f"2D array: {arr_2_d}")
print(f"3D array: {arr_3_d}")

# multi-dimentional arrays
arr_5_d = np.array([1, 2, 3, 4, 5], ndmin=5)
print(f"5D array: {arr_5_d} and Dimension: {arr_5_d.ndim}")