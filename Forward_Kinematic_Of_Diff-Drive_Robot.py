#forward kinematic of diff-drive robot
#import library

import math
import time
import numpy as np

#Robot Parameter
#
#       ______________
#       |            |
# ||    |            |     ||
# ||----|            |-----|| r = wheel raduis
# ||    |            |     ||
#       |____________|
#
# <------------------------>
#   L = Robot base

r = 80 #mm
L = 230 #mm

# Initial Pose
X = 0
Y = 0
Theta = math.radians(90)
Ts = 1
omegaR  = 0.5 #mm per sec
omegaL  = 0.5 #mm per sec

# Forward Kinematic Internal-------------------------------------
def FKI(Wr,Wl,rr,LB):
	velocity  = (rr*Wr/2) + (rr*Wl/2)
	angular_v = (rr*Wr/LB) - (rr*Wl/LB)
	return velocity,angular_v
#----------------------------------------------------------------

# Forward Kinematic External-------------------------------------
def FKE(velocity,angular_v,theta):
	m = np.array([[math.cos(theta),0],[math.sin(theta),0],[0,1]])
	n = np.array([[velocity],[angular_v]])
	o = m.dot(n) # multiply matrix in numpy
	x_dot     = o[0]#math.cos(theta)*velocity    o[0]
	y_dot     = o[1]#math.sin(theta)*velocity    o[1]
	theta_dot = o[2]#angular_v                   o[2]
	return x_dot,y_dot,theta_dot
#----------------------------------------------------------------

while True:
	print(f'X={X} , Y={Y} , Theta={Theta}')
	V,omega = FKI(omegaR,omegaL,r,L)
	x_dot,y_dot,theta_dot = FKE(V,omega,Theta)
	X = X + x_dot*Ts
	Y = Y + y_dot*Ts
	Theta = Theta + theta_dot*Ts
	time.sleep(1)