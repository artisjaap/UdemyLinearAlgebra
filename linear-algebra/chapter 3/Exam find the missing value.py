import numpy as np

M = np.array([[2,4],[2,1]])
print(M)

v = np.array([[3],[4]])

# r = np.matmul(M,v)
r = M@v

print(r)