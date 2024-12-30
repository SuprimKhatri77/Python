import numpy as np

a = np.array([[2, 3],
              [4, 6]])

b = np.array([5, 10])

output = np.linalg.solve(a, b)
print(output)