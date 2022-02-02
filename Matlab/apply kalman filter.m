Ts=0.01;
t=0:Ts:30;
Q=1;
R=1;
x=0;
xnoise=0;

x_e=0;
p=9;

xmodel=zeros(length(t),1);
xtrue=zeros(length(t),1);

ymodel=zeros(length(t),1);
ytrue=zeros(length(t),1);

X_est=zeros(length(t),1);
Y_est=zeros(length(t),1);
P=zeros(length(t),1);

for k=1:length(t)
    
    x=x+(-x+10*sin(t(k)))*Ts;
    y=x;
    
    xnoise=xnoise+(-xnoise+10*sin(t(k)))*Ts+sqrt(Q*Ts)*randn;
    ynoise=xnoise+sqrt(R)*randn;
    
    xmodel(k)=x;
    xtrue(k)=xnoise;
    
    ymodel(k)=y;
    ytrue(k)=ynoise;
end
QE=0.01;
RE=1;

C=1;
A=(1-Ts);
for k=1:length(t)
    x_e=A*x_e+10*Ts*sin(t(k));
    p=A*p*A'+QE;
    
    y_e=C*x_e;
    pxy=p*C';
    pyy=C*p*C'+RE;
    
    w=pxy/pyy;
    x_e=x_e+w*(ytrue(k)-y_e);
    p=p-w*pyy*w';
    
    X_est(k)=x_e;
    P(k)=p;
    
    Y_est(k)=y_e;
end

subplot(3,1,1)
plot(t,xmodel,t,xtrue,t,X_est)
subplot(3,1,2)
plot(t,ymodel,t,ytrue,t,Y_est)
subplot(3,1,3)
plot(t,P)