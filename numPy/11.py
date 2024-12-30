import numpy as np 

a = np.random.randint(100,size=(4,4))
print(a,"\n")


modified_array = np.where(a%2 == 0 ,1,-1)
print(modified_array)
    