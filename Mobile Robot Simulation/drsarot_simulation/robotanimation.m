function robotanimation(xytheta)
frame =500;
xy = xytheta(1:2,:);
increment = fix(length(xy)/frame); 
N_anima = length(xy); % number of points for animation
theta = xytheta(3,:);
figure(4)
title('robot animation')
ii = 0;
F(frame) = struct('cdata',[],'colormap',[]);
for i=1:increment:N_anima
    ii = ii+1;
    % call robot body and all wheel coordinates
    [robot,frame,all_wheels,w_number,wheel]=robotbody;
    % transform robot coordinates and all wheel coordinates
    robot =xy(:,i)*ones(1,length(robot))+R2_z(theta(i))*robot; 
    frame =xy(:,i)*ones(1,length(frame))+R2_z(theta(i))*frame;
    all_wheels = xy(:,i)*ones(1,length(all_wheels))+R2_z(theta(i))*all_wheels;
    
    % Plot robot body
    plot(robot(1,:),robot(2,:),'--');
    axis equal % define equal axis scale
    axis([-1 5 -1 5]);
    line(frame(1,:),frame(2,:));
    
    % Plot each wheel one by one
    for j=1:w_number
        wheel_j = all_wheels(:,(j-1)*length(wheel)+1:...
            j*length(wheel));
        line(wheel_j(1,:),wheel_j(2,:));
    end
    drawnow
    F(ii) = getframe;
    %pause(0.01)
    %display(i)
end
video = VideoWriter('Robot animation','MPEG-4');
open(video)
writeVideo(video,F);
close(video);