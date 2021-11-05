import numpy as np

def encoder_theta_2_omega(GR,PPR,count,theta_p,omega_p,a,Ts):
	"""
	Transfer function for determining the wheel velocity from encoder T(s)=s/(as+1)
	GR = Gearbox
	PPR = Pulse per revolution
	count = Encoder count
	theta = Current theta calculate from current encoder count (rad)
	theta_p = Previous theta value (rad)
	omega = Current omega (rad/s)
	omega_p = Previous omega value (rad/s)
	a = Some small constant for tuning signal and help filter out noise
	Ts = Sampling time (s)
	"""
	theta = (2*3.14*count)/(GR*PPR)
	omega = (1-Ts/a)*omega_p  + (1/a)*(theta-theta_p)
	return omega,theta

def DD_FKI(Wr,Wl,r,L):
	"""
	Differential Drive Wheel Mobile Robot Internal Forward Kinematic 
	Calculate Linear Velocity V (m/s) and Angular Velocity W (rad/s) from each wheel Wr,Wl (rad/s)
	"""
	V = (r*Wr/2) + (r*Wl/2)
	W = (r*Wr/L) - (r*Wl/L)
	return V,W

def DD_FKE(V,W,theta):
	"""
	Differential Drive Wheel Mobile Robot External Forward Kinematic
	X_dot = state_matrix @ input_matrix
	"""
	state_matrix = np.array([[math.cos(theta),0],
							 [math.sin(theta),0],
							 [      0        ,1]])
	input_matrix = np.array([[V],
							 [W]])
	state = state_matrix.dot(input_matrix)
	x_dot     = state[0]
	y_dot     = state[1]
	theta_dot = state[2]
	return x_dot,y_dot,theta_dot

def DD_IVK(V,W,r,L):
	"""
	Differential Drive Wheel Mobile Robot Inverse Kinematic
	Calculate each wheel velocity (rad/s) from V(m/s) and W(rad/s)
	r = Wheel radius (m)
	L = Robot base from left wheel to right wheel (m)
	"""
	Wr=(2*V+W*L)/(2*r)
	Wl=(2*V-W*L)/(2*r)
	return Wr,Wl