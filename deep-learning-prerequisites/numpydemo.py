import numpy as np

# an array
L = [1,2,3]

# a numpy array
A = np.array([1,2,3])

# all elements of the array
for e in L:
    print (e)

# all elements of the numpy array
for e in A:
    print (e)

# on an array, elements can be appended
L.append(5)
L = L + [6]

#doesnt work for numpy
# A.append(5)
# A = A + [5]

# to add all elements in array by itself you can do
L2 = []
for e in L:
    L2.append(e+e)

# in nunpy it is way more easy
A + A
2*A

# you can multiply an array with 2 but is has a different result...
2*L

# in numpy you can easly square elements
A**2
# or calculate the square root
np.sqrt(A)

## Multiply arrays...
a = np.array([1,2])
b = np.array([2,1])

dot = 0

for e, f in zip(a,b):
    dot += e*f

print(dot)

#element wise multiplication
print(a*b)

# and then sum to one element...
print(np.sum(a*b))
# or
(a*b).sum()

# or more easy
np.dot(a,b)
#or
a.dot(b)

#calculate the angle between a and b
amag = np.sqrt((a*a).sum())
print (amag)

# there is a function in numpy to do this
amag = np.linalg.norm(a)
print(amag)

# calculate the angle
cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(cosangle)

angle = np.arccos(cosangle)
print(angle) #in rad

# vector and matrix
M = np.array([[1,2],[3,4]])
L = [[1,2],[3,4]]

#get first element of first row:
L[0][0]
M[0,0]

#numpy has a matrix but it's better to use a multi dimensional array...
M2 = np.matrix([[1,2],[3,4]])
# it can be converted...
A =  np.array(M2)
# transpose
print(A.T)


#generate arrays of data
np.array([1,2,3])

# create array of all zeros (10 zeros)
Z = np.zeros(10)

# create a two dimensional array of all zeros 10x10
Z = np.zeros((10,10))
print(Z)

# equivalent for all 1s
# create a two dimensional array of all zeros 10x10
Z = np.ones((10,10))
print(Z)

# random numbers (uniform distributed)
R = np.random.random((10,10))
print(R)

# random numbers gaussian distributed
G = np.random.randn(10,10) #!! dont pass ass tuple but individual params
#calculate mean
G.mean()
#calculate variance
G.var()

#matrix products
# requirement: inner dimensions must match!
# eg a matrix A of size (2.3) can be multiplied with B of size (3,3)
# but we cannot multiply B with A

# calcuate matrix inverse
A = np.array([[1,2],[3,4]])
Ainv = np.linalg.inv(A)

#validate
Ainv.dot(A)
A.dot(Ainv)

#Determinant
np.linalg.det(A)

# get the diagonal of a matrix
np.diag(A)

# create a matrix with diagonal values
np.diag([1,2,3])

# outer product and inner product
a = np.array([1,2])
b = np.array([3,4])

np.outer(a,b)
np.inner(a,b)
#inner is the same as the dot
a.dot(b)


# sum of the diagonal
np.diag(A).sum()
#shorter
np.trace(A)

#eigenvalues
X = np.random.randn(100,3)
cov = np.cov(X.T)

np.linalg.eigh(cov)
#gives:
# - eigenvalues
# - eigenvectors stored in the columns