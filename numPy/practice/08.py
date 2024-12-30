import numpy as np 

v1 = np.array([1,2,3])
v2 = np.array([4,5,7])

vertical_stacking = np.vstack((v1,v2))
print(vertical_stacking)

h1 = np.array([11,22,33,44])
h2 = np.array([55,77,88,99])

horizontal_stacking = np.hstack((h1,h2))
print(horizontal_stacking)