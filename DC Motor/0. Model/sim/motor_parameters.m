clear
clc

Ra = 14.3;
Kt = 0.05;
Kb = 0.063;
Tc = 0.053*Kt;
D  = 9.4e-5*Kt;
J0 = 1.94e-4*Kt;

a = (Kt*Kb+Ra*D)/Ra/J0
b = Kt/Ra/J0
c = Tc/J0