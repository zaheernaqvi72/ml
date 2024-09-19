import numpy as np

original = np.array([1, 2, 3, 4, 5])
print(f"Original: {original}")
copied = np.copy(original)
copied[0] = 99
original[1] = 88
print(f"Original: {original}")
print(f"Copied: {copied}")

# copies array does not change the original array and vice versa and the copied array is a deep copy of the original array

neworiginal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arrayview = neworiginal.view()
# arrayview[0, 0] = 99
arrayview.shape = (2, 9)
print(f"Original: {neworiginal}")
print(f"View: {arrayview}") # the view array changes the original array

