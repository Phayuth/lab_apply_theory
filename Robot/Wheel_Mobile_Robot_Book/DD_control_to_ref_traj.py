import math
import numpy as np
import matplotlib.pyplot as plt
import time
from drawnow import *

def normalize_angle(theta):
	"""Normalize an angle theta to theta_norm so that: 0 <= theta_norm < 2 * np.pi"""
	twopi =  math.pi #* 2

	if theta >= twopi:
		m = math.floor(theta/twopi)
		if theta/twopi - m > 0.99999:   # account for rounding errors
			m += 1
		theta_norm = theta - m * twopi
	elif theta < 0:
		m = math.ceil(theta/twopi)
		if theta/twopi - m < -0.99999:   # account for rounding errors
			m -= 1
		theta_norm = abs(theta - m * twopi)
	else:
		theta_norm = theta
	return theta_norm

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
t = 0
k = 0
q = np.array([[1.1],[0.8],[0]])

def rreeff(t):
	freq   = 2*math.pi/30

	xRef   = 1.1 + 0.7*math.sin(freq*t)
	yRef   = 0.9 + 0.7*math.sin(2*freq*t)

	dxRef  = freq*0.7*math.cos(freq*t)
	dyRef  = 2*freq*0.7*math.cos(2*freq*t)

	ddxRef = -(freq**2)*0.7*math.sin(freq*t)
	ddyRef = -4*(freq**2)*0.7*math.sin(2*freq*t)

	qRef   = np.array([[xRef],[yRef],[math.atan2(dyRef, dxRef)]])
	vRef   = math.sqrt((dxRef**2)+(dyRef**2))
	wRef   = ((dxRef*ddyRef)-(dyRef*ddxRef))/((dxRef**2)+(dyRef**2))
	uRef   = np.array([[vRef],[wRef]])

	return xRef,yRef,dxRef,dyRef,ddxRef,ddyRef,qRef,vRef,wRef,uRef

while True:
	xRef,yRef,dxRef,dyRef,ddxRef,ddyRef,qRef,vRef,wRef,uRef = rreeff(t)

	e = np.array([[math.cos(q[2,0]),math.sin(q[2,0]),0],[-math.sin(q[2,0]),math.cos(q[2,0]),0],[0,0,1]]) @ (qRef - q)

	vRef = uRef[0,0]
	wRef = uRef[1,0]

	eX    = e[0,0]
	eY    = e[1,0]
	ePhi  = normalize_angle(e[2,0])
	zeta  = 0.9    # Experiment with this control design parameter
	g     = 85     # Experiment with this control design parameter
	Kx    = 2*zeta*math.sqrt((wRef**2)+g*(vRef**2))
	Kphi  = Kx
	Ky    = g*vRef
	# Gains can also be constant e.g.: Kx = Kphi = 3; Ky = 30

	# Control: feedforward and feedback
	v = vRef*math.cos(e[2,0]) + Kx*e[0,0]
	w = wRef + Ky*e[1,0] + Kphi*e[2,0]

	xpath.append(q[0,0])
	ypath.append(q[1,0])
	xrref.append(xRef)
	yrref.append(yRef)

	dq = np.array([[v*math.cos(q[2,0])],[v*math.sin(q[2,0])],[w]])
	q = q + dq * 0.033

	xpathary = np.transpose(np.array([xpath]))
	ypathary = np.transpose(np.array([ypath]))
	xrrefary = np.transpose(np.array([xrref]))
	yrrefary = np.transpose(np.array([yrref]))

	drawnow(makeFig)
	plt.pause(.000001)


	t += 0.033
	k += 1
	print("ok")