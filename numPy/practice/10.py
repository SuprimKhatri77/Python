import numpy as np

matrix1 = np.full((3,3),2)
matrix2 = np.full((3,3),5)
mat_addition = matrix1 + matrix2
print(mat_addition)
mat_multiplication = matrix1 * matrix2
print(mat_multiplication)
print(np.matmul(matrix1,matrix2))