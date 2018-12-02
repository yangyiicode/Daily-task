# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 15:55:54 2018

@author: Asus
"""
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(0,8)
y = np.arange(0,4)
x,y = np.meshgrid(x,y)
#z = np.random.uniform(low=10,high=20,size=(10,20))
z = np.array([[10,10,9,7,5,6,6,6],[10,9.8,9,7,4,7,7,6],[9,9,5,4,3,6,6,6],
              [10,8,8,8,5,5,6,6]])
print(z.shape)
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap=plt.cm.YlOrBr)
ax.contourf(x,y,z,zdir='z',offset=3,cmap=plt.cm.Greys)
ax.set_title(label='3D-drawing')
ax.set_xlabel('X-Aoxes')
ax.set_ylabel('Y-Aoxes')
ax.set_zlabel('Z-Aoxes')
plt.show()