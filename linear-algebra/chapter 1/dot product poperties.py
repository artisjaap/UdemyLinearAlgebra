import numpy as np

#Distributive

v1 = np.random.random(5)
v2 = np.random.random(5)
v3 = np.random.random(5)

vr1 = v1.dot(v2+v3)
vr2 = v1.dot(v2) + v1.dot(v3)

print(vr1)
print(vr2)