import numpy as np
import matplotlib.pyplot as plt
import time
from drawnow import *

def angnorm(theta):

	if theta>0:
		if theta>np.pi:
			theta = (2*np.pi-theta)*(-1)

	if theta<0:
		if theta*(-1)>np.pi:
			theta = (2*np.pi-(-theta))*(-1)

	return theta

def makeFig(): #Create a function that makes our desired plot
	plt.scatter(q[0,0], q[1,0],facecolor='red')
	plt.scatter([xRef], [yRef],facecolor='black')
	plt.plot(xrrefary,yrrefary)
	plt.plot(xpathary,ypathary)

xpath = []
ypath = []
xrref = []
yrref = []
t = 0
q = np.array([[1.1],[0.8],[0]])


def rreeff(t):
	freq   = 2*np.pi/30

	xRef   = 1.1 + 0.7*np.sin(freq*t)
	yRef   = 0.9 + 0.7*np.sin(2*freq*t)

	dxRef  = freq*0.7*np.cos(freq*t)
	dyRef  = 2*freq*0.7*np.cos(2*freq*t)

	ddxRef = -(freq**2)*0.7*np.sin(freq*t)
	ddyRef = -4*(freq**2)*0.7*np.sin(2*freq*t)

	qRef   = np.array([[xRef],[yRef],[np.arctan2(dyRef, dxRef)]])
	vRef   = np.sqrt((dxRef**2)+(dyRef**2))
	wRef   = ((dxRef*ddyRef)-(dyRef*ddxRef))/((dxRef**2)+(dyRef**2))
	uRef   = np.array([[vRef],[wRef]])

	return xRef,yRef,dxRef,dyRef,ddxRef,ddyRef,qRef,vRef,wRef,uRef

while True:
	xRef,yRef,dxRef,dyRef,ddxRef,ddyRef,qRef,vRef,wRef,uRef = rreeff(t)

	e = np.array([[np.cos(q[2,0]),np.sin(q[2,0]),0],
		         [-np.sin(q[2,0]),np.cos(q[2,0]),0],
		         [      0          ,     0          ,1]]) @ (qRef - q)

	vRef = uRef[0,0]
	wRef = uRef[1,0]

	eX    = e[0,0]
	eY    = e[1,0]
	ePhi  = angnorm(e[2,0])
	zeta  = 0.9    # Experiment with this control design parameter
	g     = 85     # Experiment with this control design parameter
	Kx    = 2*zeta*np.sqrt((wRef**2)+g*(vRef**2))
	Kphi  = Kx
	Ky    = g*vRef
	# Gains can also be constant e.g.: Kx = Kphi = 3; Ky = 30
	print(f"thetaref = {qRef[2,0]} ,    thetacur = {q[2,0]}")
	# Control: feedforward and feedback
	v = vRef*np.cos(ePhi) + Kx*eX
	w = wRef + Ky*eY + Kphi*ePhi

	xpath.append(q[0,0])
	ypath.append(q[1,0])
	xrref.append(xRef)
	yrref.append(yRef)

	dq = np.array([[v*np.cos(q[2,0])],[v*np.sin(q[2,0])],[w]])
	q = q + dq * 0.033

	xpathary = np.transpose(np.array([xpath]))
	ypathary = np.transpose(np.array([ypath]))
	xrrefary = np.transpose(np.array([xrref]))
	yrrefary = np.transpose(np.array([yrref]))

	drawnow(makeFig)
	plt.pause(.000001)
	t += 0.033