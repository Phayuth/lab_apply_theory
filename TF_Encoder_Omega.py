import time

count = 0
t_dot_p = 0
t_p = 0
t_pre = 0
Ts = 0.01
a = 0.04

while True:
	count += 22
	t = (2*3.14*count)/(1*22)
	t_dot = (1-Ts/a)*t_dot_p  + (1/a)*(t-t_p)

	omega = (t - t_pre)/Ts

	#update
	t_dot_p = t_dot
	t_p = t

	t_pre = t
	print(t_dot - omega)
	time.sleep(Ts)