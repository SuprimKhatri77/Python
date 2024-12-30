import numpy as np

a = np.array([1,2,3])
# print(a)

b = np.array([[8.0,7.0,9.0],[1,25,7]])
# print(b)

#get dimension
# print(a.ndim)
# print(b.ndim)

#get shape
# print(a.shape)
# print(b.shape)

#data type
# print(a.dtype)
# print(b.dtype)

#getting a speicific element out of the array
c = np.array([[1,2,3,4,5],[6,7,8,9,11]])
# print(c[1,1 ])
#c[1,1] ma first value chai row ko ho ane 2nd chai column ko. py ma indexing 0 bata suru huncha so 1,1 vako ho nai vane 2,2 hunthyo

#getting a specific row
d = np.array([[1,2,3,4,5,6,7,8],[5,6,7,8,9,10,11,12]])
# print(d[1, :])
#getting a specific row
# print(d[:,2])

#getting little more fancy[startindex:endindex:stepsize]
# print(d[0,1:7:2])

#all 0 matrix
e = np.zeros((2,3))
# print(e)
# 2 chai no fo rows ho ane 3 chai no fo columns
#we can make 3d matrix as well
f = np.ones((3,3))
# print(f)

#we can fill up the matrix with any number
g = np.full((2,3),7)
# print(g)
# 2,3 chai no of rows ho ane 7 chai kun number le matrix fill up garne ho tyo ho 
#so it takes 2 param while making a matrix with other numbers except 0,1

#full_like le chai pailai baneko array ko shape lina milcha by a custom number
h = np.full_like(a,7)
# print(h)
#aba full_like use na garera full matra use gare ne huncha but then we have to use a.shape instead of a
# h = np.full(a.shape,7)

#matrix of random decimal numbers
i = np.random.rand(2,3)
# print(i)

#matrix of random integers
j = np.random.randint(7, size=(3,3))
# print(j)
#yesma chai first ma chai kati dekhi kati samma ko number haru chaincha tyo specify garnu parcha for eg: mathi chai 7 matra cha so it will start from 0 and 7 is exclusve so if i wanted to get 7 i must end at 8 or more as the last index is exclusive
#-ve number ne milcha halna
#2nd param ma chai order/size specify garnu parcha

#identity matrix
k = np.identity(5)
# print(k)
# identity(x) x ma jati number haley pani teti ota element ko identity matrix banaucha 

#repeat an array
l = np.array([[1,2,3]])
rep = np.repeat(l,3, axis=1)
# print(rep)

#be careful while copying an array
m = np.array([1,2,3])
n = m
n[0] = 77
# print(n)
# print(m)
#so while copying an array we should use copy method otherwise a change in the variable n will result in change in the m variable
#eg:
o = np.array([1,2,3])
p = o.copy()
# print(p)

# addition subtraction multiplication division to each element of the matrix
q = np.array([1,2,3,4,5])
# print(q + 2)
# print(q * 2)
# print(q - 2)
# print(q / 2)

#use case in linear algebra
r = np.ones((2,3))
s = np.full((3,2),2)
# print(np.matmul(r , s))

#finding the determinant of identity matrix
t = np.identity(3)
# print(np.linalg.det(t))

# reorganizing arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before)
after = before.reshape((2,2,2))
# print(after)

# vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
# print(np.vstack([v1,v2]))

#horizontally stacking vectors
h1 = np.ones((2,4))
h2 = np.zeros((2,4))
# print(np.hstack([h1,h2]))

# load data from a file
file_data = np.genfromtxt('numPy\\data.txt', delimiter= ',')
# print(file_data)
