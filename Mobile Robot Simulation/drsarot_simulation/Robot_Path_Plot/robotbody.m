function [robot,frame,all_wheels,w_number,wheel] = robotbody
global w_angle
% Wheel size
w_w = 0.05; % width
w_d = 0.1; % diameter
wheel = 2\[w_d w_d -w_d -w_d w_d; w_w -w_w -w_w w_w w_w]; % wheel size defined as xy coordinates

% Number of wheel
w_number = 4;

% robot size
robot_w = 0.7; % robot width
robot_l = 0.7; % robot length
frame_w = robot_w + 0.45; % width of robot frame

% Coordinate of center of wheels = robot size
robot = 2\[robot_w -robot_w -robot_w robot_w robot_w; robot_l robot_l -robot_l -robot_l robot_l];
incR = frame_w/2/cos(pi/8);
frame = [incR*cos(pi/8) incR*cos(3*pi/8) incR*cos(5*pi/8) incR*cos(7*pi/8) incR*cos(9*pi/8) incR*cos(11*pi/8)...
    incR*cos(13*pi/8) incR*cos(15*pi/8) incR*cos(pi/8);...
    incR*sin(pi/8) incR*sin(3*pi/8) incR*sin(5*pi/8) incR*sin(7*pi/8) incR*sin(9*pi/8) incR*sin(11*pi/8)...
    incR*sin(13*pi/8) incR*sin(15*pi/8) incR*sin(pi/8)];

%%%% Plot wheel
% figure(1)
% axis equal
% line(wheel(1,:), wheel(2,:))
% title('Wheel size')
%%%% Plot robot
% figure(2)
% axis equal
% line(robot(1,:),robot(2,:))
% title('robot size')

%%%% Plot robot with wheels
% figure(3)
% hold off
% axis equal
% title('robot with wheels')
% line(robot(1,:),robot(2,:))

% Coordinates of all wheels
all_wheels = zeros(2,w_number*length(wheel));
for i=1:w_number % define wheel coordinate one by one
    wheel_i = robot(:,i)*ones(1,length(wheel))+R2_z(w_angle(i))*wheel;
    all_wheels(:,(i-1)*length(wheel)+1:i*length(wheel)) = wheel_i;
%     line(wheel_i(1,:),wheel_i(2,:));    
end
end


