%% Performing Sobel sensitivity analysis on the Mansson et al model

% Intercepts of the slopes for Sb0
n = 1;
Ca_initial = 100; % concentration of xenon in alveoli
lambda_RBC = 0.2;
lambda_T = 0.1;
lambda_PL = 0.09;
D = 1e-9; % 
F = 4e-14; % metres cubed per second (m^3/s)


% Parameters of interest 
L = 8e-6; % metres (m)
Lt = 0.7*L;
Lc = L-Lt;
ra = 35e-6; % radius of alveoli
H = 0.5;



[Hperc] = multiPerc(H);
[Ltperc] = multiPerc(Lt);
[Lperc] = multiPerc(L);


%%

Sb0_perc =[];
St0_perc =[];
Sb1_perc =[];
St1_perc =[];

for i = 1:length(Hperc)

        Aa = 4*pi*ra^2 ; 
        r2 = ra + Ltperc(i) + Lc;
        tau_1 = 40e-3; % seconds
        c = -1;
        Va = (4/3)*pi*ra^3;
        % Gaining values for k
        k = Va/(Va + lambda_T*Aa*Ltperc(i) + (lambda_T/lambda_PL)*Aa*Lc);

        alpha = Ca_initial*k;% general proportionality constant


        % Gaining values for An
        An_initial = -4*lambda_T*Ca_initial*(((2*n-1)*pi + 2*(1-k)*(-1)^n)/((2*n - 1)^2*pi^2));
        An = An_initial/(lambda_T*Ca_initial*k);

        % Gaining values for Bn
        Bn_initial = lambda_T*Ca_initial*(8*(1-k)/((2*n - 1)^2*pi^2));
        Bn = Bn_initial/(lambda_T*Ca_initial*k);

        % Gaining values for fn with respect to r2
        fn = (n-0.5)*(pi/2)*(r2 - ra);
        Tau_n = ((L/pi)^2)*(1/(D*(n-0.5)^2));


        % Gaining values for Psi_1 
        Psi_1 = An*sin(fn) + Bn*cos(fn);

        %  Values for the slopes for the blood and tissue, Sb1 and St1

%         Sb1_perc(i) = alpha*lambda_RBC*Hperc(i)*F;
% 
%         St1_perc(i) = alpha*lambda_PL*(1-Hperc(i))*F;

        Sb1_perc(i) = alpha*lambda_RBC*H*F;

        St1_perc(i) = alpha*lambda_PL*(1-H)*F; 
        
        % New parameters of ini_Sb0
        ini_Sb0 = alpha*lambda_RBC*H*Aa*Lc;

        Sb0_perc(i) = ini_Sb0 + Sb1_perc(i)*Psi_1*r2*tau_1;


        % Intercepts of the slopes for St0

        ini_St0 = alpha*lambda_T*Aa*Ltperc(i) + alpha*lambda_PL*Aa*Lc*(1-H);

        St0_perc(i) = ini_St0 + St1_perc(i)*Psi_1*r2*tau_1;




end


%%

% Putting it all together
cc = jet(100);
% Sb = zeros(10,20);
% St = zeros(10,20);
Sb = [];
St = [];
% figure;
% colorbar 
t = [0, 10e-3, 20e-3, 30e-3, 40e-3, 50e-3, 60e-3, 70e-3, 80e-3, 90e-3];
% t = linspace(0,1e-3,90e-3);
%%
for i = 1:20
%     t = [0, 10e-3, 20e-3, 30e-3, 40e-3, 50e-3, 60e-3, 70e-3, 80e-3, 90e-3];
    Sb(:,i) = Sb0_perc(i)*(1+c*exp(-t/tau_1))+ Sb1_perc(i)*t;
    St(:,i) = St0_perc(i)*(1+c*exp(-t/tau_1))+ St1_perc(i)*t;

    
%     plot(t, Sb, 'color', cc(i,:), 'LineWidth', 2)
%     hold on 
%     plot(t, St, 'color', cc(i,:), 'LineWidth', 2)
%     xlabel('delay time (ms)')
%     ylabel('Signal Amplitude');
%     pause(0.1)

end    

% t = [0, 10e-3, 20e-3, 30e-3, 40e-3, 50e-3, 60e-3, 70e-3, 80e-3, 90e-3, 0.1, 0.2];
% Sb_perc = Sb0*(1+c*exp(-t/tau_1))+ Sb1*t;
% St_perc = St0*(1+c*exp(-t/tau_1))+ St1*t;
% 
% figure;
% plot(t, Sb, 'r', 'LineWidth', 2)
% hold on 
% plot(t, St, 'b', 'LineWidth', 2)
% xlabel('delay time (ms)')
% ylabel('Signal Amplitude');

display(St);


figure;
plot(St, 'r', 'LineWidth', 2);
colormap;
% hold on 
% % plot(t, St, 'b', 'LineWidth', 2)
% xlabel('delay time (ms)')
% ylabel('Signal Amplitude');

% pcolor(t, Sb0_perc, Sb(:,1));
% contour(Sb)





