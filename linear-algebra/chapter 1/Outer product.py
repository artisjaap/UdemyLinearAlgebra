import numpy as np

v1 = np.array([1, 2, 3, 5])
v2 = np.array([2, 5, 6])

outer = np.outer(v1, v2)
outer2 = np.outer(v2, v1)

print(outer)
print(outer2)