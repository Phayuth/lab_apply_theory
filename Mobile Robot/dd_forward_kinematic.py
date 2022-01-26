import WMR_custom_lib
import math
import time

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

while True:
	print(f'X={X} , Y={Y} , Theta={Theta}')
	V,omega = WMR_custom_lib.DD_FKI(omegaR,omegaL,r,L)
	x_dot,y_dot,theta_dot = WMR_custom_lib.DD_FKE(V,omega,Theta)
	X = X + x_dot*Ts
	Y = Y + y_dot*Ts
	Theta = Theta + theta_dot*Ts
	time.sleep(1)