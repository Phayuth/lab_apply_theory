data = xlsread('Data temp.xlsx');
temp = data(:,2);

//intialization
x = 36;
p = 1;
Q = 0.1; //believe on measurement
R = 4; //

x_store = zeros(length(temp),1); //store x for later plot

for k = 0:length(temp)-1
    
    //time update
    x = x;
    P = P + Q;
    
    // measurement update
    z = x;
    Pxz = p;
    Pzz = P + R;
    
    x = x + Pxz/Pzz*(temp(k+1)-z);
    p = p - Pxz/Pzz*Pxz;
    x_store(k+1) = x;
end

plot(data(:,1),[temp,x_store])