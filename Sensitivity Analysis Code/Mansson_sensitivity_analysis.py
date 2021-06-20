import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, zeros, exp
import math
from Mansson_functions import singSig, multiPerc, ParamChange

# Performing Sobel sensitivity analysis on the Mansson et al model

# Intercepts of the slopes for Sb0

n = 1 # nth term of a sequence
Ca_initial = 100 # concentration of xenon in alveoli
lambda_RBC = 0.2 # 
lambda_T = 0.1 #
lambda_PL = 0.09
D = 1e-9  # 
F = 4e-14 # metres cubed per second (m^3/s)


''' Parameters of interest '''

L = 8e-6 # metres (m)
Lt = 5.6e-6 # Length of tissue
Lc = 2.4e-6 # diffusion capillary
ra = 35e-6 # radius of alveoli
H = 0.5 # Haematocrit


''' Changing the parameters from the mean value '''

# Hperc = multiPerc(H)
# Ltperc = multiPerc(Lt)
# Lperc = multiPerc(L)
# Lcperc = multiPerc(Lc)

N = 50

Hperc = np.linspace(0.3, 0.6, N)
Ltperc = np.linspace(3.6e-6, 7.6e-6, N)
Lperc = np.linspace(8e-6, 10e-6, N)
Lcperc = np.linspace(2.4e-6, 4e-6, N)

''' Ascertaining the original values '''

[tiss_param, RBC_param] = singSig(H, Lt, L, Lc)


Sb0_percAp =[]
St0_percAp =[]
Sb1_percAp =[]
St1_percAp =[]

# '''This function finds the parameter value with the original parameter value''' 

# # [tiss_param, RBC_param] = singSig()

# print(tiss_param)

for i in range(0,len(Hperc)):
    
    [St0_perc, Sb0_perc, St1_perc, Sb1_perc] = ParamChange(H, Ltperc[i], L, Lc)
    Sb0_percAp.append(Sb0_perc)
    St0_percAp.append(St0_perc)
    Sb1_percAp.append(Sb1_perc)
    St1_percAp.append(St1_perc)
    # print(St0_percAp)


tau_1 = 40e-3 # seconds
c = -1 


# Putting it all together

Sb_Ap = []
St_Ap = []
St_len = []
percCh_TP = []
percCh_RBC = []
# Delay time

# t = np.array([0, 100e-3, 200e-3, 300e-3, 400e-3, 500e-3, 600e-3, 700e-3, 800e-3, 900e-3])

t = np.linspace(0, 900e-3, 1000)


''' Plotting the signal due to the parameter change '''


for i in range(len(Sb1_percAp)):    
    
    # Signal from the tissue
    St = St0_percAp[i]*(1+c*exp(-t/tau_1))+ St1_percAp[i]*t;
    St_len.append(St)
   
    # Signal from the RBC
    Sb = Sb0_percAp[i]*(1+c*exp(-t/tau_1))+ (Sb1_percAp[i]*t);
    Sb_Ap.append(Sb) 
     
    # plt.plot(Sb)
    f = plt.figure(1)
    plt.plot(t,St)
    plt.xlabel('delay time(ms)')
    plt.ylabel('signal a.u')
       
    # plt.plot(Sb)
    f1 = plt.figure(2)
    plt.plot(t,Sb)
    plt.xlabel('delay time(ms)')
    plt.ylabel('signal a.u')
    
    # f2 = plt.figure(3)
    # percTP = ((St0_percAp[i]/St_len[0])-1)*100
    # # percTP = [0 if math.isnan(x) else x for x in percTP]
    # plt.plot(percTP)

''' sensitivity of the parameter '''
# print(St0_percAp[0])


percCh_TP = []
percCh_RBC = []
for i in range(len(Sb1_percAp)):
    try: 
        percTP = ((St_len[i]/St_len[0])-1)*100
        # print(percTP)
    except:
        pass
        
    f3 = plt.figure(3)
    plt.plot(t,percTP)

    # percTP = [0 if math.isnan(x) else x for x in percTP]
    # percCh_TP.append(percTP)
    
    try:
        percRBC = ((Sb_Ap[i]/Sb_Ap[0])-1)*100
    except:
        pass
    
    f4 = plt.figure(4)
    plt.plot(t,percRBC)

    # percRBC = [0 if math.isnan(x) else x for x in percRBC]
#     percCh_RBC.append(percRBC)


# ''' Plotting the signal change '''

# for i in range(len(Sb1_percAp)):
#     fTP2 = plt.figure(3)
#     plt.plot(percCh_TP)
#     plt.xlabel('Delay Time (s)')
#     plt.ylabel('Signal % change')
#     plt.title('SA Capillary Transit Time TP')

#     fRBC2 = plt.figure(4)
#     plt.plot(percCh_RBC[i])
#     plt.xlabel('Delay Time (s)')
#     plt.ylabel('Signal % change')
#     plt.title('SA Capillary Transit Time RBC')





