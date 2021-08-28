#Code_velocity_feedforward_position_feedback.py
import math
import time
import numpy as np

# Define Variable
Ts = 0.01

# Variable PID -------------------------------------------------------------------------
Pre_error = 0
Cur_error = 0
Area_old  = 0
Kp = 1
Ki = 0
Kd = 0

# PID
def PID(Kp,Ki,Kd,desired,current,pre_error,cur_error,area_old,Ts):
	cur_error = desired - current
	V = Kp*cur_error + Kd*(cur_error - pre_error)/Ts + Ki*(area_old + cur_error*Ts)
	area_old = area_old + cur_error*Ts
	pre_error = cur_error
	return V,pre_error,cur_error,area_old

# Encoder position feedback
def enfb(Ts,PPR):
	wtick1 = encoder.get()
	wtick2 = encoder.get()
	wtheta1 = (2*math.pi*wtick1)/(PPR*Ts)
	wtheta2 = (2*math.pi*wtick2)/(PPR*Ts)
	return wtheta1,wtick2
#-------------------------------------------------------------------------------------

# Motor Parameter --------------------------------------------------------------------
PPR = 44
Gear_ratio = 170
omegaL = 50 #mm/s
omegaR = 50 #mm/s

# Input votage to Speed
def vol_det(a,b,omega_desired):
	Vol_input = (a/b)*omega_desired
#-------------------------------------------------------------------------------------
# Velocity Intergration
WLI = 0
WRI = 0

while True:
	WLI = WLI + omegaL*Ts
	WRI = WRI + omegaR*Ts
	print(WLI,WRI)
	time.sleep(Ts)