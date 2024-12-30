import numpy as np 

a = np.random.randint(1,11, size=(5,5))
print(a)
print("\n")

# printing the middle 3x3 matrix
b= a[1:4,1:4]
# print(b)

# printing the first row
c = a[1:2]
# print(c)

# printing the even elements
even_elements = a[a % 2 == 0]
print(even_elements)