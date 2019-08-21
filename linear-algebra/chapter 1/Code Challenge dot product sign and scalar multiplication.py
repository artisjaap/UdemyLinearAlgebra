import numpy as np

v1 = np.array([-3, 4,  5])
v2 = np.array([3, 6, -3])

s1 = 2
s2 = 3

dotUnscaled = v1.dot(v2)

scaled1 = (v1 * s1)
scaled2 = (v2 * s2)

dotScaled = scaled1.dot(scaled2)

print(dotUnscaled)
print(dotScaled)