import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from drawnow import *

Curpose = [5,1,0.6*math.pi]
print(f'The Initial Pose of the robot are (x,y,phi){Curpose}-----------------')
Refpose = [3,0,6,4,3,4,3,1,0,3]

xpath = []
ypath = []
phiphi= []

i = 0
for k in range(1000):
	#Reference segment determination
	dx = Refpose[i+2]-Refpose[i]
	dy = Refpose[i+3]-Refpose[i+1]

	V = [dx,dy] # Direction vector of the current segment
	Vn= [dy,-dx] # Orthogonal direction vector of the current segment
	r = [Curpose[0]-Refpose[i],Curpose[1]-Refpose[i+1]]
	u = ((V[0]*r[0])+(V[1]*r[1]))/((V[0]*V[0])+(V[1]*V[1]))

	if u>1:
		i+=1
	dn = ((Vn[0]*r[0])+(Vn[1]*r[1]))/((Vn[0]*Vn[0])+(Vn[1]*Vn[1]))

	phiLin = math.atan2(V[1], V[0])
	phiRot = math.atan(5*dn)
	phiRef = phiLin + phiRot
	ephi   = phiRef - Curpose[2]

	v = 0.4*math.cos(ephi)
	w = 3*ephi

	xpath.append(Curpose[0])
	ypath.append(Curpose[1])
	phiphi.append(Curpose[2])

	dqxTs = [v*math.cos(Curpose[2])*0.03,v*math.sin(Curpose[2])*0.03,w*0.03]
	Curpose[0] = Curpose[0] + dqxTs[0]
	Curpose[1] = Curpose[1] + dqxTs[1]
	Curpose[2] = Curpose[2] + dqxTs[2]

xx=np.array([xpath])
yy=np.array([ypath])
xxx=np.transpose(xx)
yyy=np.transpose(yy)
plt.plot(xxx,yyy)
plt.show()