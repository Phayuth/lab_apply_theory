import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from drawnow import *

def makeFig(): #Create a function that makes our desired plot
	# plt.ylim(10,10)
	# plt.xlim(10,10)
	plt.grid(True)
	# refx = Refpose[:,0]
	# refy = Refpose[:,1]
	# plt.plot(refx,refy)
	plt.plot(xpathary,ypathary)

L = 0.1 #m
Curpose = [1,-5,math.pi/2]
Refpose = [4,4]
xpath = []
ypath = []
phiphi= []

K1 = 0.3
K2 = 0.2
for k in range(2000):
	phiref = math.atan2((Refpose[1]-Curpose[1]),(Refpose[0]-Curpose[0]))
	qRef = [Refpose[0],Refpose[1],phiref]

	e1 = qRef[0] - Curpose[0]
	e2 = qRef[1] - Curpose[1]
	e3 = qRef[2] - Curpose[2]

	V  = K1*math.sqrt((e1**2)+(e2**2))
	O  = K2*e3

	if abs(O)>(math.pi/4):
		O = math.pi/4*np.sign(O)
	if abs(V)>0.8:
		V = 0.8*np.sign(V)

	xpath.append(Curpose[0])
	ypath.append(Curpose[1])
	phiphi.append(Curpose[2])

	dqxTs = [V*math.cos(Curpose[2])*0.03,V*math.sin(Curpose[2])*0.03,(V/L)*math.tan(O)*0.03]
	Curpose[0] = Curpose[0] + dqxTs[0]
	Curpose[1] = Curpose[1] + dqxTs[1]
	Curpose[2] = Curpose[2] + dqxTs[2]

	xpathary=np.transpose(np.array([xpath]))
	ypathary=np.transpose(np.array([ypath]))


	drawnow(makeFig)
	plt.pause(.000001)


# xx=np.array([xpath])
# yy=np.array([ypath])
# xxx=np.transpose(xx)
# yyy=np.transpose(yy)
# plt.plot(xxx,yyy)
# plt.show()