import numpy as np

# Numeric matrix
A = np.array([[1, 2], 
              [2, 3]])
print("Matrix A: ", A)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)


