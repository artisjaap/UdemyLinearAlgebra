import numpy as np

#square matric
print(np.random.randn(5,5))

#rectangle
print(np.random.randn(5,2))

#Identity
print(np.eye(5))

#zeros
print(np.zeros((4,4)))

#diagonal
print(np.diag([1,5,9,8,4,5]))

#triangluar
M = np.random.randn(5,5);
U = np.triu(M)
L = np.tril(M)

print(U)
print(L)

#Concatenate
K = np.random.randn(5,3)
L = np.random.randn(5,2)
R = np.concatenate((K,L), axis=1)
print(R)