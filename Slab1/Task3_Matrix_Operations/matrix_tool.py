import numpy as np

# Input matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Addition
print("\nAddition of A and B:")
print(A + B)

# Subtraction
print("\nSubtraction of A and B:")
print(A - B)

# Multiplication
print("\nMultiplication of A and B:")
print(A @ B)

# Transpose
print("\nTranspose of Matrix A:")
print(A.T)

# Determinant
print("\nDeterminant of Matrix A:")
print(np.linalg.det(A))
