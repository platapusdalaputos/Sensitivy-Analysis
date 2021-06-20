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

k = 0.15 # delta/d     # tissue thickness/septal thickness

T = 30 # ms (d**2/(pi**2)*D) # Uptake time constant

mu = 0.03 #((Lamda*d*Sa)/Vg) 

tc = 1500


# plotting the values for the slope for Sd2s(t)
# Which the slope correspinding to the RBC signal


Sd2s_append = []

for t in range(1,500): # t is time in ms
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
#     print(Sd2s)
    plt.plot(Sd2s_append, label ='Sd2s')
    plt.plot(Sd1_append, label = 'Sd1')
    plt.xlabel('time(ms)')
    plt.ylabel('Amplitude')
#     plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()
    
# Sd2s_np= np.array(Sd2s_append)
# fin = (1-((1500/1500)*Sd2s_np))
# print(fin)

# Sd2 part2  

Sd22_append = []

for t in range(1,500): # t is time in ms
    B3 = []
    for n in range(1, 9):
        if(n % 2 != 0):
            s3=[]
            A3 = (1/n**2)*(np.cos(n*np.pi*k))*exp(((-n**2)*t)/T)
            s3.append(A3)
            if s3 not in B3:
                B3.append(s3)
                #extracts and sums the lists within a list
                res_3 = list() 
                for e in range(0, len(B3[0])): 
                    tmp_3 = 0
                    for f in range(0, len(B3)):
                        
                        tmp_3 = tmp_3 + B2[f][e] 
                        
                    res_3.append(tmp_3) 
                    
    Gres_3 = np.array(res_3)

    Sd22 = mu*(1-(t/tc))*((((1-(2*k))) - ((8/(np.pi**2))*Gres_3)))
    Sd22_append.append(Sd22)
#     print(Sd22s)
    plt.plot(Sd22_append)
    plt.xlabel('time(ms)')
    plt.ylabel('Amplitude')
#     plt.title('Interesting Graph\nCheck it out')
#     plt.legend()
#     plt.show()
    
# Sd2s_np= np.array(Sd2s_append)
# fin = (1-((1500/1500)*Sd2s_np))
# print(fin)