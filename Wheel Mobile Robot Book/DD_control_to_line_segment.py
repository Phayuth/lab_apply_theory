import math
import numpy as np
import matplotlib.pyplot as plt
import time
from drawnow import *

def makeFig(): #Create a function that makes our desired plot
	plt.ylim(-2.5,10)
	plt.xlim(-7.5,10)
	plt.grid(True)
	refx = Refpose[:,0]
	refy = Refpose[:,1]
	plt.plot(refx,refy)
	plt.plot(xpathary,ypathary)

Curpose = np.array([[5],[1],[0.6*math.pi]])
print("Curpose",Curpose)
Refpose = np.array([[3,0],[6,4],[3,4],[3,1],[0,3],[0,5],[-1,7],[-5,0],[-6,3]])
print("Refpose",Refpose)

xpath = []
ypath = []
phiphi= []
Ts = 0.03
cte1 = 0.9 # 0.4 good
cte2 = 3   # 3 good
i = 0


while True:
	try:
		#Reference segment determination
		dx = np.array(Refpose[i+1]-Refpose[i])[0] # correct take x each line segment to find dx
		dy = np.array(Refpose[i+1]-Refpose[i])[1] # correct take y each line segment to find dy

		V = np.array([[dx],[dy]])
		Vn= np.array([[dy],[-dx]])

		rx = Curpose[0,0]-Refpose[i,0]
		ry = Curpose[1,0]-Refpose[i,1]
		r  = np.array([[rx],[ry]])
		u = (np.transpose(V) @ r) / (np.transpose(V) @ V )

		if u>1 and i<np.shape(Refpose)[0]-1:
			i = i + 1
			dx = np.array(Refpose[i+1]-Refpose[i])[0]
			dy = np.array(Refpose[i+1]-Refpose[i])[1]

			V = np.array([[dx],[dy]])
			Vn= np.array([[dy],[-dx]])

			rx = Curpose[0,0]-Refpose[i,0]
			ry = Curpose[1,0]-Refpose[i,1]
			r  = np.array([[rx],[ry]])

		dn = (np.transpose(Vn) @ r)/(np.transpose(Vn) @ Vn)

		phiLin = math.atan2(V[1,0],V[0,0])
		phiRot = math.atan(5*dn)
		phiRef = phiLin + phiRot

		ephi = phiRef - Curpose[2,0]

		v = cte1*math.cos(ephi);
		w = cte2*ephi

		xpath.append(Curpose[0,0])
		ypath.append(Curpose[1,0])
		phiphi.append(Curpose[2,0])

		dq = np.array([[v*math.cos(Curpose[2,0])],[v*math.sin(Curpose[2,0])],[w]])
		Curpose = Curpose + dq * Ts

		xpathary=np.transpose(np.array([xpath]))
		ypathary=np.transpose(np.array([ypath]))

		drawnow(makeFig)
		plt.pause(.000001)

	except:
		break
xpathary=np.transpose(np.array([xpath]))
ypathary=np.transpose(np.array([ypath]))
plt.plot(xpathary,ypathary)
plt.show()