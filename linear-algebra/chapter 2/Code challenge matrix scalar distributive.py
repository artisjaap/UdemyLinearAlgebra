import numpy as np

s = 0.5
A = np.random.randn(5,5)
B = np.random.randn(5,5)

M1 = np.add(s*A, s*B)
M2 = s*np.add(A, B)

print(np.subtract(M1, M2))