import numpy as np

a = np.random.randint(1,10, size = (3,3))
print(a)

# other way
b = np.arange(1,10).reshape(3,3)
print(b)