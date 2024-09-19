import numpy as np
from scipy.sparse import csr_matrix

# Create a 2D NumPy array with a diagonal of ones, and zeros everywhere else

dense_matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

# Convert the NumPy array to a SciPy sparse CSR matrix
sparse_matrix = csr_matrix(dense_matrix)

print(f"Sparse matrix:\n{sparse_matrix}")
print(f"Dense matrix:\n{dense_matrix}")