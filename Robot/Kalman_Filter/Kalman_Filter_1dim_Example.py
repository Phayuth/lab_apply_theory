# TEMPERATURE TEST Kalman

import numpy as np
from drawnow import *
import time
import matplotlib.pyplot as plt
import math
import random

def makeFig(): # For drawnow function
	ax1 = plt.subplot(121)
	ax1.set_ylim(34,38)
	ax1.plot(t_store,x_store)
	ax1.plot(t_store,m_store)
	ax1.legend(('filtered','measurement'), loc='upper right', shadow=True)
	ax1.set_xlabel('time')
	ax1.set_ylabel('temperature')

	ax2 = plt.subplot(122)
	ax2.plot(t_store,p_store)

	# ax3 = plt.subplot(133)
	# ax3.plot(t_store,m_store)

def sign_rand():
	sign = random.random()
	return -1 if sign < 0.5 else 1

def sin_func(t):
	freq   = 2*math.pi/30

	y = 5*math.sin(freq*t)

	return y

x = 20
p = 1
Q = 0.1
R = 4

x_store = np.array([[x]])
t_store = np.array([[0]])
p_store = np.array([[p]])
m_store = np.empty([1,1])
t = 0

while True:
	# time update
	x       = x
	p       = p + Q
	# measurement update
	z       = x
	pxy     = p
	pyy     = p + R
	w       = pxy/pyy
	new_meas= 36 + (2*sign_rand()*round(random.random(),2))
	x       = x + w*(new_meas-z)
	p       = p - w*pyy*w

	# store data and plot
	x_store = np.append(x_store,np.array([[x]]),axis=0)
	t_store = np.append(t_store,np.array([[t]]),axis=0)
	p_store = np.append(p_store,np.array([[p]]),axis=0)
	m_store = np.append(m_store,np.array([[new_meas]]),axis=0)

	if t>100:
		x_store = np.delete(x_store, 0, 0)
		t_store = np.delete(t_store, 0, 0)
		p_store = np.delete(p_store, 0, 0)
		m_store = np.delete(m_store, 0, 0)

	drawnow(makeFig)
	plt.pause(.000001)
	t+=1