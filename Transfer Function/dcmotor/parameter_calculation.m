clc
clear

%found parameter of dc motor from the ekf indentication
a = 27.65; b = 17.35;
z = 1.2*a;
%   Kp = 4; % enter kp here after look at the root locus
kp = 4;


%system1
% num = [kp*b kp*z*b];
% den = [1 (a+kp*b) kp*z*b];
% HH = tf(num,den);
% rlocus(HH)
% sgrid


%system2
num2 = [b z*b];
den2 = [1 (a+b) z*b];
HHH = tf(num2,den2);
rlocus(HHH)
sgrid