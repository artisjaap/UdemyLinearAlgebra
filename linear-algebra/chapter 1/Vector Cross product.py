from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([-3,2,3])
v2 = np.array([2,5,6])
vc = np.cross(v1,v2)

fig = plt.figure()
ax = fig.gca(projection='3d')

xx, yy =  np.meshgrid(np.linspace(-10,10,10), np.linspace(-10,10,10))
z1 = (-vc[0]*xx - vc[1]*yy)/vc[2]
# ax.plot_surface(xx,yy,z1)

ax.plot([0, v1[0]], [0, v1[1]],[0,v1[2]],'k')
ax.plot([0, v2[0]], [0, v2[1]],[0,v2[2]],'k')
ax.plot([0, vc[0]], [0, vc[1]],[0,vc[2]],'r')

ax.view_init(azim=150, elev=45)
plt.show()