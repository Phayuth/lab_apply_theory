# DD_control_to_ref_pose_back_stepping_controller
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from drawnow import *
import random

# Ref pose
def ref_cicle(t):
	freq   = 2*math.pi/30
	radius = 3

	x     = radius*math.cos(freq*t)
	y     = radius*math.sin(freq*t)

	xdot  = -radius*freq*math.sin(freq*t)
	ydot  = radius*freq*math.cos(freq*t)

	xddot = -radius*(freq**2)*math.cos(freq*t)
	yddot = -radius*(freq**2)*math.sin(freq*t)

	xdddot= radius*(freq**3)*math.sin(freq*t)
	ydddot= -radius*(freq**3)*math.cos(freq*t)

	vr    = math.sqrt((xdot**2 + ydot**2))
	wr    = ((xdot*yddot-ydot*xddot))/((xdot**2 + ydot**2))

	vdotr = (xdot*xddot+ydot*yddot)/vr
	wdotr = ((xdot*ydddot-ydot*xdddot)/(vr**2))-((2*wr*vdotr)/vr)

	return x,y,vr,wr,ydot,xdot,vdotr,wdotr

def ref_sin_45(t):
	freq   = 2*math.pi/30
	radius = 5

	x     = (math.cos(math.radians(45))*t)-(math.sin(math.radians(45))*radius*math.sin(freq*t))
	y     = (math.sin(math.radians(45))*t)+(math.cos(math.radians(45))*radius*math.sin(freq*t))

	xdot  = math.cos(math.radians(45))-(math.sin(math.radians(45))*radius*freq*math.cos(freq*t))
	ydot  = math.sin(math.radians(45))+(math.cos(math.radians(45))*radius*freq*math.cos(freq*t))

	xddot = math.sin(math.radians(45))*radius*(freq**2)*math.sin(freq*t)
	yddot = -math.cos(math.radians(45))*radius*(freq**2)*math.sin(freq*t)

	xdddot= math.sin(math.radians(45))*radius*(freq**3)*math.cos(freq*t)
	ydddot= -math.cos(math.radians(45))*radius*(freq**3)*math.cos(freq*t)

	vr    = math.sqrt((xdot**2 + ydot**2))
	wr    = ((xdot*yddot-ydot*xddot))/((xdot**2 + ydot**2))

	vdotr = (xdot*xddot+ydot*yddot)/vr
	wdotr = ((xdot*ydddot-ydot*xdddot)/(vr**2))-((2*wr*vdotr)/vr)

	return x,y,vr,wr,ydot,xdot,vdotr,wdotr


def makeFig(): #Create a function that makes our desired plot
	#plt.ylim(-15,15)
	#plt.xlim(-15,15)
	ax1 = plt.subplot(121)
	ax1.grid(True)
	ax1.plot(xrrefary,yrrefary)
	ax1.scatter([xRef], [yRef],facecolor='red')
	ax1.plot(xpathary,ypathary)
	ax1.scatter(qc[0,0],qc[1,0],facecolor='black')
	#ax1.set_xlim([-10, 10])
	#ax1.set_ylim([-10, 10])
	ax1.legend(('reference_path','robot_path'), loc='upper left', shadow=True)
	ax1.set_xlabel('x_coordinate')
	ax1.set_ylabel('y_coordinate')
	ax1.set_title('XY_Path_control')

	ax2 = plt.subplot(222)
	ax2.plot(timesary,xpathary)
	ax2.plot(timesary,xrrefary)
	ax2.set_ylim([-10, 10])
	ax2.set_xlabel('times')
	ax2.set_ylabel('x_coordinate')
	ax2.set_title('reference_and_current_X')

	ax3 = plt.subplot(224)
	ax3.plot(timesary,ypathary)
	ax3.plot(timesary,yrrefary)
	ax3.set_ylim([-10, 10])
	ax3.set_xlabel('times')
	ax3.set_ylabel('y_coordinate')
	ax3.set_title('reference_and_current_Y')


# Store path
# xrref = np.array([[5]])
# yrref = np.array([[0]])
# xpath = np.array([[6]])
# ypath = np.array([[0]])
# times = np.array([[0]])

xrref = np.empty([1,1])
yrref = np.empty([1,1])
xpath = np.empty([1,1])
ypath = np.empty([1,1])
times = np.empty([1,1])

qc = np.array([[0],[0],[0]]) # (3X1)


def errorr(qr,qc):

	theta = qc[2,0]
	T = np.array([[math.cos(theta),math.sin(theta),0],
	             [-math.sin(theta),math.cos(theta),0],
	             [      0         ,     0         ,1]]) # (3X3)
	qe = T @ (qr - qc) # (3X1)

	return qe


def controlkinematic(qe,vr,wr):
	k1 = 10 # need tuning defualt 10
	k2 = 5 # need tuning defualt 5
	k3 = 4 # need tuning defualt 4

	vc = vr*math.cos(qe[2,0])+k1*qe[0,0]
	wc = wr+k2*vr*qe[1,0]*k3*math.sin(qe[2,0])

	return vc,wc

def dynamic_model(taur,taul):
	mass     = 4 #kg
	radius   = 0.03 #m
	length   = 0.3 #m
	Inertial = 2.5 #kg*m^2

	E          = np.array([[1/mass*radius,1/mass*radius],
	                      [length/(2*r*Inertial),-length/(2*r*Inertial)]])
	tau        = np.array([[taur],[taul]])
	dyn        = E @ tau
	dynvdot    = dyn[0,0]
	dythetaddot= dyn[1,0]

	return dynvdot,dythetaddot

def dynamic_torq(vdotref,wdotref):
	mass     = 4 #kg
	radius   = 0.03 #m
	length   = 0.3 #m
	Inertial = 2.5 #kg*m^2
	ka       = 100 # need tuning
	kb       = 3000 # need tuning

	tua1c = 1/2*((mass*radius*(vdotref+ka*z1))+((2*radius*Inertial/length)*(wdotref+kb*z2)))
	tua2c = 1/2*((mass*radius*(vdotref+ka*z1))-((2*radius*Inertial/length)*(wdotref+kb*z2)))

	return tua1c,tua2c


t = 0
while True:

	xRef,yRef,vr,wr,ydot,xdot,vdotref,wdotref = ref_cicle(t)
	#xRef,yRef,vr,wr,ydot,xdot,vdotref,wdotref = ref_sin_45(t)
	theta_ref= math.atan2(ydot, xdot)
	qr       = np.array([[xRef],[yRef],[theta_ref]])
	qe       = errorr(qr,qc)
	vc,wc    = controlkinematic(qe,vr,wr)
	print(f'{vc},{wc}')

	# Store path
	xrref = np.append(xrref, np.array([[xRef]]), axis=0)
	yrref = np.append(yrref, np.array([[yRef]]), axis=0)
	xpath = np.append(xpath, np.array([[qc[0,0]]]), axis=0)
	ypath = np.append(ypath, np.array([[qc[1,0]]]), axis=0)
	times = np.append(times, np.array([[t]]), axis=0)

	# Plot
	xrrefary = xrref # np.transpose(np.array([xrref]))
	yrrefary = yrref # np.transpose(np.array([yrref]))
	xpathary = xpath # np.transpose(np.array([xpath]))
	ypathary = ypath # np.transpose(np.array([ypath]))
	timesary = times # np.transpose(np.array([times]))
	drawnow(makeFig)
	#plt.pause(.000001)

	# Euler Intergral Update new path
	dq = np.array([[vc*math.cos(qc[2,0])],
		           [vc*math.sin(qc[2,0])],
		           [wc]]) # (3X3)
	qc  = qc + dq * 0.033 + random.random()/10

	t += 1