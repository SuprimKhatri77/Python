import numpy as np 

a = np.ones((5,5))
print(a,"\n")

z = np.zeros((3,3))
print(z,"\n")

a[1:4,1:4] = z
print(a)