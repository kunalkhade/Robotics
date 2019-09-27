import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import *

a1, a2 = 15.0, 15.0

t = np.linspace(0,3.14,50)
x = 10*np.cos(t) + 15
y = 10*np.sin(t)

print(type(x))
d = (x*x+y*y-a1*a1-a2*a2)/(2*a1*a2)
t2 = np.arctan2(-np.sqrt(1.0-d*d),d)
t1 = np.arctan2(y,x)-np.arctan2(a2*np.sin(t2),a1+a2*np.cos(t2))
x1 = a2*np.cos(t1+t2)+a1*np.cos(t1)
y1 = a2*np.sin(t1+t2)+a1*np.sin(t1) 
z = np.sum(np.square(x-x1)+np.square(y-y1))


print(type(d))
plt.xlim(0,30)
plt.ylim(0,20)
plt.plot(x,y, 'yo')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Requested Path')
plt.show()
plt.xlim(-3.14,3.14)
plt.ylim(-3.14,3.14)
plt.plot(t1, t2, 'go')
plt.xlabel('Q1')
plt.ylabel('Q2')
plt.title('Joint Angles for Path')
plt.show()
plt.xlim(0,30)
plt.ylim(0,20)
plt.plot(x1,y1,'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Traversed Path')
plt.show()


