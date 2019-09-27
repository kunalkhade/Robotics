import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import *

a1, a2= 15.0, 15.0
a = ()
t = 30

p1x = np.linspace(5, 5, t)
p1y = np.linspace(0, 15, t)
p2x = np.linspace(5, 20, t)
p2y = np.linspace(15, 15, t)
p3x = np.linspace(20, 20, t)
p3y = np.linspace(15, 0, t)
p4x = np.linspace(20, 5, t)
p4y = np.linspace(0, 0, t)

def inv_kin(x, y):
    d = (x*x+y*y-a1*a1-a2*a2)/(2*a1*a2)
    t2 = np.arctan2(-np.sqrt(1.0-d*d),d)
    t1 = np.arctan2(y,x)-np.arctan2(a2*np.sin(t2),a1+a2*np.cos(t2))
    x1 = a2*np.cos(t1+t2)+a1*np.cos(t1)
    y1 = a2*np.sin(t1+t2)+a1*np.sin(t1) 
    z = np.sum(np.square(x-x1)+np.square(y-y1))
    return [x1, y1, t1, t2]

a, b, c, d = inv_kin(p1x, p1y)
e, f, g, h = inv_kin(p2x, p2y)
i, j, k, l = inv_kin(p3x, p3y)
m, n, o, p = inv_kin(p4x, p4y)

x_axis = np.concatenate((a,e,i,m))
y_axis = np.concatenate((b,f,j,n))
q1 = np.concatenate((c,g,k,o))
q2 = np.concatenate((d,h,l,p))

plt.plot(p1x, p1y, 'b.')
plt.plot(p2x, p2y,'b.')
plt.plot(p3x, p3y,'b.')
plt.plot(p4x, p4y,'b.')
plt.xlim(0,25)
plt.ylim(0,25)
plt.xlabel(' X ')
plt.ylabel(' Y ')
plt.title(' Requested Path ')
plt.show()

plt.plot(x_axis, y_axis, 'b.')
plt.xlim(0,25)
plt.ylim(0,25)
plt.xlabel(' X ')
plt.ylabel(' Y ')
plt.title(' Traversed Path ')
plt.show()


plt.plot(q1, q2, 'g.')
plt.xlim(-3.14,3.14)
plt.ylim(-3.14,3.14)
plt.xlabel(' Q1 ')
plt.ylabel(' Q2 ')
plt.title(' Joint Angles for Path ')
plt.show()
