# Mobile robot DD kinematic and dynamic model
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from drawnow import *

def makeFig(): #Create a function that makes our desired plot
	#plt.ylim(-2.5,10)
	#plt.xlim(-7.5,10)
	#plt.grid(True)
	#refx = Refpose[:,0]
	#refy = Refpose[:,1]
	plt.plot(xrrefary,yrrefary)
	plt.plot(xpathary,ypathary)

xpath = []
ypath = []
xrref = []
yrref = []

m = 0.75  #kg
J = 0.001 #kgm^2
L = 0.075 #m
r = 0.024 #m
d = 0.01  #m

def rreeff(t):
	freq   = 2*math.pi/30;

	xRef   = 1.1 + 0.7*math.sin(freq*t)
	yRef   = 0.9 + 0.7*math.sin(2*freq*t)

	dxRef  = freq*0.7*math.cos(freq*t)
	dyRef  = 2*freq*0.7*math.cos(2*freq*t)

	ddxRef = -(freq**2)*0.7*math.sin(freq*t)
	ddyRef = -4*(freq**2)*0.7*math.sin(2*freq*t)

	dddxRef =-(freq**3)*0.7*math.cos(freq*t)
	dddyRef =-8*(freq**3)*0.7*math.cos(2*freq*t)

	qRef   = np.array([[xRef],[yRef],[math.atan2(dyRef, dxRef)]])
	vRef   = math.sqrt((dxRef**2)+(dyRef**2))
	wRef   = ((dxRef*ddyRef)-(dyRef*ddxRef))/((dxRef**2)+(dyRef**2))

	dvRef = (dxRef*ddxRef+dyRef*ddyRef)/vRef
	dwRef = ((dxRef*dddyRef)-(dyRef*dddxRef))/(vRef**2) - (2*wRef*dvRef)/vRef

	q = np.array([[qRef[0,0]],[qRef[1,0]],[qRef[2,0]],[vRef],[wRef]])

	return xRef,yRef,dxRef,dyRef,ddxRef,ddyRef,dddxRef,dddyRef,qRef,vRef,wRef,dvRef,dwRef,q
t = 0
while True:
	# Calculate torques from the trajectory and inverse model
	xRef,yRef,dxRef,dyRef,ddxRef,ddyRef,dddxRef,dddyRef,qRef,vRef,wRef,dvRef,dwRef,q = rreeff(t)
	v = vRef
	w = wRef
	dv = dvRef
	dw = dwRef
	tau = np.array([[(r*(dv*m-d*w*m*w))/2 + (r*(dw*(m*(d**2)+J) + d*w*m*v))/L],[(r*(dv*m-d*w*m*w))/2 - (r*(dw*(m*(d**2)+J) + d*w*m*v))/L]])

	# Robot motion simulation using kinematic and dynamic model
	phi = q[2,0]
	v = q[3,0]
	w = q[4,0]
	F = np.array([[v*math.cos(phi) - d*w*math.sin(phi)],[v*math.sin(phi) + d*w*math.cos(phi)],[w],[d*(w**2)],[-(d*w*v*m)/(m*(d**2) + J)]])
	G = np.array([[0,0],[0,0],[0,0],[1/(m*r),1/(m*r)],[L/(2*r*(m*(d**2) + J)),-L/(2*r*(m*(d**2) + J))]])

	xpath.append(q[0,0])
	ypath.append(q[1,0])
	xrref.append(xRef)
	yrref.append(yRef)

	dq = F + G @ tau  # State space model
	q  =  q + dq * 0.033   # Euler integration

	xpathary = np.transpose(np.array([xpath]))
	ypathary = np.transpose(np.array([ypath]))
	xrrefary = np.transpose(np.array([xrref]))
	yrrefary = np.transpose(np.array([yrref]))

	drawnow(makeFig)
	plt.pause(.000001)

	t += 0.033