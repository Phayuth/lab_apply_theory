clc
clear

%found parameter of dc motor from the ekf indentication
a = 27.65; b = 17.35;
z = 1.2*a;
Nc = [1 z]; Dc = [1 0];
Np = 1; Dp = [1 a];
C = tf(Nc,Dc); G = tf(Np,Dp);
openSys = C*G*b;
closeSys = feedback(openSys,1);
figure(1); rlocus(openSys)
figure(2); subplot 211;step(closeSys)
Kp = 4; % enter kp here after look at the root locus
closeSysFinal = feedback(Kp*openSys,1);
subplot 212; step(closeSysFinal);