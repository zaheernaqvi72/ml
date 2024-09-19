import numpy as np

arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[1,2,3],[4,5,6]])
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# use of ndmin for creating nD array
arrnd = np.array([1,2,3,4,5], ndmin=10)

# use of arr.shape
print(f"shape of 1D array: {arr1d.shape}")
print(f"shape of 2D array: {arr2d.shape}")
print(f"shape of 3D array: {arr3d.shape}")
print(f"shape of 10D array: {arrnd.shape}")