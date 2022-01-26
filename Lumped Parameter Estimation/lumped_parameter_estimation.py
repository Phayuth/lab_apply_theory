from __future__ import print_function
import Adafruit_BBIO.PWM as PWM
import time
import numpy as np
import time

def encoder_theta_2_omega(GR,PPR,count,theta_p,omega_p,a,Ts):
	theta = (2*3.14*count)/(GR*PPR)
	omega = (1-Ts/a)*omega_p  + (1/a)*(theta-theta_p)
	return omega,theta

def input(A,W,Ts):
	return A*np.sin(W*Ts)

def EKF()

def main():
	# assign pin PWM
	Lpwm="P8_13"
	Rpwm="P9_14"

	#start PWM @ 0 duty @ 400hz 
	PWM.start(Lpwm, 0, 400)
	PWM.start(Rpwm, 0, 400)
	
	GR = 13
	PPR = 44
	a = 0.04
	Ts = 0.01

	theta_p = 0
	omega_p = 0
	
	while T<duration:
		encoder = bbio.readencoder()

		omega = encoder_theta_2_omega(GR,PPR,encoder,theta_p,omega_p,a,Ts)

		if pwm < 0:
			PWM.set_duty_cycle(Lpwm,pwm)
			PWM.set_duty_cycle(Rpwm,0)
		elif pwm > 0:
			PWM.set_duty_cycle(Lpwm,0)
			PWM.set_duty_cycle(Rpwm,pwm)
		else:
			PWM.set_duty_cycle(Lpwm,0)
			PWM.set_duty_cycle(Rpwm,0)		

		#update
		theta_p = theta
		omega_p = omega
		time.sleep(Ts)

	# End Loop
	PWM.stop(Lpwm)
	PWM.stop(Rpwm)
	PWM.cleanup()
	print("Parameter a = ", a)
	print("Parameter b = ", b)

if __name__ == "__main__":
	main()