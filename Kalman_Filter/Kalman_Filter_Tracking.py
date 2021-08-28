import numpy as np
from drawnow import *
import time
import matplotlib.pyplot as plt
import math
import random

def makeFig(): # For drawnow function
	plt.plot(x_store,y_store)
	plt.grid(True)

# Covariance for EKF simulation
Q = np.diag([0.1,0.1,np.deg2rad(1.0),1.0]) ** 2
R = np.diag([1.0, 1.0]) ** 2

def input():
	v = -1 #m/s
	w = 0.2 #rad/s

	u = np.array([[v],[w]])

	return u

def measure(t):

	freq   = 2*math.pi/30

	x = 5*math.cos(freq*t)
	y = 5*math.sin(freq*t)
	z_measure = np.array([[x],[y]])

	return z_measure

def EKF_predict(x,u,P,Q):

	DT = 0.03

	yaw = x[2, 0]
	v   = u[0, 0]

	F = np.array([[1.0, 0, 0, 0],
	              [0, 1.0, 0, 0],
	              [0, 0, 1.0, 0],
	              [0, 0,   0, 0]]) # (4X4)

	B = np.array([[DT * math.cos(yaw), 0],
	              [DT * math.sin(yaw), 0],
	              [0.0               ,DT],
	              [1.0               ,0.0]]) # (4X2)

	J_F = np.array([[1.0, 0.0, -DT * v * math.sin(yaw), DT * math.cos(yaw)],
					[0.0, 1.0,  DT * v * math.cos(yaw), DT * math.sin(yaw)],
					[0.0, 0.0,                     1.0,                0.0],
					[0.0, 0.0,                     0.0,                1.0]])

	x_pred = F @ x + B @ u        # (4X1) = (4X4)(4X1)+(4X2)(2X1)
	p_pred = J_F @ P @ np.transpose(J_F) + Q

	return x_pred,p_pred

def EKF_update(x_pred,z_measure,p_pred,R):

	H = np.array([[1, 0, 0, 0],
		          [0, 1, 0, 0]])

	J_H = np.array([[1, 0, 0, 0],
		            [0, 1, 0, 0]])

	z_pred = H @ x_pred
	y = z_measure - z_pred
	S = J_H @ p_pred @ np.transpose(J_H) + R
	K = p_pred @ np.transpose(J_H) @ np.linalg.inv(S)

	x_est = x_pred + K @ y
	p_est = (np.eye(len(x_est)) - K @ J_H) @ p_pred

	return x_est,p_est

# Initialize
x_est = np.array([[0],[0],[0],[0]])
p_est = np.eye(4)

x_store = np.empty([1,1])
y_store = np.empty([1,1])
t_store = np.empty([1,1])

t=0
while True:
	u = input()
	z_measure = measure(t)
	x_pred,p_pred = EKF_predict(x_est,u,p_est,Q)
	x_est,p_est = EKF_update(x_pred,z_measure,p_pred,R)

	x_store = np.append(x_store,np.array([[x_est[0,0]]]), axis=0)
	y_store = np.append(y_store,np.array([[x_est[1,0]]]), axis=0)
	t_store = np.append(t_store,np.array([[t]]), axis=0)

	if t>100:
		x_store = np.delete(x_store, 0, 0)
		y_store = np.delete(y_store, 0, 0)
		t_store = np.delete(t_store, 0, 0)
	drawnow(makeFig)
	plt.pause(.000001)
	t+=1