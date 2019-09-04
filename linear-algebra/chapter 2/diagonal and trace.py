import numpy as np

M = 5*np.random.randn(4, 4)
diag = np.diag(M)
tr = np.trace(M)

print(M)
print(diag)
print(tr)