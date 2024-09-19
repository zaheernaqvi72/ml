import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr[1:3])

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[1:3, 0:3])

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d[1, 0:2, 0:3])