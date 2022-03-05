from math import sin,cos
import numpy as np
import matplotlib.pyplot as plt
import time
from drawnow import *

def makeFig():
	plt.plot(link_1_x,link_1_y)
	plt.plot(link_2_x,link_2_y)
	plt.plot(link_3_x,link_3_y)
	plt.xlim([-15, 15])
	plt.ylim([-15, 15])
	# plt.scatter([xRef], [yRef],facecolor='red')


link_1_r = 5
link_2_r = 5
link_3_r = 2

theta_1 = 0
theta_2 = 0
theta_3 = 0

while True:
	x_1 = link_1_r*sin(theta_1)
	y_1 = link_1_r*cos(theta_1)
	
	x_2 = x_1 + link_2_r*sin(theta_2+theta_1)
	y_2 = y_1 + link_2_r*cos(theta_2+theta_1)

	x_3 = x_2 + link_3_r*sin(theta_3+theta_2+theta_1)
	y_3 = y_2 + link_3_r*cos(theta_3+theta_2+theta_1)

	link_1_x = [0,x_1]
	link_1_y = [0,y_1]

	link_2_x = [x_1,x_2]
	link_2_y = [y_1,y_2]

	link_3_x = [x_2,x_3]
	link_3_y = [y_2,y_3]

	drawnow(makeFig)
	time.sleep(0.1)
	theta_1 = theta_1 + 0.01
	theta_2 = theta_2 + 0.05
	theta_3 = theta_2 + 0.01