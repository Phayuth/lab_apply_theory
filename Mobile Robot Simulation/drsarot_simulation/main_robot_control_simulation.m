clear
close all
clc

global w_angle
% Wheel angle
w_angle = [-45 90-45 -45 90-45]; % wheel angle in degree
%w_angle = [0 0 0 0]; % wheel angle in degree
w_angle = pi/180*w_angle; % wheel angle in radian

% Important parameter for actual system
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% P = [w_d,robot_w,robot_l,m,I_robot,La,Ra,Kb,Kt,J1,Tc,D,k,eps,...
%   n_G,J2,delta_1,delta_2,delta_3,delta_4,gamma_1,gamma_2,gamma_3,...
%   gamma_4];
tf = 10;
Kt = 0.013;
  p = [0.127,0.7,0.7,25,0.68,0.001,0.99,0.015,Kt,0.002*Kt,0.56*Kt,... %%
    0.00024*Kt,100,0.01,19.2,0,pi/4,-pi/4,pi/4,-pi/4,0,0,0,0];  %%
k_E = 1;                                                          %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Data for animation testing
%%% coordinates of origine of robot frame
% x = 0:0.005:3;
% y = 0:0.005:3;
% xy = [x;y];
% N_anima = length(xy);
% %%% Angle of robot frame with respect to global frame
% theta_f = 30*pi/180;
% theta = 0:theta_f/(N_anima-1):theta_f;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
sim('fourWheelRobotControl_v1.slx');
xytheta = xytheta';
robotanimation(xytheta);
figure(5)
plot(t,position_error)
xlabel('time')
ylabel('robot position error')
figure(6)
plot(t,error1)
xlabel('time')
ylabel('motor velocity error')
figure(7)
plot(t,X_r(:,1))
xlabel('time')
ylabel('robot x reference')
figure(8)
plot(t,X_r(:,2));
xlabel('time')
ylabel('robot y reference')
figure(9)
plot(t,X_r(:,3))
xlabel('time')
ylabel('robot theta reference')
figure(10)
subplot 211
% plot(t,X_r(:,1)-position_error(:,1))
plot(t,xytheta(1,:))
subplot 212
plot(t,xytheta(2,:))
figure(11)
plot(t,xytheta(3,:))
% figure(12)
% plot(t,voltages)
