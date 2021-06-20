import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, zeros, exp
import math

def singSig(H, Lt, L, Lc):
    # Performing Sobel sensitivity analysis on the Mansson et al model
    
    # Intercepts of the slopes for Sb0
    
    n = 1 # nth term of a sequence
    Ca_initial = 0.01 # concentration of xenon in alveoli
    lambda_RBC = 0.02 # 
    lambda_T = 0.01 #
    lambda_PL = 0.009
    D = 1e-9  # 
    F = 4e-14 # metres cubed per second (m^3/s)
    
    
    # Parameters of interest 
    
    # L = 8e-6 # metres (m)
    # Lt = 0.7*L # Length of tissue
    # Lc = L-Lt # diffusion capillary
    ra = 35e-6 # radius of alveoli
    # H = 0.5 # Haematocrit
    
    
    
    
    
    Hperc = H
    Ltperc = Lt
    Lperc = L
    
        
        
    Aa = 4*np.pi*ra**2  
    r2 = ra + Ltperc + Lc
    tau_1 = 40e-3 # seconds
    c = -1 
    Va = (4/3)*np.pi*ra**3
    
    # Gaining values for k
    k = Va/(Va + lambda_T*Aa*Ltperc + (lambda_T/lambda_PL)*Aa*Lc)
    
    alpha = Ca_initial*k # General proportionality constant
    
    # Gaining values for An
    An_initial = -4*lambda_T*Ca_initial*(((2*n-1)*np.pi + 2*(1-k)*(-1)**n)/(((2*n - 1)**2)*np.pi**2))
    An = An_initial/(lambda_T*Ca_initial*k)
    
    # Gaining values for Bn
    Bn_initial = lambda_T*Ca_initial*(8*(1-k)/(((2*n - 1)**2)*np.pi**2))
    Bn = Bn_initial/(lambda_T*Ca_initial*k)
    
    # Gaining values for fn with respect to r2
    fn = (n-0.5)*(np.pi/2)*(r2 - ra)
    Tau_n = ((L/np.pi)**2)*(1/(D*(n-0.5)**2))
    
    # Gaining values for Psi_1 
    Psi_1 = An*np.sin(fn) + Bn*np.cos(fn)
    
    # Values for the slopes for the blood and tissue, Sb1 and St1
    Sb1_perc = alpha*lambda_RBC*H*F
    # Sb1_percAp.append(Sb1_perc)
    
    St1_perc = alpha*lambda_PL*(1-H)*F
    # St1_percAp.append(St1_perc)
    
    # New parameters of ini_Sb0
    ini_Sb0 = alpha*lambda_RBC*H*Aa*Lc
    
    Sb0_perc = ini_Sb0 + Sb1_perc*Psi_1*r2*tau_1
    # Sb0_percAp.append(Sb0_perc)
    
    # Intercepts of the slopes for St0
    ini_St0 = alpha*lambda_T*Aa*Ltperc + alpha*lambda_PL*Aa*Lc*(1-H)
    
    St0_perc = ini_St0 + St1_perc*Psi_1*r2*tau_1
    
    # St0_percAp.append(St0_perc)
    
    
    # Putting it all together
    
    t = np.array([0, 10e-3, 20e-3, 30e-3, 40e-3, 50e-3, 60e-3, 70e-3, 80e-3, 90e-3])
        
    # Signal from the tissue
    St = St0_perc*(1+c*exp(-t/tau_1))+ St1_perc*t;
    
    # Signal from the RBC
    Sb = Sb0_perc*(1+c*exp(-t/tau_1))+ (Sb1_perc*t);
    
    return St, Sb

# Function to change the range of the parameters by a certain amount

def multiPerc(parameter):
    
    Multi_p = [parameter*2.0, parameter*1.9, parameter*1.8, parameter*1.7, parameter*1.6, parameter*1.5, parameter*1.4, parameter*1.3, parameter*1.2, parameter*1.1,parameter,parameter*0.9, parameter*0.8, parameter*0.7, parameter*0.6, parameter*0.5, parameter*0.4, parameter*0.3, parameter*0.2, parameter*0.1]
    
    # RangesAp = []
    # Multi_p = np.linspace(0, 4, num=101)
    # for i in range(1,len(Multi_p)):
    #     Ranges = Multi_p[i]*parameter
    #     RangesAp.append(Ranges)
        
        
    return(Multi_p)

# Function to assess the different parameters independently 

def ParamChange(Hperc, Ltperc, Lperc, Lcperc):
    
    # Performing OAT sensitivity analysis on the Mansson et al model

    # Intercepts of the slopes for Sb0
    
    n = 1 # nth term of a sequence
    Ca_initial = 100 # concentration of xenon in alveoli
    lambda_RBC = 0.2 # 
    lambda_T = 0.1 # 
    lambda_PL = 0.09
    D = 1e-9  # 
    F = 4e-14 # metres cubed per second (m^3/s)
    
    
    # Parameters of interest 
    
    L = Lperc # metres (m)
    Lt = Ltperc # This is the septal thickness
    Lc = Lcperc # diffusion capillary
    ra = 35e-6 # radius of alveoli
    H = Hperc # Haematocrit    
    
    Aa = 4*np.pi*ra**2  
    r2 = ra + Lt + Lc
    tau_1 = 40e-3 # seconds
    c = -1 
    Va = (4/3)*np.pi*ra**3
    
    # Gaining values for k
    k = Va/(Va + lambda_T*Aa*Lt + (lambda_T/lambda_PL)*Aa*Lc)

    alpha = Ca_initial*k # General proportionality constant

    # Gaining values for An
    An_initial = -4*lambda_T*Ca_initial*(((2*n-1)*np.pi + 2*(1-k)*(-1)**n)/(((2*n - 1)**2)*np.pi**2))
    An = An_initial/(lambda_T*Ca_initial*k)

    # Gaining values for Bn
    Bn_initial = lambda_T*Ca_initial*(8*(1-k)/(((2*n - 1)**2)*np.pi**2))
    Bn = Bn_initial/(lambda_T*Ca_initial*k)

    # Gaining values for fn with respect to r2
    fn = (n-0.5)*(np.pi/2)*(r2 - ra)
    Tau_n = ((L/np.pi)**2)*(1/(D*(n-0.5)**2))

    # Gaining values for Psi_1 
    Psi_1 = An*np.sin(fn) + Bn*np.cos(fn)

    # Values for the slopes for the blood and tissue, Sb1 and St1
    Sb1_perc = alpha*lambda_RBC*H*F
    # Sb1_percAp.append(Sb1_perc)
    
    St1_perc = alpha*lambda_PL*(1-H)*F
    # St1_percAp.append(St1_perc)
    
    # New parameters of ini_Sb0
    ini_Sb0 = alpha*lambda_RBC*H*Aa*Lc

    Sb0_perc = ini_Sb0 + Sb1_perc*Psi_1*r2*tau_1
    # Sb0_percAp.append(Sb0_perc)

    # Intercepts of the slopes for St0
    ini_St0 = alpha*lambda_T*Aa*Lt + alpha*lambda_PL*Aa*Lc*(1-H)

    St0_perc = ini_St0 + St1_perc*Psi_1*r2*tau_1
    
    # St0_percAp.append(St0_perc)

    return St0_perc, Sb0_perc, St1_perc, Sb1_perc

# plt.plot(Sb)
# plt.plot(St)

    
    # res1 = [l / m for l, m in zip(signal1, signal2)]


    









