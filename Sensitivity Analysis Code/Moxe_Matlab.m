%% MOXE in Matlab


delta = 1e-6;

d = 10e-6;

k = 0.15;  % delta/d  tissue thickness/septal thickness

T =  0.030; % s for seconds (d**2/(pi**2)*D) # Uptake time constant

Lambda_tiss = 0.1;

Sa_Vg = 210;

mu = 0.03; %((Lamda*d*Sa)/Vg) 

eta = 0.5; % greek n

tc = 1.3; % s for seconds

t = linspace(0,700e-3,100); % s for seconds

n = [1,3,5,7,9,11,13,15,17,19,21];

% b = (lamda*d)/2)*(Sa/Vg);

% Values to hold or plot

d1 = [];
Sumd1 = [];
Sd1 = [];


for i = 1:length(t)
    
    for j = 1:length(n)         
        d1(j) = (1/n(j)^2)*(1-cos(n(j)*pi*k))*exp(((-n(j)^2)*t(i)/T));
    end
    % Sum the values from each iteration
    Sumd1(i) = sum(d1);
    % Attain the Sd1 values
    Sd1 = mu*(2*k - ((8/pi^2)*Sumd1));
                   
end 


%% Attaining the values for the slope Sd2s

d2s = [];
Sumd2s = [];
Sd2s = [];

for i = 1:length(t)
    
    for j = 1:length(n)         
        d2s(j) = (1/n(j)^2)*(cos(n(j)*pi*k))*exp(((-n(j)^2)*t(i)/T));
    end
    % Sum the values from each iteration
    Sumd2s(i) = sum(d2s);
    % Attain the Sd2s values
    Sd2s = mu*(1-2*k - ((8/pi^2)*Sumd2s));
                   
end 




%% Attaining the values for the slope Sd2 part1
d2 = [];
d22 = [];
Sumd2 = [];
Sumd22 = [];
Sd2 = zeros(1,2);
Sd22 = [];
SD2 = [];
for i = 1:length(t)
    
    for j = 1:length(n)         
        d2(j) = (1/n(j)^4)*(cos(n(j)*pi*k))*(1-(exp(((-n(j)^2)*t(i)/T))));        
    end
    % Sum the values from each iteration
    Sumd2(i) = sum(d2);
    
    Sd2(i) = 2*mu*(((1-(2*k))*(t(i)/tc)) - ((8/(pi^2))*(T/tc))*Sumd2(i));
                   
end 

plot(t, Sd2)

%% Attaining the values for the slope Sd2 part2

for i = 1:length(t)    
    for j = 1:length(n)         
        d22(j) = (1/n(j)^2)*(cos(n(j)*pi*k))*exp(((-n(j)^2)*t(i)/T));
    end        
    % Sum the values from each iteration
    Sumd22(i) = sum(d22);
    
    % Attain the Sd2 values
    Sd22(i) = mu*(1-(t(i)/tc))*((((1-(2*k))) - ((8/(pi^2))*Sumd22(i))));
end 

SD2 = Sd2+Sd22;
plot(t, SD2)

%% Calculating STP and SRBC

    
STP = Sd1+ (1-eta)*SD2;
SRBC = eta*SD2;
plot(t,STP)
hold on
plot(t,SRBC)

