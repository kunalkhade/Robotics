import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import *


curve = plt.plot([],[],'ro')
p1x = np.linspace(5, 15, 200)
p1y = np.linspace(8,8, 200)


for t in np.linspace(0,3.14,200):

        x = 5*np.cos(t) + 10
        y = 5*np.sin(t) + 8
        
        plt.setp(curve, xdata = x, ydata = y)
        plt.draw()
        plt.xlim(0,20)
        plt.ylim(0,20)
        plt.xlabel(' X ')
        plt.ylabel(' Y ')
        plt.title(' Semi Circle and Line Plot ')
        plt.plot([x],[y], 'b.')
        plt.plot(p1x, p1y, 'b.')

plt.show()
