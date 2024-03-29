from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#angle between vectors
v1 = np.array([2, 4, -3])
v2 = np.array([0, -3, -3])

cosA = v1.dot(v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))
angle = np.arccos(cosA)

print(angle)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot([0, v1[0]],[0, v1[1]], [0, v1[2]], 'b')
ax.plot([0, v2[0]],[0, v2[1]], [0, v2[2]], 'r')

plt.axis((-6, 6, -6, 6))
plt.title('angle between verctors: %s rad.' %angle)
plt.show()