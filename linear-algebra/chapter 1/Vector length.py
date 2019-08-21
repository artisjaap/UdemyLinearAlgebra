import numpy as np

v = np.array([1,2,3,4,5,6])

mag = np.sqrt(v.dot(v))

print(mag)

print(np.linalg.norm(v))