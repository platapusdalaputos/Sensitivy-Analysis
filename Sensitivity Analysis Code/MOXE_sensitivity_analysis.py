import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, zeros, exp
import math

#Parameters and constants for the uptake curves

# Lamda =  # Ostwald solubility

# d =      # Septal thickness tissue + capillary + tissue

# D =      # Diffusion coefficient

# delta =  # tissue thickness

# Sa =     # Surface area in the lungs

# Vg =     # volume of the gas


##############################################################################

                    #Parameters for Sensitivity Analysis

##############################################################################

# A = 0.9 # percentage change

# d = 10e-6 # micrometers 

# delta = 1.5e-6 # micrometers

# Lambda_tiss = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)

# Sa_Vg = 30000*A  # Surface area /volume of gas




#D = 337# diffusion coefficient of dissolved gas
#Lambda_plas = 0.09 # Ostwald solubility of xenon in plasma septum
#Lambda_RBC = 0.2 # Ostwald solubility of xenon in blood septum


# plotting the values for the slope for Sd1(t) 
# Which is the slope corresponding to the tissue signal

def moxe_tp_function(d, delta, Lambda_tiss, Sa_Vg):
    
    k = delta/d # delta/d     # tissue thickness/septal thickness
    
    T = 30 # ms (d**2/(pi**2)*D) # Uptake time constant
    # T = (d**2/(pi**2)*D) # Uptake time constant

    mu = Lambda_tiss*d*Sa_Vg # = 0.03 #((Lamda*d*Sa)/Vg) 
    
    tc = 1.5
    
    # t = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9]
    
    Sd1_append = []
    fourth_val =[]
    for t in range(1,50):
        
        #Appends the list of appended A into a nested list
        B=[]
        for n in range(1, 9):
            if(n % 2 != 0):
                s=[]
                A = (1/n**2)*(1-np.cos(n*np.pi*k))*exp(((-n**2)*t)/T)
                s.append(A)
                if s not in B:
                    B.append(s)
                    #extracts and sums the lists within a list
                    res = list() 
                    for j in range(0, len(B[0])): 
                        tmp = 0
                        for i in range(0, len(B)):
                            
                            tmp = tmp + B[i][j] 
                            
                        res.append(tmp) 
        #Turns the list into a np.array
        Gres = np.array(res)
    
        Sd1 =mu*(2*k - ((8/np.pi**2)*Gres))
        Sd1_append.append(Sd1)

        
        
        
        
    Sd2s_append = []
        
    for t in range(1,50): # t is time in ms
        B1 = []
        for n in range(1, 9):
            if(n % 2 != 0):
                s1=[]
                A1 = (1/n**2)*(np.cos(n*np.pi*k))*exp(((-n**2)*t)/T)
                s1.append(A1)
                if s1 not in B1:
                    B1.append(s1)
                    #extracts and sums the lists within a list
                    res_1 = list() 
                    for j in range(0, len(B1[0])): 
                        tmp_1 = 0
                        for i in range(0, len(B1)):
                            
                            tmp_1 = tmp_1 + B1[i][j] 
                            
                        res_1.append(tmp_1) 
                        
        Gres_1 = np.array(res_1)
    
        Sd2s = (mu*((1-2*k) - ((8/np.pi**2))*Gres_1))
        Sd2s_append.append(Sd2s)
        if t == 49:
            return(Sd1_append, Sd2s_append)
