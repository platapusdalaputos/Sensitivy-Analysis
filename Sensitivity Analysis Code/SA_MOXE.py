import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace, zeros, exp
from MOXE_Code import moxe_function
import math


d = 10e-6 # septal wall thickness micrometers 

delta = 1.5e-6 # Alveor-capillary barrier micrometers

Lambda_tiss = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)
Lambda_tiss1 = 0.1 # Ostwald solubility of xenon in lung septum (In vivo methods and applications of xenon-129 magnetic resonance)

Sa_Vg = 210  # Surface area /volume of gas
Sa_Vg1 = 210  # Surface area /volume of gas

T = 0.030 # time constant
tc = 1.5 # Capillary transit time

'''The healthy range values for the physiological parameters'''

Sa_VgLim = np.linspace(160,260,num=9)
dLim = np.linspace(3.7e-6,15.7e-6,num=9)
deltaLim = np.linspace(0.7e-6,1.3e-6,num=9)
TLim = np.linspace(0.020,0.039,9)
HCTConstant = np.linspace(23,31,9)
txConstant = np.linspace(1.0,1.6,9)   

sigTP1, sigRBC1, t = moxe_function(d, delta, Lambda_tiss, Sa_Vg, tc)


''' Sensitivity of the septal wall thickness '''

TP = []
RBC = []
labels = ['Lowest', 'Lowest1', 'lowest2', 'lowest3', 'mid', 'upper3', 'upper2', 'upper1', 'upper']


for i in range(len(dLim)):  

    sigTP, sigRBC, t = moxe_function(d, deltaLim[i], Lambda_tiss, Sa_Vg, tc)
    TP.append(sigTP)
    RBC.append(sigRBC)
 

for i in range(len(dLim)):
    fTP = plt.figure(1)
    plt.plot(t,TP[i], label = labels[i])
    plt.xlabel('Delay Time (s)')
    plt.ylabel('Signal Amplitude a.u.')
    plt.title('Tissue Phase (TP) Septal Wall Thickness')
    plt.legend()
    
    fRBC = plt.figure(2)
    plt.plot(t,RBC[i], label = labels[i])
    plt.xlabel('Delay Time (s)')
    plt.ylabel('Signal Amplitude a.u.')
    plt.title('RBC Phase (RBC) Septal Wall Thickness')    
    plt.legend()

''' Calculating the percentage change for the different Parameters '''

percCh_TP = []
percCh_RBC = []
for i in range(len(dLim)):
    
    percTP = ((TP[i]/sigTP1) - 1)*100
    percCh_TP.append(percTP)
    percRBC = ((RBC[i]/sigRBC1) - 1)*100
    percCh_RBC.append(percRBC)
    plt.legend()

for i in range(len(dLim)):
    fTP2 = plt.figure(3)
    plt.plot(t,percCh_TP[i], label = labels[i])
    plt.xlabel('Delay Time (s)')
    plt.ylabel('Signal % increase')
    plt.title('SA Septal wall thickness TP')
    plt.legend()

    fRBC2 = plt.figure(4)
    plt.plot(t,percCh_RBC[i], label = labels[i])
    plt.xlabel('Delay Time (s)')
    plt.ylabel('Signal % increase')
    plt.title('SA Septal wall thickness RBC')
    plt.legend()
 
''' plotting individual upper and lower limits '''
Fig = plt.figure(5)
plt.plot(percCh_RBC[0], label = 'lowest')
plt.xlabel('Delay Time (s)')
plt.ylabel('Signal % increase')
plt.title('SA Septal wall thickness RBC')
plt.legend()

Fig = plt.figure(6)
plt.plot(percCh_RBC[8], label = 'upper')
plt.xlabel('Delay Time (s)')
plt.ylabel('Signal % increase')
plt.title('SA Septal wall thickness RBC')
plt.legend()


# res1 = [i / j for i, j in zip(signal1, signal2)]
# res2 = [i / j for i, j in zip(signal1, signal3)]
# res3 = [i / j for i, j in zip(signal1, signal4)]
# res4 = [i / j for i, j in zip(signal1, signal5)]





    