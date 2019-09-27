import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

N = 50
t0 = 0.0
t1 = 5.0
t2 = 6.0
t3 = 10.0

ta = np.linspace(t0, t1, N)
tb = np.linspace(t1, t2, N)
tc = np.linspace(t2, t3, N)

dta = (t1-t0)/N
dtb = (t2-t1)/N
dtc = (t3-t2)/N

xp1 = np.ones((N))
yp1 = np.ones((N))
th1 = np.ones((N))
xp2 = np.ones((N))
yp2 = np.ones((N))
th2 = np.ones((N))
xp3 = np.ones((N))
yp3 = np.ones((N))
th3 = np.ones((N))

r = 5.0
L = 16.0

w11 = [2]*N #wheel speed 
w12 = [2]*N 
w21 = [3]*N  
w22 = [4]*N  
w31 = [1]*N  
w32 = [2]*N  
print(w11)
xp1[0] = 0.0
yp1[0] = 0.0
th1[0] = 0.0

for i in range(N-1):
        xp1[i+1] = xp1[i] + (r*dta/2.0)*(w11[i] + w12[i])*math.cos(th1[i])
        yp1[i+1] = yp1[i] + (r*dta/2.0)*(w11[i] + w12[i])*math.sin(th1[i])
        th1[i+1] = th1[i] + (r*dta/(2.0*L))*(w11[i] - w12[i])

xp2[0] = xp1[N-1]
yp2[0] = yp1[N-1]
th2[0] = th1[N-1]

for i in range(N-1):
        xp2[i+1] = xp2[i] + (r*dtb/2.0)*(w21[i] + w22[i])*math.cos(th2[i])
        yp2[i+1] = yp2[i] + (r*dtb/2.0)*(w21[i] + w22[i])*math.sin(th2[i])
        th2[i+1] = th2[i] + (r*dtb/(2.0*L))*(w21[i] - w22[i])

xp3[0] = xp2[N-1]
yp3[0] = yp2[N-1]
th3[0] = th2[N-1]

for i in range(N-1):
        xp3[i+1] = xp3[i] + (r*dtc/2.0)*(w31[i] + w32[i])*math.cos(th3[i])
        yp3[i+1] = yp3[i] + (r*dtc/2.0)*(w31[i] + w32[i])*math.sin(th3[i])
        th3[i+1] = th3[i] + (r*dtc/(2.0*L))*(w31[i] - w32[i])

xx = np.concatenate((xp1, xp2, xp3), axis=None) 
yy = np.concatenate((yp1, yp2, yp3), axis=None)

plt.xlabel(' X- Axis ')
plt.ylabel(' Y- Axis ')
plt.title(' Path of The Robot ')
plt.plot(xx,yy, 'ro')
plt.plot(xp3[N-1],yp3[N-1], 'bo')
plt.show()

