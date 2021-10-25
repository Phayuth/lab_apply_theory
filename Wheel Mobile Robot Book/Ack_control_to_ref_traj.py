import numpy as np
import matplotlib.pyplot as plt
import time
from drawnow import *
import math

def angnorm(theta):

	if theta>0:
		if theta>math.pi:
			theta = (2*math.pi-theta)*(-1)

	if theta<0:
		if theta*(-1)>math.pi:
			theta = (2*math.pi-(-theta))*(-1)

	return theta

Ts = 0.03
d = 0.1
def reff(t):
	freq = 2*np.pi/30
	xRef = 1.1 + 0.7*np.sin(freq*t)
	yRef = 0.9 + 0.7*np.sin(2*freq*t)
	return xRef,yRef

def makeFig(): #Create a function that makes our desired plot
	plt.plot(xrrefary,yrrefary)
	plt.plot(xpathary,ypathary)
	plt.legend(('reference_path','robot_path'), loc='upper left', shadow=True)

xpath = []
ypath = []
xrref = []
yrref = []

# Control Gain
Kphi = 2;
Kv = 5;

t = 0
upgradedControl = True

q = np.array([[1.1],[0.8],[0]])

while True:
	#Reference
	xRef,yRef = reff(t)
	phiRef = np.arctan2((yRef-q[1,0]),(xRef-q[0,0]))
	qRef = np.array([[xRef],[yRef],[phiRef]])

	# Error with respect to the (moving) reference
	e = qRef - q;		  # Error on x, y and orientation
	e[2,0] = angnorm(e[2,0]) # Mapped to the [-pi, pi] interval
	print(f"phiref = {phiRef} ,    phicurr = {q[2,0]}")
	# Control
	alpha = e[2,0]*Kphi		  # Orientation control (basic)
	v = np.sqrt(e[0,0]**2+e[1,0]**2)*Kv # Forward-motion control (basic)
	# if upgradedControl
	# 	# If e(3) is not on the [-pi/2, pi/2], +/- pi should be added
	# 	# to e(3), and negative velocity should be commanded
	# 	v = v*sign(cos(e(3)));  % Changing sign of v if necessary
	# 	e(3) = atan(tan(e(3))); % Mapped to the [-pi/2, pi/2] interval
	# 	alpha = e(3)*Kphi;	  % Orientation control (upgraded)
	# end

	xpath.append(q[0,0])
	ypath.append(q[1,0])
	xrref.append(xRef)
	yrref.append(yRef)

	# Physical limitations of the vehicle
	if abs(alpha)>np.pi/4:
		alpha = np.pi/4*np.sign(alpha)
	if abs(v)>0.8:
		v = 0.8*np.sign(v)

	# Robot motion simulation
	dq = np.array([[v*np.cos(q[2,0])],[v*np.sin(q[2,0])],[v/d*np.tan(alpha)]])
	noise = 0.00 # Set to experiment with noise (e.g. 0.001)
	q = q + Ts*dq #+ randn(3,1)*noise; # Euler integration

	xpathary = np.transpose(np.array([xpath]))
	ypathary = np.transpose(np.array([ypath]))
	xrrefary = np.transpose(np.array([xrref]))
	yrrefary = np.transpose(np.array([yrref]))

	drawnow(makeFig)
	plt.pause(.000001)
	t+=0.03
	time.sleep(0.01)