clc
clear

eta = 0.9;
a = 27.65;
b = 17.35;
c = 5.63;

wn = 2*pi*2;
zeta = 20;
lamda1 = 40;


kp_i = (eta*a)/(b*(1-eta))
kp_o = (wn^2 + 2*zeta*wn*lamda1)/(b*kp_i)
ki_o = (lamda1*wn^2)/(b*kp_i)
kd_o = (lamda1 + 2*zeta*wn - a - b*kp_i)/(b*kp_i)