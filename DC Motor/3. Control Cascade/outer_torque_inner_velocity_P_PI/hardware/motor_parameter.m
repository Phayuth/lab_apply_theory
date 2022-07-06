clear
clc

% parameters from estimation
a = 24.43;
b = 40.34;
c = 18.37;
R = 0.3826
Kt = 0.6777
L = 0.001; % Henry

J = (Kt/(R*b))
Tc = (c*J)
D = (a*R*J - Kt^2)/R

wn = 2*pi*6;
zeta = 1;

% We want to choose kpi and kii in function of kpo
kpo = 10
kpi = -(D^2*R+J^2*R*wn^2+kpo*(Kt^2-2*J*R*wn*zeta)+D*(Kt^2+R*(kpo-2*J*wn*zeta))/(Kt*(D^2+kpo^2+J^2*wn^2-2*J*kpo*wn*zeta+2*D*(kpo-J*wn*zeta))))
kii = (J*(-Kt^2+kpo*R)*wn^2)/(Kt*(D^2+kpo^2+J^2*wn^2-2*J*kpo*wn*zeta+2*D*(kpo-J*wn*zeta)))

% We want to choose kpo and kii while giving kpi = 0
% kpi = 0
% kii = (2*zeta*wn*R*J-R*D-Kt^2)/(Kt*J)
% kpo = (wn^2*R*J)/(Kt*kii)-D
