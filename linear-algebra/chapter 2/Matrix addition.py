import numpy as np

# adding a matrix
A = np.random.randn(5,5)
B = np.random.randn(5,5)

np.add(A, B)

# shifting a matrix
l = .3
I = np.eye(5)

S = np.add(A, l*I)
print(S)