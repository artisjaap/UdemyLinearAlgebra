from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1,2,3])

v21 = np.array([1,2,4])
v22 = np.array([3,2,5])

v31 = np.array([1,0,0])
v32 = np.array([0,1,0])

v41 = np.array([2,6,-3])
v42 = np.array([0,-2,9])L

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot([0,v21[0]],[0,v21[1]],[0,v21[2]],'b')
ax.plot([0,v22[0]],[0,v22[1]],[0,v22[2]],'b')

ax.plot([0,v31[0]],[0,v31[1]],[0,v31[2]],'r')
ax.plot([0,v32[0]],[0,v32[1]],[0,v32[2]],'r')

ax.plot([0,v41[0]],[0,v41[1]],[0,v41[2]],'g')
ax.plot([0,v42[0]],[0,v42[1]],[0,v42[2]],'g')

ax.plot([0,v1[0]],[0,v1[1]],[0,v1[2]],'y')

plt.show()
