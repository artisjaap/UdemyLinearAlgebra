import numpy as np

A = np.random.randn(5, 5)
B = np.random.randn(5, 5)

trAtrB = np.trace(A) + np.trace(B)
trAB = np.trace(np.add(A,B))

print(trAtrB-trAB)


l = 0.3
trlA = np.trace(l*A)
ltrA = l*np.trace(A)

print(trlA-ltrA)